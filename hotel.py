# users = [['arun',933837333,'a','b']]
# rooms = [True] * 10
# bookings = []
# while True:
#     print("\n1.Registration \n2.Login\n")
#     c=int(input("enter the choice : "))
#     if c==1:
#         name=input("\nenter your name : ")
#         number=int(input("enter your number : "))
#         email=input("enter your email : ")
#         password=input("enter your password : ")
#         users.append([name,number,email,password])
#     elif c==2:
#         a=input("\nenter your email :")
#         b=input("enter your password :")
#         f=0
#         for i in users:
#             if a==i[2] and b==i[3]:
#                 f=2
#                 print("\nlogin successful..\n")
#                 while True:
#                     print("1.Book a room\n2.Check available rooms\n3.Cancel a booking\n4.Logout\n")
#                     ch=int(input("enter the choice :"))
#                     if ch==1:
#                          room_id = int(input("Enter the room number to book (1-10): "))
#                          if 1<= room_id <= 10 and rooms[room_id-1]:
#                             rooms[room_id-1] = False
#                             bookings.append([a,room_id])
#                             print("Room No. -",room_id,"booked successfully.\n")
#                          else:
#                             print("Room is not available or already booked by someone.")
#                     elif ch==2:
#                           print("Available rooms:")
#                           for i in range(len(rooms)):
#                             if rooms[i]:
#                                 print("Room",i+1," is available")
#                           print()
#                     elif ch==3:
#                         room_id = int(input("Enter the room number to cancel the booking (1-10): "))
#                         if 1 <= room_id <= 10:
#                             for i in bookings:
#                                 if i[0] == a and i[1] == room_id:
#                                     rooms[room_id - 1] = True
#                                     bookings.remove(i)
#                                     print("Room No. -", room_id, "booking cancelled successfully.\n")
#                     elif ch==4:
#                         print("logged out")
#                         break
#         if f==0:
#             print("\nInvalid email or password.\n")

i=0
def asd(i):
    if (i<=10):
        print(i)
        i+=1
        asd(i)


asd(i)