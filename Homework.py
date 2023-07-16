# def is_leap_year(Year):  
 
#   if((Year % 400 == 0)  or  (Year % 100 != 0) and  (Year % 4 == 0)):   
#     print("Given Year is a leap Year");  
   
#   else:  
#     print ("Given Year is not a leap Year")  
  
# Year = int(input("Enter the year: "))  
 
# is_leap_year(Year)  

















import os
from datetime import datetime, timezone, timedelta



TH_dateTime = datetime.now(timezone(timedelta(hours=+7), 'MST'))
print("In TH::", TH_dateTime)


CA_dateTime = datetime.now(timezone(timedelta(hours=-7), 'MST'))
print("In CA::", CA_dateTime)
def read_file(file_name):
    file_handle = open(file_name,'w')
   
    file_handle.write("Convert time from Thailand to Canada :")
    file_handle.write("Input:")
    file_handle.close()
    
file_dir = os.path.dirname(os.path.realpath('D:/IthXD'))
print (file_dir)


file_name = "Time.txt"
read_file(file_name)


file_name = os.path.join(file_dir, file_name)
read_file(file_name)


file_name = os.path.join(file_dir, file_name)
file_name = os.path.abspath(os.path.realpath(file_name))
print (file_name)
read_file(file_name)




