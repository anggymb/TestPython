"""Class for Airplane model."""

MAX_DISTANCE_CAN_TRAVEL = 5

class Airplane():

    def __init__(self, brand: str, engines_quanity: int, door_quantity:int) -> None:
        """Constructor for Airplane class."""

        self.__brand = brand
        self.__engines_quanity = engines_quanity
        self.__door_quantity = door_quantity
        self.__distance_traveled = 0

        
    def move(self, additional_distance) -> None:

        if additional_distance <= MAX_DISTANCE_CAN_TRAVEL:
            self.__distance_traveled += additional_distance
        else:
            self.__distance_traveled += MAX_DISTANCE_CAN_TRAVEL
