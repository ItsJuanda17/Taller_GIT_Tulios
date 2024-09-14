from Vehicle import Vehicle

class MainClass:
    def __init__(self):
        self.vehicles = []

    def addVehicle(self):
        make = input("Ingrese la marca del vehículo: ")
        model = input("Ingrese el modelo del vehículo: ")
        year = int(input("Ingrese el año del vehículo: "))
        mileage = int(input("Ingrese el kilometraje del vehículo: "))
        currentStatus = input("Ingrese el estado actual del vehículo: ")
        fuelType = input("Ingrese el tipo de combustible del vehículo: ")
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

        vehicle = Vehicle(make, model, year, mileage, currentStatus, fuelType, power, color)
        self.vehicles.append(vehicle)
        print(f"Vehículo añadido: {vehicle.getBrand()} {vehicle.getModel()}")

    def printVehicles(self):
        for vehicle in self.vehicles:
            print(f"Marca: {vehicle.getBrand()} Modelo: {vehicle.getModel()} Año: {vehicle.getYear()} Kilometraje: {vehicle.getMileage()} Estado actual: {vehicle.getCurrentStatus()} Tipo de combustible: {vehicle.getFuelType()}" + (f" Potencia: {vehicle.getPower()}" if vehicle.getPower() is not None else "") + (f" Color: {vehicle.getColor()}" if vehicle.getColor() is not None else ""))

    def searchByYear(self):
        year = int(input("Ingrese el año para buscar vehículos: "))
        comparison = input("Ingrese 'mayor' o 'menor' para especificar la búsqueda: "))
        results = [vehicle for vehicle in self.vehicles if (comparison == "mayor" and vehicle.getYear() > year) or (comparison == "menor" and vehicle.getYear() < year)]
        for vehicle in results:
            print(f"Marca: {vehicle.getBrand()} Modelo: {vehicle.getModel()} Año: {vehicle.getYear()}")

    def searchByYearRange(self):
        startYear = int(input("Ingrese el año inicial del rango: "))
        endYear = int(input("Ingrese el año final del rango: "))
        results = [vehicle for vehicle in self.vehicles if startYear <= vehicle.getYear() <= endYear]
        for vehicle in results:
            print(f"Marca: {vehicle.getBrand()} Modelo: {vehicle.getModel()} Año: {vehicle.getYear()}")

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
                self.addVehicle()
            elif option == "2":
                self.printVehicles()
            elif option == "3":
                self.searchByYear()
            elif option == "4":
                self.searchByYearRange()
            elif option == "5":
                break
            else:
                print("Opción inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main = MainClass()
    main.menu()
