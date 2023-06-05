class Login():
    def __init__(self , username ,password):
        self.username = username
        self.password = password
        
    def login(self):
        if self.username == 'admin' and self.password == '2097':
            print('Done')
        else :
            print('Wrong')
            return  get_user_pass()
def get_user_pass():
    username = input('username :')
    password = input('password :')
    return username ,password
class Transportation():
    class CRUD():
        pass
    class Package():
        def __init__(self , package_number , weight , destination ,origin):
            self.package_number = package_number
            self.weight         = weight
            self.destination    = destination
            self.origin         = origin
    class Breakabl_Packages(Package):
        def __init__(self, package_number, weight, destination, origin , *args):
            super().__init__(package_number, weight, destination, origin)
            pass
    class cold_Packages(Package) :
        def __init__(self, package_number, weight, destination, origin ,Minimum_temperature, *args):
            super().__init__(package_number, weight, destination, origin)
            self.Minimum_temperature = Minimum_temperature
    class Container():
        def __init__(self , container_number , Maximum_weight , Maximum_package_number , load_package_list ):
            self.container_number       = container_number
            self.Maximum_weight         = Maximum_weight
            self.Maximum_package_number = Maximum_package_number
            self.load_package_list      = load_package_list
                
    class FreezerـContainer(Container):
        def __init__(self, container_number, Maximum_weight, Maximum_package_number, load_package_list , container_Minimum_temperature , *args):
            super().__init__(container_number, Maximum_weight, Maximum_package_number, load_package_list)
            self.container_Minimum_temperature = container_Minimum_temperature
    class Breakable_Container(Container):
        def __init__(self, container_number, Maximum_weight, Maximum_package_number, load_package_list , Maximum_speed , *args):
            super().__init__(container_number, Maximum_weight, Maximum_package_number, load_package_list)
            self.Maximum_speed = Maximum_speed
    class Cars():
        def __init__(self , cars_number , car_Maximum_portable_weight):
            self.cars_number             = cars_number
            self.car_Maximum_portable_weight = car_Maximum_portable_weight
    class Simple_Cars(Cars):
        def __init__(self, cars_number, Maximum_portable_weight , Maximum_portable_number , package_list  , *args):
            super().__init__(cars_number, car_Maximum_portable_weight)
            self.Maximum_portable_number = Maximum_portable_number
            self.package_list            = package_list
    class Container_Cars(Cars):
        def __init__(self, cars_number, car_Maximum_portable_weight , Maximum_connectable_container , *args):
            super().__init__(cars_number, car_Maximum_portable_weight)
            self.Maximum_connectable_container = Maximum_connectable_container
            
username ,password = get_user_pass()
Transportation(username, password).login()

