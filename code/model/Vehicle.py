class Vehicle:
    TYPES_OF_FUEL = ["Gasoline", "Diesel", "Electric"]

def validate_fuel(self):
    if self._fuel_type not in Vehicle.TYPES_OF_FUEL:
        raise ValueError(f"Invalid fuel type: {self._fuel_type}. Must be one of {Vehicle.TYPES_OF_FUEL}")
    
def set_fuel_type(self, fuel_type):
    if fuel_type not in Vehicle.TYPES_OF_FUEL:
        raise ValueError(f"Invalid fuel type: {fuel_type}. Must be one of {Vehicle.TYPES_OF_FUEL}")
    self._fuel_type = fuel_type
