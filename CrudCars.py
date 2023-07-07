from Transportation import Transportation
from json.decoder import JSONDecodeError
import os
import json
# import operator
class CRUD2():
    
        def __init__(self):
            self.cars = []

        
        def pack(self , id):
            for i in self.cars:
                if int(i.cars_number) == int(id):
                    return i
        
        def load_from_file(self):
            file_name = "./Cars.json"
            json_list=[]
            try:
                with open(file_name) as f:
                    data = json.load(f)
                    for i in range(len(data)):
                        if data[i-1]['CarType'] == 'simple':
                            self.cars.append(Transportation.Cars.create_car(data[i-1]['CarType'],data[i-1]['cars_number'],data[i-1]['car_Maximum_portable_weight'], data[i-1]['Maximum_portable_weight'], data[i-1]['Maximum_portable_number'],data[i-1]['package_list']))
                        elif data[i-1]['CarType'] == 'container':
                            self.cars.append(Transportation.Cars.create_car(data[i-1]['CarType'],data[i-1]['cars_number'],data[i-1]['car_Maximum_portable_weight'] ,data[i-1]['Maximum_connectable_container'],data[i-1]['container_list'] ))
            except JSONDecodeError:
                pass
        
        def delete(self , DeleteCarNumber):
            for j in DeleteCarNumber:
                self.cars = [i for i in self.cars if i.cars_number != int(j) ]

            print(self.cars)
                    
                
        
        def add(self , car):
            self.cars.append(car)
            for i in self.cars:
                print(i)
            
        def update(self , CarEditParam , CarEditParamValue,CarEditNumber):
            if CarEditParam   =='3':
                for i in self.cars:
                    if i.cars_number == CarEditNumber:
                        i.car_Maximum_portable_weight = CarEditParamValue
            elif CarEditParam =='4':
                for i in self.cars:
                    if i.CarType == 'simple':
                        if i.cars_number == CarEditNumber:
                            i.Maximum_portable_weight = CarEditParamValue
                    elif i.CarType == 'container' :
                        for i in self.cars:
                            if i.cars_number == CarEditNumber:
                                i.Maximum_connectable_container = CarEditParamValue        
            elif CarEditParam =='5':
                for i in self.cars:
                    if i.CarType == 'simple':
                        if i.cars_number == CarEditNumber:
                            i.Maximum_portable_number = CarEditParamValue
                else :
                    pass           
                            
                        # try:
                        #     i.container_Minimum_temperature = ContainerEditParamValue  
                        # except:
                        #     i.Maximum_speed = ContainerEditParamValue  
                    
        def target(self , CarEditNumber):
            for i in self.cars:
                if i.cars_number == CarEditNumber:
                    print(str(i))
                    # typePackage = type(i).__name__
                    # if typePackage == 'Breakabl_Packages':
                    #     print(str(i))
                    # elif typePackage == 'cold_Packages':
                    #     print(str(i))
        def show(self):
            if len(self.cars) ==0:
                return len(self.cars)
            for i in self.cars:
                print(str(i))
        
        def save(self):
            file_name = "./Cars.json"
            json_list=[]
            try:
                with open(file_name) as f:
                    for i in self.cars:
                        if i.CarType == 'simple':
                            dictionary ={
                                    "cars_number": i.cars_number,
                                    "car_Maximum_portable_weight": i.car_Maximum_portable_weight,
                                    "Maximum_portable_weight": i.Maximum_portable_weight,
                                    "CarType" : i.CarType,
                                    "package_list" : i.package_list,
                                    'Maximum_portable_number':i.Maximum_portable_number,
                                    }
                        elif i.CarType == 'container':
                            dictionary ={
                                    "cars_number": i.cars_number,
                                    "car_Maximum_portable_weight": i.car_Maximum_portable_weight,
                                    "Maximum_connectable_container": i.Maximum_connectable_container,
                                    "CarType" : i.CarType,
                                    "container_list" : i.container_list,
                                    }
                        json_list.append(dictionary) 
                os.remove(file_name)
                with open(file_name, 'w') as f:
                    json.dump(json_list, f, indent=4)
            except JSONDecodeError:
                with open(file_name) as f:
                    for i in self.containers:
                        if i.CarType == 'simple':
                            dictionary ={
                                    "cars_number": 1,
                                    "car_Maximum_portable_weight": i.car_Maximum_portable_weight,
                                    "Maximum_portable_weight": i.Maximum_portable_weight,
                                    "CarType" : i.CarType,
                                    "package_list" : i.package_list,
                                    'Maximum_portable_number':i.Maximum_portable_number,
                                    }
                        elif i.CarType == 'container':
                            dictionary ={
                                    "cars_number": 1,
                                    "car_Maximum_portable_weight": i.car_Maximum_portable_weight,
                                    "Maximum_connectable_container": i.Maximum_connectable_container,
                                    "CarType" : i.CarType,
                                    }
                        json_list.append(dictionary)
                os.remove(file_name)
                with open(file_name, 'w') as f:
                    json.dump(json_list, f, indent=4)
        def Ready_car(self):
            Ready_list=[]
            for i in self.cars:
                try:
                    if len(i.container_list)>0:
                        Ready_list.append(i)    
                except AttributeError:
                    if len(i.package_list)>0:
                        Ready_list.append(i) 
            for i in Ready_list:
                print(i)                        
        def recive(self):
            pass
        def send(self , send_car_id):
            sent_car=[]
            for i in self.cars:
                for j in send_car_id:
                    if int(i.cars_number) == int(j):
                        sent_car.append(i)
                        self.cars = [i for i in self.cars if i.cars_number != int(j) ]
            return sent_car
                
            
            
                        
                        
                        
                
                