from abc import ABC, abstractmethod

class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code

#é feito a transformação da classe para abstrata, para protege-lá
class Employee(ABC):
    def __init__(self, code, name, salary):
        self.code = code
        self.name = name
        self.salary = salary
        self.hour = 8

    @abstractmethod
    def calc_bonus(self):
        pass

#se transformar esse metodo em abstrato, não consigo realizar get_hours em Seller

    def get_hours(self):
        pass

# o "__" no nome da variavel serve para protege-la
class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__departament = Department('managers', 1)
    
    def get_hours(self):
        return self.hour

    def get_departament(self):
        return self.__departament.name
    
    def set_departament(self, nome):
        self.__departament.name = nome

    def calc_bonus(self):
        return self.salary * 0.15


class Seller(Manager):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__departament = Department('sellers', 2)
        self.__sales = 0

    def get_hours(self):
        return self.hour
    
    def get_sales(self):
        return self.__sales
    
    def get_departament(self):
        return self.__departament.name
    
    def set_departament(self, nome):
        self.__departament.name = nome


    def put_sales(self, sale):
        self.__sales+=sale
    
    def calc_bonus(self):
        return self.__sales*0.15


