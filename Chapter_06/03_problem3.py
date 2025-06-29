p1 = "Make a lot of money"
p2 = "Buy now"
p3 = "Subbscribe this"
p4 = "Click this"

message =  input("Enter your comment: ")

if ( p1 in message or p2 in message or p3 in message or p4 in message):
    print("This is a spam comment")

else:
    print("This is not a spam comment")