class Car:
    car_count = 0
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
        Car.car_count += 1
    def display_name(self):
        return f"{self.__brand} {self.model}"
    def get_brand(self):
        return self.__brand + "!!"
    def fuel_type(self):
        return "diesel"

c1 = Car("Mahindra" , "Thar")
c2 = Car("SUV" , "Sumo")
# print(c1.__brand , c1.model)
# print(c1.get_brand())

# print(c2.display_name())
# print(c1.display_name())

class Electric_Car(Car):

    def __init__(self,brand,model, battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Charging"

my_electric_car = Electric_Car("Tesla","X" , "78kWh")
# print(my_electric_car.display_name() ,my_electric_car.battery_size)

print(c1.fuel_type())
print(my_electric_car.fuel_type())
print(Car.car_count)







































































