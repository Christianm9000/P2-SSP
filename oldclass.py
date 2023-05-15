import time, threading


class GreenHouse:
    def __init__(self, current_time) -> None:
        #-----# Initialize Variables #-----#
        self.presets: dict[str, {str, int | float}] = {
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
        self.sections = []
        self.time = current_time

        #Current Stats
        self.water_level: float = 100.0 # How much water is left in liters
        self.carbon_level: float | int = 400
        self.temperature: float = 23.0
        self.humidity: float = None # Bro idk

        #Prefered Stats
        self.pref_temperature = 23.0
        self.pref_carbon_level= 400
        self.pref_humidity = None

        #GreenHouse States
        self.venting = False

        #-----# Initialize Starter Objects #-----#
        self.upper = Section('upper', current_time)
        self.middle = Section('middle', current_time)
        self.lower = Section('lower', current_time)
        self.sections = [self.upper, self.middle, self.lower]

        main_thread = threading.Thread(name='handler', target=self.main, args=())
        main_thread.start()


    def monitor_water_level(self):
        #-----# Measure the Water Level #-----#
        while True:
            if self.water_level <= 30 and self.water_level > 10:
                print("Water Tank Running Low - Please Refill")
            
            if self.water_level <= 10:
                print("Water Tank Level Critical - Refill Required")

            time.sleep(0.5)

    def monitor_carbon_level(self):
        #-----# Read Carbon Level From Sensor #-----#
        pass

    def monitor_temperature(self):
        #-----# Monitor the Temperature #-----#
            #Get the Temperature
            print(f"Current Temperature: {self.temperature}")

            if self.temperature < self.pref_temperature:
                print("Temperature Lower Than Prefered Temperature")
                if self.venting:
                    print("Stopping Ventilation")
                    self.venting = False

            if self.temperature > self.pref_temperature:
                print("Temperature is Higher Than Prefered Temperature")
                if not self.venting:
                    self.venting = True
                    print("Starting Ventilation")
            
         
    def monitor_humidity(self):
        pass

    def main(self):
        #-----# Handles the GreenHouse Object #-----#
        water_thread = threading.Thread(name='water', target=self.monitor_water_level, args=())
        water_thread.start()

        temp_thread = threading.Thread(name='temp', target=self.monitor_temperature, args=())
        temp_thread.start()

        while True:
            if self.time == 0:
                for section in self.sections:
                    section.lighting()

class Section:
    def __init__(self, name, current_time):
        #Initialize Variables
        self.name = name
        self.time = current_time
        self.plants: list[Plant] = [] #List of Plant Objects
        self.lamps = False #Are the Lamps turned on or off

    def lighting(self):
        if len(self.plants) == 0:
            return

        lighting_time = self.plants[0].light_consumption
        while self.time <= lighting_time:
            self.lamps = True
        self.lamps = False

    def add_plant(self, plant):
        self.plants.append(plant)
    
    def remove_plant(self, index_number: int):
        del self.plants[index_number]
        

class Plant:
    def __init__(self, name: str, growth_time, water_consumption, light_consumption, carbon_level, temperature):
        #-----# Initiate Variables #-----#
        self.name = name
        self.growth_time = growth_time # Days - Total Time Needed in Hours For the plant to fully grow
        self.water_consumption = water_consumption # L/Hour - Amount of Water needed Per Day
        self.light_consumption = light_consumption # Hours - The amount of light (defined in hours) the plant needs per day
        self.carbon_level = carbon_level # PPM (Parts per million) - The optimal carbon level for the plant
        self.temperature = temperature # Celsius - The Optimal Temperature for the Plant

