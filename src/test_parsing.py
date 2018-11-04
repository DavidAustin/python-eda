
import unittest
from geda_pcb_parsing import *
import math


class PCBTestCase(unittest.TestCase):

    def assertDimsSame(self, a, b, msg=None):
        if msg is None:
            msg = '{0:f} {1:f}'.format(a, b)
        self.assertTrue(math.fabs(a - b) < 1e-6, msg=msg)


class ParseElementTest(PCBTestCase):
    def test_it(self):
        tt = '''Element["" "my0603" "R800" "0R_DNF" 35966 506184 -6298 -8331 0 100 ""]
(
        Pad[-4133 0 -3347 0 3150 0 3150 "1" "1" "square"]
        Pad[3347 0 4133 0 3150 0 3150 "2" "2" "square,edge2"]
        ElementLine [6495 2362 -6495 2362 1000]
        ElementLine [-6495 2362 -6495 -2362 1000]
        ElementLine [-6495 -2362 6495 -2362 1000]
        ElementLine [6495 -2362 6495 2362 1000]

        )
'''
        p = GEDAPCBFileParser()
        r = p.parse_string_element(tt)
        self.assertEqual(len(r), 1, msg='{0}'.format(len(r)))
        self.assertTrue(isinstance(r[0], GEDAPCBElement))

        self.assertTrue(isinstance(r[0].children[0], GEDAPCBPad))
        self.assertDimsSame(r[0].children[0].x1, old_pcb_units_to_mm(-4133))
        self.assertDimsSame(r[0].children[0].y1, old_pcb_units_to_mm(0))

        self.assertTrue(isinstance(r[0].children[2], GEDAPCBElementLine))
        self.assertDimsSame(r[0].children[2].x1, old_pcb_units_to_mm(6495))
        self.assertDimsSame(r[0].children[2].y1, old_pcb_units_to_mm(2362))
        self.assertDimsSame(r[0].children[2].x2, old_pcb_units_to_mm(-6495))
        self.assertDimsSame(r[0].children[2].y2, old_pcb_units_to_mm(2362))
        

        
    def test_elt2(self):
        tt = '''Element["" "HEADER10_2" "J801" "unknown" 68898 375984 -5000 -21000 0 100 ""]
(
        Pin[0 0 6000 3000 6600 3800 "1" "1" "square,edge2"]
        Pin[0 -10000 6000 3000 6600 3800 "2" "2" "edge2,thermal(1X,5X)"]
        Pin[10000 0 6000 3000 6600 3800 "3" "3" "edge2"]
        Pin[10000 -10000 6000 3000 6600 3800 "4" "4" "edge2"]
        Pin[20000 0 6000 3000 6600 3800 "5" "5" "edge2"]
        Pin[20000 -10000 6000 3000 6600 3800 "6" "6" "edge2"]
        Pin[30000 0 6000 3000 6600 3800 "7" "7" "edge2"]
        Pin[30000 -10000 6000 3000 6600 3800 "8" "8" "edge2"]
        Pin[40000 0 6000 3000 6600 3800 "9" "9" "edge2"]
        Pin[40000 -10000 6000 3000 6600 3800 "10" "10" "edge2,thermal(1X,5X)"]
        ElementLine [-5000 5000 45000 5000 1000]
        ElementLine [45000 -15000 45000 5000 1000]
        ElementLine [-5000 -15000 45000 -15000 1000]
        ElementLine [-5000 -15000 -5000 5000 1000]
        ElementLine [5000 -5000 5000 5000 1000]
        ElementLine [-5000 -5000 5000 -5000 1000]

        )
        '''
        p = GEDAPCBFileParser()
        r = p.parse_string_element(tt)
        self.assertTrue(len(r) == 1)
        self.assertTrue(isinstance(r[0], GEDAPCBElement))


        

    def test_elt3(self):
        tt = '''Element["" "TSSOP8" "U501" "unknown" 658924 353764 -10856 -10920 0 100 ""]
(
        Pad[-11161 -3838 -6555 -3838 1299 1000 2299 "1" "1" "square"]
        Pad[-11161 -1279 -6555 -1279 1299 1000 2299 "2" "2" "square"]
        Pad[-11161 1279 -6555 1279 1299 1000 2299 "3" "3" "square"]
        Pad[-11161 3838 -6555 3838 1299 1000 2299 "4" "4" "square"]
        Pad[6555 3838 11161 3838 1299 1000 2299 "5" "5" "square,edge2"]
        Pad[6555 1279 11161 1279 1299 1000 2299 "6" "6" "square,edge2"]
        Pad[6555 -1279 11161 -1279 1299 1000 2299 "7" "7" "square,edge2"]
        Pad[6555 -3838 11161 -3838 1299 1000 2299 "8" "8" "square,edge2"]
        ElementLine [-12811 -5488 -12811 5488 1000]
        ElementLine [-12811 5488 12811 5488 1000]
        ElementLine [12811 5488 12811 -5488 1000]
        ElementLine [-12811 -5488 -2500 -5488 1000]
        ElementLine [12811 -5488 2500 -5488 1000]
        ElementArc [0 -5488 2500 2500 0 180 1000]

        )
'''
        p = GEDAPCBFileParser()
        r = p.parse_string_element(tt)
        self.assertTrue(len(r) == 1)
        self.assertTrue(isinstance(r[0], GEDAPCBElement))

    def test_elt4(self):
        tt = '''Element["onsolder" "asp_122952_01" "J1" "unknown" 246791 29528 4000 -20000 2 100 "auto"]
(
	Pad[-7834 9901 -7834 17381 1181 2000 1359 "2" "2" "onsolder,square,edge2"]

)'''
        p = GEDAPCBFileParser()
        r = p.parse_string_element(tt)
        self.assertTrue(len(r) == 1)
        self.assertTrue(isinstance(r[0], GEDAPCBElement))

    def test_via(self):
        tt = '''Via[203937 319685 2008 866 0 1181 "" ""]
'''
        p = GEDAPCBFileParser()
        r = p.parse_string_element(tt)
        self.assertTrue(len(r) == 1)
        self.assertTrue(isinstance(r[0], GEDAPCBVia))


    def test_via2(self):
        tt = '''Via[25591 94488 1969 1574 0 1181 "" "thermal(3X,4X)"]
'''
        p = GEDAPCBFileParser()
        r = p.parse_string_element(tt)
        self.assertTrue(len(r) == 1)
        self.assertTrue(isinstance(r[0], GEDAPCBVia))



    def test_rat(self):
        tt = '''Rat[303802 506184 0 322455 479017 0  ""]
'''

        p = GEDAPCBFileParser()
        r = p.parse_string_element(tt)
        self.assertTrue(len(r) == 1)
        self.assertTrue(isinstance(r[0], GEDAPCBRat))



    def test_symbol(self):
        tt = '''Symbol['#' 1200]
(
        SymbolLine[0 2625 1500 2625 600]
        SymbolLine[0 1875 1500 1875 600]
        SymbolLine[1125 1500 1125 3000 600]
        SymbolLine[375 1500 375 3000 600]
)'''
        p = GEDAPCBFileParser()
        r = p.parse_string_element(tt)
        self.assertTrue(len(r) == 1)
        self.assertTrue(isinstance(r[0], GEDAPCBSymbol))



    def test_layer(self):
        tt = '''Layer(1 "component")
(
        Line[205512 305512 207086 303937 413 866 "clearline"]
        Line[208661 305512 207087 303937 413 866 "clearline"]
        Line[207086 303937 207087 303937 413 866 "clearline"]
        Line[202362 299213 200787 300787 413 866 "clearline"]
        Line[200787 300787 199213 299213 413 866 "clearline"]
        Line[203937 303936 203937 306496 413 866 "clearline"]
)'''

        p = GEDAPCBFileParser()
        r = p.parse_string_element(tt)
        self.assertTrue(len(r) == 1)
        self.assertTrue(isinstance(r[0], GEDAPCBLayer))


    def test_netlist(self):
        tt = '''NetList()
(
        Net("+5V" "(unknown)")
        (
                Connect("C100-1")
                Connect("C105-1")
                Connect("C110-1")
                Connect("C154-1")
                Connect("C156-1")
                Connect("C403-1")
                Connect("J2-85")
                Connect("J2-97")
                Connect("J2-101")
                Connect("J2-105")
                Connect("J601-1")
                Connect("R100-1")
	)
)
'''
        p = GEDAPCBFileParser()
        r = p.parse_string_element(tt)
        self.assertTrue(len(r) == 1)
        self.assertTrue(isinstance(r[0], GEDAPCBNetList))


    def test_layer2(self):
        tt = '''Layer(2 "GND-top")
(
        Line[202362 299213 200787 300787 413 866 "clearline"]
        Polygon("clearpoly")
        (
                [32480 20669] [502953 20669] [502953 412402] [32480 412402] 
        )
)'''
        p = GEDAPCBFileParser()
        r = p.parse_string_element(tt)
        self.assertTrue(len(r) == 1)
        self.assertTrue(isinstance(r[0], GEDAPCBLayer))


        
    def test_layer3(self):
        tt = '''Layer(1 "component")
(
	Line[105315 85827 104981 85493 787 1575 "clearline"]
	Line[104981 85493 104981 79291 787 1575 "clearline"]
	Line[106950 85373 106950 79291 787 1575 "clearline"]
	Line[106950 85354 106526 85778 787 1575 "clearline"]
	Line[100787 69291 100787 67126 1575 1574 "clearline"]
	Text[19685 118110 0 70 "DE2 Carrier v2" "clearline"]
)
Layer(2 "solder")
(
	Line[105315 85827 104981 85493 787 1575 "clearline"]
	Line[104981 85493 104981 79291 787 1575 "clearline"]
	Line[106950 85373 106950 79291 787 1575 "clearline"]
	Line[106950 85354 106526 85778 787 1575 "clearline"]
	Line[100787 69291 100787 67126 1575 1574 "clearline"]
	Text[19685 118110 0 70 "DE2 Carrier v2" "clearline"]
)'''
        p = GEDAPCBFileParser()
        r = p.parse_string_element(tt)
        self.assertTrue(len(r) == 2)
        self.assertTrue(isinstance(r[0], GEDAPCBLayer))
        self.assertTrue(isinstance(r[1], GEDAPCBLayer))


    def test_layer4(self):
        tt = '''Layer(1 "component")
(
        Line[205512 293701 207086 292126 413 866 "clearline"]
        Line[208661 293701 207087 292126 413 866 "clearline"]
        Line[207086 292126 207087 292126 413 866 "clearline"]
)
Layer(2 "GND-top")
(
        Line[146457 215748 146850 216142 394 788 "clearline"]
        Polygon("clearpoly")
        (
                [32480 20669] [502953 20669] [502953 412402] [32480 412402] 
                Hole (
                        [71133 179208] [71133 186282] [78600 186282] [78600 179208] 
                )
        )
        Polygon("clearpoly")
        (
                [32480 20669] [502953 20669] [502953 412402] [32480 412402] 
                Hole (
                        [71133 179208] [71133 186282] [78600 186282] [78600 179208] 
                )
        )
)
'''
        p = GEDAPCBFileParser()
        r = p.parse_string_element(tt)
        self.assertTrue(len(r) == 2)
        self.assertTrue(isinstance(r[0], GEDAPCBLayer))
        self.assertTrue(isinstance(r[1], GEDAPCBLayer))

        
        
    def test_pcb_file(self):
        tt = '''

# release: pcb 20110918

# To read pcb files, the pcb version (or the git source date) must be >= the file version
FileVersion[20100606]

PCB["" 788976 787402]

Grid[393.7 0 0 0]
Cursor[93110 166929 0.000000]
PolyArea[200000000.000000]
Thermal[0.500000]
DRC[390 197 390 354 1181 390]
Flags("showdrc,nameonpcb,autodrc,clearnew,snappin")
Groups("1,c:8,s:2:3:4:5:6:9:7")
Styles["Signal,787,2362,1181,787:Power,1969,3937,1969,984:Diff,591,2362,1181,787:Skinny,394,1969,1181,394"]

Symbol[' ' 1800]
(
)
Attribute("PCB::grid::unit" "mil")
Via[194488 292126 2008 866 0 1181 "" "thermal(1X)"]
Via[344291 317714 1969 788 0 1181 "" ""]
Element["" "my0603" "R803" "120k" 67559 219961 -6298 -8331 0 100 ""]
(
        Pad[-4133 0 -3347 0 3150 0 3150 "1" "1" "square"]
        Pad[3347 0 4133 0 3150 0 3150 "2" "2" "square,edge2"]
        ElementLine [6495 2362 -6495 2362 1000]
        ElementLine [-6495 2362 -6495 -2362 1000]
        ElementLine [-6495 -2362 6495 -2362 1000]
        ElementLine [6495 -2362 6495 2362 1000]

        )

Rat[83464 125984 0 55512 112992 4  "via"]
Rat[513753 411970 0 241772 173425 4  ""]
Layer(1 "component")
(
        Line[205512 293701 207086 292126 413 866 "clearline"]
        Line[208661 293701 207087 292126 413 866 "clearline"]
        Line[207086 292126 207087 292126 413 866 "clearline"]
)
Layer(2 "GND-top")
(
        Line[146457 215748 146850 216142 394 788 "clearline"]
        Polygon("clearpoly")
        (
                [32480 20669] [502953 20669] [502953 412402] [32480 412402] 
                Hole (
                        [71133 179208] [71133 186282] [78600 186282] [78600 179208] 
                )
        )
        Polygon("clearpoly")
        (
                [32480 20669] [502953 20669] [502953 412402] [32480 412402] 
                Hole (
                        [71133 179208] [71133 186282] [78600 186282] [78600 179208] 
                )
        )
)
Layer(3 "signal1")
(
        Line[105709 170079 105709 161102 394 788 "clearline"]
        Line[105709 161102 104213 159606 394 788 "clearline"]
        Line[104213 159606 102835 159606 394 788 "clearline"]
        Polygon("clearpoly")
        (
                [214343 141094] [249776 141094] [249776 176527] [214343 176527] 
        )
)
NetList()
(
        Net("+5V" "(unknown)")
        (
                Connect("C100-1")
                Connect("C105-1")
                Connect("C110-1")
                Connect("C154-1")
                Connect("C156-1")
                Connect("C403-1")
                Connect("J2-85")
                Connect("J2-97")
                Connect("J2-101")
                Connect("J2-105")
                Connect("J601-1")
                Connect("R100-1")
                Connect("R104-1")
                Connect("R109-1")
                Connect("R114-1")
                Connect("R118-1")
        )
        Net("ECP3_CCLK" "(unknown)")
        (
                Connect("R526-2")
                Connect("U1-A24")
        )
)'''

        
        p = GEDAPCBFileParser()
        r = p.parse_string_file(tt)
        self.assertTrue(isinstance(r, GEDAPCBFile))



    def test_pcb_file_newer(self):
        tt = '''# release: pcb 20140316

# To read pcb files, the pcb version (or the git source date) must be >= the file version
FileVersion[20091103]

PCB["" 6000.00mil 5000.00mil]

Grid[3937.007874 0.0000 0.0000 1]
PolyArea[200000000.000000]
Thermal[0.500000]
DRC[0.1500mm 0.0600mm 0.1500mm 0.0990mm 0.2990mm 0.1500mm]
Flags("showdrc,nameonpcb,uniquename,clearnew,snappin")
Groups("1,c:2:3:4:5:6,s:7:8")
Styles["Signal,0.2000mm,0.7000mm,0.3000mm,0.2000mm:Power,0.5000mm,1.0000mm,0.5000mm,0.2000mm:Fat,40.00mil,60.00mil,35.00mil,10.00mil:Skinny,6.00mil,24.02mil,11.81mil,6.00mil"]

Symbol[' ' 18.00mil]
(
)
Symbol['!' 12.00mil]
(
        SymbolLine[0.0000 45.00mil 0.0000 50.00mil 8.00mil]
        SymbolLine[0.0000 10.00mil 0.0000 35.00mil 8.00mil]
)
Attribute("PCB::grid::unit" "mm")
Attribute("PCB::grid::size" "1.0000mm")
Via[9.6000mm 5.9000mm 0.7000mm 0.4000mm 0.0000 0.3000mm "" ""]
Via[13.6000mm 5.9000mm 0.7000mm 0.4000mm 0.0000 0.3000mm "" ""]
'''
        
        p = GEDAPCBFileParser()
        r = p.parse_string_file(tt)
        self.assertTrue(isinstance(r, GEDAPCBFile))

        self.assertTrue(isinstance(r.children[-2], GEDAPCBVia))
        self.assertDimsSame(r.children[-2].x, 9.6)
        self.assertDimsSame(r.children[-2].y, 5.9)
        self.assertTrue(isinstance(r.children[-1], GEDAPCBVia))
        self.assertDimsSame(r.children[-1].x, 13.6)
        self.assertDimsSame(r.children[-1].y, 5.9)

