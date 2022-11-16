 # this class contains a menu text and password change function

class menu_list(object):
    def __init__(self):
       pass


#function generates a new password

    def pass_gen(self,ticket,default=not yet provided):
        #logic to create password will go here

    #return ticket

#display menu options and input prompt, actual control for each choice is in main script ,could move here later

    def get_menu(self,name,staffid,email,desc):

        #list of menu and logic to take input from user goes here

        self.name = input("Enter Name :  ")
        self.staffid = input("Enter Staff ID :  ")
        self.email = input("Enter your email :  ")
        self.desc = input("Enter Description")

        return menu





