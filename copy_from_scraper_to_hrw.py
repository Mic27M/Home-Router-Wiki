import shutil
import os
import argparse

from pathlib import Path


parser = argparse.ArgumentParser()
parser.add_argument('-v', dest='vendor', required=True)
args = parser.parse_args()

input_vendor = args.vendor
input_vendor = input_vendor.lower()

cwd = Path(os.getcwd())

firmware_files_scraper = Path(cwd/'FirmwareScraper/firmware_files')
firmware_files_hrw = Path(cwd/f"geekdoc/sites/content/firmware_files/{input_vendor}")
scraper = Path(cwd/'FirmwareScraper')
router_json = Path(cwd/'router_json')

list_of_files = os.listdir(firmware_files_scraper)

if not os.path.isdir(firmware_files_hrw):
    os.mkdir(firmware_files_hrw)

for file in list_of_files:
    try:
        shutil.copy(Path(firmware_files_scraper/file), firmware_files_hrw)
    except BaseException as err:
        print(err)

print(Path(scraper/f'{input_vendor}.json'))

if os.path.isfile(Path(scraper/f'{input_vendor}.json')):
    if os.path.isfile(Path(router_json/f'{input_vendor}.json')):
        try:
            os.remove(Path(router_json/f'{input_vendor}.json'))
        except OSError as e:
            print(e)
        else:
            print("File is deleted successfully")

    shutil.move(Path(scraper/f'{input_vendor}.json'), router_json)

os.system(f'python3 json_to_markdown.py -v {input_vendor}')
