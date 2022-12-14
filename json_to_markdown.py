import json
import os
import argparse
from pathlib import Path

def MkOutputDir(vendor_dict):
    cwd = os.getcwd()
    wiki_dir = cwd+"/geekdoc/sites/content/"
    output_dir = {}
    output_dir["vendor"]= Path(f'{wiki_dir}/{vendor_dict["vendor"]}')
    output_dir["device_class"] = Path(f'{wiki_dir}/{vendor_dict["vendor"]}/{vendor_dict["device_class"]}')
    output_dir["model"] = Path(f'{wiki_dir}/{vendor_dict["vendor"]}/{vendor_dict["device_class"]}/{vendor_dict["model"]}')

    if output_dir["vendor"].is_dir():
        if output_dir["device_class"].is_dir():
            if output_dir["model"].is_dir():
                return output_dir['model']
            else:
                os.mkdir(output_dir["model"])
        else:
            os.mkdir(output_dir["device_class"])
            Path(output_dir["device_class"]/"_index.md").touch()
            os.mkdir(output_dir["model"])
    else:
        os.mkdir(output_dir["vendor"])
        Path(output_dir['vendor']/"_index.md").touch()
        os.mkdir(output_dir["device_class"])
        Path(output_dir['device_class']/"_index.md").touch()
        os.mkdir(output_dir["model"])

    return output_dir['model']


def TestIfMarkdownExist(device_name, dir):
    file_exists = os.path.exists(f'{dir}/{device_name}.md')

    if not file_exists:
        os.mknod(f'{dir}/{device_name}.md')
        return False

    return True


def KeywordInFile(keyword,device,dir):
    try:
        f1 = open(f'{dir}/{device}.md','r')
        lines = f1.readlines()
        f1.close()
        keyword_in_md = False
        for line in lines:
            if keyword in line:
                keyword_in_md = True
                return keyword_in_md

        return keyword_in_md

    except BaseException as err:
        print(f'(Error: {err})')


def WriteVendor(vendor, model, dir):
    try:
        f1 = open(f'{dir}/{model}.md','w')
        f1.write(f'\n# {vendor}\n')
        f1.close()  
    except BaseException as err:
        print(f'(Error: {err})')


def WriteDeviceClass(device_class, model, dir): 
    try:
        f1 = open(f'{dir}/{model}.md','at')
        f1.write(f"\n## {device_class}\n")
        f1.close()  
    except BaseException as err:
        print(f'(Error: {err})')


def WriteDevice(device, model, dir):
    # if model is in MD:
    if KeywordInFile(f'{device["model"]}',model, dir):
        # if firmware version of model is in MD:
        if KeywordInFile(f'|{device["model"]}|{device["version"]}', model, dir):
            print("device already in list")
        # if just another version of the firmware is in the MD
        else:
            filepath = f'[{device["filepath"]}](../../../../firmware_files/{device["filepath"]})'
            url = f'[{device["filepath"]}]({device["url"]})'
            
            try:
                f1 = open(f'{dir}/{model}.md','a')
                f1.write(f'|{device["model"]}|{device["version"]}|{device["date"]}|{url}|{filepath}|{device["checksum"]}|\n')
                f1.close()
            except BaseException as err:
                print(f'(Error: {err})')

    # if model is NOT in MD:
    else:
        filepath = f'[{device["filepath"]}](../../../../firmware_files/{device["filepath"]})'
        url = f'[{device["filepath"]}]({device["url"]})'

        try:
            f1 = open(f'{dir}/{model}.md','at')
            f1.write(f"\n|modell|version|date|url|filepath|checksum|")
            f1.write(f"\n|:---:|:---:|:---:|:---:|:---:|:---:|\n")
            f1.write(f'|{device["model"]}|{device["version"]}|{device["date"]}|{url}|{filepath}|{device["checksum"]}|\n')
            f1.close()  
        except BaseException as err:
            print(f'(Error: {err})')
       

## Start
parser = argparse.ArgumentParser()
parser.add_argument('-v', dest='vendor', required=True)
args = parser.parse_args()

input_vendor = args.vendor
input_vendor = input_vendor.lower()

# input_vendor = "zyxel"

try:
    with open(f'router_json/{input_vendor}.json', 'r') as read_file:
        device_json_list = json.load(read_file)
        read_file.close()
        
except BaseException as err:
    print(f'Something went wrong while reading the file: {err}')


device ={}

for devices in device_json_list:

    device["vendor"] = devices['vendor'][0]
    device["device_class"] = devices['device_class'][0]
    device["model"] = devices['device_name'][0]
    device["version"] = devices['firmware_version'][0]
    device["date"] = devices['release_date'][0]
    device["url"] = devices['files'][0]['url']
    device["filepath"] = devices['files'][0]['path']
    device["checksum"] = devices['files'][0]['checksum']
    # device["status"] = devices['files'][0]['status']

    output_dir = MkOutputDir(device)

    mdExisted= TestIfMarkdownExist(device["model"], output_dir)

    if not mdExisted:
        WriteVendor(device["vendor"],device["model"],output_dir)
        WriteDeviceClass(device["device_class"],device["model"], output_dir)
        
    WriteDevice(device, device["model"],output_dir)    