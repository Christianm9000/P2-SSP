import unittest
from classes_new import GreenHouse, Section, Plant

class test_green_house(unittest.TestCase):

    def test_temperature_monitoring(self):
        # Initialize Greenhouse Object
        greenhouse = GreenHouse()
        greenhouse.pref_temperature = 23

        # Test when the temperature is lower than the preferred temperature
        greenhouse.temperature = 20
        greenhouse._monitor_temperature()
        self.assertFalse(greenhouse.venting, "Ventilation should be off when the temperature is lower than preferred.\n")

        # Test when the temperature is higher than the preferred temperature
        greenhouse.temperature = 26
        greenhouse._monitor_temperature()
        self.assertTrue(greenhouse.venting, "Ventilation should be on when the temperature is higher than preferred.\n")

        # Test when the temperature is equal to the preferred temperature
        greenhouse.temperature = 23
        greenhouse._monitor_temperature()
        self.assertFalse(greenhouse.venting, "Ventilation should be off when the temperature is equal to the preferred.")

if __name__ == '__main__':
    unittest.main()