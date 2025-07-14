class Room:
    def __init__(self, room_number, room_type, price):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.is_booked = False

    def book_room(self):
        if not self.is_booked:
            self.is_booked = True
            return True
        return False

    def release_room(self):
        if self.is_booked:
            self.is_booked = False
            return True
        return False

class Guest:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Booking:
    def __init__(self, guest, room):
        self.guest = guest
        self.room = room

    def make_reservation(self):
        if self.guest.age < 18:
            print(f"Sorry, {self.guest.name}, next time (under 18) are not allowed to book rooms.")
            return
        if self.room.book_room():
            print(f"Room {self.room.room_number} booked for {self.guest.name}.")
        else:
            print(f"Room {self.room.room_number} is already booked.")

    def cancel_reservation(self):
        if self.room.release_room():
            print(f"Reservation for Room {self.room.room_number} cancelled.")
        else:
            print(f"Room {self.room.room_number} is not booked.")

def get_guest_info(guest_number):
    name = input(f"Guest {guest_number}, enter your name: ")
    age = int(input(f"Guest {guest_number}, enter your age: "))
    gender = input(f"Guest {guest_number}, enter your gender: ")
    return Guest(name, age, gender)

# Initialize rooms
rooms = [
    Room(1, "Single", 100),
    Room(2, "Double", 150),
    Room(3, "Suite", 200),
    Room(4, "Flat", 250),
    Room(5, "Double", 150),
    Room(6, "Single", 100)
]

# Create guests
guests = [get_guest_info(i) for i in range(1, 7)]

# Process bookings
bookings = [Booking(guests[i], rooms[i]) for i in range(6)]
for booking in bookings:
    booking.make_reservation()
    
    
    # cancel booking
    
bookingn = [Booking(guests[j],rooms[j]) for j in range (6) ]

for booking in bookingn:
    booking.cancel_reservation()