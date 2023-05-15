import unittest
from classes_new import GreenHouse, Section, Plant

# Testing of the requirement: The greenhouse must be able to regulate the temperature of its environment

class test_green_house(unittest.TestCase):

    def test_temperature_monitoring(self):
        greenhouse = GreenHouse()
        greenhouse.pref_temperature = 25

        # Simulate a scenario where the temperature is higher than the preferred temperature
        greenhouse.temperature = 30
        greenhouse.venting = False
        greenhouse._monitor_temperature()

        # Check if the ventilation system is turned on
        self.assertTrue(greenhouse.venting, True)

        # Simulate a scenario where the temperature is lower than the preferred temperature
        greenhouse.temperature = 20
        greenhouse.venting = True
        greenhouse._monitor_temperature()

        # Check if the ventilation system is turned off
        self.assertFalse(greenhouse.venting, False)

if __name__ == '__main__':
    unittest.main()