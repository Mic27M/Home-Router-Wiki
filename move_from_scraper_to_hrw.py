import logging
import shutil
import os
import argparse
import log
import json_to_MD_and_DB
from pathlib import Path

logging.basicConfig(filename=f'{log.current_log}', level=logging.INFO)

def MoveToHRW(vendor):

    cwd = Path(os.getcwd())

    firmware_files_scraper = Path(cwd/'FirmwareScraper/firmware_files')
    firmware_files_hrw = Path(cwd/f"geekdoc/sites/content/firmware_files/{vendor}")
    scraper = Path(cwd/'FirmwareScraper')
    router_json = Path(cwd/'router_json')

    list_of_files = os.listdir(firmware_files_scraper)

    if not os.path.isdir(firmware_files_hrw):
        try:
            os.mkdir(firmware_files_hrw)
        except OSError as err:
            logging.warning(err)

    for file in list_of_files:
        try:
            shutil.copy(Path(firmware_files_scraper/file), firmware_files_hrw)
            os.remove(Path(firmware_files_scraper/file))
        except OSError as err:
            logging.warning(err)

    if os.path.isfile(Path(scraper/f'{vendor}.json')):
        if os.path.isfile(Path(router_json/f'{vendor}.json')):
            try:
                os.remove(Path(router_json/f'{vendor}.json'))
            except OSError as err:
                logging.warning(err)
        try:
            shutil.move(Path(scraper/f'{vendor}.json'), router_json)
        except OSError as err:
            logging.warning(err)
    # try:       
        json_to_MD_and_DB.CopyJsonEntriesToMDAndDB(vendor)
    # except:
    #        logging.warning('!!!!Problem at json_to_MD_DB.py!!!!')


parser = argparse.ArgumentParser()

if parser.prog == "scrape_from.py":

    parser.add_argument('-v', dest='vendor', required=True)
    args = parser.parse_args()

    input_vendor = args.vendor
    input_vendor = input_vendor.lower()
    MoveToHRW(input_vendor)