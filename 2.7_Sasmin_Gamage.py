import datetime

def force_number(message,lower,upper): #The purpose of this function is to enter in a valid number within
    while True: #infinite loop that keeps repeating until a valid number is entered
        try:
            num=int(input(message)) #try to convert the input into an interger
            if lower <= num <= upper: #check if number is in range
                break
            else:
                print(f"Invalid number, please enter between {lower}-{upper}")
        except ValueError: #this will only print if you type in a string
            print("Error, please enter in a number not text")
    return num #returning back a valid number within a range

def ticket_options():
ticket_options()

def force_name(message,lower,upper):
    while True: #this is an infinite loop that will only break if a valid name is entered
        name=str(input(message)).title()
        if len(name)>=lower and len(name)<=upper and name.isalpha():
            print("The name is valid")
            break #the loop breaks if the above conditions is met
        else:
            print(f"Invalid name, the characters must be between {lower}-{upper}")
    return name #a valid name is returned back to the variable that called the function

def force_cellphone_number(message,lower,upper):
    while True: #infinite loop that keeps repeating until a valid number is entered
        cell=str(input(message))
        if len(cell)>=lower and len(cell)<=upper and cell.isnumeric():
            break
        else:
            print(f"ERROR!, please enter between {lower}-{upper}")
    return cell #returning back a valid number within a range

def main_menu():
    print("*********** Dunedin Food Festival  2025. - Forsyth Barr - Dunedin – *************")
    choice = force_number("Please enter your choice: \n 0 to quit the program \n 1 to make a new booking",0,1)
    while True:
        if choice == 0:
            break
        if choice == 1:
            first_name = force_name("Enter your first name: ",2,30)
            last_name = force_name("Enter your last name: ",2,30)
            cell_phone = force_cellphone_number("Enter your cellphone number: ",9,12)
            break
main_menu()