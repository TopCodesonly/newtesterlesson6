class Vehicle:
    def __init__(self,color,doors):
        self.color=color
        self.doors=doors
    def get_details(self):
        return f"the color is {self.color} and door are {self.doors}."

class Bike(Vehicle):
    def __init__(self,color,doors,mileage,company):
        super().__init__(color,doors)
        self.mileage=mileage
        self.company=company
        self.color=color



b=Bike("red",0,45,"mersadez")
print(b.get_details())