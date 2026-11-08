class Vector:
    def __init__(self, x,y):
        self.x=x
        self.y=y

    # Addition
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # Subtraction
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    # Comparison
    def __lt__(self, other):
        length1= self.x**2 + self.y**2
        length2= other.x**2 + other.y**2
        return length1 < length2

    # Equal comparison
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Display
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1=Vector(2,3)
v2=Vector(4,1)

print("Vector 1:", v1)
print("Vector 2:", v2)

print("Addition: ", v1 + v2)
print("Subtraction: ", v1 - v2)

print("Is v1 < v2? ", v1 < v2)
print("Is v1 == v2? ", v1 == v2)

vectors=[
v1, v2, Vector(1,1), Vector(3,4)
]

print("\nSorted Vectors: ")
for v in sorted(vectors):
    print(v)