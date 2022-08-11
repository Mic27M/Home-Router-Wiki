import os 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-v', dest='vendor', required=True)
args = parser.parse_args()

input_vendor = args.vendor
input_vendor = input_vendor.lower()


os.system(f'python3 scrape_from.py -v {input_vendor}')
os.system(f'python3 copy_from_scraper_to_hrw.py -v {input_vendor}')

