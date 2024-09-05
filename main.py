import csv
from termcolor import colored
class ContactDetail:
    def __init__(self,name,email,phonenumber) :
        self.name = name
        self.email = email
        self.phonenumber = phonenumber
 
    def AddContact(self):
        print("Enter Your Details Below :")
        self.name = input("Enter Your Name : ")
        self.email = input("Enter Email : ")
        self.phonenumber = input("Enter Contact : ")
        print("Contact Added Successfully")
        with open('contacts.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(["Name", "Email", "Phone Number"])
                writer.writerow([self.name, self.email, self.phonenumber])
            else:
                writer.writerow([self.name, self.email, self.phonenumber])
 
    def ViewContact(self):
        with open('contacts.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"{row[0]} \t{row[1]} \t{row[2]}")
                print("-"*30)
 
    def DeleteContact(self):
        email = input("Enter Email : ")
        rows_to_keep = []
        with open('contacts.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[1] == email:
                    continue
                rows_to_keep.append(row)
        with open('contacts.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows_to_keep)
 
        print("Contact deleted successfully.")
 
 
    def SearchContact(self):
        email_name = input("Enter Email or name : ")
        with open('contacts.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[1] == email_name or row[0] == email_name:
                    print("\n"*5)
                    print(colored("*"*20, "yellow", attrs=["bold"]))
                    print(colored("Name :", "red", attrs=["bold"]), colored(row[0], "red"))
                    print(colored("Email:", "blue", attrs=["bold"]), colored(row[1], "blue"))
                    print(colored("Phone number :", "green", attrs=["bold"]), colored(row[2], "green"))
                    print(colored("*"*20, "yellow", attrs=["bold"]))
                    print("\n"*5)
 
 
def main():
    while True: 
        print ("Welcome to Phonebook")
        print ("Enter Your Choice : ")
        print ("1. Add Contact")
        print ("2. View Contacts")
        print ("3. Delete Contacts")
        print ("4. Search Contact")
        print ("5. Exit")
        choice = int(input())
        if choice == 1:
            contact = ContactDetail("","","")
            contact.AddContact()
        elif choice == 2:
            contact = ContactDetail("","","")
            contact.ViewContact()
        elif choice == 3:
            contact = ContactDetail("","","")
            contact.DeleteContact()
        elif choice == 4:
            contact = ContactDetail("","","")
            contact.SearchContact()
        elif choice == 5:
            exit()
        else:
            print("Invalid Choice")
            exit()
 
        continue_choice = input("Do you want to continue? (y/n): ")
        if continue_choice.lower() != "y":
            break
 
main()
