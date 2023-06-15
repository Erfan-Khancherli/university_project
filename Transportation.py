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
            if type_ == "breakable":
                return Transportation.Breakabl_Packages(package_number,type_, weight, destination, origin)
            elif type_ == "cold":
                return Transportation.cold_Packages(package_number,type_, weight, destination, origin ,args[0])
            elif type_=="Default":
                return Transportation.Package(package_number,type_, weight , destination ,origin)
            
            
    class Breakabl_Packages(Package):
        def __init__(self,package_number,PackageType , weight, destination, origin , **kwargs):
            super().__init__(package_number,PackageType ,weight, destination, origin , **kwargs)
        
        def __str__(self):
            return "\n1-package number is: {}\n2-PackageType is: {}\n3-weight is: {}\n4-destination is: {}\n5-origin is: {}\n----------".format(self.package_number,self.PackageType, self.weight , self.destination,self.origin)
        
        
        
    class cold_Packages(Package) :
        def __init__(self, package_number,PackageType, weight, destination, origin ,Minimum_temperature , **kwargs):
            super().__init__(package_number, PackageType,weight, destination, origin ,**kwargs)
            self.Minimum_temperature = Minimum_temperature
        def __str__(self):
            return "\n1-package number is: {}\n2-PackageType is: {}\n3-weight is: {}\n4-destination is: {}\n5-origin is: {}\n6-Minimum_temperature is: {}\n----------".format(self.package_number,self.PackageType, self.weight , self.destination,self.origin,self.Minimum_temperature)
            
            
    class Container():
        def __init__(self , container_number ,ContainerType, Maximum_weight , Maximum_package_number , **kwargs):
            self.container_number       = container_number
            self.ContainerType          = ContainerType
            self.Maximum_weight         = Maximum_weight
            self.Maximum_package_number = Maximum_package_number
            self.load_package_list      = []
        def __str__(self):
            return "\n1-container number is: {}\n2-ContainerType is: {}\n3-Maximum_weight is: {}\n4-Maximum_package_number is: {}\n5-load_package_list is: {}\n----------".format(self.container_number,self.ContainerType, self.Maximum_weight , self.Maximum_package_number , self.load_package_list)    
        @staticmethod
        def create_container(type_,container_number,Maximum_weight, Maximum_package_number , *args):
            if   type_ == "breakable":
                return Transportation.Breakable_Container(container_number,type_, Maximum_weight, Maximum_package_number,args[0])
            elif type_ == "freezer":
                return Transportation.FreezerـContainer(container_number,type_, Maximum_weight, Maximum_package_number ,args[0])
                
                
    class FreezerـContainer(Container):
        def __init__(self, container_number,ContainerType,Maximum_weight, Maximum_package_number,  container_Minimum_temperature , **kwargs):
            super().__init__(container_number,ContainerType ,Maximum_weight, Maximum_package_number, **kwargs)
            self.container_Minimum_temperature = container_Minimum_temperature
        def __str__(self):
            return "\n1-container number is: {}\n2-ContainerType is: {}\n3-Maximum_weight is: {}\n4-Maximum_package_number is: {}\n5-load_package_list is: {}\n6-container_Minimum_temperature is: {}\n----------".format(self.container_number,self.ContainerType, self.Maximum_weight , self.Maximum_package_number , self.load_package_list,self.container_Minimum_temperature)    
            
            
            
            
    class Breakable_Container(Container):
        def __init__(self, container_number, ContainerType,Maximum_weight, Maximum_package_number,Maximum_speed ,**kwargs):
            super().__init__(container_number,ContainerType ,Maximum_weight, Maximum_package_number , **kwargs)
            self.Maximum_speed = Maximum_speed
        def __str__(self):
            return "\n1-container number is: {}\n2-ContainerType is: {}\n3-Maximum_weight is: {}\n4-Maximum_package_number is: {}\n5-load_package_list is: {}\n6-Maximum_speed is: {}\n----------".format(self.container_number,self.ContainerType, self.Maximum_weight , self.Maximum_package_number , self.load_package_list,self.Maximum_speed)    
            
            
            
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
