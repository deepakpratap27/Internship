import json
from re import S
from this import s

class User:
    def __init__(self, first_name, last_name, mobile_number, email_id, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.mobile_number = mobile_number
        self.email_id = email_id
        self.username = username
        self.password = password

def is_registered():
    user_registered=input("Are you registered (Y/N):").upper()
    if user_registered=='Y':
        return True

def registration():
    first_name = str(input('Enter your first name: '))
    last_name = str(input('Enter your last name: '))
    mobile_number = str(input('Enter your mobile number: '))
    email_id = str(input('Enter your email ID: '))
    username = str(input('Enter your username: '))
    password = str(input('Enter your password: '))
    user_object = User(first_name, last_name, mobile_number, email_id, username, password)
    return user_object

def write_json(user_object):
    new_data = json.dumps(user_object.__dict__)
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data['user_info'].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)
        

def login(username, password):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        if file_data:
            for i in range(0,len(file_data["user_info"])):
                obj=json.loads(file_data["user_info"][i])
                if (obj['username']==username and obj['password']==password):
                    print_data=str(input("Logged in!\nDo you want to print details?(Y/N):")).upper()
                    if print_data=='Y':
                        print('First name: %s\nLast name: %s\nMobile number: %s\nEmail ID: %s\n'
                        % (obj['first_name'], obj['last_name'], obj['mobile_number'], obj['email_id'])) 
                

def main():
    if is_registered():
        username=str(input("Enter username: "))
        password=str(input("Enter Password: "))
        login(username, password)
    else:
        user_object=registration()
        write_json(user_object)
        print("Registered!")

global filename
filename='user_details.json'

if __name__ == '__main__':
    main()