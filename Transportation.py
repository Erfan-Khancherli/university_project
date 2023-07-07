from json.decoder import JSONDecodeError

class Transportation():             
    class Package():
        def __init__(self ,package_number,PackageType, weight , destination ,origin , **kwargs):
            
            self.PackageType    = PackageType
            self.package_number = package_number
            self.weight         = weight
            self.destination    = destination
            self.origin         = origin
            
        def __str__(self):
            return "\n1-package number is: {}\n2-PackageType is: {}\n3-weight is: {}\n4-destination is: {}\n5-origin is: {}\n----------".format(self.package_number,self.PackageType, self.weight , self.destination,self.origin)
        @staticmethod
        def create_package(type_,package_number,weight, destination, origin , *args):
            if   type_ == "breakable":
                return Transportation.Breakable_Packages(package_number,type_, weight, destination, origin)
            elif type_ == "cold":
                return Transportation.Cold_Packages(package_number,type_, weight, destination, origin ,args[0])
            elif type_ == "Default":
                return Transportation.Package(package_number,type_, weight , destination ,origin)
            
            
    class Breakable_Packages(Package):
        def __init__(self,package_number,PackageType , weight, destination, origin , **kwargs):
            super().__init__(package_number,PackageType ,weight, destination, origin , **kwargs)
        
        def __str__(self):
            return "\n1-package number is: {}\n2-PackageType is: {}\n3-weight is: {}\n4-destination is: {}\n5-origin is: {}\n----------".format(self.package_number,self.PackageType, self.weight , self.destination,self.origin)
        
        
        
    class Cold_Packages(Package) :
        def __init__(self, package_number,PackageType, weight, destination, origin ,Minimum_temperature , **kwargs):
            super().__init__(package_number, PackageType,weight, destination, origin ,**kwargs)
            self.Minimum_temperature = Minimum_temperature
        def __str__(self):
            return "\n1-package number is: {}\n2-PackageType is: {}\n3-weight is: {}\n4-destination is: {}\n5-origin is: {}\n6-Minimum_temperature is: {}\n----------".format(self.package_number,self.PackageType, self.weight , self.destination,self.origin,self.Minimum_temperature)
            
            
    class Container():
        def __init__(self , container_number ,ContainerType, Maximum_weight , Maximum_package_number ,load_package_list, **kwargs):
            self.container_number       = container_number
            self.ContainerType          = ContainerType
            self.Maximum_weight         = Maximum_weight
            self.Maximum_package_number = Maximum_package_number
            self.load_package_list      = load_package_list
        def __str__(self):
            return "\n1-container number is: {}\n2-ContainerType is: {}\n3-Maximum_weight is: {}\n4-Maximum_package_number is: {}\n5-load_package_list is: {}\n----------".format(self.container_number,self.ContainerType, self.Maximum_weight , self.Maximum_package_number , self.load_package_list)    
        @staticmethod
        def create_container(type_,container_number,Maximum_weight, Maximum_package_number , *args):
            if   type_ == "breakable":
                return Transportation.Breakable_Container(container_number,type_, Maximum_weight, Maximum_package_number,args[0],args[1])
            elif type_ == "freezer":
                return Transportation.FreezerـContainer(container_number,type_, Maximum_weight, Maximum_package_number ,args[0],args[1])
        
        def add_package():
            pass        
                
    class FreezerـContainer(Container):
        def __init__(self, container_number,ContainerType,Maximum_weight, Maximum_package_number,  container_Minimum_temperature ,load_package_list ,**kwargs):
            super().__init__(container_number,ContainerType ,Maximum_weight, Maximum_package_number,load_package_list, **kwargs)
            self.container_Minimum_temperature = container_Minimum_temperature
        def __str__(self):
            return "\n1-container number is: {}\n2-ContainerType is: {}\n3-Maximum_weight is: {}\n4-Maximum_package_number is: {}\n5-load_package_list is: {}\n6-container_Minimum_temperature is: {}\n----------".format(self.container_number,self.ContainerType, self.Maximum_weight , self.Maximum_package_number , self.load_package_list,self.container_Minimum_temperature)    
            
        def show_compatible(self, packages_list):
            compatible_list = []
            for i in packages_list:
                try:
                    if type(i) is Transportation.Cold_Packages and int(i.Minimum_temperature) >= int(self.container_Minimum_temperature):
                        compatible_list.append((i))
                except:
                    print('your Minimum_temperature is not a number ')
            return compatible_list
        
        def package_to_container(self , compatibles ,packages_id):
            check_list=[]
            count = 0
            for i in compatibles:
                for j in packages_id:
                    if int(i.package_number) == int(j):
                        check_list.append(int(j))
            if len(self.load_package_list)>0:
                for i in check_list:
                    for j in self.load_package_list:
                        if i == int(j):
                            count+=1
                    if count ==0:
                        self.load_package_list.append(j)
                    count=0
            else:
                for j in check_list:
                    self.load_package_list.append(j)
                    
                    
     
    class Breakable_Container(Container):
        def __init__(self, container_number, ContainerType,Maximum_weight, Maximum_package_number,Maximum_speed,load_package_list,**kwargs):
            super().__init__(container_number,ContainerType ,Maximum_weight, Maximum_package_number ,load_package_list, **kwargs)
            self.Maximum_speed = Maximum_speed
        def __str__(self):
            return "\n1-container number is: {}\n2-ContainerType is: {}\n3-Maximum_weight is: {}\n4-Maximum_package_number is: {}\n5-load_package_list is: {}\n6-Maximum_speed is: {}\n----------".format(self.container_number,self.ContainerType, self.Maximum_weight , self.Maximum_package_number , self.load_package_list,self.Maximum_speed)    
        def show_compatible(self, packages_list):
            compatible_list = []
            for i in packages_list:
                if type(i) is Transportation.Breakable_Packages:
                    compatible_list.append((i))    
            return compatible_list
        def package_to_container(self , compatibles ,packages_id):
            check_list=[]
            count = 0
            for i in compatibles:
                for j in packages_id:
                    if int(i.package_number) == int(j):
                        check_list.append(int(j))
            if len(self.load_package_list)>0:
                for i in check_list:
                    for j in self.load_package_list:
                        if i == int(j):
                            count+=1
                    if count ==0:
                        self.load_package_list.append(int(j))
                    count=0
            else:
                for j in check_list:
                    self.load_package_list.append(int(j))            
            
    class Cars():
        def __init__(self , cars_number ,CarType, car_Maximum_portable_weight ,**kwargs):
            self.CarType                     = CarType
            self.cars_number                 = cars_number
            self.car_Maximum_portable_weight = car_Maximum_portable_weight
        
        def __str__(self):
            return "\n1-car number is: {}\n2-CarType is: {}\n3-car_Maximum_portable_weight is: {}\n----------".format(self.cars_number,self.CarType, self.car_Maximum_portable_weight)    
        
        @staticmethod
        def create_car(type_,cars_number,car_Maximum_portable_weight , *args):
            if   type_ == "simple":
                return Transportation.Simple_Cars(cars_number,type_, car_Maximum_portable_weight,args[0],args[1],args[2])
            elif type_ == "container":
                return Transportation.Container_Cars(cars_number,type_, car_Maximum_portable_weight,args[0],args[1])        
            
            
    class Simple_Cars(Cars):
        def __init__(self, cars_number, CarType,car_Maximum_portable_weight ,Maximum_portable_weight ,Maximum_portable_number,package_list , **kwargs):
            super().__init__(cars_number,CarType ,car_Maximum_portable_weight ,**kwargs)
            self.Maximum_portable_weight = Maximum_portable_weight
            self.Maximum_portable_number = Maximum_portable_number
            self.package_list            = package_list
            
            
        def __str__(self):
            return "\n1-car number is: {}\n2-CarType is: {}\n3-car_Maximum_portable_weight is: {}\n4-Maximum_portable_weight is: {}\n5-Maximum_portable_number is: {}\n6-package_list is: {}\n----------".format(self.cars_number,self.CarType, self.car_Maximum_portable_weight , self.Maximum_portable_weight , self.Maximum_portable_number,self.package_list)    
        
        
        def show_compatible(self,containers_list,packages_list ):
            compatible_list = []
            for i in packages_list:
                if type(i) is Transportation.Package:
                    compatible_list.append((i))  
            return compatible_list
        
        def container_to_car(self,compatibles , packages_id):
            check_list=[]
            count = 0
            for i in compatibles:
                for j in packages_id:
                    if int(i.package_number) == int(j):
                        check_list.append(int(j))
            print(check_list)
            if len(self.package_list)>0:
                for i in check_list:
                    for j in self.package_list:
                        if i == int(j):
                            count+=1
                    if count ==0:
                        self.package_list.append(int(i))
                    count=0
            else:
                for j in check_list:
                    self.package_list.append(int(j)) 
            
            
            
    class Container_Cars(Cars):
        def __init__(self, cars_number, CarType,car_Maximum_portable_weight , Maximum_connectable_container,container_list , **kwargs):
            super().__init__(cars_number,CarType ,car_Maximum_portable_weight ,**kwargs)
            self.Maximum_connectable_container = Maximum_connectable_container
            self.container_list            = container_list
        def __str__(self):
            return "\n1-car number is: {}\n2-CarType is: {}\n3-car_Maximum_portable_weight is: {}\n4-Maximum_connectable_container is: {}\n5-container_list is : {}\n----------".format(self.cars_number,self.CarType, self.car_Maximum_portable_weight , self.Maximum_connectable_container,self.container_list)    
        
        def show_compatible(self,containers_list,packages_list ):
            compatible_list = []
            for i in containers_list:
                compatible_list.append((i))
            return compatible_list
        
        def container_to_car(self,compatibles , packages_id):
            check_list=[]
            count = 0
            for i in compatibles:
                for j in packages_id:
                    if int(i.container_number) == int(j):
                        check_list.append(int(j))
            print(check_list)
            if len(self.container_list)>0:
                for i in check_list:
                    for j in self.container_list:
                        if i == int(j):
                            count+=1
                if count ==0:
                    self.container_list.append(i)
                count=0
            else:
                for j in check_list:
                    self.container_list.append(j)