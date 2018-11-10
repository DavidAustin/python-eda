# Python-EDA
# Copyright (C) 2018 David Austin
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import pyparsing as pp

from geda_pcb import *


class GEDAPCBFileParser(object):

    def __init__(self):
        self.pcb_float = pp.Combine(pp.Optional(pp.Literal('-')) +
                                    pp.Word(pp.nums + '.'))
        self.pcb_dimen = pp.Combine(self.pcb_float + 
                                    pp.Optional(pp.Or([pp.Literal('mil'),
                                                       pp.Literal('mm')])))
        def parse_dimen(toks):
            s = toks[0]
            if s[-3:] == 'mil':
                return miltomm(float(s[0:-3]))
            elif s[-2:] == 'mm':
                return float(s[0:-2])
            else:
                return tomm(float(s))
        self.pcb_dimen.setParseAction(parse_dimen)

        self.pcb_coords = pp.Combine(self.pcb_float + pp.White() +
                                     self.pcb_float + 
                                     pp.Optional(pp.Or([pp.Literal('mil'),
                                                        pp.Literal('mm')])))
        def parse_coords(toks):
            s = toks[0]
            if s[-3:] == 'mil':
                return Coord(map(miltomm, map(float, s[0:-3].split(' '))))
            elif s[-2:] == 'mm':
                return Coord(map(float, s[0:-2].split(' ')))
            else:
                raise NotImplementedError, toks
        self.pcb_coords.setParseAction(parse_coords)
    

        self.pcb_int = pp.Combine(pp.Optional(pp.Literal('-')) +
                                  pp.Word(pp.nums))
        self.pcb_hex = pp.Combine('0x' + pp.Word(pp.hexnums))
        self.pcb_str = pp.dblQuotedString.setParseAction(pp.removeQuotes)
        self.pcb_sstr = (pp.Literal("'").suppress() +
                         pp.Regex('.', flags=re.DOTALL) +
                         pp.Literal("'").suppress())
        #pcb_sstr = pp.Literal("'").suppress() +
        #pp.Regex('.') + pp.Literal("'").suppress()
        self.pcb_sstr.leaveWhitespace().setParseAction(lambda toks: toks[0])
        self.pcb_sflags = pp.Or([self.pcb_hex, self.pcb_str])
        self.pcb_body_end = pp.LineStart() + ')'
        self.pcb_start = pp.Or([pp.Literal('['), pp.Literal('(')]).suppress()
        self.pcb_end = pp.Or([pp.Literal(']'), pp.Literal(')')]).suppress()
        self.pcb_lbrac = pp.Literal('[').suppress()
        self.pcb_rbrac = pp.Literal(']').suppress()
        self.pcb_lpar = pp.Literal('(').suppress()
        self.pcb_rpar = pp.Literal(')').suppress()
        self.pcb_comment = pp.Or([pp.LineStart() +
                                  pp.Literal('#') + pp.restOfLine +
                                  pp.LineEnd(),
                                  pp.LineStart() + pp.LineEnd()])

        self.pcb_pad = (
            pp.Literal('Pad').suppress() + self.pcb_lbrac + 
            self.pcb_dimen.setResultsName('x1') + 
            self.pcb_dimen.setResultsName('y1') + 
            self.pcb_dimen.setResultsName('x2') + 
            self.pcb_dimen.setResultsName('y2') + 
            self.pcb_dimen.setResultsName('thickness') + 
            self.pcb_dimen.setResultsName('clearance') + 
            self.pcb_dimen.setResultsName('mask') + 
            self.pcb_str.setResultsName('name') + 
            self.pcb_str.setResultsName('number') + 
            self.pcb_sflags.setResultsName('flags') + self.pcb_rbrac
        )
        self.pcb_pad.setParseAction(lambda toks: GEDAPCBPad(toks.asDict()))

        self.pcb_pin = (
            pp.Literal('Pin').suppress() + self.pcb_lbrac + 
            self.pcb_dimen.setResultsName('x') + 
            self.pcb_dimen.setResultsName('y') + 
            self.pcb_dimen.setResultsName('thickness') + 
            self.pcb_dimen.setResultsName('clearance') + 
            self.pcb_dimen.setResultsName('mask') + 
            self.pcb_dimen.setResultsName('hole_dia') + 
            self.pcb_str.setResultsName('name') + 
            self.pcb_str.setResultsName('number') + 
            self.pcb_sflags.setResultsName('flags') + self.pcb_rbrac
        )
        self.pcb_pin.setParseAction(lambda toks: GEDAPCBPin(toks.asDict()))

        self.pcb_element_line = (
            pp.Literal('ElementLine').suppress() + 
            self.pcb_lbrac + 
            self.pcb_dimen.setResultsName('x1') + 
            self.pcb_dimen.setResultsName('y1') + 
            self.pcb_dimen.setResultsName('x2') + 
            self.pcb_dimen.setResultsName('y2') + 
            self.pcb_dimen.setResultsName('thickness') + 
            self.pcb_rbrac
        )
        self.pcb_element_line.setParseAction(
            lambda toks: GEDAPCBElementLine(toks.asDict()))



        self.pcb_element_arc = (
            pp.Literal('ElementArc').suppress() + 
            self.pcb_lbrac + 
            self.pcb_dimen.setResultsName('x') + 
            self.pcb_dimen.setResultsName('y') + 
            self.pcb_dimen.setResultsName('width') + 
            self.pcb_dimen.setResultsName('height') + 
            self.pcb_int.setResultsName('start_angle') + 
            self.pcb_int.setResultsName('delta_angle') + 
            self.pcb_dimen.setResultsName('thickness') + 
            self.pcb_rbrac
        )
        self.pcb_element_arc.setParseAction(
            lambda toks: GEDAPCBElementArc(toks.asDict()))


        self.pcb_attribute = (
            pp.Literal('Attribute').suppress() + 
            self.pcb_lpar + 
            self.pcb_str.setResultsName("name") +
            self.pcb_str.setResultsName("value") +
            self.pcb_rpar
        )
        self.pcb_attribute.setParseAction(
            lambda toks: GEDAPCBAttribute(toks.asDict()))

        self.pcb_element_child = pp.Or([self.pcb_attribute,
                           self.pcb_pad,
                           self.pcb_pin,
                           self.pcb_element_line,
                           self.pcb_element_arc])

        self.pcb_via = (
            pp.Literal('Via').suppress() + self.pcb_lbrac + 
            self.pcb_dimen.setResultsName('x') + 
            self.pcb_dimen.setResultsName('y') + 
            self.pcb_dimen.setResultsName('thickness') + 
            self.pcb_dimen.setResultsName('clearance') + 
            self.pcb_dimen.setResultsName('mask') + 
            self.pcb_dimen.setResultsName('hole_dia') + 
            self.pcb_str.setResultsName('name') + 
            self.pcb_sflags.setResultsName('flags') + 
            self.pcb_rbrac
        )
        self.pcb_via.setParseAction(lambda toks: GEDAPCBVia(toks.asDict()))

        self.pcb_rat = (
            pp.Literal('Rat').suppress() + self.pcb_lbrac + 
            self.pcb_dimen.setResultsName('x1') + 
            self.pcb_dimen.setResultsName('y1') + 
            self.pcb_int.setResultsName('group1') + 
            self.pcb_dimen.setResultsName('x2') + 
            self.pcb_dimen.setResultsName('y2') + 
            self.pcb_int.setResultsName('group2') + 
            self.pcb_sflags.setResultsName('flags') + self.pcb_rbrac
        )
        self.pcb_rat.setParseAction(lambda toks: GEDAPCBRat(toks.asDict()))

        self.pcb_element = (
            pp.Literal('Element').suppress() + 
            pp.Or([pp.Literal('[').suppress() + 
                   self.pcb_sflags.setResultsName('flags') + 
                   self.pcb_str.setResultsName('desc') + 
                   self.pcb_str.setResultsName('name') + 
                   self.pcb_str.setResultsName('value') + 
                   self.pcb_dimen.setResultsName('mx') + 
                   self.pcb_dimen.setResultsName('my') + 
                   self.pcb_dimen.setResultsName('tx') + 
                   self.pcb_dimen.setResultsName('ty') + 
                   self.pcb_int.setResultsName('tdir') + 
                   self.pcb_int.setResultsName('tscale') + 
                   self.pcb_sflags.setResultsName('tflags') + 
                   pp.Literal(']').suppress(),
                   pp.Literal('(').suppress() + 
                   self.pcb_hex.setResultsName('flags') + 
                   self.pcb_str.setResultsName('desc') + 
                   self.pcb_str.setResultsName('name') + 
                   self.pcb_str.setResultsName('value') + 
                   pp.Optional(
                       self.pcb_int.setResultsName('mx') + 
                       self.pcb_int.setResultsName('my')) + 
                   self.pcb_int.setResultsName('tx') + 
                   self.pcb_int.setResultsName('ty') + 
                   self.pcb_int.setResultsName('tdir') + 
                   self.pcb_int.setResultsName('tscale') + 
                   self.pcb_hex.setResultsName('tflags') + 
                   pp.Literal(')').suppress(),
                   pp.Literal('(').suppress() + 
                   pp.Optional(
                       self.pcb_hex.setResultsName('flags')) + 
                   self.pcb_str.setResultsName('desc') + 
                   self.pcb_str.setResultsName('name') + 
                   self.pcb_int.setResultsName('tx') + 
                   self.pcb_int.setResultsName('ty') + 
                   self.pcb_int.setResultsName('tdir') + 
                   self.pcb_int.setResultsName('tscale') + 
                   self.pcb_hex.setResultsName('tflags') + 
                   pp.Literal(')').suppress()]) + 
            self.pcb_lpar + 
            pp.ZeroOrMore(self.pcb_element_child).setResultsName('children') + 
            self.pcb_rpar
        )
        self.pcb_element.setParseAction(
            lambda toks: GEDAPCBElement(toks.asDict()))

        self.pcb_symbol_line = (
            pp.Literal('SymbolLine').suppress() + 
            self.pcb_lbrac + 
            self.pcb_dimen.setResultsName('x1') + 
            self.pcb_dimen.setResultsName('y1') + 
            self.pcb_dimen.setResultsName('x2') + 
            self.pcb_dimen.setResultsName('y2') + 
            self.pcb_dimen.setResultsName('thickness') + 
            self.pcb_rbrac
        )
        self.pcb_symbol_line.setParseAction(
            lambda toks: GEDAPCBSymbolLine(toks.asDict()))
           
        self.pcb_symbol_child = self.pcb_symbol_line

        self.pcb_symbol = (
            pp.Literal('Symbol').suppress() + 
            pp.Or([pp.Literal('[').suppress() + 
                   self.pcb_sstr.setResultsName('name') + 
                   self.pcb_dimen.setResultsName('width') + 
                   pp.Literal(']').suppress(),
                   pp.Literal('(').suppress() + 
                   self.pcb_sstr.setResultsName('name') + 
                   self.pcb_dimen.setResultsName('width') + 
                   pp.Literal(')').suppress()]) + 
            self.pcb_lpar + 
            pp.ZeroOrMore(self.pcb_symbol_child).setResultsName('children') + 
            self.pcb_rpar
        )
        self.pcb_symbol.setParseAction(
            lambda toks: GEDAPCBSymbol(toks.asDict()))

        self.pcb_line = (
            pp.Literal('Line').suppress() + self.pcb_lbrac + 
            self.pcb_dimen.setResultsName('x1') + 
            self.pcb_dimen.setResultsName('y1') + 
            self.pcb_dimen.setResultsName('x2') + 
            self.pcb_dimen.setResultsName('y2') + 
            self.pcb_dimen.setResultsName('thickness') + 
            self.pcb_dimen.setResultsName('clearance') + 
            self.pcb_sflags.setResultsName('flags') + 
            self.pcb_rbrac
        )
        self.pcb_line.setParseAction(lambda toks: GEDAPCBLine(toks.asDict()))

        self.pcb_arc = (
            pp.Literal('Arc').suppress() + self.pcb_lbrac + 
            self.pcb_dimen.setResultsName('x') + 
            self.pcb_dimen.setResultsName('y') + 
            self.pcb_dimen.setResultsName('width') + 
            self.pcb_dimen.setResultsName('height') + 
            self.pcb_dimen.setResultsName('thickness') + 
            self.pcb_dimen.setResultsName('clearance') + 
            self.pcb_int.setResultsName('start_angle') + 
            self.pcb_int.setResultsName('delta_angle') + 
            self.pcb_sflags.setResultsName('flags') + self.pcb_rbrac
        )
        self.pcb_arc.setParseAction(lambda toks: GEDAPCBArc(toks.asDict()))

        self.pcb_text = (
            pp.Literal('Text').suppress() + self.pcb_lbrac + 
            self.pcb_dimen.setResultsName('x') + 
            self.pcb_dimen.setResultsName('y') + 
            self.pcb_int.setResultsName('tdir') + 
            self.pcb_int.setResultsName('tscale') + 
            pp.dblQuotedString.setResultsName('name') + 
            self.pcb_sflags.setResultsName('flags') + 
            self.pcb_rbrac
        )
        self.pcb_text.setParseAction(lambda toks: GEDAPCBText(toks.asDict()))
           
        self.pcb_polypoint = (
            self.pcb_lbrac + 
            self.pcb_dimen.setResultsName('x') + 
            self.pcb_dimen.setResultsName('y') + 
            self.pcb_rbrac
        )
        self.pcb_polypoint.setParseAction(
            lambda toks: GEDAPCBPolyPoint(toks.asDict()))

        self.pcb_polyhole = (
            pp.Literal('Hole').suppress() + 
            self.pcb_lpar + 
            pp.ZeroOrMore(self.pcb_polypoint).setResultsName('children') + 
                            self.pcb_rpar
        )
        self.pcb_polyhole.setParseAction(
            lambda toks: GEDAPCBPolyHole(toks.asDict()))

        self.pcb_polygon = (
            pp.Literal('Polygon').suppress() + 
            pp.Literal('(').suppress() + 
            self.pcb_sflags.setResultsName('flags') + 
            pp.Literal(')').suppress() + 
            self.pcb_lpar + 
            pp.Group(pp.ZeroOrMore(self.pcb_polypoint))
                .setResultsName('points') + 
            pp.Group(pp.ZeroOrMore(self.pcb_polyhole))
                .setResultsName('holes') + 
            self.pcb_rpar
        )
        self.pcb_polygon.setParseAction(
            lambda toks: GEDAPCBPolygon(toks.asDict()))

        self.pcb_layer_child = pp.Or([self.pcb_line, self.pcb_polygon,
                                      self.pcb_text, self.pcb_arc])

        self.pcb_layer = (
            pp.Literal('Layer').suppress() + 
            pp.Literal('(').suppress() + 
            self.pcb_int.setResultsName('layer_num') + 
            pp.dblQuotedString.setResultsName('name') + 
            pp.Literal(')').suppress() + 
            self.pcb_lpar + 
            pp.Group(pp.ZeroOrMore(self.pcb_layer_child))
                .setResultsName('children') + 
            self.pcb_rpar
        )
        self.pcb_layer.setParseAction(lambda toks: GEDAPCBLayer(toks.asDict()))

        self.pcb_connect = (
            pp.Literal('Connect').suppress() + 
            pp.Literal('("').suppress() + 
            pp.Word(pp.printables, excludeChars='-"')
                .setResultsName('refdes') + 
            pp.Literal('-').suppress() + \
            pp.Word(pp.printables, excludeChars='-"')
                .setResultsName('number') + 
            pp.Literal('")').suppress()
        )
        self.pcb_connect.setParseAction(
            lambda toks: GEDAPCBConnect(toks.asDict()))


        self.pcb_net = (
            pp.Literal('Net').suppress() + 
            pp.Literal('(').suppress() + 
            pp.dblQuotedString.setResultsName('name') + 
            pp.dblQuotedString.setResultsName('style') + 
            pp.Literal(')').suppress() + 
            self.pcb_lpar + 
            pp.Group(pp.ZeroOrMore(self.pcb_connect))
                .setResultsName('children') + 
            self.pcb_rpar
        )
        self.pcb_net.setParseAction(lambda toks: GEDAPCBNet(toks.asDict()))

        self.pcb_netlist = (
            pp.Literal('NetList').suppress() + 
            pp.Literal('()').suppress() + 
            self.pcb_lpar + 
            pp.Group(pp.ZeroOrMore(self.pcb_net)).setResultsName('children') + 
            self.pcb_rpar
        )
        self.pcb_netlist.setParseAction(
            lambda toks: GEDAPCBNetList(toks.asDict()))

        self.pcb_attribute = (
            pp.Literal('Attribute').suppress() + 
            pp.Literal('(').suppress() + 
            pp.dblQuotedString.setResultsName('name') + 
            pp.dblQuotedString.setResultsName('value') + 
            pp.Literal(')').suppress()
        )
        self.pcb_attribute.setParseAction(
            lambda toks: GEDAPCBAttribute(toks.asDict()))

    
        self.pcb_filecontent = pp.Group(pp.ZeroOrMore(pp.Or(
            [pp.OneOrMore(self.pcb_netlist), 
             pp.OneOrMore(self.pcb_layer),
             pp.OneOrMore(self.pcb_symbol),
             pp.OneOrMore(self.pcb_rat),
             pp.OneOrMore(self.pcb_element), 
             pp.OneOrMore(self.pcb_via),
             pp.OneOrMore(self.pcb_attribute)]))
        ).setResultsName('children')
        #def f2(toks):
        #    print toks
        #    for t in toks:
        #        print t.asDict()
        #pcb_filecontent.setParseAction(f2)

        self.pcb_file = (
            pp.ZeroOrMore(self.pcb_comment).suppress() + 
            pp.Literal('FileVersion[').suppress() + 
            self.pcb_int.setResultsName('fileversion') + 
            pp.Literal(']').suppress() + 
            pp.Literal('PCB[').suppress() + 
            pp.dblQuotedString.setResultsName('pcbname') + 
            self.pcb_dimen.setResultsName('sizex') + 
            self.pcb_dimen.setResultsName('sizey') + 
            pp.Literal(']').suppress() + 
            pp.Literal('Grid[').suppress() + 
            self.pcb_float.setResultsName('step') + 
            self.pcb_float.setResultsName('gridoffx') + 
            self.pcb_float.setResultsName('gridoffy') + 
            self.pcb_int.setResultsName('gridvisible') + 
            pp.Literal(']').suppress() + 
            pp.Optional(pp.Literal('Cursor[').suppress() + 
                        self.pcb_int.setResultsName('cursorx') + 
                        self.pcb_int.setResultsName('cursory') + 
                        self.pcb_float.setResultsName('zoom') + 
                        pp.Literal(']').suppress()) + 
            pp.Literal('PolyArea[').suppress() + 
            self.pcb_float.setResultsName('minpolyarea') + 
            pp.Literal(']').suppress() + 
            pp.Literal('Thermal[').suppress() + 
            self.pcb_float.setResultsName('thermalscale') + 
            pp.Literal(']').suppress() + 
            pp.Literal('DRC[').suppress() + 
            self.pcb_dimen.setResultsName('drcbloat') + 
            self.pcb_dimen.setResultsName('drcshrink') + 
            self.pcb_dimen.setResultsName('drcline') + 
            self.pcb_dimen.setResultsName('drcsilk') + 
            self.pcb_dimen.setResultsName('drcdrill') + 
            self.pcb_dimen.setResultsName('drcring') + 
            pp.Literal(']').suppress() + 
            pp.Literal('Flags(').suppress() + 
            self.pcb_sflags.setResultsName('pcbflags') + 
            pp.Literal(')').suppress() + 
            pp.Literal('Groups("').suppress() + 
            pp.Word(pp.nums + ',:cs').setResultsName('groups_str') + 
            pp.Literal('")').suppress() + 
            pp.Literal('Styles["').suppress() + 
            pp.Word(pp.printables, excludeChars='"')
                .setResultsName('styles_str') +
            pp.Literal('"]').suppress() + 
            self.pcb_filecontent + pp.StringEnd()
        )
        self.pcb_file.setParseAction(lambda toks: GEDAPCBFile(toks.asDict()))




    def load_element_file(self, f):
        return self.pcb_element.parseFile(f)[0]

    def load_pcb_file(self, f):
        return self.pcb_file.parseFile(f)[0]

    def parse_string_file(self, s):
        return self.pcb_file.parseString(s)[0]

    def parse_string_element(self, s):
        return self.pcb_filecontent.parseString(s)[0]
    
