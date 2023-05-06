class Car:
    make="Benz"
    def __init__(self,model,speed,mileage,speed,color):
        self.model= model
        self.speed= speed
        self.mileage= mileage
        self.speed= speed
        self.color= color

    def accelerate(self):
        return f"The acceleration of {self.model} is {self.speed}"  

    def type_engine(self):
        return f"The engine of {self.make} is single model"

    def hired_car(self):
        return f"Rose hired {self.make} {self.model} colour {self.color}"    
