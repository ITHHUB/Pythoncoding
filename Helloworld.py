# How=int(input("How many words to analyse?"))
# print("OK-I will analyse",How,"words")
# word=[0 for i in range (How)]
# print(word)
# Num=0
# Numvowel=0
# Numletter=0
# while(Num<How):
  
#   word[Num]=input("word:")
#   Num=Num+1
# print(word)

# check=word[0]
# c_num=len(check)

# for j in range(c_num):
#   if(check[j]=="A"):
#     print("vowel")
#     Numvowel=Numvowel+1
    
#   elif(check[j]=="E"):
#     print("vowel")
#     Numvowel=Numvowel+1
    
#   elif(check[j]=="I"):
#     print("vowel")
#     Numvowel=Numvowel+1
    
#   elif(check[j]=="O"):
#     print("vowel")
#     Numvowel=Numvowel+1
    
#   elif(check[j]=="U"):
#     print("vowel")
#     Numvowel=Numvowel+1
    
#   else:
#     print("letter")
#     Numletter=Numletter+1
#     print("Num letter:",Numletter)
#     print("Num vowel",Numvowel)
#from array import *
#from ctypes import Array
#arrey1=array('i',[1,2,3,4,5,6,7,8,9,10])
#arrey2=array('i',[0,0,0])
#arrey3=array('i',[0,0,0])
#for i in range(3):
 #arrey2[i]=int(input("plese select:"))
 #arrey1.append(arrey2[i])
 #arrey3[i]=arrey1.index(arrey2[i])

#print(arrey1)
#print(arrey3)

#HW
# from array import *
# name=("English ","Math","Science")

# Credit=int(input('Your credit:'))
# grade=array("i",[4,3,2])
# print(name)
# print(Credit)
# print(grade)
# Change=input("Do you want to change your grade?(Yes/No):")
# while(Change=="Yes"):
#     name=input("which subjects?")
#     index=name.index(name)
#     print("The index of",name,index)
#     grade2=int(input("what is your new grade?:"))
#     grade[index]
   
#     Change=input("Do you want to change your grade?(Yes/No):")



# list=[]
# dict={'subject':'unknown','credit':0,'grade':0}
# Ask=input("Add for subject?(Yes/No):")
# while(Ask=="Yes"):
#     subject=input("select your subject")
#     credit=int(input('Your credict:'))
#     grade=int(input('your grade:'))
#     dict['subject']=subject
#     dict['credit']=credit
#     dict['grade']=grade
#     list.append(dict)
#     Ask=input("Do you want to add more subject?(Yes/No):")
#     list2={'subject':subject,'credit':credit,'grade':grade}
#     list.append(list2)
# Change=input("Do you want to change your grade?(Yes/No):")
# while(Change=="Yes"):
#    Subject=input('Enter your subject:')
#    dict['subject']=Subject
#    Grade=int(input("Your new grade?:"))
#    dict['grade']=Grade
#    print("Subject",dict['subject'])
#    print("Grade",dict['grade'])
#    Change=input("Do you want to change your grade?(Yes/No):")




# subjects=[]
# grades=[]

# Ask=input("Add for subject?(Yes/No):")
# while(Ask=="Yes"):
#     subject=input("select your subject:")
   
#     grade=int(input('your grade:'))
#     subjects.append(subject)
#     grades.append(grade)
#     Dict=dict(zip(subjects,grades))
    
    
#     Ask=input("Do you want to add more subject?(Yes/No):")
#     print(Dict)
#     print("min",min(Dict,key=Dict.get))
#     print("max",max(Dict,key=Dict.get))
    
# Change=input("Do you want to change your grade?(Yes/No):")
# while(Change=="Yes"):
#     Subject=input('Enter your subject:')
#     Dict['subject']=Subject
#     Grade=int(input("Your new grade?:"))
#     Dict['grade']=Grade
#     print("Subject",Dict['subject'])
#     print("Grade",Dict['grade'])
#     Change=input("Do you want to change your grade?(Yes/No):")


# bookings=[]
# Mode=input("Enter mode(q-quit,b-booking,c-cancel,p-print booking):")

# while(Mode!="q"):
#  if(Mode=="b"):
#     Name=input("Your name:")
#     checkin=int(input("Enter checkin day:"))
#     checkout=int(input("Enter checkout day:"))
#     roomtype=input("Select your type:")
#     BookingNumber=checkin*checkout
#     booking={"Name":Name,"check in":checkin,"check out":checkout,"roomtype":roomtype,"BookingNumber":BookingNumber}
#     bookings.append(booking)
#     Choice=input("Do you want to booking more?(Yes/No):")    
#     print(bookings)
#     print("Booking success")
#  elif(Mode=="c"):
#     BookingNumbers=int(input("Your book number:"))
#     for booking in bookings:
#        if booking['BookingNumber']==BookingNumbers:
#           bookings.remove(booking)
#  elif(Mode=="p"):
#     print(bookings)

#  Mode=input("Enter mode(q-quit,b-booking,c-cancel,p-print booking):")



# def multiplication_or_sum(num1, num2):
#     # calculate product of two number
#     product = num1 * num2
#     # check if product is less then 1000
#     if product <= 1000:
#         return product
#     else:
#         # product is greater than 1000 calculate sum
#         return num1 + num2
#num1=int(input("num1:"))
#num2=int(input("num2:"))
# # first condition
# result = multiplication_or_sum(20, 30)
# print("The result is", result)

# # Second condition
# result = multiplication_or_sum(40, 30)
# print("The result is", result)


# Num=0
# for i in range(0,10):
#     Sum1=Num+i
#     print("Current Number",i,"Previous Number",Sum1)
    
# String=input("word:")
# print("Original String is",String)
# print("Printing only even index chars")





income = int(input("Your income :"))
salary = income * 12
tax = 0
tax1 = 0
tax2 = 0
tax3 = 0
tax4 = 0
tax5 = 0
tax6 = 0
tax7 = 0
tax8 = 0
if(income <= 150000):
    tax1 = 0
elif(income <= 300000):
    
    x1 = income - 150000 
   
    tax2 = x1 * 5 / 100
elif(income<=500000):
    x2 = income - 300000
    tax3 = x2*10 / 100
elif(income<=750000):
    x3 = income - 500000
    tax4 = x3*15 / 100
elif(income<=1000000):
    x4 = income - 750000
    tax5 = x4*20 / 100
elif(income<=2000000):
    x5 = income - 1000000
    tax6 = x5*25 / 100
elif(income<=5000000):
    x6 = income - 2000000
    tax7 = x6*30 / 100
elif(income>500000):
    x7 = income - 5000000
    tax8 = x7*35 / 100


print("Total tax to pay is", tax+tax1+tax2+tax3+tax4+tax5+tax6+tax7+tax8)
