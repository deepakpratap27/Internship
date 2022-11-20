import json





f = open("details.json","w+")
details = {}
command = ""
while command != 'exit':
    command = input('Enter a command(options: register,retrieve): ')
    command =command.lower()
    if command == "register" :
        FirstName = input('Enter your FirstName : ')
        LastName = input('Enter your LastName : ')
        Number = input('Phone number: ')
        Email_ID = input('Email ID: ')
        UserName = input('UserName : ')
        PassWord = input("Password : ")
        details[UserName] = {'FirstName':FirstName , 'LastName': LastName , 'Number' :Number , 'Email-ID': Email_ID , 'PassWord': PassWord}
        f.write(json.dumps(details))
    elif command == 'retrieve':
        UserName = input('Enter the UserName')
        if UserName in details:
             pswd =input("please Enter Password")
             if pswd == details[PassWord] :
                print(details[FirstName],details[LastName],details[Number],details[Email_ID])
             else :
                print("Please Enter Correct Password")
        else:
            print('User Details not found')
