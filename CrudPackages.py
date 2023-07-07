from Transportation import Transportation
from json.decoder import JSONDecodeError
import os
import json
import operator
class CRUD():
    
        def __init__(self):
            self.packages = []
        
        def load_from_file(self):
            file_name = "./Packages.json"
            json_list=[]
            try:
                with open(file_name) as f:
                    data = json.load(f)
                    for i in range(len(data)):
                        if data[i-1]['package_type'] == 'breakable':
                            self.packages.append(Transportation.Package.create_package(data[i-1]['package_type'],data[i-1]['package_number'],data[i-1]['weight'], data[i-1]['destination'], data[i-1]['origin']))
                        elif data[i-1]['package_type'] == 'cold':
                            self.packages.append(Transportation.Package.create_package(data[i-1]['package_type'],data[i-1]['package_number'],data[i-1]['weight'], data[i-1]['destination'], data[i-1]['origin'] , data[i-1]['Minimum_temperature']))
                        elif data[i-1]['package_type'] =='Default':
                            self.packages.append(Transportation.Package.create_package(data[i-1]['package_type'],data[i-1]['package_number'],data[i-1]['weight'], data[i-1]['destination'], data[i-1]['origin']))
            except JSONDecodeError:
                pass
        
        def delete(self , DeletePackageNumber):
            for j in DeletePackageNumber:
                print(type(j))
                
                self.packages = [i for i in self.packages if i.package_number != int(j) ]

            print(self.packages)
                    
                
        
        def add(self , package):
            self.packages.append(package)
            
        def update(self , packageEditParam , packageEditParamValue,packageEditNumber):
            if packageEditParam   =='3':
                for i in self.packages:
                    if i.package_number == packageEditNumber:
                        i.weight = packageEditParamValue
            elif packageEditParam =='4':
                for i in self.packages:
                    if i.package_number == packageEditNumber:
                        i.destination = packageEditParamValue        
            elif packageEditParam =='5':
                for i in self.packages:
                    if i.package_number == packageEditNumber:
                        i.origin = packageEditParamValue 
            elif packageEditParam =='6':
                for i in self.packages:
                    if i.package_number == packageEditNumber:
                        i.Minimum_temperature = packageEditParamValue  
        def target(self , packageEditNumber):
            for i in self.packages:
                if i.package_number == packageEditNumber:
                    print(str(i))
                    # typePackage = type(i).__name__
                    # if typePackage == 'Breakabl_Packages':
                    #     print(str(i))
                    # elif typePackage == 'cold_Packages':
                    #     print(str(i))
        def show(self):
            for i in self.packages:
                print(str(i))
        
        def save(self):
            file_name = "./Packages.json"
            json_list=[]
            try:
                with open(file_name) as f:
                    for i in self.packages:
                        if i.PackageType == 'cold':
                            dictionary ={
                                    "package_number": i.package_number,
                                    "weight": i.weight,
                                    "destination": i.destination,
                                    "origin" : i.origin,
                                    "package_type" : i.PackageType,
                                    'Minimum_temperature':i.Minimum_temperature,
                                    }
                        elif i.PackageType == 'breakable' or i.PackageType == 'Default':
                            dictionary ={
                                    "package_number": i.package_number,
                                    "weight": i.weight,
                                    "destination": i.destination,
                                    "origin" : i.origin,
                                    "package_type" : i.PackageType,
                                    }
                        json_list.append(dictionary) 
                os.remove(file_name)
                with open(file_name, 'w') as f:
                    json.dump(json_list, f, indent=4)
            except JSONDecodeError:
                with open(file_name) as f:
                    for i in self.packages:
                        if i.PackageType == 'cold':
                            dictionary ={
                                    "package_number": 1,
                                    "weight": i.weight,
                                    "destination": i.destination,
                                    "origin" : i.origin,
                                    "package_type" : i.PackageType,
                                    'Minimum_temperature':i.Minimum_temperature,
                                    }
                        elif i.PackageType == 'breakable' or i.PackageType == 'Default':
                            dictionary ={
                                    "package_number": 1,
                                    "weight": i.weight,
                                    "destination": i.destination,
                                    "origin" : i.origin,
                                    "package_type" : i.PackageType,
                                    }
                        json_list.append(dictionary)
                os.remove(file_name)
                with open(file_name, 'w') as f:
                    json.dump(json_list, f, indent=4)
            