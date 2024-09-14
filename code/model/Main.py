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
            
    def search_by_year(self, year):
        """
        Busca vehículos por año.
        
        :param year: Año para buscar vehículos
        :return: Lista de vehículos que coinciden con el año dado
        """
        results = [vehicle for vehicle in self.vehicles if vehicle.year == year]
        return results
    
    def search_by_year_range(self, start_year, end_year):
        """
        Busque vehículos dentro de un rango de años.

        :param start_year: Inicio del rango de años
        :param end_year: Fin del rango de años
        :return: Lista de vehículos dentro del rango de años indicado
        """
        results = [vehicle for vehicle in self.vehicles if start_year <= vehicle.get_year() <= end_year]
        return results
