#lab Classes BONUS

class Vehicle:

    def __init__(self , brand:str, name:str, color:str, capacity: int, plate_number:int) -> None:
        
        self.__brand = brand
        self.__name = name
        self.__color = color
        self.__capacity = capacity
        self.__plate_number = plate_number

    
    def drive(self):
        print(f" the {self.__name} is driving!")
    
    def drift(self):
        print(f" the {self.__name} is drifting !!")
    
    def carry_cargo(self):
        print(f" the {self.__name} is carrying cargo !!")
    
    def plate(self):
        print(f"the plate number is: {self.__plate_number}")
    


    #setter & getter

    def set_brand(self, brand):
        self._brand = brand

    def get_brand(self):
        return self._brand

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color
    
    def set_capacity(self, capacity):
        self._capacity = capacity

    def get_capacity(self):
        return self._capacity

    def set_plate_number(self, plate_number):
        self._plate_number = plate_number

    def get_plate_number(self):
        return self._plate_number
    


    #subClasses

class Bus(Vehicle):
    def __init__(self, brand, name, color, capacity, plate_number):
        super().__init__(brand, name, color, capacity, plate_number)


    def drift(self):
        print("The bus doesn't drifts.")


    def carry_cargo(self):
        print("The bus is carrying people.")

    

class Truck(Vehicle):
    def __init__(self, brand, name, color, capacity, plate_number):
        super().__init__(brand, name, color, capacity, plate_number)

    def carry_cargo(self):
        print("The truck is carrying cargo.")




car = Vehicle("hyundai", "elantra", "gray", 5, "س ه ى 2000")
bus = Bus("Volvo", "DFL6140", "white", 40 , "376ABC")
truck = Truck("Ford", "F150", "black", 7, "789GHI")


car.drive()
car.drift()
car.carry_cargo()
car.plate()

bus.drive()
bus.drift()
bus.carry_cargo()

truck.drive()
truck.drift()
truck.carry_cargo()