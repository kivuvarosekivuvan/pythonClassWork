class Car:
    make="Benz"
    def __init__(self,model,speed,mileage,color,acceleration):
        self.model= model
        self.speed= speed
        self.mileage= mileage
        self.speed= speed
        self.color= color
        self.acceleration= 0

    def accelerate(self):
        self.speed+=acceleration
        return acceleration
  

    def type_engine(self):
        return f"The engine of {self.make} is single model"

    def hired_car(self):
        return f"Rose hired {self.make} {self.model} colour {self.color}"    
