def is_leap_year(Year):  
 
  if((Year % 400 == 0)  or  (Year % 100 != 0) and  (Year % 4 == 0)):   
    print("Given Year is a leap Year");  
   
  else:  
    print ("Given Year is not a leap Year")  
  
Year = int(input("Enter the year: "))  
 
is_leap_year(Year)  

















# import os

# def read_file(file_name):
#     file_handle = open(file_name,'w')
#     # print (file_handle.read())
#     file_handle.write("Leap year?")
#     file_handle.close()
    
# file_dir = os.path.dirname(os.path.realpath('D:/IthXD'))
# print (file_dir)

# #For accessing the file in the same folder
# file_name = "Date.txt"
# read_file(file_name)

# #For accessing the file in a folder contained in the current folder
# file_name = os.path.join(file_dir, file_name)
# read_file(file_name)



# #For accessing the file inside a sibling folder.
# file_name = os.path.join(file_dir, file_name)
# file_name = os.path.abspath(os.path.realpath(file_name))
# print (file_name)
# read_file(file_name)




