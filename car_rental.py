# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 19:00:03 2021

@author: EGBUNA

Car Rental Services
"""

class CarRent:
    def __init__(self, available_cars):
        self.available_cars = available_cars
        
    def allAvailableCars(self):
        print('below are the cars available for rent: ')
        for car in self.available_cars:
            print(car, 'cost ', self.available_cars[car], 'daily')
    
    def Rent(self, tup):
        if tup[0] in self.available_cars: 
            print('Hurray, you just rented ', tup[0], ' and it cost ', tup[1] * self.available_cars[tup[0]])
            self.available_cars.pop(tup[0])
        else:
            print('Sorry, car not currently available, check back later')
    
    def AddCar(self, nap):
        self.available_cars[nap[0]] = nap[1]
        
class Customer:
    def CheckRent(self):
        car = input('enter car you wish to rent: ')
        days = int(input('enter number of days to rent ' + car ))
        return car, days
    
    def ReturnCar(self):
        car = input('name of car to return: ')
        price = int(input('price of the borrowed car: '))
        return car, price
    
def main():
    car_company = CarRent({'SUV':200, 'Sedan':100, 'Hatchback':10})
    customer = Customer()
    
    while True:
        print('''
              ======CAR INVENTORY======
              1. Display all available cars and see prices
              2. Request a car
              3. Return a car
              4. Exit
              ''')
    
        choice = int(input('Enter Choice: '))
        if choice == 1:
            car_company.allAvailableCars()
        elif choice == 2:
            car_company.Rent(customer.CheckRent())
        elif choice == 3:
            car_company.AddCar(customer.ReturnCar())
        else:
            print('Thanks for visiting the car inventory today')
            break
    
        
    
main()   
    

