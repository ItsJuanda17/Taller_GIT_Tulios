import Vehicle

class Main:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, make, model, year):
        """
        Añade un vehículo a la lista de vehículos.
        
        :param make: Marca del vehículo
        :param model: Modelo del vehículo
        :param year: Año del vehículo
        """
        vehicle = Vehicle(make, model, year)
        self.vehicles.append(vehicle)
        print(f"Vehículo añadido: {vehicle}")

    def print_vehicles(self):
        for vehicle in self.vehicles:
            print(f"Brand: {vehicle.brand} Model: {vehicle.model} Year: {vehicle.year} Mileage: {vehicle.mileage} Current Status: {vehicle.current_status} Fuel Type: {vehicle._fuel_type}")