# simple_file_organiser
This project contains simple functions to organise files on the disk.

Functions:
- __get_filelist(directory)__ - function returns list of all files in the directory;
  
- __get_elemlist(directory)__ - function returns list of all elements in the directory;
  
- __delete_files_by_name(directory, substring)__ - function deletes files that contain a 'substring' in their filename;
  
- __delete_files_by_date(directory, timestamp1, timestamp2=dt.now(), mode=0)__ - function deletes files created between timestamp1 and timestamp2. Timestamp format: '%d-%m-%Y %H:%M'. Mode: 0 - by creation date, 1 - by modification date;
  
- __move_files_by_name(old_directory, new_directory, substring)__ - function moves files that contain a 'substring' in their filename;
  
- __move_files_by_date(old_directory, new_directory, timestamp1, timestamp2=dt.now(), mode=0)__ - This function moves files created between timestamp1 and timestamp2.Timestamp format: '%d-%m-%Y %H:%M'. Mode: 0 - by creation date, 1 - by modification date;
  
- __copy_files_by_name(old_directory, new_directory, substring)__ - function copies files that contain a 'substring' in their filename;
  
- __copy_files_by_date(old_directory, new_directory, timestamp1, timestamp2=dt.now(), mode=0)__ -  function copies files created between timestamp1 and timestamp2. Timestamp format: '%d-%m-%Y %H:%M'. Mode: 0 - by creation date, 1 - by modification date;
