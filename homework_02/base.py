from abc import ABC
from homework_02.exceptions import LowFuelError
from homework_02.exceptions import NotEnoughFuel



class Vehicle(ABC):

    started = False
    distance = 0
    max_distance = 0
    fuel = 0
    fuel_consumption = 0
    weight = 0


    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption


    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError


    def move(self, distance):
        if self.fuel // self.fuel_consumption >= distance:
            self.fuel = self.fuel - distance * self.fuel_consumption
        else:
            raise NotEnoughFuel

