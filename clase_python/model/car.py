"""Class for Car model."""


from clase_python.core.abcs.vehicle_abcs import VehicleABC

MAX_DISTANCE_CAN_TRAVEL = 10

AVAILABLE_CAR_BRANDS = ['Nissan', 'Toyota', 'bmw']

class Car(VehicleABC):


    def __init__(self, brand: str, model: int, door_quantity:int) -> None:
        """Constructor for Car class."""

        self.__brand = brand
        self.__model = model
        self.__door_quantity = door_quantity
        self.__distance_traveled = 0

        
    def move(self, additional_distance) -> None:

        if additional_distance <= MAX_DISTANCE_CAN_TRAVEL:
            self.__distance_traveled += additional_distance
        else:
            self.__distance_traveled += MAX_DISTANCE_CAN_TRAVEL

    @property
    def brand(self):
        return self.__brand
    
    @brand.setter
    def brand(self, brand):
        if brand in AVAILABLE_CAR_BRANDS:
            self.__brand = brand
        else:
            print("Ingrese una marca valida.")


    @property
    def distance_traveled(self):
        return self.__distance_traveled
    
    @distance_traveled.setter
    def distance_traveled(self, distance_traveled):
        self.distance_traveled = distance_traveled
       

    """ Otro método  """

    def acelerar(self):
        print(f"El carro {self.__brand}, está acelerando!")

    
    def frenar(self):
         print(f"El carro {self.__brand}, está frenando!")
