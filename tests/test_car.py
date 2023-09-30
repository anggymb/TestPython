"""Test for Car Class."""


class TestCar:
    """Test class for Car model."""
    

    def test_move_distance_traveled_modified(self, car):
        
        car.move(9)

        assert car.distance_traveled == 9

        car.move(4)

        assert car.distance_traveled == 13

    # Dos pruebas adicionales

    def test_move_distance_traveled_modified_dos(self, car):
        
        car.move(7)

        assert car.distance_traveled == 7

        car.move(3)

        assert car.distance_traveled == 10

    def test_move_distance_traveled_modified_tres(self, car):
        
        car.move(5)

        assert car.distance_traveled == 5

        car.move(6)

        assert car.distance_traveled == 11


    """Otro método"""

    def test_acelerar(self, car):
        car.acelerar()

    def test_frenar(self, car):
        car.frenar()
    
    
   