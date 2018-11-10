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
from gschem import *


class GschemFileParser(object):

    def __init__(self):
        #pp.ParserElement.setDefaultWhitespaceChars(' \t\r')
        # this messes with geda_pcb_parsing and unittest

        self.gschem_int = pp.Combine(pp.Optional(pp.Literal('-')) +
                                     pp.Word(pp.nums))
        self.gschem_str = pp.Word(pp.printables)
        self.gschem_linestr = pp.Regex('.*') + pp.lineEnd.suppress()
        
        self.gschem_version = (
            pp.lineStart.suppress() + 
            pp.Literal('v').suppress() + 
            self.gschem_int.setResultsName('version') + 
            self.gschem_int.setResultsName('fileversion') + 
            pp.lineEnd.suppress()
        )
        self.gschem_version.setParseAction(
            lambda toks: GschemVersion(toks.asDict()))


        def mk_int(toks):
            return int(toks[0])

        self.int_nl = pp.Word(pp.nums) + pp.lineEnd.suppress()
        self.int_nl.setParseAction(mk_int)

        self.gschem_text = (
            pp.lineStart.suppress() + 
            pp.Literal('T').suppress() + 
            self.gschem_int.setResultsName('x') + 
            self.gschem_int.setResultsName('y') + 
            self.gschem_int.setResultsName('color') + 
            self.gschem_int.setResultsName('size') + 
            self.gschem_int.setResultsName('visibility') + 
            self.gschem_int.setResultsName('show_name_value') + 
            self.gschem_int.setResultsName('angle') + 
            self.gschem_int.setResultsName('alignment') + 
            pp.countedArray(self.gschem_linestr,
                            intExpr=self.int_nl).setResultsName('children')
        )
        self.gschem_text.setParseAction(lambda toks: GschemText(toks.asDict()))
        #int_nl.setDebug(True)
        #gschem_text.setDebug(True)
        
        self.gschem_attr = (
            pp.lineStart.suppress() + 
            pp.Literal('T').suppress() + 
            self.gschem_int.setResultsName('x') + 
            self.gschem_int.setResultsName('y') + 
            self.gschem_int.setResultsName('color') + 
            self.gschem_int.setResultsName('size') + 
            self.gschem_int.setResultsName('visibility') + 
            self.gschem_int.setResultsName('show_name_value') + 
            self.gschem_int.setResultsName('angle') + 
            self.gschem_int.setResultsName('alignment') + 
            pp.countedArray(self.gschem_linestr,
                            intExpr=self.int_nl).setResultsName('children')
        )
        self.gschem_attr.setParseAction(lambda toks: GschemText(toks.asDict()))
        
        self.gschem_attr_list = pp.Optional(
            pp.Literal('{\n').suppress() + 
            pp.OneOrMore(self.gschem_attr).setResultsName('attrib') +
            pp.Literal('}\n').suppress()
        )

        self.gschem_line = (
            pp.lineStart.suppress() + 
            pp.Literal('L').suppress() + 
            self.gschem_int.setResultsName('x1') + 
            self.gschem_int.setResultsName('y1') + 
            self.gschem_int.setResultsName('x2') + 
            self.gschem_int.setResultsName('y2') + 
            self.gschem_int.setResultsName('color') + 
            self.gschem_int.setResultsName('width') + 
            self.gschem_int.setResultsName('capstyle') + 
            self.gschem_int.setResultsName('dashstyle') + 
            self.gschem_int.setResultsName('dashlength') + 
            self.gschem_int.setResultsName('dashspace') + 
            pp.lineEnd.suppress()
        )
        self.gschem_line.setParseAction(lambda toks: GschemLine(toks.asDict()))

        self.gschem_box = (
            pp.lineStart.suppress() + 
            pp.Literal('B').suppress() + 
            self.gschem_int.setResultsName('x') + 
            self.gschem_int.setResultsName('y') + 
            self.gschem_int.setResultsName('width') + 
            self.gschem_int.setResultsName('height') + 
            self.gschem_int.setResultsName('color') + 
            self.gschem_int.setResultsName('width') + 
            self.gschem_int.setResultsName('capstyle') + 
            self.gschem_int.setResultsName('dashstyle') + 
            self.gschem_int.setResultsName('dashlength') + 
            self.gschem_int.setResultsName('dashspace') + 
            self.gschem_int.setResultsName('filltype') + 
            self.gschem_int.setResultsName('fillwidth') + 
            self.gschem_int.setResultsName('angle1') + 
            self.gschem_int.setResultsName('pitch1') + 
            self.gschem_int.setResultsName('angle2') + 
            self.gschem_int.setResultsName('pitch2') + 
            pp.lineEnd.suppress()
        )
        self.gschem_box.setParseAction(lambda toks: GschemBox(toks.asDict()))

        self.gschem_circle = (
            pp.lineStart.suppress() + 
            pp.Literal('V').suppress() + 
            self.gschem_int.setResultsName('x') + 
            self.gschem_int.setResultsName('y') +
            self.gschem_int.setResultsName('radius') + 
            self.gschem_int.setResultsName('color') + 
            self.gschem_int.setResultsName('width') + 
            self.gschem_int.setResultsName('capstyle') + 
            self.gschem_int.setResultsName('dashstyle') + 
            self.gschem_int.setResultsName('dashlength') + 
            self.gschem_int.setResultsName('dashspace') + 
            self.gschem_int.setResultsName('filltype') + 
            self.gschem_int.setResultsName('fillwidth') + 
            self.gschem_int.setResultsName('angle1') + 
            self.gschem_int.setResultsName('pitch1') + 
            self.gschem_int.setResultsName('angle2') + 
            self.gschem_int.setResultsName('pitch2') + 
            pp.lineEnd.suppress()
        )
        self.gschem_circle.setParseAction(
            lambda toks: GschemCircle(toks.asDict()))

        self.gschem_arc = (
            pp.lineStart.suppress() + 
            pp.Literal('A').suppress() + 
            self.gschem_int.setResultsName('x') + 
            self.gschem_int.setResultsName('y') + 
            self.gschem_int.setResultsName('radius') + 
            self.gschem_int.setResultsName('startangle') + 
            self.gschem_int.setResultsName('sweepangle') + 
            self.gschem_int.setResultsName('color') + 
            self.gschem_int.setResultsName('width') + 
            self.gschem_int.setResultsName('capstyle') + 
            self.gschem_int.setResultsName('dashstyle') + 
            self.gschem_int.setResultsName('dashlength') + 
            self.gschem_int.setResultsName('dashspace') + 
            pp.lineEnd.suppress()
        )
        self.gschem_arc.setParseAction(lambda toks: GschemArc(toks.asDict()))


        self.gschem_component = (
            pp.lineStart.suppress() + 
            pp.Literal('C').suppress() + 
            self.gschem_int.setResultsName('x') + 
            self.gschem_int.setResultsName('y') + 
            self.gschem_int.setResultsName('selectable') + 
            self.gschem_int.setResultsName('angle') + 
            self.gschem_int.setResultsName('mirror') + 
            pp.Regex('\S+.*').setResultsName('basename') + 
            pp.lineEnd.suppress() + 
            self.gschem_attr_list
        )
        self.gschem_component.setParseAction(
            lambda toks: GschemComponent(toks.asDict()))

        self.gschem_net = (
            pp.lineStart.suppress() + 
            pp.Literal('N').suppress() + 
            self.gschem_int.setResultsName('x1') + 
            self.gschem_int.setResultsName('y1') + 
            self.gschem_int.setResultsName('x2') + 
            self.gschem_int.setResultsName('y2') + 
            self.gschem_int.setResultsName('color') + 
            pp.lineEnd.suppress() + 
            self.gschem_attr_list
        )
        self.gschem_net.setParseAction(lambda toks: GschemNet(toks.asDict()))

        self.gschem_pin = (
            pp.lineStart.suppress() + 
            pp.Literal('P').suppress() + 
            self.gschem_int.setResultsName('x1') + 
            self.gschem_int.setResultsName('y1') + 
            self.gschem_int.setResultsName('x2') + 
            self.gschem_int.setResultsName('y2') + 
            self.gschem_int.setResultsName('color') + 
            self.gschem_int.setResultsName('pintype') +
            self.gschem_int.setResultsName('whichend') + 
            pp.lineEnd.suppress() + 
            self.gschem_attr_list
        )
        self.gschem_pin.setParseAction(lambda toks: GschemPin(toks.asDict()))

        def f(toks):
            #print 'DEBUG', toks.asDict()
            #return GschemNet(toks.asDict())
            try:
                r = GschemFile(toks.asDict())
            except :
                import traceback
                traceback.print_exc()
            return r 
        #gschem_net.setParseAction(f)


        self.gschem_file = (
            self.gschem_version.setResultsName('ver') + 
            pp.ZeroOrMore(pp.Or([
                self.gschem_net,
                self.gschem_component,
                self.gschem_pin,
                self.gschem_line,
                self.gschem_box,
                self.gschem_circle,
                self.gschem_arc,
                self.gschem_text])).setResultsName('children') + 
            pp.stringEnd
        )
        self.gschem_file.setParseAction(lambda toks: GschemFile(toks.asDict()))
        #gschem_file.setParseAction(f)

    def load_gschem_file(self, f):
        return self.gschem_file.parseFile(f)[0]
        
    def load_gschem_symbol(self,f):
        r = self.gschem_file.parseFile(f)[0]
        return GschemSymbol(r)

    def parse_string_file(self, s):
        return self.gschem_file.parseString(s)[0]

