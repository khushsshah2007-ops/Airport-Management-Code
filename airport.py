flights = []
passengers = []
bookings = []

flight_id = 1
passenger_id = 1
booking_id = 1

def input_num():
    while True:
        try:
            a = int(input())
            return a
        except ValueError or TypeError:
            print("Please enter an integer")


def add_flight():
    global flight_id
    print("\n Add Flight ")
    flight_no = input("Flight Number: ")
    origin = input("Origin: ")
    destination = input("Destination: ")
    time = input("Departure Time: ")
    print("Enter the total number of seats below: ")
    seats = input_num()
    runway=12
    while runway>=12:
        print("Enter the runway number between 1 and 12: ", end=' ')
        runway = input_num()
    gate=21
    while gate>=21:
        print("Enter the gate number between 1 and 20: ",end=' ')
        gate = input_num()
    while origin or destination is not "Ahmedabad":
        print("If airplane not arriving or departing from Ahmedabad, please add it elsewhere.")
        return

    for f in flights:
        if f["runway"] == runway and f["time"] == time:
            print("\n The runway is already occupied. \n Please choose another runway number")
            return

    flights.append({"id": flight_id,"flight_no": flight_no,"origin": origin,"destination": destination,"time": time,"total_seats": seats,"booked": 0,"runway": runway,"gate": gate, "status": "Scheduled"})
    print(f"Flight added with ID {flight_id}")
    flight_id += 1


def view_flights():
    print("\n Flight List ")
    if not flights:
        print("No flights found.")
        return
    for f in flights:
        print(f"ID: {f['id']}, Flight: {f['flight_no']}, "f"{f['origin']} to {f['destination']}, Time: {f['time']}, "f"Seats: {f['booked']}/{f['total_seats']},"f"Runway: {f['runway']}, Gate: {f['gate']}, "f"Status: {f['status']}")

def add_passenger():
    global passenger_id
    print("\n Register Passenger ")
    name = input("Name: ")

    passengers.append({"id": passenger_id,"name": name})

    print(f"Passenger registered with ID {passenger_id}")
    passenger_id += 1


def view_passengers():
    print("\n Passenger List ")
    for p in passengers:
        print(f"ID: {p['id']}, Name: {p['name']}")


def book_ticket():
    global booking_id
    print("\n Book Ticket ")
    print("Enter the Passenger ID: ", end=' ')
    pid = input_num()
    print("Enter FLight ID: ", end=' ')
    fid = input_num()

    passenger = next((p for p in passengers if p["id"] == pid), None)
    flight = next((f for f in flights if f["id"] == fid), None)

    if passenger is None:
        print("Passenger not found!")
        return

    if flight is None:
        print("Flight not found!")
        return

    if flight["booked"] >= flight["total_seats"]:
        print("No seats available!")
        return

    seat_no = flight["booked"] + 1
    flight["booked"] += 1

    bookings.append({"id": booking_id,"passenger_id": pid,"flight_id": fid,"seat": seat_no})

    print(f"Booking successful! Booking ID: {booking_id}, Seat No: {seat_no}")
    booking_id += 1


def view_bookings():
    print("\n Booking List ")
    if not bookings:
        print("No bookings.")
        return

    for b in bookings:
        p = next(p for p in passengers if p["id"] == b["passenger_id"])
        f = next(f for f in flights if f["id"] == b["flight_id"])

        print(f"Booking ID: {b['id']}, Passenger: {p['name']}, "f"Flight: {f['flight_no']}, Seat: {b['seat']}")
def update_status():
    print(" Update Flight Status ")
    fid=int(input("Enter Flight ID: "))
    flight=next((f for f in flights if f["id"] == fid), None)
    if flight is None:
        print("Flight not found!")
        return
    else:
        new_status = str(input("Enter the New Status(On-time/Delayed/Cancelled: "))
        flight["status"] = new_status
        print("The flight status has been updated.")
def main():
    while True:
        print("\n===== Airport Management System =====")
        print("1. Add Flight")
        print("2. View Flights")
        print("3. Register Passenger")
        print("4. View Passengers")
        print("5. Book Ticket")
        print("6. View Bookings")
        print("7. Update Flight Status")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_flight()
        elif choice == '2':
            view_flights()
        elif choice == '3':
            add_passenger()
        elif choice == '4':
            view_passengers()
        elif choice == '5':
            book_ticket()
        elif choice == '6':
            view_bookings()
        elif choice == '7':
            update_status()
        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid choice!")


main()