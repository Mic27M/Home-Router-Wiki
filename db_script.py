from sre_constants import SUCCESS
import statistics
import sqlalchemy
from sqlalchemy import func

engine = sqlalchemy.create_engine('sqlite:///Home_Router_DB.sqlite')
conn = engine.connect()


meta_data = sqlalchemy.MetaData(bind=engine)
sqlalchemy.MetaData.reflect(meta_data)

device = meta_data.tables['device']
vendor = meta_data.tables['Vendor']
device_class = meta_data.tables['Device_class']
db_info = meta_data.tables['db_info']

def InsertVendor(vend):
    stm = vendor.select()
    result = conn.execute(stm)
    # Test if vendor is alredy in table
    test = 0
    for row in result:
        if vend in str(row):
            test = 1
    if test !=1:
        stm = vendor.insert().values({"name": vend})
        conn.execute(stm)
                

def InsertDeviceClass(vend, dev_class):
    
    stm = device_class.select()
    result = conn.execute(stm)
    # Test if device_class is alredy in table
    test = 0
    for row in result:
        if vend in str(row) and dev_class in str(row):
            test = 1
    if test !=1:
        stm = device_class.insert().values({"vendor": vend, "device_class": dev_class})
        conn.execute(stm)


def InsertDevice(vend, dev_class, dev_name, fw_version, date, url, filepath, checksum):
    stm = device.select()
    result = conn.execute(stm)
    # Test if device is alredy in table
    test = 0
    for row in result:
        if (dev_name in str(row) and fw_version in str(row)):
            test = 1
    if test !=1:
        stm = device.insert().values({"vendor": vend, "device_class": dev_class, "device_name": dev_name, "fw_version":fw_version, "date": date, "url": url, "filepath": filepath, "checksum": checksum, "in in DB since": "now" })
        conn.execute(stm)


def InsertDBInfo(start, stop, stats, logfile, success):    
    stm = db_info.insert().values({"start_time": start, "stop_time": stop, "statistic": stats, "logfile": logfile, "success": success})
    conn.execute(stm)
    

def GetNextDBInfoID():
    stm = db_info.select()
    result = conn.execute(stm)

    all_id = []
    for row in result:
        all_id.append(row.id)
    
    max_id = max(all_id)

    return max_id + 1
    

def CountDBEntries(db):
    stm = db.select()
    result = conn.execute(stm)
    count = 0
    for row in result:
        count = count + 1
    
    return count


def StatisticDBInfo(vendor_start, vendor_stop, dv_class_start, dv_class_stop, device_start, device_stop):
    vendor_diff = vendor_stop - vendor_start
    dv_class_diff = dv_class_stop - dv_class_start
    device_diff = device_stop - device_start

    diff_stat = ""

    if vendor_diff > 0:
        diff_stat = diff_stat + f" new vendors: {vendor_diff} "

    if dv_class_diff > 0:
        diff_stat = diff_stat + f" new device_classes: {dv_class_diff} "

    if device_diff > 0:
        diff_stat = diff_stat + f" new devices: {device_diff} "

    return diff_stat



# GetNextDBInfoID()