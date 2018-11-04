
import pyparsing as pp

from geda_pcb import *


    
pcb_float = pp.Combine(pp.Optional(pp.Literal('-')) + pp.Word(pp.nums + '.'))
pcb_dimen = pp.Combine(pcb_float + 
                       pp.Optional(pp.Or([pp.Literal('mil'), pp.Literal('mm')])))
def parse_dimen(toks):
    s = toks[0]
    if s[-3:] == 'mil':
        return miltomm(float(s[0:-3]))
    elif s[-2:] == 'mm':
        return float(s[0:-2])
    else:
        return tomm(float(s))
        
pcb_dimen.setParseAction(parse_dimen)

pcb_coords = pp.Combine(pcb_float + pp.White() +
                        pcb_float + 
                        pp.Optional(pp.Or([pp.Literal('mil'), pp.Literal('mm')])))
def parse_coords(toks):
    print 'PC', toks
    s = toks[0]
    if s[-3:] == 'mil':
        return Coord(map(miltomm, map(float, s[0:-3].split(' '))))
    elif s[-2:] == 'mm':
        return Coord(map(float, s[0:-2].split(' ')))
    else:
        raise NotImplementedError, toks

pcb_coords.setParseAction(parse_coords)
    

pcb_int = pp.Combine(pp.Optional(pp.Literal('-')) + pp.Word(pp.nums))
pcb_hex = pp.Combine('0x' + pp.Word(pp.hexnums))
pcb_str = pp.dblQuotedString.setParseAction(pp.removeQuotes)
pcb_sstr = pp.Literal("'").suppress() + pp.Regex('.', flags=re.DOTALL) + pp.Literal("'").suppress()
#pcb_sstr = pp.Literal("'").suppress() + pp.Regex('.') + pp.Literal("'").suppress()
pcb_sstr.leaveWhitespace().setParseAction(lambda toks: toks[0])
pcb_sflags = pp.Or([pcb_hex, pcb_str])
pcb_body_end = pp.LineStart() + ')'
pcb_start = pp.Or([pp.Literal('['), pp.Literal('(')]).suppress()
pcb_end = pp.Or([pp.Literal(']'), pp.Literal(')')]).suppress()
pcb_lbrac = pp.Literal('[').suppress()
pcb_rbrac = pp.Literal(']').suppress()
pcb_lpar = pp.Literal('(').suppress()
pcb_rpar = pp.Literal(')').suppress()
pcb_comment = pp.Or([pp.LineStart() + pp.Literal('#') + pp.restOfLine + pp.LineEnd(),
                     pp.LineStart() + pp.LineEnd()])

pcb_pad = pp.Literal('Pad').suppress() + pcb_lbrac + \
    pcb_dimen.setResultsName('x1') + \
    pcb_dimen.setResultsName('y1') + \
    pcb_dimen.setResultsName('x2') + \
    pcb_dimen.setResultsName('y2') + \
    pcb_dimen.setResultsName('thickness') + \
    pcb_dimen.setResultsName('clearance') + \
    pcb_dimen.setResultsName('mask') + \
    pcb_str.setResultsName('name') + \
    pcb_str.setResultsName('number') + \
    pcb_sflags.setResultsName('flags') + pcb_rbrac
pcb_pad.setParseAction(lambda toks: GEDAPCBPad(toks.asDict()))

pcb_pin = pp.Literal('Pin').suppress() + pcb_lbrac + \
    pcb_dimen.setResultsName('x') + \
    pcb_dimen.setResultsName('y') + \
    pcb_dimen.setResultsName('thickness') + \
    pcb_dimen.setResultsName('clearance') + \
    pcb_dimen.setResultsName('mask') + \
    pcb_dimen.setResultsName('hole_dia') + \
    pcb_str.setResultsName('name') + \
    pcb_str.setResultsName('number') + \
    pcb_sflags.setResultsName('flags') + pcb_rbrac
pcb_pin.setParseAction(lambda toks: GEDAPCBPin(toks.asDict()))

pcb_element_line = pp.Literal('ElementLine').suppress() + pcb_lbrac + \
    pcb_dimen.setResultsName('x1') + \
    pcb_dimen.setResultsName('y1') + \
    pcb_dimen.setResultsName('x2') + \
    pcb_dimen.setResultsName('y2') + \
    pcb_dimen.setResultsName('thickness') + pcb_rbrac
pcb_element_line.setParseAction(lambda toks: GEDAPCBElementLine(toks.asDict()))




pcb_element_arc = pp.Literal('ElementArc').suppress() + pcb_lbrac + \
    pcb_dimen.setResultsName('x') + \
    pcb_dimen.setResultsName('y') + \
    pcb_dimen.setResultsName('width') + \
    pcb_dimen.setResultsName('height') + \
    pcb_int.setResultsName('start_angle') + \
    pcb_int.setResultsName('delta_angle') + \
    pcb_dimen.setResultsName('thickness') + pcb_rbrac
pcb_element_arc.setParseAction(lambda toks: GEDAPCBElementArc(toks.asDict()))


pcb_attribute = pp.Literal('Attribute').suppress() + pcb_lpar + \
                pcb_str.setResultsName("name") +\
                pcb_str.setResultsName("value") +\
                pcb_rpar
pcb_attribute.setParseAction(lambda toks: GEDAPCBAttribute(toks.asDict()))

pcb_element_child = pp.Or([pcb_attribute,
                           pcb_pad,
                           pcb_pin,
                           pcb_element_line,
                           pcb_element_arc])


pcb_via = pp.Literal('Via').suppress() + pcb_lbrac + \
    pcb_dimen.setResultsName('x') + \
    pcb_dimen.setResultsName('y') + \
    pcb_dimen.setResultsName('thickness') + \
    pcb_dimen.setResultsName('clearance') + \
    pcb_dimen.setResultsName('mask') + \
    pcb_dimen.setResultsName('hole_dia') + \
    pcb_str.setResultsName('name') + \
    pcb_sflags.setResultsName('flags') + pcb_rbrac
pcb_via.setParseAction(lambda toks: GEDAPCBVia(toks.asDict()))

pcb_rat = pp.Literal('Rat').suppress() + pcb_lbrac + \
    pcb_dimen.setResultsName('x1') + \
    pcb_dimen.setResultsName('y1') + \
    pcb_int.setResultsName('group1') + \
    pcb_dimen.setResultsName('x2') + \
    pcb_dimen.setResultsName('y2') + \
    pcb_int.setResultsName('group2') + \
    pcb_sflags.setResultsName('flags') + pcb_rbrac
pcb_rat.setParseAction(lambda toks: GEDAPCBRat(toks.asDict()))

pcb_element = pp.Literal('Element').suppress() + \
    pp.Or([pp.Literal('[').suppress() + \
               pcb_sflags.setResultsName('flags') + \
               pcb_str.setResultsName('desc') + \
               pcb_str.setResultsName('name') + \
               pcb_str.setResultsName('value') + \
               pcb_dimen.setResultsName('mx') + \
               pcb_dimen.setResultsName('my') + \
               pcb_dimen.setResultsName('tx') + \
               pcb_dimen.setResultsName('ty') + \
               pcb_int.setResultsName('tdir') + \
               pcb_int.setResultsName('tscale') + \
               pcb_sflags.setResultsName('tflags') + \
               pp.Literal(']').suppress(),
           pp.Literal('(').suppress() + \
               pcb_hex.setResultsName('flags') + \
               pcb_str.setResultsName('desc') + \
               pcb_str.setResultsName('name') + \
               pcb_str.setResultsName('value') + \
               pp.Optional(pcb_int.setResultsName('mx') + \
                               pcb_int.setResultsName('my')) + \
               pcb_int.setResultsName('tx') + \
               pcb_int.setResultsName('ty') + \
               pcb_int.setResultsName('tdir') + \
               pcb_int.setResultsName('tscale') + \
               pcb_hex.setResultsName('tflags') + \
               pp.Literal(')').suppress(),
           pp.Literal('(').suppress() + \
               pp.Optional(pcb_hex.setResultsName('flags')) + \
               pcb_str.setResultsName('desc') + \
               pcb_str.setResultsName('name') + \
               pcb_int.setResultsName('tx') + \
               pcb_int.setResultsName('ty') + \
               pcb_int.setResultsName('tdir') + \
               pcb_int.setResultsName('tscale') + \
               pcb_hex.setResultsName('tflags') + \
               pp.Literal(')').suppress()]) + \
               pcb_lpar + \
               pp.ZeroOrMore(pcb_element_child).setResultsName('children') + \
               pcb_rpar

pcb_element.setParseAction(lambda toks: GEDAPCBElement(toks.asDict()))

pcb_symbol_line = pp.Literal('SymbolLine').suppress() + pcb_lbrac + \
    pcb_dimen.setResultsName('x1') + \
    pcb_dimen.setResultsName('y1') + \
    pcb_dimen.setResultsName('x2') + \
    pcb_dimen.setResultsName('y2') + \
    pcb_dimen.setResultsName('thickness') + pcb_rbrac
pcb_symbol_line.setParseAction(lambda toks: GEDAPCBSymbolLine(toks.asDict()))
           
pcb_symbol_child = pcb_symbol_line

pcb_symbol = pp.Literal('Symbol').suppress() + \
    pp.Or([pp.Literal('[').suppress() + \
               pcb_sstr.setResultsName('name') + \
               pcb_dimen.setResultsName('width') + \
               pp.Literal(']').suppress(),
           pp.Literal('(').suppress() + \
               pcb_sstr.setResultsName('name') + \
               pcb_dimen.setResultsName('width') + \
               pp.Literal(')').suppress()]) + \
               pcb_lpar + \
               pp.ZeroOrMore(pcb_symbol_child).setResultsName('children') + \
               pcb_rpar

pcb_symbol.setParseAction(lambda toks: GEDAPCBSymbol(toks.asDict()))

pcb_line = pp.Literal('Line').suppress() + pcb_lbrac + \
    pcb_dimen.setResultsName('x1') + \
    pcb_dimen.setResultsName('y1') + \
    pcb_dimen.setResultsName('x2') + \
    pcb_dimen.setResultsName('y2') + \
    pcb_dimen.setResultsName('thickness') + \
    pcb_dimen.setResultsName('clearance') + \
    pcb_sflags.setResultsName('flags') + \
    pcb_rbrac
pcb_line.setParseAction(lambda toks: GEDAPCBLine(toks.asDict()))

pcb_arc = pp.Literal('Arc').suppress() + pcb_lbrac + \
    pcb_dimen.setResultsName('x') + \
    pcb_dimen.setResultsName('y') + \
    pcb_dimen.setResultsName('width') + \
    pcb_dimen.setResultsName('height') + \
    pcb_dimen.setResultsName('thickness') + \
    pcb_dimen.setResultsName('clearance') + \
    pcb_int.setResultsName('start_angle') + \
    pcb_int.setResultsName('delta_angle') + \
    pcb_sflags.setResultsName('flags') + pcb_rbrac
pcb_arc.setParseAction(lambda toks: GEDAPCBArc(toks.asDict()))

pcb_text = pp.Literal('Text').suppress() + pcb_lbrac + \
    pcb_dimen.setResultsName('x') + \
    pcb_dimen.setResultsName('y') + \
    pcb_int.setResultsName('tdir') + \
    pcb_int.setResultsName('tscale') + \
    pp.dblQuotedString.setResultsName('name') + \
    pcb_sflags.setResultsName('flags') + \
    pcb_rbrac
pcb_text.setParseAction(lambda toks: GEDAPCBText(toks.asDict()))
           
pcb_polypoint = pcb_lbrac + \
    pcb_dimen.setResultsName('x') + \
    pcb_dimen.setResultsName('y') + \
    pcb_rbrac
pcb_polypoint.setParseAction(lambda toks: GEDAPCBPolyPoint(toks.asDict()))

pcb_polyhole = pp.Literal('Hole').suppress() + \
    pcb_lpar + \
    pp.ZeroOrMore(pcb_polypoint).setResultsName('children') + \
    pcb_rpar
pcb_polyhole.setParseAction(lambda toks: GEDAPCBPolyHole(toks.asDict()))

pcb_polygon = pp.Literal('Polygon').suppress() + \
    pp.Literal('(').suppress() + \
    pcb_sflags.setResultsName('flags') + \
    pp.Literal(')').suppress() + \
    pcb_lpar + \
    pp.Group(pp.ZeroOrMore(pcb_polypoint)).setResultsName('points') + \
    pp.Group(pp.ZeroOrMore(pcb_polyhole)).setResultsName('holes') + \
    pcb_rpar
pcb_polygon.setParseAction(lambda toks: GEDAPCBPolygon(toks.asDict()))

pcb_layer_child = pp.Or([pcb_line, pcb_polygon, pcb_text, pcb_arc])

pcb_layer = pp.Literal('Layer').suppress() + \
    pp.Literal('(').suppress() + \
    pcb_int.setResultsName('layer_num') + \
    pp.dblQuotedString.setResultsName('name') + \
    pp.Literal(')').suppress() + \
    pcb_lpar + \
    pp.Group(pp.ZeroOrMore(pcb_layer_child)).setResultsName('children') + \
    pcb_rpar
pcb_layer.setParseAction(lambda toks: GEDAPCBLayer(toks.asDict()))

pcb_connect = pp.Literal('Connect').suppress() + \
    pp.Literal('("').suppress() + \
    pp.Word(pp.printables, excludeChars='-"').setResultsName('refdes') + \
    pp.Literal('-').suppress() + \
    pp.Word(pp.printables, excludeChars='-"').setResultsName('number') + \
    pp.Literal('")').suppress()
pcb_connect.setParseAction(lambda toks: GEDAPCBConnect(toks.asDict()))


pcb_net = pp.Literal('Net').suppress() + \
    pp.Literal('(').suppress() + \
    pp.dblQuotedString.setResultsName('name') + \
    pp.dblQuotedString.setResultsName('style') + \
    pp.Literal(')').suppress() + \
    pcb_lpar + \
    pp.Group(pp.ZeroOrMore(pcb_connect)).setResultsName('children') + \
    pcb_rpar
pcb_net.setParseAction(lambda toks: GEDAPCBNet(toks.asDict()))

pcb_netlist = pp.Literal('NetList').suppress() + \
    pp.Literal('()').suppress() + \
    pcb_lpar + \
    pp.Group(pp.ZeroOrMore(pcb_net)).setResultsName('children') + \
    pcb_rpar
pcb_netlist.setParseAction(lambda toks: GEDAPCBNetList(toks.asDict()))

pcb_attribute = pp.Literal('Attribute').suppress() + \
    pp.Literal('(').suppress() + \
    pp.dblQuotedString.setResultsName('name') + \
    pp.dblQuotedString.setResultsName('value') + \
    pp.Literal(')').suppress()
pcb_attribute.setParseAction(lambda toks: GEDAPCBAttribute(toks.asDict()))

    
pcb_filecontent = pp.Group(pp.ZeroOrMore(pp.Or([pp.OneOrMore(pcb_netlist), 
                                                pp.OneOrMore(pcb_layer),
                                                pp.OneOrMore(pcb_symbol),
                                                pp.OneOrMore(pcb_rat),
                                                pp.OneOrMore(pcb_element), 
                                                pp.OneOrMore(pcb_via),
                                                pp.OneOrMore(pcb_attribute)]))
                           ).setResultsName('children')
#def f2(toks):
#    print toks
#    for t in toks:
#        print t.asDict()
#pcb_filecontent.setParseAction(f2)

pcb_file = pp.ZeroOrMore(pcb_comment).suppress() + \
    pp.Literal('FileVersion[').suppress() + \
    pcb_int.setResultsName('fileversion') + \
    pp.Literal(']').suppress() + \
    pp.Literal('PCB[').suppress() + \
    pp.dblQuotedString.setResultsName('pcbname') + \
    pcb_dimen.setResultsName('sizex') + \
    pcb_dimen.setResultsName('sizey') + \
    pp.Literal(']').suppress() + \
    pp.Literal('Grid[').suppress() + \
    pcb_float.setResultsName('step') + \
    pcb_float.setResultsName('gridoffx') + \
    pcb_float.setResultsName('gridoffy') + \
    pcb_int.setResultsName('gridvisible') + \
    pp.Literal(']').suppress() + \
    pp.Optional(pp.Literal('Cursor[').suppress() + \
                pcb_int.setResultsName('cursorx') + \
                pcb_int.setResultsName('cursory') + \
                pcb_float.setResultsName('zoom') + \
                pp.Literal(']').suppress()) + \
    pp.Literal('PolyArea[').suppress() + \
    pcb_float.setResultsName('minpolyarea') + \
    pp.Literal(']').suppress() + \
    pp.Literal('Thermal[').suppress() + \
    pcb_float.setResultsName('thermalscale') + \
    pp.Literal(']').suppress() + \
    pp.Literal('DRC[').suppress() + \
    pcb_dimen.setResultsName('drcbloat') + \
    pcb_dimen.setResultsName('drcshrink') + \
    pcb_dimen.setResultsName('drcline') + \
    pcb_dimen.setResultsName('drcsilk') + \
    pcb_dimen.setResultsName('drcdrill') + \
    pcb_dimen.setResultsName('drcring') + \
    pp.Literal(']').suppress() + \
    pp.Literal('Flags(').suppress() + \
    pcb_sflags.setResultsName('pcbflags') + \
    pp.Literal(')').suppress() + \
    pp.Literal('Groups("').suppress() + \
    pp.Word(pp.nums + ',:cs').setResultsName('groups_str') + \
    pp.Literal('")').suppress() + \
    pp.Literal('Styles["').suppress() + \
    pp.Word(pp.printables, excludeChars='"').setResultsName('styles_str') +\
    pp.Literal('"]').suppress() + \
    pcb_filecontent + pp.StringEnd()
pcb_file.setParseAction(lambda toks: GEDAPCBFile(toks.asDict()))





class GEDAPCBFileParser(object):

    def __init__(self):
        pass

    def load_element_file(self, f):
        return pcb_element.parseFile(f)[0]

    def load_pcb_file(self, f):
        return pcb_file.parseFile(f)[0]


    def parse_string_file(self, s):
        return pcb_file.parseString(s)[0]

    def parse_string_element(self, s):
        return pcb_filecontent.parseString(s)[0]
    
