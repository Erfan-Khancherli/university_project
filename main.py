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
    
    
    class CRUD(cold_Packages ,Package,Container):
        def __init__(self,package_type=None,package_number=1 , weight = None, destination =None, origin = None,container_number = None , Maximum_weight =None, Maximum_package_number=None , load_package_list=None , Minimum_temperature=None):
            super().__init__(weight = weight, destination = destination, origin = origin , Maximum_weight = Maximum_weight , Maximum_package_number = Maximum_package_number , load_package_list = load_package_list,package_number=package_number , Minimum_temperature=Minimum_temperature,container_number=container_number)
            self.package_type = package_type
            
            
        def Add_Package(self):
            self.weight      = input('weight ? :')
            self.destination = input('maghsad shoma kojast : ')
            self.origin      = input('mabda shoma kojast : ')
            self.package_type= input('age baste shoma shekastani ast addad 1 va agar sard ast addad 2 ra vared konid : ')
            while(1):
                if package_type =='1' or package_type=='2':
                    if   package_type =='1' :
                         package_type = 'Shekastani'
                    elif package_type =='2':
                         package_type = 'Sard'
                         self.Minimum_temperature=input('give me your Minimum temperature :  ')
                    break
                else:
                    print('addad entekhabi shoma bayad 1 ya 2 bashad !')
                    package_type = input('age baste shoma shekastani ast addad 1 va agar sard ast addad 2 ra vared konid : ')
            json_list=[]
            file_name = "./Packages.json"
            try:    
                with open(file_name) as f:
                    data = json.load(f)
                    json_list=data
                    self.package_number=json_list[-1]['package_number'] +1
                    
                    
                    dictionary ={
                        "package_number": self.package_number,
                        "weight": self.weight,
                        "destination": self.destination,
                        "origin" : self.origin,
                        "package_type" : package_type,
                        'Minimum_temperature':self.Minimum_temperature,
                            }
                    json_list.append(dictionary)
                    
                    
                    
                    
                os.remove(file_name)
                with open(file_name, 'w') as f:
                    json.dump(json_list, f, indent=4)
                    
                    
                    
            except JSONDecodeError:
                
                dictionary ={
                            "package_number": self.package_number,
                            "weight": self.weight,
                            "destination": self.destination,
                            "origin" : self.origin,
                            "package_type" : package_type,
                            'Minimum_temperature':self.Minimum_temperature,
                                }
                json_list.append(dictionary)
                
                
                
                os.remove(file_name)
                with open(file_name, 'w') as f:
                    json.dump(json_list, f, indent=4)
                    
        def edit_input(self , value_to_edit ,weight ,destination ,origin , package_type , Minimum_temperature ):
            if value_to_edit == 'weight':
                self.weight= input('vazn jadid ra vared konid : ')
            if value_to_edit == 'destination':
                self.destination= input('maghsad jadid ra vared konid : ')
            if value_to_edit == 'origin':
                self.origin =input('mabda jadid ra vared konid : ') 
            if value_to_edit == 'package_type':
                self.package_type = input('package_type jadid ra vared konid : ')
            if value_to_edit == 'Minimum_temperature':
                self.Minimum_temperature =  input('Minimum_temperature jadid ra vared konid : ')    
            return self.weight ,self.destination ,self.origin , self.package_type , self.Minimum_temperature           
        def Edit_Packages(self):
            file_name = "./Packages.json"
            try:
                with open(file_name) as f:
                    data = json.load(f)
                    for i in range (len(data)):
                        print(data[i])
            except JSONDecodeError:
                print('There is no packages')
            self.package_number= int(input('give me your package_number that you need to Edit : '))
            x = data[self.package_number-1]['package_number']
            print(list(data[self.package_number-1].keys()))
            value_to_edit=input("which you want to change ?!!! : ")
            self.weight               =data[self.package_number-1]['weight'] 
            self.destination          =data[self.package_number-1]['destination'] 
            self.origin               =data[self.package_number-1]['origin'] 
            self.package_type         =data[self.package_number-1]['package_type'] 
            self.Minimum_temperature  =data[self.package_number-1]['Minimum_temperature'] 
            self.weight , self.destination , self.origin , self.package_type , self.Minimum_temperature = self.edit_input(value_to_edit,self.weight , self.destination , self.origin , self.package_type , self.Minimum_temperature)
            data[self.package_number-1]['weight'] = self.weight
            data[self.package_number-1]['destination'] = self.destination
            data[self.package_number-1]['origin'] = self.origin
            data[self.package_number-1]['package_type'] = self.package_type
            data[self.package_number-1]['Minimum_temperature'] = self.Minimum_temperature
            os.remove(file_name)
            with open(file_name, 'w') as f:
                json.dump(data, f, indent=4)
            edit_again  = input('do you want to change more ? (Y/N)')
            if edit_again == 'Y' or edit_again=='y':
                self.Edit_Packages()
            elif edit_again == 'N' or edit_again == 'n':
                pass
        
            
# username ,password = get_user_pass()
# Transportation(username, password).login()
# Transportation.CRUD(destination = 80).Add_Package()
Transportation.CRUD(destination = 80).Edit_Packages()