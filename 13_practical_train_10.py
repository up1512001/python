
class train:
    # l = []
    def __init__(self,name,fare,seats):
        self.name = name
        self.fare = fare
        self.seats = seats
        i=1
        self.l = []
        while i<=self.seats:
            self.l.append(i)
            i=i+1

    def getinfo(self):
        print(f'name of train {self.name} fare of train is {self.fare} and avalable seats are {self.seats}')


    def fareinfo(self):
        print(f'ticket amount is {self.fare}')

    def bookticket(self,l):
        if self.seats > 0:
            print(f'your ticket is booked at seat No {self.seats}')
            l.pop()
            self.seats=self.seats-1
            
        else:
            print('train is full')
            
    
    def cancelticket(self,l):
        x = int(input("Enter seat no "))
        if x in self.l:
            print('NOT BOOKED...')
            print('not able to cancel this ticket')
        else:
            l.append(x)
            print(f'your ticket cancel sussefully...')
            


intercity = train('Express',90,300)
intercity.getinfo()
intercity.fareinfo()
intercity.bookticket(intercity.l)
intercity.bookticket(intercity.l)
intercity.getinfo()
print(intercity.l)
intercity.cancelticket(intercity.l)
print(intercity.l)