class Vehicle:
    def __init__(self, brand, model, year, mileage, current_status, fuel_type):
        self._brand = brand
        self._model = model
        self._year = year
        self._mileage = mileage
        self._current_status = current_status
        self._fuel_type = fuel_type

    
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

    def set_fuel_type(self, fuel_type):
        self._fuel_type = fuel_type



