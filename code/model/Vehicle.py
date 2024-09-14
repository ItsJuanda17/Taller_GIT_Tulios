class Vehicle:
    TYPES_OF_FUEL = ["Gasoline", "Diesel", "Electric"]

    def __init__(self, brand, model, year, mileage, current_status, fuel_type, power=None, color=None):
        self._brand = brand
        self._model = model
        self._year = year
        self._mileage = mileage
        self._current_status = current_status
        self.set_fuel_type(fuel_type)  
        self.set_power(power) 
        self._color = color

    def get_power(self):
        return self._power

    def get_brand(self):
        return self._brand

    def get_model(self):
        return self._model

    def get_year(self):
        return self._year

    def get_mileage(self):
        return self._mileage

    def get_current_status(self):
        return self._current_status

    def get_fuel_type(self):
        return self._fuel_type

    def get_color(self):
        return self._color

    def set_brand(self, brand):
        self._brand = brand

    def set_model(self, model):
        self._model = model

    def set_year(self, year):
        self._year = year

    def set_mileage(self, mileage):
        self._mileage = mileage

    def set_current_status(self, current_status):
        self._current_status = current_status

    def set_power(self, power):
        if power is not None and power < 0:
            raise ValueError("Power cannot be a negative number.")
        self._power = power

    def set_fuel_type(self, fuel_type):
        if fuel_type not in Vehicle.TYPES_OF_FUEL:
            raise ValueError(f"Invalid fuel type: {fuel_type}. Must be one of {Vehicle.TYPES_OF_FUEL}")
        self._fuel_type = fuel_type

    def set_color(self, color):
        self._color = color
