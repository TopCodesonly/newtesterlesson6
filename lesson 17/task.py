class circle:
    def __init__(self,radius):
        self.radius=radius
        
    def total(self,other):
        return self.radius+other.radius
    
    def __add__(self,other):
        return self.radius + other.radius
    
    def __gt__(self,other):
        return self.radius > other.radius
    

c1=circle(10)
c2 =circle(20)
print(c1.radius+c2.radius)
print(c1.total(c2))
print(c1+c2)
print(c1>c2)

