class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_coordinates(self):
        return self.x, self.y

point1 = Point(9, 10)
print(point1.get_coordinates())  

point1.x = 5 
point1.y = 15
print(point1.get_coordinates())