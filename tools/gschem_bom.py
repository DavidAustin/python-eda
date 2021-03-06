# Python-EDA
# Copyright (C) 2018-2000 Luke Cole
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

import argparse
import sys
import os
import re
import urllib.request
import urllib.parse
import json
import pprint

#==============================================================================
# default settings

is_debug = False
apikey = None
filename = None

#==============================================================================
# parse arguments

parser = argparse.ArgumentParser(description='gEDA gschem BOM Generation Tool')
parser.add_argument("-d", '--debug', action='store_true', help='Print debug comments')
parser.add_argument("-p", '--debug_part', metavar='KEY', type=str, nargs=1, help='Print debug info for this part')
parser.add_argument("-k", '--octopart_apikey', metavar='KEY', type=str, nargs=1, help='Register with octopart.com', required = True)
parser.add_argument("-i", '--input_file', metavar='PATH', type=str, nargs=1, help='Example: example01.sch', required = True)

args = parser.parse_args()
is_debug = args.debug
debug_part = ""
if args.debug_part:
  debug_part = args.debug_part[0]
if args.octopart_apikey:
  apikey = args.octopart_apikey[0]
if args.input_file:
  filename = args.input_file[0]

#==============================================================================
# process

if not os.path.exists(filename):
  print (("%s - File does not exist") % (filename))
  exit()

infile = open(filename, "r")
lines = infile.read()
infile.close()

part = {
  'refdes': '',
  'seller': '',
  'sku': '',
  'device': '',
  'value': '',
  'footprint': '',
  'unit_cost_1': '',
  'unit_cost_10': '',
  'unit_cost_100': '',
  'unit_cost_500': '',
  'unit_cost_1000': '',
  'unit_cost_10000': '',
  'description': '',
  'octopart_url': ''
}

total_unit_cost_1 = 0.0
total_unit_cost_100 = 0.0
total_unit_cost_500 = 0.0
total_unit_cost_1000 = 0.0
total_unit_cost_10000 = 0.0

total_missing_part_price_1 = 0
total_missing_part_price_100 = 0
total_missing_part_price_500 = 0
total_missing_part_price_1000 = 0
total_missing_part_price_10000 = 0

print (",".join(part.keys()))

def process_start(matchobj):
  part["description"] = ""
  part["octopart_url"] = ""
  part["device"] = ""
  part["footprint"] = ""
  part["value"] = ""
  part["refdes"] = ""
  part["seller"] = ""
  part["sku"] = ""
  part["unit_cost_1"] = ""
  part["unit_cost_10"] = ""
  part["unit_cost_100"] = ""
  part["unit_cost_500"] = ""
  part["unit_cost_1000"] = ""
  part["unit_cost_10000"] = ""

def process_device(matchobj):
  part["device"] = matchobj.group(0).replace("device=", "")

def process_value(matchobj):
  part["value"] = matchobj.group(0).replace("value=", "")

def process_footprint(matchobj):
  part["footprint"] = matchobj.group(0).replace("footprint=", "")

def process_refdes(matchobj):
  part["refdes"] = matchobj.group(0).replace("refdes=", "")

def process_end(matchobj):
  global total_unit_cost_1
  global total_unit_cost_100
  global total_unit_cost_500
  global total_unit_cost_1000
  global total_unit_cost_10000
  global total_missing_part_price_1
  global total_missing_part_price_100
  global total_missing_part_price_500
  global total_missing_part_price_1000
  global total_missing_part_price_10000

  if is_debug:
    print (part)
  print_out = True
  if not part["device"]:
    print_out = False
  if part['device'] == "terminal":
    print_out = False
  if part['device'] == "TESTPOINT":
    print_out = False
    
  if "RESISTOR" in part['device']:
    part['device'] = part['device'] + " " + part['value'] + " " + part['footprint'].replace("pei", "")
  if "CAPACITOR" in part['device']:
    part['device'] = part['device'] + " " + part['value'] + " " + part['footprint'].replace("pei", "")

  if print_out:
    parse_octopart(part['device'])
    print (",".join(part.values()))
    if part['unit_cost_1']:
      total_unit_cost_1 += float(part['unit_cost_1'])
    else:
      total_missing_part_price_1 += 1

    if part['unit_cost_100']:
      total_unit_cost_100 += float(part['unit_cost_100'])
    else:
      total_missing_part_price_100 += 1

    if part['unit_cost_500']:
      total_unit_cost_500 += float(part['unit_cost_500'])
    else:
      total_missing_part_price_500 += 1
      
    if part['unit_cost_1000']:
      total_unit_cost_1000 += float(part['unit_cost_1000'])
    else:
      total_missing_part_price_1000 += 1

    if part['unit_cost_10000']:
      total_unit_cost_10000 += float(part['unit_cost_10000'])
    else:
      total_missing_part_price_10000 += 1
      
    if is_debug:
      print ("%s, %s, %s, %s" % (part['refdes'], part['device'], part['value'], part['footprint']))

def parse_octopart(device):
  if is_debug:
    print (("processing device=%s..........................................") % (device))

  device = urllib.parse.quote_plus(device)
  response = urllib.request.urlopen('https://octopart.com/api/v3/parts/match?apikey=%s&queries=[{"mpn":"%s"}]' % (apikey, device))
  data = response.read()
  data = json.loads(data)

  if debug_part and debug_part in device:
    pp = pprint.PrettyPrinter(indent=1)
    pp.pprint(data)

  hits = data["results"][0]['hits']
  
  if hits > 0:
    
    items = data["results"][0]["items"]
    item_idx = -1
    offer_idx = -1

    if is_debug:
      print ("items_count=%d" % (len(items)))
      
    for i in range(len(items)):
      offers = data["results"][0]["items"][i]['offers']
      if is_debug:
        print ("offers_count=%d" % (len(offers)))
      for j in range(len(offers)):
        seller_name = data["results"][0]["items"][i]['offers'][j]['seller']['name']
        if is_debug:
          print (seller_name)
        if seller_name == "Digi-Key":
          item_idx = i
          offer_idx = j
          if is_debug:
            print ("item_idx=%d offer_idx=%d" % (item_idx, offer_idx))
          break
        
    if offer_idx >= 0:
      
      octopart_url = data["results"][0]["items"][item_idx]['octopart_url']
      seller_name = data["results"][0]["items"][item_idx]['offers'][offer_idx]['seller']['name']
      sku = data["results"][0]["items"][item_idx]['offers'][offer_idx]['sku']
      packaging = data["results"][0]["items"][item_idx]['offers'][offer_idx]['packaging']
      unit_cost_1 = ''
      unit_cost_10 = ''
      unit_cost_100 = ''
      unit_cost_500 = ''
      unit_cost_1000 = ''
      unit_cost_10000 = ''
      has_prices = False

      if is_debug:
        print (packaging)
      
      if packaging == "Tape & Reel" or packaging == "Cut Tape" or packaging == "Tray" or packaging == "Tube" or packaging == "Bulk" or packaging == "Bag" or packaging == "Box":
        try:
          unit_cost_1 = data["results"][0]["items"][item_idx]['offers'][offer_idx]['prices']['USD'][0][1]
        except:
          pass
        try:
          unit_cost_10 = data["results"][0]["items"][item_idx]['offers'][offer_idx]['prices']['USD'][1][1]
        except:
          pass
        try:
          unit_cost_100 = data["results"][0]["items"][item_idx]['offers'][offer_idx]['prices']['USD'][2][1]
        except:
          pass
        try:
          unit_cost_500 = data["results"][0]["items"][item_idx]['offers'][offer_idx]['prices']['USD'][3][1]
        except:
          pass
        try:
          unit_cost_1000 = data["results"][0]["items"][item_idx]['offers'][offer_idx]['prices']['USD'][4][1]
        except:
          pass
        try:
          unit_cost_10000 = data["results"][0]["items"][item_idx]['offers'][offer_idx]['prices']['USD'][5][1]
        except:
          pass
        has_prices = True

      if has_prices:
        part['octopart_url'] = octopart_url
        part['seller'] = seller_name
        part['sku'] = sku
        part['unit_cost_1'] = unit_cost_1
        part['unit_cost_10'] = unit_cost_10
        part['unit_cost_100'] = unit_cost_100
        part['unit_cost_500'] = unit_cost_500
        part['unit_cost_1000'] = unit_cost_1000
        part['unit_cost_10000'] = unit_cost_10000
        if is_debug:
          print (part)

for l in lines.splitlines():
  if is_debug:
    print (l)
  lines = re.sub(r'{', process_start, l)
  lines = re.sub(r'device=.+', process_device, l)
  lines = re.sub(r'value=.+', process_value, l)
  lines = re.sub(r'footprint=.+', process_footprint, l)
  lines = re.sub(r'refdes=.+', process_refdes, l)
  lines = re.sub(r'}', process_end, l)

print ("Total (1x): $%f (%d part prices missing)" % (total_unit_cost_1, total_missing_part_price_1))
print ("Total (100x): $%f (%d part prices missing)" % (total_unit_cost_100, total_missing_part_price_100))
print ("Total (500x): $%f (%d part prices missing)" % (total_unit_cost_500, total_missing_part_price_500))
print ("Total (1000x): $%f (%d part prices missing)" % (total_unit_cost_1000, total_missing_part_price_1000))
print ("Total (10000x): $%f (%d part prices missing)" % (total_unit_cost_10000, total_missing_part_price_10000))
