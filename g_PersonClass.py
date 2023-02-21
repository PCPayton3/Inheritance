class Person:
    def __init__(self, name, address, telephone):
        self.__name = name
        self.__address = address
        self.__telephone = telephone

    def set_person(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_telephone(self, telephone):
        self.__telephone = telephone

    def get_person(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_telephone(self):
        return self.__telephone


class Customer(Person):
    def __init__(self, name, address, telephone, cust_num,):
        Person.__init__(self, name, address, telephone)
        self.__cust_num = cust_num

    def set_cust_num(self, cust_num):
        self.__cust_num = cust_num

    def get_cust_num(self):
        return self.__cust_num
