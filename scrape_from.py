from importlib.resources import path
import os

input_vendor = "avm"

os.chdir("./FirmwareScraper")

exit = os.system(f"scrapy crawl {input_vendor} -o {input_vendor}.json")