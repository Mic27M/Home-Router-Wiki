import json
import os
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
                Path(output_dir['model']/"_index.md").touch()
        else:
            os.mkdir(output_dir["device_class"])
            Path(output_dir["device_class"]/"_index.md").touch()
            os.mkdir(output_dir["model"])
            Path(output_dir['model']/"_index.md").touch()
    else:
        os.mkdir(output_dir["vendor"])
        Path(output_dir['vendor']/"_index.md").touch()
        os.mkdir(output_dir["device_class"])
        Path(output_dir['device_class']/"_index.md").touch()
        os.mkdir(output_dir["model"])
        Path(output_dir['model']/"_index.md").touch()

    return output_dir['model']


def TestIfMarkdownExist(vendor_name, version, dir):
    file_exists = os.path.exists(f'{dir}/{vendor_name}{version}.md')

    if not file_exists:
        os.mknod(f'{dir}/{vendor_name}{version}.md')


def KeywordInFile(keyword,vendor,version,dir):
    try:
        f1 = open(f'{dir}/{vendor}{version}.md','r')
        lines = f1.readlines()
        f1.close()
        keyword_in_md = False
        for line in lines:
            if keyword in line:
                keyword_in_md = True

        return keyword_in_md

    except BaseException as err:
        print(f'(Error: {err})')
    


def ReplaceLine(old,vendor, dir):
    # print(f'replace: {old}')
    try:
        f1 = open(f'{dir}/{vendor}.md','r')
        lines = f1.readlines()
        f1.close()
    except BaseException as err:
        print(f'(Error: {err})')

    for line in lines:
        if old in line:
            line.replace("uptodate", "old")
            try:
                f1 = open(f'{dir}/{vendor}.md','w')
                f1.write(lines)
                f1.close()
            except BaseException as err:
                print(f'(Error: {err})')


def WriteVendor(vendor,model,version, dir):
   if KeywordInFile(f'# {vendor}',model,version, dir):
        print("Vendor already excists")
   else:
        try:
            f1 = open(f'{dir}/{model}{version}.md','w')
            f1.write(f'\n# {vendor}\n')
            f1.close()  
        except BaseException as err:
            print(f'(Error: {err})')


def WriteDeviceClass(device_class, model, version, dir): 
    if KeywordInFile(f'## {device_class}',model,version, dir):
        print('device class already excists')
    else:
        try:
            f1 = open(f'{dir}/{model}{version}.md','at')
            f1.write(f"\n## {device_class}\n")
            f1.write(f"\n|modell|version|date|url|filepath|checksum|status|")
            f1.write(f"\n|:---:|:---:|:---:|:---:|:---:|:---:|:---:|\n")
            f1.close()  
        except BaseException as err:
            print(f'(Error: {err})')


def WriteDevice(device, model, version, dir):
    if KeywordInFile(f'{device["model"]}',model,version, dir):
        if KeywordInFile(f'{device["model"]} |{device["version"]}',model,version, dir):
            print("device already in list")
        else:
            ReplaceLine(f'{device["model"]}|',model, dir)
    else:
        try:
            f1 = open(f'{dir}/{model}{version}.md','r')
            lines = f1.readlines()
            f1.close()
        except BaseException as err:
            print(f'(Error: {err})')

        for line in lines:
            if device["device_class"] in line:
                position_of_deviceclass = lines.index(line)

        filepath = f'[{device["filepath"]}](../../../../firmware_files/{device["filepath"]})'
        url = f'[{device["filepath"]}]({device["url"]})'

        lines.insert(position_of_deviceclass+4, f'|{device["model"]} |')  
        lines.insert(position_of_deviceclass+5, f'{device["version"]} |')
        lines.insert(position_of_deviceclass+6, f'{device["date"]} |')
        lines.insert(position_of_deviceclass+7, f'{url} |')
        lines.insert(position_of_deviceclass+8, f'{filepath} |')
        lines.insert(position_of_deviceclass+9, f'{device["checksum"]} |')
        lines.insert(position_of_deviceclass+10, f'{device["status"]} |\n')

        try:
            f1 = open(f'{dir}/{model}{version}.md','w')
            f1.writelines(lines)       
            f1.close()

        except BaseException as err:
            print(f'(Error: {err})')

## Start
# parser = argparse.ArgumentParser()
# parser.add_argument('-v', dest='vendor', required=True)
# args = parser.parse_args()

# input_vendor = args.vendor
# input_vendor = input_vendor.lower()

input_vendor = "tplink"

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
    device["status"] = devices['files'][0]['status']

    output_dir = MkOutputDir(device)

    TestIfMarkdownExist(device["model"], device['version'], output_dir)
    
    WriteVendor(device["vendor"],device["model"], device['version'],output_dir)
    WriteDeviceClass(device["device_class"],device["model"], device['version'] , output_dir)
    WriteDevice(device, device["model"], device['version'],output_dir)    