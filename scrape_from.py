
import subprocess
import os
import argparse
import log

def ScrapeFirmware(vendor):
    current_log = log.current_log
    os.chdir("./FirmwareScraper")
    scrape_command = (f"TMPDIR=$HOME/tmp scrapy crawl {vendor} -o {vendor}.json --logfile {current_log} -L WARNING -s DOWNLOAD_WARNSIZE=0")
    # scrape_command_args = shlex.split(scrape_command)
    p2 = subprocess.Popen(scrape_command, shell=True)
    p2.wait()

    os.chdir("..")
    


parser = argparse.ArgumentParser()

if parser.prog == "scrape_from.py":
    parser.add_argument('-v', dest='vendor', required=True)
    args = parser.parse_args()

    input_vendor = args.vendor
    input_vendor = input_vendor.lower()

    ScrapeFirmware(input_vendor)


    
