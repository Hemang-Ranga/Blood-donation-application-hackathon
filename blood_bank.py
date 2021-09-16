print("---------------------------------------++ WELCOME TO XYZ BLOOD DONATION BLOOD SERVICES ++-----------------------------------------")
#It is assumed that there is only one admin
#password of the admin for logging in into the application
admin_password = "cba321"

#The users which are already signed in
users = ['Rani', 'Ramesh', 'Mahesh', 'Suresh', 'Anup', 'Sushila', 'Pooja', 'Manav']

#Passwords of the signed in users index-wise
user_passwords = ['zyx987', 'R@m123', 'M@h567', 'sur123', 'lmnop', 'ila@sush', 'P#2o', 'M@n101']

#Areas of the cty are divided into 6 parts: City side East, West, North, South, North-East, South-West
#so the location of registered users is stored in this list index-wise
user_location = ['South', 'West', 'North-East', 'West', 'East', 'South-West', 'North', 'North-East']

#There are 4 types of blood groups: A,B, AB, O each has two subtypes: A+, A-, B+, B-, O+, O-, AB+, AB-
# The Blood group of registered users are there in list index-wise
user_group = ['O-', 'AB+', 'A-', 'B+', 'O+', 'B-', 'A+', 'AB-']

#we are assuming that Ramesh and Manav have given the request to admin
user_request = [users[1], users[7]]

#assuming that admin sent request to Anup, Pooja
admin_request = [users[4], users[6]]

#Blood banks in this have code names as BB-1, BB-2 etc. below is the dictionary with blood bank names and it's location
blood_banks = {'BB1': 'North', 'BB2': 'East', 'BB3': 'West', 'BB4': 'West', 'BB5': 'North-East', 'BB6': 'North-East', 'BB7': 'South', 'BB8': 'South', 'BB9': 'South-West', 'BB10': 'North'}

#asking the application user that he is blood donation admin or user 
ask = int(input("Please specify, you are a User or an Admin: \n1__Admin \n2__User(The one who can donate or accept blood)\n"))
if ask == 1:
    ad_pass=input("Enter admin password: ")
    if ad_pass == admin_password:
        print("Admin Succesfully logged in")
        print("------WELCOME! Admin------")
        while True:
            print("\nWhat you want to know: \n1__Details of blood banks\n2__Details of the users\n3__Add hoptals to this program\n4__Check for any request of blood doner\n5__Send request to user\n6__Exit")
            x = int(input("Enter the choice from above: "))
            if x == 1:
                print("added blood banks in this city: ", blood_banks.keys())
                print("Location of these blood banks: ", blood_banks.values())
            elif x == 2:
                print("There are 8 signed in users")
                for i in range(8):
                    print(i+1, "th user")
                    print("**name of user: ", users[i])
                    print("**location in which user live: ", user_location[i])
                    print("**blood group of user: ", user_group[i])
                    print("------------------------------")
            elif x == 3:
                print("Hospitals which are not part of blood bank program: \nH-1(South)\nH-2(West)\nH-3(North)\nH-4(South-West)")
                y = int(input("Which one you want to enter(1,2,3 or 4): "))
                if y == 1:
                    blood_banks.update({'H-1': 'South'})
                    print("Hospital added")
                    print("added blood banks in this city: ", blood_banks.keys())
                    print("Location of these blood banks: ", blood_banks.values())
                elif y == 2:
                    blood_banks.update({'H-2': 'West'})
                    print("Hospital added")
                    print("added blood banks in this city: ", blood_banks.keys())
                    print("Location of these blood banks: ", blood_banks.values())
                elif y == 3:
                    blood_banks.update({'H-3': 'North'})
                    print("Hospital added")
                    print("added blood banks in this city: ", blood_banks.keys())
                    print("Location of these blood banks: ", blood_banks.values())
                elif y == 4:
                    blood_banks.update({'H-4': 'South-West'})
                    print("Hospital added")
                    print("added blood banks in this city: ", blood_banks.keys())
                    print("Location of these blood banks: ", blood_banks.values())
                else:
                    print("Invalid input")
            elif x == 4:
                print("There are two requests by", len(user_request), "users: ", user_request)
                z=input("Do you want to accept the request('y' or 'n'): ")
                if z == 'y':
                    a=int(input("whose request you want to accept(press 1,2 and press 3 for accepting all): "))
                    if a == 1:
                        print("Request accepted of ", users[1])
                    elif a == 2:
                        print("Request accepted of ", users[7])
                    elif a == 3:
                        print("All requests got accepted")
                    else:
                        print("Wrong input, request not accepted")
                else:
                    print("Request not accepted")
            elif x == 5:
                print("Send request to which user: ")
                print(users)
                req_user=input("Enter user name: ")
                if req_user in users:
                    if req_user != users[4] and req_user != users[6]:
                        admin_request.append(req_user)
                        print("Request sent")
                        print("Sent request by admin to users : ", admin_request)
                    else:
                        print("Request already sent previously")
                        print("Sent request by admin to users : ", admin_request)
                else:
                    print("Request not sent, entered user is not regitered")
                    print("Sent request by admin to users : ", admin_request)
            elif x == 6:
                print("Exit")
                break
            else:
                print("Incorrect input")
    else:
        print("Wrong password")
elif ask == 2:
    user_options = int(input("1__User login \n2__New user sign in \n"))
    if user_options == 1:
        us_name=input("Enter User name: ")
        if us_name in users:
            print("User found")
            us_pass=input("Enter your password: ")
            if us_pass == user_passwords[users.index(us_name)]:
                print("User succesfully logged in")
                while True:
                    print("\nWhat you want to do: \n1__Request for blood of particular group\n2__Check total no. of users\n3__Check for requests given to you by admin\n4__Exit")
                    b=int(input("Choose a choice from above: "))
                    if b==1:
                        group=input("Which blood group you want: ")
                        if group not in user_group:
                            print("invalid blood group")
                        else:
                            print("User with this blood group is present")
                            #The user name will be added in the user request list
                            if us_name != users[1] and us_name != users[7]:
                                user_request.append(us_name)
                                print("Request sent to admin succesfully")
                            else:
                                print("Request already sent")
                    elif b==2:
                        #user can only know know number and names
                        print("Total number of users:", len(users))
                        print("Name of users: ")
                        for I in range(len(users)):
                            print(users[I])
                    elif b==3:
                        #assuming that admin sent request to Anup, Pooja only
                        if us_name != users[4] and us_name != users[6]:
                            print("you got no requests from admin")
                        else:
                            print("You got a request from the admin")
                            c=input("Do you want to accept the request('y' or 'n'): ")
                            if c == 'y':
                                print("Request accepted")
                            else:
                                print("Request not accepted")
                    elif b==4:
                        print("Exit")
                        break
                    else:
                        print("wrong input")
            else:
                print("Wrong password")
        else:
            print("User not registered")
    elif user_options == 2:
        new_us_name=input("Enter user name: ")
        users.append(new_us_name)
        new_us_pass=input("Enter your password: ")
        user_passwords.append(new_us_pass)
        while True:
            new_us_loc=input("Enter your location in this City: ")
            if new_us_loc in user_location:
                user_location.append(new_us_loc)
                break
            else:
                print("Wrong city location")
        while True:
            new_us_grp=input("Enter your blood group: ")
            if new_us_grp in user_group:
                user_group.append(new_us_grp)
                break
            else:
                print("Wrong blood group")
        print("User signed in and logged in to the account")
        while True:
            print("\nWhat you want to do: \n1__Request for blood of particular group\n2__Check total no. of users\n3__Check for requests given to you by admin\n4__Exit")
            b2=int(input("Choose a choice from above: "))
            if b2==1:
                group=input("Which blood group you want: ")
                if group not in user_group:
                    print("invalid blood group")
                else:
                    print("User with this blood group is present")
                    user_request.append(new_us_name)
                    print("Request sent to admin succesfully")
            elif b2==2:
                #user can only know know number and names
                print("Total number of users:", len(users))
                print("Name of users: ")
                for I in range(len(users)):
                    print(users[I])
            elif b2==3:
                #new user will not get any request from admin ofcourse
                print("you got no requests from admin")
            elif b2==4:
                print("Exit")
                break
            else:
                print("wrong input")
    else:
        print("wrong input")
else:
    print("Wrong input")