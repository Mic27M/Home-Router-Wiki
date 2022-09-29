import os
from pathlib import Path


cwd = Path(os.getcwd())

log_dir = Path(cwd/'logs')

def LogfileCounter():
    count = 0
    for log in os.listdir(log_dir):
    # check if current path is a file
        if os.path.isfile(os.path.join(log_dir, log)):
            count += 1
    return count


def CurrentLogfile(log_number):
    log = log_dir/f'logfile{log_number}.log'
    return log


def CountWarnings():
    counter = 0
    f1 = open(f'{current_log}','r')
    lines = f1.readlines()
    f1.close()
    for line in lines:
        if "WARNING" in line:
            counter = counter + 1
    
    return counter

def UpdateSuccess():
    counted_warnings = CountWarnings()
    if counted_warnings == 0:
        return "No Anomalies"
    elif counted_warnings == 1:
        return f"{counted_warnings} WARNING!!!"
    else:
        return f"{counted_warnings} WARNINGS!!!"


log_number = LogfileCounter()
current_log = CurrentLogfile(log_number)


