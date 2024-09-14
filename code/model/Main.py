from Vehicle import Vehicle

class Main:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self):
        make = input("Ingrese la marca del vehículo: ")
        model = input("Ingrese el modelo del vehículo: ")
        year = int(input("Ingrese el año del vehículo: "))
        mileage = int(input("Ingrese el kilometraje del vehículo: "))
        current_status = input("Ingrese el estado actual del vehículo: ")
        fuel_type = input("Ingrese el tipo de combustible del vehículo: ")
        power = input("Ingrese la potencia del vehículo (opcional): ")
        color = input("Ingrese el color del vehículo (opcional): ")

        if power:
            power = int(power)
        else:
            power = None

        if color:
            color = color
        else:
            color = None

        vehicle = Vehicle(make, model, year, mileage, current_status, fuel_type, power, color)
        self.vehicles.append(vehicle)
        print(f"Vehículo añadido: {vehicle.get_brand()} {vehicle.get_model()}")

    def print_vehicles(self):
        for vehicle in self.vehicles:
            print(f"Marca: {vehicle.get_brand()} Modelo: {vehicle.get_model()} Año: {vehicle.get_year()} Kilometraje: {vehicle.get_mileage()} Estado actual: {vehicle.get_current_status()} Tipo de combustible: {vehicle.get_fuel_type()}" + (f" Potencia: {vehicle.get_power()}" if vehicle.get_power() is not None else "") + (f" Color: {vehicle.get_color()}" if vehicle.get_color() is not None else ""))

    def search_by_year(self):
        year = int(input("Ingrese el año para buscar vehículos: "))
        comparison = input("Ingrese 'mayor' o 'menor' para especificar la búsqueda: ")
        results = [vehicle for vehicle in self.vehicles if (comparison == "mayor" and vehicle.get_year() > year) or (comparison == "menor" and vehicle.get_year() < year)]
        for vehicle in results:
            print(f"Marca: {vehicle.get_brand()} Modelo: {vehicle.get_model()} Año: {vehicle.get_year()}")

    def search_by_year_range(self):
        start_year = int(input("Ingrese el año inicial del rango: "))
        end_year = int(input("Ingrese el año final del rango: "))
        results = [vehicle for vehicle in self.vehicles if start_year <= vehicle.get_year() <= end_year]
        for vehicle in results:
            print(f"Marca: {vehicle.get_brand()} Modelo: {vehicle.get_model()} Año: {vehicle.get_year()}")

    def menu(self):
        while True:
            print("\nMenú:")
            print("1. Agregar vehículo")
            print("2. Imprimir vehículos")
            print("3. Buscar vehículos por año")
            print("4. Buscar vehículos por rango de años")
            print("5. Salir")
            option = input("Ingrese la opción deseada: ")
            if option == "1":
                self.add_vehicle()
            elif option == "2":
                self.print_vehicles()
            elif option == "3":
                self.search_by_year()
            elif option == "4":
                self.search_by_year_range()
            elif option == "5":
                break
            else:
                print("Opción inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main = Main()
    main.menu()
