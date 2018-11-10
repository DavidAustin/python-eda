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

import unittest
from gschem_parsing import *
import math

class GschemParseTest(unittest.TestCase):

    
    def test_version(self):
        
        tt = '''v 20110115 2
        '''
        parser = GschemFileParser()
        r = parser.gschem_version.parseString(tt)[0]
        self.assertTrue(isinstance(r, GschemVersion))
        self.assertEqual(r.version, 20110115)
        self.assertEqual(r.fileversion, 2)

    def test_text(self):
        tt = '''T 1900 31600 8 40 1 0 0 0 2
Some test string
two lines
'''
        parser = GschemFileParser()
        r = parser.gschem_text.parseString(tt)[0]

        self.assertTrue(isinstance(r, GschemText))
        self.assertEqual(r.x, 1900)
        self.assertEqual(r.y, 31600)
        self.assertEqual(r.children[0], 'Some test string')
        self.assertEqual(r.children[1], 'two lines')

    def test_component(self):
        tt = '''C 3100 16800 1 0 0 SOME_PART.sym
'''
        parser = GschemFileParser()
        r = parser.gschem_component.parseString(tt)[0]

        self.assertTrue(isinstance(r, GschemComponent))
        self.assertEqual(r.x, 3100)
        self.assertEqual(r.y, 16800)
        self.assertEqual(r.basename, 'SOME_PART.sym')


    def test_component_text(self):
        tt = '''C 3100 16800 1 0 0 SOME_PART2.sym
{
T 5800 30600 5 10 1 1 0 6 1
refdes=U1
T 3500 30800 5 10 0 0 0 0 1
device=SOME_DEVICE
T 3100 16800 5 10 0 1 0 0 1
footprint=BGA672
}
'''
        parser = GschemFileParser()
        r = parser.gschem_component.parseString(tt)[0]
        self.assertTrue(isinstance(r, GschemComponent))
        self.assertEqual(r.x, 3100)
        self.assertEqual(r.y, 16800)
        self.assertEqual(r.basename, 'SOME_PART2.sym')

        self.assertEqual(len(r.attrib), 3, msg="%d != 3" % len(r.attrib))
        self.assertEqual(r.attrib['refdes'], 'U1')
        self.assertEqual(r.attrib['device'], 'SOME_DEVICE')
        self.assertEqual(r.attrib['footprint'], 'BGA672')

    def test_net(self):
        tt = '''N 46000 7900 47000 7900 4
{
T 46200 8000 5 10 1 1 0 0 1
netname=I2C_SCL
}'''
        parser = GschemFileParser()
        r = parser.gschem_net.parseString(tt)[0]
        self.assertTrue(isinstance(r, GschemNet))


    def test_file1(self):
        tt = '''v 20130925 2
C 40000 40000 0 0 0 title-B.sym
C 44900 46400 1 0 0 resistor-1.sym
{
T 45200 46800 5 10 0 0 0 0 1
device=RESISTOR
T 45100 46700 5 10 1 1 0 0 1
refdes=R1
T 45100 46200 5 10 1 1 0 0 1
value=1k
}
'''
        parser = GschemFileParser()
        r = parser.parse_string_file(tt)
        self.assertTrue(isinstance(r, GschemFile))
        self.assertEqual(len(r.children), 2)
        self.assertTrue(isinstance(r.children[0], GschemComponent))
        self.assertTrue(isinstance(r.children[1], GschemComponent))
        self.assertEqual(r.children[1].attrib['device'], 'RESISTOR')
        self.assertEqual(r.children[1].attrib['refdes'], 'R1')
        self.assertEqual(r.children[1].attrib['value'], '1k')
        
