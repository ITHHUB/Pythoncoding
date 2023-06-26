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


bookings=[]
Mode=input("Enter mode(q-quit,b-booking,c-cancel,p-print booking):")

while(Mode!="q"):
 if(Mode=="b"):
    Name=input("Your name:")
    checkin=int(input("Enter checkin day:"))
    checkout=int(input("Enter checkout day:"))
    roomtype=input("Select your type:")
    BookingNumber=checkin*checkout
    booking={"Name":Name,"check in":checkin,"check out":checkout,"roomtype":roomtype,"BookingNumber":BookingNumber}
    bookings.append(booking)
    Choice=input("Do you want to booking more?(Yes/No):")    
    print(bookings)
    print("Booking success")
 elif(Mode=="c"):
    BookingNumbers=int(input("Your book number:"))
    for booking in bookings:
       if booking['BookingNumber']==BookingNumbers:
          bookings.remove(booking)
 elif(Mode=="p"):
    print(bookings)

 Mode=input("Enter mode(q-quit,b-booking,c-cancel,p-print booking):")