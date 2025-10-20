import datetime
import random

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

def main_menu(): #defining my function
    ticket_options=["Friday Student",
            "Friday General Admission",
            "Friday Feldspar VIP Admission",
            "Saturday Student",
            "Saturday HTQ 18+",
            "Saturday Feldspar VIP Exprience"]
    ticket_prices=[65,70,220,65,125,220]
    print("*********** Dunedin Food Festival  2025. - Forsyth Barr - Dunedin – *************")
    confirmed_bookings=[] #setting my list to zero
    total_price = 0 #setting my price to zero
    while True: #infinite loop with forced input
        choice = force_number("Please enter your choice: \n 0 to quit the program \n 1 to make a new booking",0,1)
        if choice == 0:
            break #breaking out of the loop
        if choice == 1:
            print("Avaliable Tickets: ")
            for i in range(len(ticket_options)): #going through the ticket options
                print(f"{i+1}. {ticket_options[i]} - ${ticket_prices[i]}")
            ticket_section = force_number("What ticket number do you want? ",1,6)
            quantity_ticket = force_number("How many tickets do you want? ",1,10)
            first_name = force_name("Enter your first name: ",2,30)
            last_name = force_name("Enter your last name: ",2,30)
            cell_phone = force_cellphone_number("Enter your cellphone number: ",8,13)
            total_price += 30
            confirm_booking = str(input("Do you wish to confirm this booking? (Y/N): "))
            if confirm_booking.lower() == "N":
                print("Okay...")
            if confirm_booking.lower() == "Y":
                confirmed_bookings.append(ticket_options)
                first_name_slice=first_name[0:2]
                random_number=random.randint(100000,999999)
                unique_code=last_name+first_name_slice+str(random_number)
                name=first_name+str(" ")+last_name
                date_time=datetime.datetime.now()
                outF=open("bookings.txt")
                outF.write(f"Customer Full Name: {name}")
                outF.write(f"Customer Cellphone Number: {cell_phone}")
                outF.write(f"Date and Time of Booking: {date_time}")
                print("****Please remember to bring photo ID to the Forsyth Barr to pay for and collect your tickets***")
            break
main_menu() #calling out my functions