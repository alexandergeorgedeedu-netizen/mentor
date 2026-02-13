# Online Ticket Booking System

available_seats = 50

print("Welcome to Ticket Booking System")
print("Total Seats Available:", available_seats)

while available_seats > 0:
    try:
        tickets = int(input("\nEnter number of tickets to book (0 to exit): "))

        if tickets == 0:
            print("Booking cancelled.")
            break

        if tickets <= 0:
            raise Exception("Ticket count must be greater than zero.")

        if tickets > available_seats:
            raise Exception("Not enough seats available.")

        available_seats -= tickets

        print(f"Booking successful! Seats left: {available_seats}")

        if available_seats == 0:
            print("All seats are booked. Housefull!")

    except ValueError:
        print("Invalid input! Enter a number.")
    except Exception as e:
        print("Error:", e)