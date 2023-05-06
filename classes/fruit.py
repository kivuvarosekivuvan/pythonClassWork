class Fruit:
    def __init__(self,name,color,taste,price):
        self.name = name
        self.color = color
        self.taste = taste

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color

    def get_taste(self):
        return self.taste

    def set_name(self):
        self.name = name                

    def set_color(self):
        self.color = color 

    def set_taste(self):
        self.taste = taste         #apple.set_color("green")

    def describe(self):
        print(f"This is a {self.color} {self.name} that tastes {self.taste}.")
        