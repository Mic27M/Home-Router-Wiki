import argparse
import datetime
import logging
import db_script
import log
import scrape_from
import move_from_scraper_to_hrw


current_log =str(log.current_log)

logging.basicConfig(filename=f'{log.current_log}', level=logging.INFO)

start_time = datetime.datetime.now().isoformat()
entries_db_vendor_start = db_script.CountDBEntries(db_script.vendor)
entries_db_dv_class_start = db_script.CountDBEntries(db_script.device_class)
entries_dB_device_start = db_script.CountDBEntries(db_script.device)

logging.info(f'----------database update started at {start_time}')

parser = argparse.ArgumentParser()
parser.add_argument('-v', dest='vendor', required=False)
args = parser.parse_args()

input_vendor = args.vendor

if not input_vendor is None:
    input_vendor = input_vendor.lower()
    logging.info(f'----- just update vendor {input_vendor}')
    logging.info(f'----- start scrape firmware from vendor {input_vendor}')
    scrape_from.ScrapeFirmware(input_vendor)
    
    logging.info(f'----- stop scrape firmware from vendor {input_vendor}')
    logging.info(f'----- start to copy firmware from scraper to MD and DB (vendor {input_vendor})')
    move_from_scraper_to_hrw.MoveToHRW(input_vendor)
    logging.info(f'----- stop to copy firmware from scraper to MD and DB (vendor {input_vendor})')


else :
    vendor_list = ["asus","tplink"] #avm, netgear, dlink,linksys, zyxel do not work at the moment
    logging.info(f'-----  update all vendors')
    for vendor in vendor_list:
        logging.info(f'----- start scrape firmware from vendor {vendor}')
        scrape_returncode = scrape_from.ScrapeFirmware(vendor)
        logging.info(f'----- stop scrape firmware from vendor {vendor}')
       
        logging.info(f'----- start to copy firmware from scraper to MD and DB (vendor {vendor})')
        move_from_scraper_to_hrw.MoveToHRW(input_vendor)
        logging.info(f'----- stop to copy firmware from scraper to MD and DB (vendor {vendor})')
        

stop_time = datetime.datetime.now().isoformat()
entries_db_vendor_stop = db_script.CountDBEntries(db_script.vendor)
entries_db_dv_class_stop = db_script.CountDBEntries(db_script.device_class)
entries_db_devices_stop = db_script.CountDBEntries(db_script.device)

success = log.UpdateSuccess()

db_stats = db_script.StatisticDBInfo(entries_db_vendor_start, entries_db_vendor_stop, entries_db_dv_class_start, entries_db_dv_class_stop, entries_dB_device_start, entries_db_devices_stop)

try:
    db_script.InsertDBInfo(start_time, stop_time, db_stats, current_log, success)
except BaseException as err:
    logging.warning(err)

logging.info(f"----------database update stopped at {stop_time}")
