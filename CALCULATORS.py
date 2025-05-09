def main():
    while True:
        print ("Hello i will calculate the radius and lenght of the following shapes, ")
        choice = input("Hello! 1.Circle 2.Rectangle 3.Triangle 4.Exit Choice: ")
        if choice == "1": shape = Circle(int(input(r"Radius: ")))
        elif choice == "2": shape = Rectangle(int(input(r"Length: ")), int(input(r"Width: ")))
        elif choice == "3": shape = Triangle(int(input(r"Side 1: ")), int(input(r"Side 2: ")), int(input(r"Side 3: ")))
        elif choice == "4": 
            print("ok then goodbye")
            break
        else: 
            print(r"Invalid choice.")
            continue
        print(f"Area: {shape.area()}, Perimeter: {shape.perimeter()}")

class Shape:
    def area(self): pass
    def perimeter(self): pass

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return 3.14 * self.r ** 2
    def perimeter(self): return 2 * 3.14 * self.r

class Rectangle(Shape):
    def __init__(self, l, w): self.l, self.w = l, w
    def area(self): return self.l * self.w
    def perimeter(self): return 2 * (self.l + self.w)

class Triangle(Shape):
    def __init__(self, a, b, c): self.a, self.b, self.c = a, b, c
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
    def perimeter(self): return self.a + self.b + self.c

main()