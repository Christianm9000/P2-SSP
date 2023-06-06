'''A simulation of the greenhouse environment.'''
# Python 
import time

# Own class
from classes_new import GreenHouse, Plant


def __main() -> None:

    # The hour of the day. 24 Hour Clock. 1 sec = 1 hour.
    current_hour = 0

    # The greenouse object
    greenhouse = GreenHouse()

    # Add a plant to the lower section in the greenhouse.
    greenhouse.lower.add_plant(
        Plant(
            name = 'Cucumber', 
            growth_time = 60, # The time it takes a plant to fully grow.
            water_consumption = 8, # Litres of water consumption per day.
            light_consumption = 15, # The amout of hours of light per day.
            carbon_level = 400, # The carbon PPM needed for it to grow.
            temperature = 23 # The optimale temperature.
        )
    )

    # Now start the simulation.
    while True:
        print(current_hour)
        greenhouse.time = current_hour # Pass the time into the greenhouse control system
        control_temp(greenhouse) # Simulate the temperature in the greenhouse
        current_hour += 1 # Increment the time.
        time.sleep(1) 

        # Rest the timer when hitting 24
        current_hour = current_hour % 24


def control_temp(greenhouse: GreenHouse) -> None:
    """Simulate the temperature in the greenhouse.

    Arguments:
        greenhouse (GreenHouse): The green house to simulate.
    """

    # If ventilation is on.
    if greenhouse.venting:

        # Cool the green house down.
        greenhouse.temperature -= 1
    
    # Check if for every section in the green house.
    for section in greenhouse.sections:

        # If the heating/UV lamps are on.
        if section.lamps:

            # Then the temperatur is increasing 
            greenhouse.temperature += 1


if __name__ == '__main__':
 __main()