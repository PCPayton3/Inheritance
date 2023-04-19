class Autombile:
    def __init__(self, make, model, miles, price):
        self.__make = make
        self.__model = model
        self.__miles = miles
        self.__price = price

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_milage(self):
        return self.__miles

    def get_price(self):
        return self.__price


class Truck(Autombile):
    def __init__(self, make, model, miles, price, drivetype):
        Autombile.__init__(self, make, model, miles, price)

        self.__drivetype = drivetype

    def get_drive_type(self):
        return self.__drivetype


class SUV(Autombile):
    def __init__(self, make, model, miles, price, pass_cap):
        Autombile.__init__(self, make, model, miles, price)

        self.pass_cap = pass_cap

    def get_pass_cap(self):
        return self.__pass_cap


class Car(Autombile):
    def __init(self, make, model, miles, price, doors):
        Autombile.__init__(self, make, model, miles, price)

        self.__doors = doors

    def get_doors(self):
        return self.__doors
