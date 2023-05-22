'''The main file that contains the `GreenHouse`, `Section` and `Plant`.'''


import threading

class GreenHouse:
    """A class of a greenhouse"""
    def __init__(self):
        # The presets of type of plants.
        self.presets: dict = {
            'Cucumber': {
                'name': 'Cucumber',
                'growth_time': 60, 
                'water_consumption': 2.5, 
                'light_consumption': 15, 
                'carbon_level': 400, 
                'temperature': 23 
            },
            'Tomato': {
                'name': 'Tomato',
                'growth_time': 56, 
                'water_consumption': 4, 
                'light_consumption': 15, 
                'carbon_level': 400, 
                'temperature': 23
            }
        }

        # A List of sections.
        self.sections: list[Section] = []

        #Current Stats
        self.water_level: float = 100.0 # How much water is left in liters.
        self.carbon_level: float | int = 400 # The co2 level in the green house.
        self.temperature: float = 23.0 # In celsius.
        self.time: int = 0 # The current time of the day

        #Prefered Stats
        self.pref_temperature: float = 23.0
        self.pref_carbon_level: float = 400

        # Is the venting system active?
        self.venting = False

        # Initialize the sections.
        self.upper = Section('upper')
        self.middle = Section('middle')
        self.lower = Section('lower')

        # Append them to the list of sections.
        self.sections = [self.upper, self.middle, self.lower]

        # Start the green house.
        #main_thread = threading.Thread(name='handler', target=self.__main, args=())
        #main_thread.start()

    def _monitor_temperature(self) -> None:
        """Monitor the temperature.
        
        Note:
            You should not normally not call this method.
        """

        print(f"Current Temperature: {self.temperature}")

        # If it is too cold or preffered.
        if self.temperature <= self.pref_temperature:
            print("Temperature Lower Than Preferred Temperature")

            # Are the ventilation system active?
            if self.venting:

                # Then stop it.
                print("Stopping Ventilation")
                self.venting = False

        # If it is to warm.
        if self.temperature > self.pref_temperature:
            print("Temperature is Higher Than Preferred Temperature")

            # If the centilation system is not active.
            if not self.venting:

                # Then start it.
                print("Starting Ventilation")
                self.venting = True

    def __main(self) -> None:
        """The main init method for this class.
        
        Note:
            You should never call this method.
        """
        #
        past_time = None

        while self.time != past_time:
            #-----# Run Monitors For The Hour #-----#
            self._monitor_temperature()

            #-----# Check Time For Lighting #-----#
            if self.time == 0:
                for section in self.sections:
                    light_thread = threading.Thread(target=section.lighting)
                    light_thread.start()

            #-----# Update Time In Sections #-----#
            for section in self.sections:
                section.time = self.time
            
            past_time = self.time


class Section:
    """A section in a green house."""
    def __init__(self, name: str) -> None:
        
        self.name: str = name
        self.time: int = 0
        self.plants: list[Plant] = [] 
        self.lamps = False # Lamps On or Off

    def lighting(self):
        # Check if there is any plants.
        if len(self.plants) > 0:

            # Take the first plant in the section for messuring.
            # NOTE: Every plant in a section is the same.
            light_time = self.plants[0].light_consumption

            print("Lighting On")
            self.lamps = True

            
            while True:
                # If the plant does not need more light.
                if self.time == light_time:
                    print("Lighting Off")
                    self.lamps = False
                    break

        # NOTE: This can be removed.
        return # Kill the thread

    def add_plant(self, plant: object) -> None:
        """Add a plant to the section.
        
        Arguments:
            plant (Plant): The plant object to add.
        """
        self.plants.append(plant)

    def remove_plant(self, index_number: int) -> None:
        """Remove a plant from the section.
        
        Arguments:
            index_number (int): The index of the plant to remove.
        """
        del self.plants[index_number]


class Plant:
    """A plant class"""
    def __init__(
            self, 
            name: str, 
            growth_time: int, 
            water_consumption: float, 
            light_consumption: int, 
            carbon_level: int, 
            temperature: int
    ) -> None:
        """The init

        Arguments:
            name (str): The name or type of plant.
            growth_time (int): How many hours it takes for a plant to grow.
            water_consumption (float): How much water the plant co
        
        """

        #-----# Initiate Variables #-----#
        self.name = name
        self.growth_time = growth_time # Days - Total Time Needed in Hours For the plant to fully grow
        self.water_consumption = water_consumption # L/Hour - Amount of Water needed Per Day
        self.light_consumption = light_consumption # Hours - The amount of light (defined in hours) the plant needs per day
        self.carbon_level = carbon_level # PPM (Parts per million) - The optimal carbon level for the plant
        self.temperature = temperature # Celsius - The Optimal Temperature for the Plant