import os 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-v', dest='vendor', required=False)
args = parser.parse_args()

input_vendor = args.vendor
if not input_vendor is None:
    input_vendor = input_vendor.lower()

    os.system(f'python3 scrape_from.py -v {input_vendor}')
    os.system(f'python3 copy_from_scraper_to_hrw.py -v {input_vendor}')

else :
    print("alle")
    vendor_list = ["asus","avm","dlink","linksys","netgear","tplink","zxel"]

    for vendor in vendor_list:

        os.system(f'python3 scrape_from.py -v {vendor}')
        os.system(f'python3 copy_from_scraper_to_hrw.py -v {vendor}')

