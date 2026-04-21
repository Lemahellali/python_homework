class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def distance(self, other):
        return ((other.x - self.x) ** 2 + (other.y - self.y) ** 2) ** 0.5


class Vector(Point):
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

p1 = Point(2, 3)
p2 = Point(2, 3)
p3 = Point(5, 7)

print(p1)                
print(p2)                 
print(p3)                 
print(p1 == p2)          
print(p1 == p3)           
print(p1.distance(p3))    

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2

print(v1)                
print(v2)                 
print(v3)                 
print(v1.distance(v2))    

