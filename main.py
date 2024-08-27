import os
from datetime import datetime as dt
import platform


def get_filelist(directory):
    "This function returns list of all files in the directory."
    files = os.listdir(directory)
    return [f for f in files if os.path.isfile(directory+'/'+f)]


def get_elemlist(directory):
    "This function returns list of all elements in the directory."
    return os.listdir(directory)


def delete_files_by_name(directory, substring):
    "This function deletes files that contain a 'substring' in their filename."
    filelist = get_filelist(directory)
    for elem in filelist: 
        if substring in elem: os.remove(directory + elem) 


def delete_files_by_date(directory, timestamp1, timestamp2=dt.now(), mode=0):
    """"This function deletes files created between timestamp1 and timestamp2.
    Timestamp format: '%d-%m-%Y %H:%M'. Mode: 0 - by creation date, 1 - by 
    modification date"""
    
    timestamp1 =  dt.strptime(timestamp1, '%d-%m-%Y %H:%M')
    if type(timestamp2) == str:
        timestamp2 = dt.strptime(timestamp2, '%d-%m-%Y %H:%M')
        
    filelist = get_filelist(directory)
    if mode == 0:
        filedate = [dt.fromtimestamp(os.path.getctime(directory + elem)) for elem in filelist]
    else:
        filedate = [dt.fromtimestamp(os.path.getmtime(directory + elem)) for elem in filelist]
    
    for i in range(len(filedate)): 
        if timestamp1 <= filedate[i] <= timestamp2: os.remove(directory + filelist[i])


def move_files_by_name(old_directory, new_directory, substring):
    "This function moves files that contain a 'substring' in their filename."
    filelist = get_filelist(old_directory)
    for elem in filelist: 
        if substring in elem: os.rename(old_directory + elem, new_directory + elem)
    

def move_files_by_date(old_directory, new_directory, timestamp1, timestamp2=dt.now(), mode=0):
    """"This function moves files created between timestamp1 and timestamp2.
    Timestamp format: '%d-%m-%Y %H:%M'. Mode: 0 - by creation date, 1 - by 
    modification date"""
    
    timestamp1 =  dt.strptime(timestamp1, '%d-%m-%Y %H:%M')
    if type(timestamp2) == str:
        timestamp2 = dt.strptime(timestamp2, '%d-%m-%Y %H:%M')
        
    filelist = get_filelist(old_directory)
    if mode == 0:
        filedate = [dt.fromtimestamp(os.path.getctime(old_directory + elem)) for elem in filelist]
    else:
        filedate = [dt.fromtimestamp(os.path.getmtime(old_directory + elem)) for elem in filelist]
    
    for i in range(len(filedate)): 
        if timestamp1 <= filedate[i] <= timestamp2:
            os.rename(old_directory + filelist[i], new_directory + filelist[i])
        

def copy_files_by_name(old_directory, new_directory, substring):
    "This function copies files that contain a 'substring' in their filename."
    filelist = get_filelist(old_directory)
    for elem in filelist: 
        if substring in elem: 
            if platform.system() == 'Widnows':
                os.system(("copy '" + old_directory + elem + "' '" + new_directory + elem + "'"))
            else:
                os.system("cp '" + old_directory + elem + "' '" + new_directory + elem + "'")


def copy_files_by_date(old_directory, new_directory, timestamp1, timestamp2=dt.now(), mode=0):
    """"This function copies files created between timestamp1 and timestamp2.
    Timestamp format: '%d-%m-%Y %H:%M'. Mode: 0 - by creation date, 1 - by 
    modification date"""
    
    timestamp1 =  dt.strptime(timestamp1, '%d-%m-%Y %H:%M')
    if type(timestamp2) == str:
        timestamp2 = dt.strptime(timestamp2, '%d-%m-%Y %H:%M')
        
    filelist = get_filelist(old_directory)
    if mode == 0:
        filedate = [dt.fromtimestamp(os.path.getctime(old_directory + elem)) for elem in filelist]
    else:
        filedate = [dt.fromtimestamp(os.path.getmtime(old_directory + elem)) for elem in filelist]
    
    for i in range(len(filedate)): 
        if timestamp1 <= filedate[i] <= timestamp2:            
            if platform.system() == 'Widnows':
                os.system("copy '" + old_directory + filelist[i] + "' '" + new_directory + filelist[i] + "'")
            else:
                os.system("cp '" + old_directory + filelist[i] + "' '" + new_directory + filelist[i] + "'")


if __name__ == '__main__':
    copy_files_by_date(r'/Users/', r'/Users/Example/','27-08-2024 20:53')
    
