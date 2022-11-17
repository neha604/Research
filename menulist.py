x=10



class menulist():
    def __init__(self,i,j,k,l):
        self.name=i
        self.id=j
        self.desc=k
        self.email=l

    def pg(self):
        if "password" in k:
            print("y")
        else:
            print("Not Yet Provided")


while x!=0:
        print("Welcome to Helpdesk")
        print("Select from the following choices: \n 0:Exit \n 1:Submit Helpdesk ticket \n 2:Show all tickets"
              "\n 3:Respond to ticket by Number \n 4: Re-open resolved ticket \n 5: Display Ticket Stats")
        x=int(input("select option" ))

        if x==1:
            i = input("enter your name")
            j = input("enter yiur id")
            k = input("enter desc")
            l = input("enter email")









n1=menulist(i,j,k,l)
n1.pg()
