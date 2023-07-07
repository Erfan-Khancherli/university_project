from Transportation import Transportation
from json.decoder import JSONDecodeError
import os
import json
import operator
class CRUD1():
    
        def __init__(self):
            self.containers = []
            
        def pack(self , id):
            for i in self.containers:
                if int(i.container_number) == int(id):
                    return i
            
            
        def load_from_file(self):
            file_name = "./Containers.json"
            json_list=[]
            try:
                with open(file_name) as f:
                    data = json.load(f)
                    for i in range(len(data)):
                        if data[i-1]['ContainerType'] == 'breakable':
                            self.containers.append(Transportation.Container.create_container(data[i-1]['ContainerType'],data[i-1]['container_number'],data[i-1]['Maximum_weight'], data[i-1]['Maximum_package_number'], data[i-1]['Maximum_speed'],data[i-1]['load_package_list']))
                        elif data[i-1]['ContainerType'] == 'freezer':
                            self.containers.append(Transportation.Container.create_container(data[i-1]['ContainerType'],data[i-1]['container_number'],data[i-1]['Maximum_weight'], data[i-1]['Maximum_package_number'], data[i-1]['container_Minimum_temperature'],data[i-1]['load_package_list']))
            except JSONDecodeError:
                pass
        
        def delete(self , DeleteContainerNumber):
            for j in DeleteContainerNumber:
                self.containers = [i for i in self.containers if i.container_number != int(j) ]

            print(self.containers)
                    
                
        
        def add(self , container):
            self.containers.append(container)
            for i in self.containers:
                print(i)
            
        def update(self , ContainerEditParam , ContainerEditParamValue,ContainerEditNumber):
            if ContainerEditParam   =='3':
                for i in self.containers:
                    if i.container_number == ContainerEditNumber:
                        i.Maximum_weight = ContainerEditParamValue
            elif ContainerEditParam =='4':
                for i in self.containers:
                    if i.container_number == ContainerEditNumber:
                        i.Maximum_package_number = ContainerEditParamValue        
            elif ContainerEditParam =='6':
                for i in self.containers:
                    if i.container_number == ContainerEditNumber:
                        if i.ContainerType == 'breakable':
                            i.Maximum_speed = ContainerEditParamValue
                        elif i.ContainerType == 'freezer':
                            i.container_Minimum_temperature = ContainerEditParamValue
                             
                    
        def target(self , ContainerEditNumber):
            for i in self.containers:
                if i.container_number == ContainerEditNumber:
                    print(str(i))
                    
                    
        def show(self):
            if len(self.containers) ==0:
                return len(self.containers)
            for i in self.containers:
                print(str(i))
        
        def save(self):
            file_name = "./Containers.json"
            json_list=[]
            try:
                with open(file_name) as f:
                    for i in self.containers:
                        if i.ContainerType == 'freezer':
                            dictionary ={
                                    "container_number": i.container_number,
                                    "Maximum_weight": i.Maximum_weight,
                                    "Maximum_package_number": i.Maximum_package_number,
                                    "ContainerType" : i.ContainerType,
                                    "load_package_list" : i.load_package_list,
                                    'container_Minimum_temperature':i.container_Minimum_temperature,
                                    }
                        elif i.ContainerType == 'breakable':
                            dictionary ={
                                    "container_number": i.container_number,
                                    "Maximum_weight": i.Maximum_weight,
                                    "Maximum_package_number": i.Maximum_package_number,
                                    "ContainerType" : i.ContainerType,
                                    "load_package_list" : i.load_package_list,
                                    'Maximum_speed':i.Maximum_speed,
                                    }
                        json_list.append(dictionary) 
                os.remove(file_name)
                with open(file_name, 'w') as f:
                    json.dump(json_list, f, indent=4)
            except JSONDecodeError:
                with open(file_name) as f:
                    for i in self.containers:
                        if i.ContainerType == 'freezer':
                            dictionary ={
                                    "container_number": 1,
                                    "Maximum_weight": i.Maximum_weight,
                                    "Maximum_package_number": i.Maximum_package_number,
                                    "ContainerType" : i.ContainerType,
                                    "load_package_list" : i.load_package_list,
                                    'container_Minimum_temperature':i.container_Minimum_temperature,
                                    }
                        elif i.ContainerType == 'breakable':
                            dictionary ={
                                    "container_number": 1,
                                    "Maximum_weight": i.Maximum_weight,
                                    "Maximum_package_number": i.Maximum_package_number,
                                    "ContainerType" : i.ContainerType,
                                    "load_package_list" : i.load_package_list,
                                    'Maximum_speed':i.Maximum_speed,
                                    }
                        json_list.append(dictionary)
                os.remove(file_name)
                with open(file_name, 'w') as f:
                    json.dump(json_list, f, indent=4)
            