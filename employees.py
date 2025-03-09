"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On my/our honor, <KASHIF GHANI>, this
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: KHG388
"""

from abc import ABC, abstractmethod
import random

DAILY_EXPENSE = 60
HAPPINESS_THRESHOLD = 50
MANAGER_BONUS = 1000
TEMP_EMPLOYEE_PERFORMANCE_THRESHOLD = 50
PERM_EMPLOYEE_PERFORMANCE_THRESHOLD = 25
RELATIONSHIP_THRESHOLD = 10
INITIAL_PERFORMANCE = 75
INITIAL_HAPPINESS = 50
PERCENTAGE_MAX = 100
PERCENTAGE_MIN = 0
SALARY_ERROR_MESSAGE = "Salary must be non-negative."


class Employee(ABC):
    """
    Abstract base class representing a generic employee in the system.
    """

    def __init__(self, name, manager, salary, savings):
        self.relationships = {}
        self.savings = savings
        self.is_employed = True
        self.__name = name
        self.__manager = manager
        self.performance = INITIAL_PERFORMANCE
        self.happiness = INITIAL_HAPPINESS
        self.salary = salary

    @property
    def name(self):
        return self.__name

    @property
    def manager(self):
        return self.__manager
    
    @property
    def salary(self):
        return self.salary
    
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError(SALARY_ERROR_MESSAGE)
    
    @property
    def happiness(self):
        return self.happiness
    
    @happiness.setter
    def happiness(self, value):
        self.happiness = max(PERCENTAGE_MIN, min(PERCENTAGE_MAX), value)

    @property
    def performance(self):
        return self.performance
    
    @performance.setter
    def performance(self, value):
        self.performance = max(PERCENTAGE_MIN, min(PERCENTAGE_MAX), value)

    @abstractmethod
    def work(self):
        pass

    def interact(self, other):
        if other.name not in self.relationships:
            self.relationships[other.name] = 0
        if self.relationships[other.name] > RELATIONSHIP_THRESHOLD:
            self.happiness += 1
        elif self.happiness >= HAPPINESS_THRESHOLD and other.happiness >= HAPPINESS_THRESHOLD:
            self.relationships[other.name] += 1
        else:
            self.relationships[other.name] -= 1
            self.happiness -= 1
    
    def dailyexpense(self):
        self.savings -= DAILY_EXPENSE
        self.happiness -= 1


class Manager(Employee):
    """
    A subclass of Employee representing a manager.
    """
    def work(self):
        performance_adjusted = random.randint(-5,5)
        self.performance += performance_adjusted
        if performance_adjusted <= 0:
            self.happiness -= 1
            for employee in self.relationships:
                self.relationships[employee] -= 1
        else:
            self.happiness += 1


class TemporaryEmployee(Employee):
    """
    A subclass of Employee representing a temporary employee.
    """
    def work(self):
        performance_adjusted = random.randint(-15, 15)
        self.performance += performance_adjusted
        if performance_adjusted <= 0:
            self.happiness -= 2
        else:
            self.happiness += 1


class PermanentEmployee(Employee):
    """
    A subclass of Employee representing a permanent employee.
    """
    def work(self):
        perforamnce_adjusted = random.randint(10, 10)
        self.performance += perforamnce_adjusted
        if perforamnce_adjusted >= 0:
            self.happiness += 1
