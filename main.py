import json
import os
from json.decoder import JSONDecodeError


class Login():
    def __init__(self , username ,password):
        self.username = username
        self.password = password
        
    def login(self):
        if self.username == 'admin' and self.password == '2097':
            print('Done')
        else:
            print('Wrong')
            return  get_user_pass()
def get_user_pass():
    username = input('username :')
    password = input('password :')
    return username ,password



class Transportation():
                       
    class Package():
        def __init__(self , package_number, weight , destination ,origin , **kwargs):
            self.package_number = package_number
            self.weight         = weight
            self.destination    = destination
            self.origin         = origin
            
            
    class Breakabl_Packages(Package):
        def __init__(self, package_number, weight, destination, origin , **kwargs):
            super().__init__(package_number, weight, destination, origin , **kwargs)
            pass
        
        
        
    class cold_Packages(Package) :
        def __init__(self, package_number, weight, destination, origin ,Minimum_temperature, **kwargs):
            super().__init__(package_number, weight, destination, origin ,**kwargs)
            self.Minimum_temperature = Minimum_temperature
            
            
            
    class Container():
        def __init__(self , container_number , Maximum_weight , Maximum_package_number , load_package_list ,**kwargs):
            self.container_number       = container_number
            self.Maximum_weight         = Maximum_weight
            self.Maximum_package_number = Maximum_package_number
            self.load_package_list      = load_package_list
                
                
                
    class FreezerـContainer(Container):
        def __init__(self, container_number, Maximum_weight, Maximum_package_number, load_package_list , container_Minimum_temperature , **kwargs):
            super().__init__(container_number, Maximum_weight, Maximum_package_number, load_package_list , **kwargs)
            self.container_Minimum_temperature = container_Minimum_temperature
            
            
            
            
    class Breakable_Container(Container):
        def __init__(self, container_number, Maximum_weight, Maximum_package_number, load_package_list , Maximum_speed , **kwargs):
            super().__init__(container_number, Maximum_weight, Maximum_package_number, load_package_list , **kwargs)
            self.Maximum_speed = Maximum_speed
            
            
            
    class Cars():
        def __init__(self , cars_number , car_Maximum_portable_weight ,**kwargs):
            self.cars_number             = cars_number
            self.car_Maximum_portable_weight = car_Maximum_portable_weight
            
            
            
            
    class Simple_Cars(Cars):
        def __init__(self, cars_number, Maximum_portable_weight , Maximum_portable_number , package_list  , **kwargs):
            super().__init__(cars_number, car_Maximum_portable_weight ,**kwargs)
            self.Maximum_portable_number = Maximum_portable_number
            self.package_list            = package_list
            
            
            
    class Container_Cars(Cars):
        def __init__(self, cars_number, car_Maximum_portable_weight , Maximum_connectable_container , **kwargs):
            super().__init__(cars_number, car_Maximum_portable_weight ,**kwargs)
            self.Maximum_connectable_container = Maximum_connectable_container
    
    
    class CRUD(Package , Container):
        def __init__(self,id=1,package_number=1 , weight = None, destination =None, origin = None,container_number = None , Maximum_weight =None, Maximum_package_number=None , load_package_list=None):
            super().__init__(weight = weight, destination = destination, origin = origin , Maximum_weight = Maximum_weight , Maximum_package_number = Maximum_package_number , load_package_list = load_package_list,package_number=package_number)
            self.id =id
        
        def Add_Package(self):
            json_list=[]
            try:    
                    with open("./Packages.json",) as f:
                
                        data = json.load(f)
                        json_list=data
                        self.package_number=json_list[-1]['package_number'] +1
                    # print(self.package_number)
                    # json_data = json.dumps(dictionary, indent=2)
                    dictionary ={
                            "package_number": self.package_number,
                            "weight": "programmer",
                            "destination": "34",
                            "container_number": "54000",
                            "Maximum_weight": "54000",
                            "Maximum_package_number": "54000",
                            "load_package_list": "54000", 
                                }
                    json_list.append(dictionary)
                    os.remove('./Packages.json')
                    with open('./Packages.json', 'w') as f:
                        json.dump(json_list, f, indent=4)
            except JSONDecodeError:
                dictionary ={
                            "package_number": self.package_number,
                            "weight": "programmer",
                            "destination": "34",
                            "container_number": "54000",
                            "Maximum_weight": "54000",
                            "Maximum_package_number": "54000",
                            "load_package_list": "54000", 
                                }
                json_list.append(dictionary)
                os.remove('./Packages.json')
                with open('./Packages.json', 'w') as f:
                    json.dump(json_list, f, indent=4)
            
# username ,password = get_user_pass()
# Transportation(username, password).login()

Transportation.CRUD(destination = 80).Add_Package()