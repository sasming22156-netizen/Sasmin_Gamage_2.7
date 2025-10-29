import datetime #generates a timestamp
import random #that generates a random number

BOOKING_FEE=30 #flat booking fee for all tickets

def force_number(message,lower,upper): #The purpose of this function is to enter in a valid number within
    """
    Ensures the user enters an integer within a specific range [lower,upper]. 
    Repeats until a valid number is entered
    """
    while True: #infinite loop that keeps repeating until a valid number is entered
        try:
            num=int(input(message)) #asks user for input and try to convert the input into an interger
            if lower <= num <= upper: #check if number is in range
                break
            else:
                print(f"Invalid number, please enter between {lower}-{upper}")
        except ValueError: #this will only print if you type in a string
            print("Error, please enter in a number not text")
    return num #returning back a valid number within a range

def force_name(message,lower,upper):
    """
    Ensures the user enters a valid name, with only letters allowed. 
    Length must be between lower and upper and this function.
    The function also captalizses the first letter of each word. 
    """
    while True: #this is an infinite loop that will only break if a valid name is entered
        name=str(input(message)).title()
        if len(name)>=lower and len(name)<=upper and name.isalpha():
            print("The name is valid")
            break #the loop breaks if the above conditions is met
        else:
            print(f"Invalid name, the characters must be between {lower}-{upper}")
    return name #a valid name is returned back to the variable that called the function

def force_cellphone_number(message,lower,upper):
    """
    Ensures the user enters a valid cellphone number. 
    Only digits are allowed which are within the length of lower and upper.
    """
    while True: #infinite loop that keeps repeating until a valid number is entered
        cell=str(input(message)) #ask for phone number
        if len(cell)>=lower and len(cell)<=upper and cell.isnumeric(): #validate length and digits
            break
        else:
            print(f"ERROR!, please enter between {lower}-{upper}") #error message
    return cell #returning back a valid number within a range

def get_user_choice(message):
    """
    Unified menu and confirmation function.
    1 = Create / confirm new booking.
    2 = Quit / cancel booking.
    """
    return force_number(message,0,1) == 1

def generate_reference(first_name,last_name,ticket_type):
    """
    Generates a unique booking reference.
    This contains the last name plus first two letters of first name and random 6 digit code and daycode in uppercase.
    """
    day = "FRI" if "Friday" in ticket_type else "SAT" #determines the day code
    return(last_name.upper()+first_name[0:2].upper()+str(random.randint(100000,999999))+day) #combines references to build a single booking code

def format_booking(name,cell_phone,ticket_type,quantity,total):
    """
    Returns a formated string showing the booking details of the customer name, phone, ticket type, quantity, and total cost (to 2sf).
    """
    return (f"Name: {name}\n"
           f"Phone: {cell_phone}\n"
           f"Tickets: {ticket_type} x{quantity}\n"
           f"Total Cost: ${total:.2f}\n" #formatted to 2dp
           "---------------------------------------------------\n")

def main_menu(): #defining my function
    """
    Main menu function for the booking sequence. 
    This function displays the tickets and prices collects users information, confirms the bookings and writes it to a textfile.
    """
    print("*********** Dunedin Food Festival  2025. - Forsyth Barr - Dunedin – *************")
    ticket_options=["Friday Student",
            "Friday General Admission",
            "Friday Feldspar VIP Admission",
            "Saturday Student",
            "Saturday HTQ 18+",
            "Saturday Feldspar VIP Exprience"] #avaliable ticket options
    ticket_prices=[65,70,220,65,125,200] #prices corresponding to ticket
    total_price=0
    confirmed_bookings=[] #list to store confirmed booking, setting my list to zero
    while get_user_choice("\n 0 to quit the program, 1 to make a new booking: "): #main booking loop
        print("Avaliable Tickets: ")
        for i in range(len(ticket_options)): #going through the ticket options
            print(f"{i+1}. {ticket_options[i]} - ${ticket_prices[i]}") #displays ticket information through calculations
        ticket_section = force_number("What ticket number do you want? ",1,6)
        quantity_ticket = force_number("How many tickets do you want? ",1,10)
        first_name = force_name("Enter your first name: ",2,30) #get first name
        last_name = force_name("Enter your last name: ",2,30) #get last name
        name=first_name+" "+last_name #getting full name by combining the strings together
        cell_phone = force_cellphone_number("Enter your cellphone number: ",8,13) #gets the cellphone number
        ticket_type = ticket_options[ticket_section-1] #calculating the selected ticket type
        price = ticket_prices[ticket_section-1] #calculating the selected ticket price
        total_price += price * quantity_ticket + BOOKING_FEE #calculating total cost
        print("\nBooking Summary")
        print("-----------------------------")
        print(format_booking(name,cell_phone,ticket_type,quantity_ticket,total_price)) #show booking summary
        while get_user_choice("Confirm booking? (1=Yes, 0=No): "): #confirmation loop
            reference = generate_reference(first_name,last_name,ticket_type) #generate booking reference
            date_time=datetime.datetime.now() #gets the timestamp       
            outF=open("booking.txt", "a") #opens the bookings text file
            outF.write(f"Booking Reference Code: {reference}\n")
            outF.write(f"Date and Time of Booking: {date_time}\n")
            outF.write(format_booking(name,cell_phone,ticket_type,quantity_ticket,total_price))
            outF.close() #closes the bookings text file
            print("****Please remember to bring photo ID to the Forsyth Barr to pay for and collect your tickets***")
            break #exit confirmation loop
        else:   
            print("Booking Cancelled.") #cancel message
main_menu() #calling out my main function, starts the program