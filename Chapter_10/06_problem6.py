from random import randint

class Train:
    def __init__(slf, trainNo):
         slf.trainNo = trainNo

    def book(milan, frm, to):
        print(f"Ticket is booked in train no.: {milan.trainNo} from {frm} to {to}")

    def getStatus(self):
         print(f"Train no.: {self.trainNo} is running on time.")

    def getFare(self, frm, to):
         print(f"Ticket fare in train no.: {self.trainNo} from {frm} to {to} is {randint(222, 5555)}")

t = Train(12399)
t.book("Kathmandu", "Pokhara")
t.getStatus()
t.getFare("Kathmandu", "Pokhara")
