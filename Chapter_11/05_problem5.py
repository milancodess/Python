class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result
    
    def __mul__(self, other):
        reesult = self.x * other.x + self.y * other.y + self.z * other.z
        return reesult
    
    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

#test the implementation
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8, 9) # same dimension vector

print(v1 + v2) # Output:Vector(5, 7, 9)
print(v1 * v2) # Output: 32