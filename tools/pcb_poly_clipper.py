import sys
import os
import re
import pyclipper
from ast import literal_eval

filename = sys.argv[1]
cut = float(sys.argv[2])

if not os.path.exists(filename):
  print ("%s - File does not exist") % (filename)
  exit()

infile = open(filename, "r")
lines = infile.read()
infile.close()

# replace mil's with mm's
def fix_mil(matchobj):
    value = float(matchobj.group(0).replace("mil", ""))
    return str(round(value / 39.37, 4)) + "mm"
lines = re.sub(r'[-+]?[0-9]*\.?[0-9]+mil', fix_mil, lines)

# convert pcb to tuples of tuple pairs
lines = lines.replace("mm ", ", ")
lines = lines.replace("mm", "")
lines = lines.replace("\n", "")
lines = lines.replace("\t", "")
lines = lines.replace("] [", "), (")
lines = lines.replace("]", "))")
lines = lines.replace("[", "((")
subj = literal_eval(lines)

# multiply tuple elements by 10000
tuples = ()
for value in subj:
    new = (int(value[0] * 10000), int(value[1] * 10000))
    tuples = tuples + (new,)
subj = tuples

pco = pyclipper.PyclipperOffset()
pco.AddPath(subj, pyclipper.JT_ROUND, pyclipper.ET_CLOSEDPOLYGON)

solution = pco.Execute(cut * 10000)

# divide list elements by 10000
output = ""
i = 0
for i in range(len(solution[0])):
    new = "[%fmm %fmm] " % (float(round(solution[0][i][0] / 10000.0, 4)),
                            float(round(solution[0][i][1] / 10000.0, 4)))
    output += new
print (output)
