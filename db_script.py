import sqlalchemy
import time

engine = sqlalchemy.create_engine('sqlite:///Home_Router_DB.sqlite')
conn = engine.connect()


meta_data = sqlalchemy.MetaData(bind=engine)
sqlalchemy.MetaData.reflect(meta_data)

device = meta_data.tables['device']
vendor = meta_data.tables['Vendor']
device_class = meta_data.tables['Device_class']

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
        if dev_class in str(row):
            test = 1
    if test !=1:
        stm = device_class.insert().values({"vendor": vend, "device_class": dev_class})
        conn.execute(stm)


def InsertDevice(vend, dev_class, dev_name, fw_version, date, url, filepath, checksum):
    today = time.ctime(time.time())
    stm = device.select()
    result = conn.execute(stm)
    # Test if device is alredy in table
    test = 0
    for row in result:
        if (dev_name in str(row) and fw_version in str(row)):
            test = 1
    if test !=1:
        stm = device.insert().values({"vendor": vend, "device_class": dev_class, "device_name": dev_name, "fw_version":fw_version, "date": date, "url": url, "filepath": filepath, "checksum": checksum, "in in DB since": today })
        conn.execute(stm)


InsertDevice("test", "test_class","test_name", "test_version", "test_date", "test_url", "test_path", "test_checksum")
InsertVendor("test2")
InsertDeviceClass("test3", "test3_class")