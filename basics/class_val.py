class Microwave: 
    def __init__(self, brand :str, power :int) -> None:
        self.brand = brand
        self.power = power
        self.turned_on : bool = False

    def turn_on(self) -> None:
        if self.turned_on:
            print(f"{self.brand} microwave is already on.")
        else:
            self.turned_on = True
            print(f"{self.brand} microwave is now on.")

    def turn_off(self) -> None:
        if not self.turned_on:
            print(f"{self.brand} microwave is already off.")
        else:
            self.turned_on = False
            print(f"{self.brand} microwave is now off.")

    def run_microwave(self, time :int) -> None:
        if not self.turned_on:
            print(f"{self.brand} microwave is off. Please turn it on first.")
        else:
            print(f"{self.brand} microwave is running for {time} seconds.")

smeg: Microwave = Microwave("Smeg", 800)
print(smeg.brand)  # Output: Smeg
print(smeg.power)  # Output: 800

boosh: Microwave = Microwave("Boosh", 1000)
print(boosh.brand)  # Output: Boosh
print(boosh.power)  # Output: 1000

smeg.turn_on()  # Output: Smeg microwave is now on.
smeg.turn_on()  # Output: Smeg microwave is already on.
smeg.turn_off()  # Output: Smeg microwave is now off.
smeg.turn_off()  # Output: Smeg microwave is already off.

boosh.run_microwave(30)  # Output: Boosh microwave is off. Please turn it on first.
boosh.turn_on()  # Output: Boosh microwave is now on.
boosh.run_microwave(30)  # Output: Boosh microwave is running for 30 seconds.cd ..


class Employee: 
    def __init__(self, empid :int, name :str, salary :float) -> None:
        self.empid = empid
        self.name = name
        self.salary = salary
    
    # setter methods for the Employee class
    def set_empid(self, empid :int) -> None:
        self.empid = empid
    def set_name(self, name :str) -> None:
        self.name = name
    def set_salary(self, salary :float) -> None:
        self.salary = salary

    # getter methods for the Employee class
    def get_empid(self) -> int:
        return self.empid
    def get_name(self) -> str:
        return self.name
    def get_salary(self) -> float:
        return self.salary


emp1: Employee = Employee(1, "Alice", 50000.0)
print(emp1.get_empid())  # Output: 1
print(emp1.get_name())  # Output: Alice
print(emp1.get_salary())  # Output: 50000.0

emp1.set_empid(2)
emp1.set_name("Bob")    
emp1.set_salary(60000.0)
print(emp1.get_empid())  # Output: 2
print(emp1.get_name())  # Output: Bob
print(emp1.get_salary())  # Output: 60000.0

