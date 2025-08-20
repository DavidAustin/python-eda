#!/usr/bin/env python3
import re, sys, math, json, argparse, pathlib

try:
    import yaml  # optional for --sizes
    HAVE_YAML = True
except Exception:
    HAVE_YAML = False

INCH_TO_MM = 25.4

# --- Built-in footprint size guesses (width_mm, length_mm) BEFORE margin ---
# Values are conservative courtyards (body-ish), you can tweak via --margin.
# These "peiXXXX" values come directly from mk_pe_foots.py:
#   data[k] = [part_length (a), pad_gap (b), pad_w (c), pad_h (d)]
# We map to (W, L) = (d, a) and let --margin add any extra courtyard.
SIZE_MAP = {
    # Passives from mk_pe_foots.py (W, L)
    "pei0100": (0.20, 0.48),
    "pei0201": (0.40, 1.00),
    "pei0402": (0.60, 1.50),
    "pei0603": (0.80, 2.60),
    "pei0805": (1.20, 3.00),
    "pei1008": (2.00, 2.50),
    "pei1206": (1.50, 4.20),
    "pei1210": (2.40, 4.20),
    "pei1218": (4.80, 4.20),
    "pei1812": (3.15, 4.55),
    "pei2010": (2.40, 6.10),
    "pei2220": (5.00, 5.70),
    "pei2512": (3.00, 8.00),

    # Polarized variants from mk_pe_foots.py (W, L)
    "pei2917_pol": (4.00, 7.30),
    "pei2312_pol": (2.40, 6.00),
    "pei1206_pol": (1.50, 4.20),
    "pei0603_pol": (0.80, 2.60),
    "pei0402_pol": (0.60, 1.50),

    # Diodes & small-outline (body-ish before margin)  (W, L)
    "DIODE_SMA":     (2.90, 4.60),  # DO-214AC
    "DIODE_SMB":     (3.70, 6.10),  # DO-214AA
    "DIODE_SMC":     (6.80, 7.80),  # DO-214AB

    # SOD family (body-ish):
    "DIODE_SOD123":  (1.60, 2.70),
    "DIODE_SOD123F": (1.60, 2.70),
    "DIODE_SOD323":  (1.30, 2.50),
    "DIODE_SOD923":  (0.60, 1.00),

    # SOT-23 family (bodies are very similar; keep conservative):
    "SOT23_GSD": (1.60, 3.00),
    "SOT23_BCE": (1.60, 3.00),
    "SOT23_3":   (1.60, 3.00),
    "SOT23_5":   (1.70, 2.90),
    "SOT23_6":   (1.70, 2.90),

    # Radial placeholder (Diameter≈W≈L) if named like RADIAL-<diameter>-...
    "RADIAL-5.00": (5.00, 5.00),

    # Modules / specials
    "ESP32-WROOM":          (18.0, 25.5),
    "SARA-R5":              (16.0, 26.0),
    "RPI_HAT":              (5.1, 51.0),
    "UFL-R-SMT-1-10":       (3.0, 3.0),
    "CONN8_SDCARD-MSD-4-A": (26.3, 19.35),
    "CONN8_SIM-0475532001": (26.3, 19.35),
    "BH-25C-1":             (25.0, 25.0),
    "DLW21SZ900HQ2L":       (1.25, 2.00),
    "SRN8040-3R3Y":         (8.0, 8.0),
    "SDER041H-2R2MS":       (4.0, 4.0),
    "CD-1206-SMT":          (12.0, 12.0),

    # Crystals
    "LFXTAL035939": (13.4, 4.9),

    # Power packages (body envelopes; not pads/tabs)
    "TO220_2":   (10.0, 9.7),
    "TO247_GCE": (15.6, 20.0),
    "TO252_GSD": (6.6, 6.1),   # DPAK / TO-252 body
    "TO252_3":   (6.6, 6.1),
    "TO263_2":   (10.2, 9.1),  # D2PAK / TO-263 body
    "TO263_GSD": (10.2, 9.1),
    "TO263_7":   (10.2, 9.1),

    # Small ICs without numeric dims in name (generic bodies)
    "LGA14":   (3.0, 3.0),
    # "TSSOP16": (4.4, 5.0),
    #"SOIC-8":  (3.9, 4.9),
    #"SOIC-14": (3.9, 8.7),

    # “Big” connectors (rough)
    "CONN_DT13-48PABCD-R015": (36.0, 127.0),
    "CONN8_254":  (8.0, 21.0),
    "CONN3_254":  (8.0, 8.0),
}

# Names we ignore for fitting estimate (non-real estate or tiny)
IGNORE_PREFIXES = ("FID", "TP", "T")
IGNORE_EXACT = set(["hole1", "M3"])

# ---------------------------------------------
# Helpers for parsing names & dimensions
# ---------------------------------------------

# Package names from our -N generators, e.g.:
#   SOIC-8-4.40x3.60-1.27x6.46-0.64x1.80
#   TSSOP-16-4.40x5.00-0.65x6.40-0.31x1.00
#   QFN-32-5.00x5.00-0.50x5.50-0.25x0.80-3.20x3.20
# IMPORTANT: In your logs, the first pair is always PARTWIDTH x PARTHEIGHT.
# For estimator, treat that **directly** as (W, L) = (PARTWIDTH, PARTHEIGHT).
PACKAGE_PREFIXES = [
    "SOIC", "SSOP", "TSSOP", "MSOP",
    "QFN", "WFDFN", "WSON",
    "HTSSOP", "uSIP", "SMD",
    "BGA", "QFP", "LQFP", "TQFP"
]
PKG_LEADING_DIMS_RE = re.compile(
    r'^(?:' + '|'.join(PACKAGE_PREFIXES) + r')-\d+-'
    r'(?P<pw>\d+(?:\.\d+)?)x(?P<ph>\d+(?:\.\d+)?)\b',  # PARTWIDTH x PARTHEIGHT
    flags=re.IGNORECASE
)

def package_body_dims_from_name(name: str):
    """
    If the footprint name starts with one of our -N generator names,
    return the leading body (W, L) in mm where:
      W = PARTWIDTH, L = PARTHEIGHT
    """
    m = PKG_LEADING_DIMS_RE.match(name.strip())
    if not m:
        return None
    pw = float(m.group("pw"))
    ph = float(m.group("ph"))
    return (pw, ph)  # <-- no swapping

# PEI imperial code, e.g. pei2312 -> 0.23" x 0.12"
PEI_RE = re.compile(r'^pei(\d{2})(\d{2})', re.I)

def infer_pei_imperial_mm(fpname: str):
    m = PEI_RE.match(fpname.strip())
    if not m:
        return None
    L_in = int(m.group(1)) / 100.0   # first two digits = length in inches
    W_in = int(m.group(2)) / 100.0   # last two digits  = width in inches
    L_mm = L_in * 25.4
    W_mm = W_in * 25.4
    return (W_mm, L_mm)  # (W, L)

def parse_board_size(s):
    s = s.strip().lower().replace(" ", "")
    m = re.match(r'^([\d\.]+)x([\d\.]+)(mm|in)$', s)
    if not m:
        raise ValueError(f"Bad --board '{s}'. Use e.g. 127x165.1mm or 5x6.5in")
    a, b, unit = m.groups()
    a = float(a); b = float(b)
    if unit == "in":
        a *= INCH_TO_MM; b *= INCH_TO_MM
    return (a, b)

def load_overrides(path):
    if not path:
        return {}
    p = pathlib.Path(path)
    if not p.exists():
        raise FileNotFoundError(path)
    text = p.read_text()
    try:
        data = json.loads(text)
        return normalize_size_map(data)
    except Exception:
        if not HAVE_YAML:
            raise RuntimeError("pyyaml not installed; install it or provide JSON for --sizes")
        data = yaml.safe_load(text)
        return normalize_size_map(data)

def normalize_size_map(d):
    out = {}
    for k, v in d.items():
        if isinstance(v, (list, tuple)) and len(v) == 2:
            out[k] = (float(v[0]), float(v[1]))
        elif isinstance(v, dict) and "w" in v and "l" in v:
            out[k] = (float(v["w"]), float(v["l"]))
    return out

EL_RE = re.compile(r'^Element\["([^"]*)"\s+"([^"]+)"\s+"([^"]+)"\s+"[^"]*"', re.IGNORECASE)

def looks_bottom(flags):
    return "onsolder" in flags.lower()

def is_ignored(footprint, refdes):
    if footprint in IGNORE_EXACT: return True
    for p in IGNORE_PREFIXES:
        if refdes.startswith(p):
            return True
    return False

def first_dims_in_name(name):
    """
    Extract first AxB numeric token from footprint name (fallback).
    Returns tuple (A, B) as floats if found else None.
    """
    m = re.search(r'(\d+(?:\.\d+)?)x(\d+(?:\.\d+)?)', name)
    if not m:
        return None
    return float(m.group(1)), float(m.group(2))

def radial_guess(name):
    m = re.match(r'RADIAL-(\d+(?:\.\d+)?)', name.upper())
    if m:
        d = float(m.group(1))
        return (d, d)
    return None

def normalize_key(s):
    return s.strip()

# Name variants to try during lookup (handle lib/category prefixes)
def footprint_name_variants(name: str):
    yield name  # as-is
    prefixes = ("IND_",)  # extend if needed (e.g., "LED_", "MECH_", ...)
    for p in prefixes:
        if name.startswith(p):
            yield name[len(p):]

def lookup_size(footprint):
    for cand in footprint_name_variants(footprint):
        # 1) exact match
        if cand in SIZE_MAP:
            return SIZE_MAP[cand]

        # 2) generator naming (e.g., SOIC-8-4.40x3.60-…)
        pkg_dims = package_body_dims_from_name(cand)
        if pkg_dims:
            return pkg_dims  # (W,L) from first pair, no swap

        # 3) radial capacitor heuristic
        r = radial_guess(cand)
        if r:
            return r

        # 4) numeric dims anywhere (generic fallback; keep order)
        dims = first_dims_in_name(cand)
        if dims:
            return dims

        # 5) common generics (fallbacks)
        up = cand.upper()
        if up.startswith("SOIC-8"):
            return SIZE_MAP.get("SOIC-8")
        if up.startswith("SOIC-14"):
            return SIZE_MAP.get("SOIC-14")
        if up.startswith("SOT23"):
            return SIZE_MAP.get("SOT23_3")
        if up.startswith("TSSOP16"):
            return SIZE_MAP.get("TSSOP16")

        # 6) PEI imperial inference last
        pei = infer_pei_imperial_mm(cand)
        if pei:
            return pei

        # 7) finally, prefix matches in SIZE_MAP (broad brush)
        for key in SIZE_MAP:
            if cand.startswith(key):
                return SIZE_MAP[key]

    return None  # unknown

def mm2(x): return x*x

def main():
    ap = argparse.ArgumentParser(description="Estimate if all parts fit one side of a PCB at target utilization.")
    ap.add_argument("pcb", help=".pcb file (pcb-gtk / pcb-rnd)")
    ap.add_argument("--board", required=True, help="Board size, e.g. 127x165.1mm or 5x6.5in")
    ap.add_argument("--util", type=float, default=0.60, help="Target max component area utilization (default 0.60)")
    ap.add_argument("--margin", type=float, default=0.25, help="Extra courtyard margin per side in mm (default 0.25)")
    ap.add_argument("--side", choices=["top", "bottom", "both"], default="top", help="Which side to consider (default top)")
    ap.add_argument("--sizes", help="YAML or JSON mapping of {footprint: [Wmm, Lmm]} to override/extend")
    ap.add_argument("--include-ignored", action="store_true", help="Include testpads/fids/mount holes in area")
    args = ap.parse_args()

    board_w, board_h = parse_board_size(args.board)
    board_area = board_w * board_h
    target_area = board_area * args.util

    # Load file
    text = pathlib.Path(args.pcb).read_text(errors="ignore").splitlines()

    # Merge overrides
    overrides = load_overrides(args.sizes) if args.sizes else {}
    override_exact = {normalize_key(k): tuple(v) for k, v in overrides.items()}
    override_prefix = sorted(override_exact.keys(), key=len, reverse=True)

    selected = []  # (footprint, refdes, flags)
    for line in text:
        m = EL_RE.match(line)
        if not m: continue
        flags, fp, ref = m.groups()
        if not args.include_ignored and is_ignored(fp, ref):
            continue
        if args.side != "both":
            bottom = looks_bottom(flags)
            if args.side == "top" and bottom:
                continue
            if args.side == "bottom" and not bottom:
                continue
        selected.append((fp, ref, flags))

    # Tally sizes
    per_fp = {}   # fp -> dict(count, w, l, area_each, area_total)
    unknown = []  # list of (fp, ref)

    margin = args.margin
    def inflate(w, l):
        return (w + 2*margin, l + 2*margin)

    total_area = 0.0
    for fp, ref, flags in selected:
        size = None

        # 1) override exact
        if fp in override_exact:
            size = override_exact[fp]
        # 2) override via longest prefix match
        if size is None:
            for pref in override_prefix:
                if fp.startswith(pref) and pref not in override_exact:
                    size = overrides[pref]
                    break
        # 3) builtin
        if size is None:
            size = lookup_size(fp)

        if size is None:
            unknown.append((fp, ref))
            continue

        w, l = size
        iw, il = inflate(w, l)
        a = iw * il
        total_area += a
        key = fp
        if key not in per_fp:
            per_fp[key] = dict(count=0, w=w, l=l, iw=iw, il=il, area_each=a, area_total=0.0)
        per_fp[key]["count"] += 1
        per_fp[key]["area_total"] += a

    used_pct_of_board = 100.0 * total_area / board_area if board_area else 0.0
    used_pct_of_target = 100.0 * total_area / target_area if target_area else 0.0
    pass_fit = total_area <= target_area

    # Report
    print(f"Board: {board_w:.3f} mm x {board_h:.3f} mm  (area {board_area:.1f} mm^2)")
    print(f"Target utilization: {args.util:.0%}  -> allowed component area {target_area:.1f} mm^2")
    print(f"Courtyard margin per side: {margin:.2f} mm (adds {(2*margin):.2f} mm to width & length)")
    print()
    print(f"Parsed elements on {args.side.upper()} side: {len(selected)}")
    print(f"Known-size elements: {sum(v['count'] for v in per_fp.values())}")
    print(f"Unknown-size elements: {len(unknown)}")
    if unknown:
        uniq = {}
        for fp, ref in unknown:
            uniq[fp] = uniq.get(fp, 0) + 1
        top = sorted(uniq.items(), key=lambda x: -x[1])[:12]
        print("  Unknown footprints (count): " + ", ".join([f"{k} ({v})" for k, v in top]))
        print("  Tip: supply exact/prefix sizes with --sizes my_sizes.yaml (see example below)")

    print()
    print("Per-footprint totals (inflated by margin):")
    print("  {:<40s} {:>6s}  {:>8s} x {:>8s} mm   {:>10s} mm^2".format("Footprint", "Qty", "W", "L", "Area total"))
    for fp, data in sorted(per_fp.items(), key=lambda kv: -kv[1]["area_total"]):
        print(f"  {fp:<40s} {data['count']:>6d}  {data['iw']:>8.2f} x {data['il']:>8.2f}   {data['area_total']:>10.1f}")

    print()
    print(f"TOTAL component area (inflated): {total_area:.1f} mm^2")
    print(f"Occupancy vs whole board: {used_pct_of_board:.1f}%")
    print(f"Occupancy vs target ({args.util:.0%} of board): {used_pct_of_target:.1f}%")
    print()
    print("RESULT:", "✅ FITS within target utilization" if pass_fit else "❌ EXCEEDS target utilization")
    if not pass_fit:
        req_area = total_area / args.util if args.util > 0 else float('inf')
        req_w = board_w
        req_h = req_area / req_w if req_w > 0 else float('inf')
        print(f"At {args.util:.0%} util, you’d need at least ~{req_area:.0f} mm^2 per side.")
        print(f"For current width {board_w:.1f} mm, min height ≈ {req_h:.1f} mm.")

    # Example for overrides (print only if asked explicitly)
    if args.sizes and not overrides:
        print("\nWARNING: --sizes provided but contained no valid entries.")
    elif not args.sizes:
        print("""
# To override/add sizes, create my_sizes.yaml like:
# (keys can be exact footprint names or prefixes)
#
# ESP32-WROOM: [18.0, 25.5]
# CONN_DT13-48PABCD-R015: [40.0, 70.0]
# SSOP-28-10.19x5.30: {w: 10.5, l: 5.6}
#
# Then run:
#   python3 pcb_fit_estimator.py <file>.pcb --board 5x6.5in --sizes my_sizes.yaml
""".strip())

if __name__ == "__main__":
    main()
