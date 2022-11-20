import json


class Registration:
    def __init__(self,First_Name,Last_Name,Mobile_Number,Email_ID,UserName,PassWord):

        self.First_Name=First_Name
        self.Last_Name=Last_Name
        self.Mobile_Number=Mobile_Number
        self.Email_ID = Email_ID
        self.UserName=UserName
        self.PassWord=PassWord
 

   granted = False
   
   def grant():
    global granted
    granted = True
    
    
    
   def login(UserName,PassWord):
    success = False
    file = open("user_detail.json","r")
    for i in file:
         a,b = i.split(",")
         b = b.strip()
         if(a==UserName and b==PassWord):
             success = True
             break
    file.close()
    if(success):
        print("Login Successful")
        grant()
    else:
        print("wrong user name or password")
        
  def register(UserName,PassWord,First_Name,Last_Name,Mobile_Number,Email_ID):
    file = open("user_detail.json","a")
    file.write("\n"+UserName+","+PassWord)
    grant()
  def access(option):
    global UserName
    global PassWord
    if(option=="login"):
        UserName = input("Enter your name: ")
        PassWord = input("Enter your password: ")
        login()
    else:
        print("Enter your name and password to register")
        UserName = input("Enter your UserName: ")
        PassWord = input("Enter your password: ")
        First_Name =input('Enter your FirstName: ')
        Last_Name = input('Enter your LastName: ')
        Mobile_Number=input("Enter your Mobile Number: ")
        Email_ID =input("Enter your Email-ID")


        register(UserName,PassWord,First_Name,Last_Name,Mobile_Number,Email_ID)

  def begin():
    global option
    option = input("Login or Register (Login,Reg): ")
    if(option!="login" and option!="reg"):
        begin()
        
begin()
access(option)

if(granted):
    print("### USER DETAILS ###")
    print("Username: ",UserName)
    print("Name: ",First_Name,Last_Name ) 
