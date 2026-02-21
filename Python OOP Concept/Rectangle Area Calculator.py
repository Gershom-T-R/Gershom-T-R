class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        area = self.length * self.breadth
        print(f"Area of Rectangle: {area}")
        return area

    def update_dimensions(self, new_length, new_breadth):
        if new_length > 0 and new_breadth > 0:
            self.length = new_length
            self.breadth = new_breadth
            print("Dimensions updated successfully.")
        else:
            print("Length and breadth must be positive values.")


# Create an object and test methods
rectangle1 = Rectangle(10, 5)

rectangle1.calculate_area()
rectangle1.update_dimensions(15, 8)
rectangle1.calculate_area()