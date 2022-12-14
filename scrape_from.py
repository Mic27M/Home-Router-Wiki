from importlib.resources import path
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-v', dest='vendor', required=True)
args = parser.parse_args()

input_vendor = args.vendor
input_vendor = input_vendor.lower()

os.chdir("./FirmwareScraper")

exit = os.system(f"TMPDIR=$HOME/tmp scrapy crawl {input_vendor} -o {input_vendor}.json")