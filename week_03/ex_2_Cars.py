#https://www.coursera.org/learn/diving-in-python/programming/bd6aI/klassy-i-nasliedovaniie

import csv
import os


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
        
    def __str__(self):
        return f'car_type = {self.car_type}, \n\
            brand = {self.brand}, \n\
            photo_file_name = {self.photo_file_name}, \n\
            carrying = {self.carrying}'
        
    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]

class Car(CarBase):
    car_type = 'car'
    
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):      
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count
        
    def __str__(self):
        return f'{super().__str__()} \n\
            passenger_seats_count = {self.passenger_seats_count}'

class Truck(CarBase):
    car_type = 'truck'
    
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        
        def _body_whl_parse(body_whl):
            whl = body_whl.split('x')        
            self.body_length = float(whl[0])
            self.body_width = float(whl[1])
            self.body_height = float(whl[2])
            self.body_whl = body_whl
        
        try:
            _body_whl_parse(body_whl)
        except ValueError:
            _body_whl_parse('0x0x0')
            
    def __str__(self):
        return f'{super().__str__()} \n\
            body_whl = {self.body_whl}\n\
            body_length = {self.body_length}\n\
            body_width = {self.body_width}\n\
            body_height = {self.body_height}'
  
                       
    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height
        
class SpecMachine(CarBase):
    car_type = 'spec_machine'
    
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra
        
    def __str__(self):
        return f'{super().__str__()} \n\
            extra = {self.extra}'

        
        
def get_car_list(csv_filename):
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        car_list = []
        for row in reader:
            if row == [] or None:
                continue
            car = get_car(row)
            if car == None:
                continue
            car_list.append(car)
            
    return car_list

def is_valid_ext(photo_file_name):
    list_ext = ['.jpg', '.jpeg', '.png', '.gif']
    ext = os.path.splitext(photo_file_name)[1]
    if ext not in list_ext:
        raise ValueError
    else:
        return photo_file_name

def get_car(row):
    if row[0] == 'car':
        try:
            brand = row[1]
            photo_file_name = is_valid_ext(row[3])
            carrying = float(row[5])
            passenger_seats_count = int(row[2])
            car_ = Car(brand, photo_file_name, carrying, passenger_seats_count)
        except ValueError as err:
            #print(f'ValueError: {err.args[0]}')
            return None
        return car_
    elif row[0] == 'truck':
        try:
            brand = row[1]
            photo_file_name = is_valid_ext(row[3])
            carrying = float(row[5])
            body_whl = row[4]
            car_ = Truck(brand, photo_file_name, carrying, body_whl) 
        except ValueError as err:
            #print(f'ValueError: {err.args[0]}')
            return None
        return car_
    elif row[0] == 'spec_machine':
        try:
            brand = row[1]
            photo_file_name = is_valid_ext(row[3])
            carrying = float(row[5])
            extra = row[6]
            car_ = SpecMachine(brand, photo_file_name, carrying, extra)
        except ValueError as err:
            #print(f'ValueError: {err.args[0]}')
            return None
        return car_
    else:
        return None

cars = get_car_list('coursera_week3_cars.csv')
len(cars)
for car in cars:
    print(type(car))
print(cars[0].passenger_seats_count)
print(cars[1].get_body_volume())
