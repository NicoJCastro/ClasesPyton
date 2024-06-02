class Flight:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
        
    def add_passanger(self, name):
        if not self.open_seat():
            return False
        self.passengers.append(name)
        return True
    
    def open_seat(self):
        return self.capacity - len(self.passengers)
    
flight = Flight(3)
people = ["Nico", "Ani", "Rita", "Nina", "Perla"]

for person in people:
    if  flight.add_passanger(person):    
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}.")