# Hotel_booking_system program
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
    def __init__(self, name,):
        self.name = name
        


class Booking:
    def __init__(self, guest, room):
        self.guest = guest
        self.room = room

    def make_reservation(self):
        if self.room.book_room():
            print(f"Room {self.room.room_number} booked successfully for {self.guest.name}.")
        else:
            print(f"Room {self.room.room_number} is already booked.")

    def cancel_reservation(self):
        if self.room.release_room():
            print(f"Room {self.room.room_number} reservation cancelled for {self.guest.name}.")
        else:
            print(f"Room {self.room.room_number} is not currently booked.")



print("WELCOME_TO_OUR_HOTEL_BOOKING_SYSTEM .........enjoy your stay with us")

# ROOM BOOKING AREA
if __name__ == "__main__":
    room1 = Room(1, "Single",3)
    room2 = Room(2, "Double", 4)
    room3 = Room(6, "save contain",5)
    room4 = Room(7, "flat", 8)
    room5 = Room(10, "double",9)
    room6 = Room(12, "single",11)
    




    guest1 = Guest( input(" first guest enter your name:"))
    guest2 = Guest (input("second guest enter your name:"))
    guest3 = Guest(input("third guest enter your name:"))
    guest4 = Guest(input("forth guest enter your name:"))
    guest5 = Guest(input("fifth guest enter your name:"))
    guest6 = Guest(input("sixth guest enter your name: "))




    booking1 = Booking(guest1, room1)
    booking1.make_reservation()

    booking2 = Booking(guest2, room1)
    booking2.make_reservation()

    booking3 = Booking(guest3,room3)
    booking3.make_reservation()

    booking4 = Booking(guest4,room4)
    booking4.make_reservation()

    booking5 = Booking(guest5, room5)
    booking5.make_reservation()

    booking6 = Booking(guest6, room6)
    booking6.make_reservation()



    booking1.cancel_reservation()
    booking2.make_reservation()
    booking3.cancel_reservation()
    booking4.cancel_reservation()
    booking5.cancel_reservation()
    booking6.cancel_reservation()