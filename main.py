import json
import os
from json import JSONDecodeError
from Transportation import Transportation
from CrudPackages import CRUD
from CrudContainers import CRUD1
from tkinter import *
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

# username ,password = get_user_pass()
# Transportation(username, password).login()
# Transportation.CRUD(destination = 80).Add_Package()
# CRUD('1' , 30 , 'qom' , 'tehran' , 30)

if __name__ == '__main__':
    packageCrud = CRUD()
    containerCrud = CRUD1()
    AdminMenu          = ['1-Crud packages' , '2-Crud Containers' , '3-Crud Cars' , '4-Loading' , '5-Send and Recive' , '6-Exit']
    CrudPackagesMenu   = ['1-Add package' , '2-edit package' , '3-Delete package']
    CrudContainersMenu = ['1-Add container' , '2-edit container' , '3-Delete container']
    Packages_type      = ['1-Breakable' , '2-Cold' , '3-Default']
    Container_type     = ['1-Breakable' , '2-Freezer']
    packageCrud.load_from_file()
    containerCrud.load_from_file()
    # top = Tk()
    
    
    # crud1 = Button(top, text = "packages").grid(row = 0, column = 0) 
    # crud2 = Button(top, text = "Containers").grid(row = 1, column = 0) 
    # crud3 = Button(top, text = "Cars").grid(row = 2, column = 0)  
    
    
    # top.mainloop()
    # pass
    while(True):
        for i in AdminMenu:
            print(i)
        AdminSelector = input('enter the number : ')
        if AdminSelector =='1':
            
            for i in CrudPackagesMenu:
                print(i)
            CrudSelector = input('enter you number : ')
            
            if CrudSelector == '1':
                type_ = ""
                for i in Packages_type:
                    print(i)
                package_type = input('enter you number : ')
                Weight       = input('Weight :')
                Destination  = input('Destination : ')
                Origin       = input('Origin : ')
                file_name = "./Packages.json"
                try:
                    temp = 0
                    with open(file_name) as f:
                        data = json.load(f)
                        for i in range(len(data)):
                            if data[i-1]['package_number']>temp:
                                temp = data[i-1]['package_number']
                        package_number=temp +1
                except JSONDecodeError:
                    package_number = 1
                if package_type == '1':
                    type_ = "breakable"
                    package = Transportation.Package.create_package(type_,package_number, Weight, Destination, Origin)
                    print(package)
                    packageCrud.add(package)
                    packageCrud.save()
                elif package_type =='2':
                    type_ = "cold"
                    Minimum_temperature = input('Minimum_temperature : ')
                    package = Transportation.Package.create_package(type_,package_number, Weight, Destination, Origin , Minimum_temperature)
                    packageCrud.add(package)
                    packageCrud.save()
                    
                elif package_type =='3':
                    type_ = "Default"
                    package = Transportation.Package.create_package(type_,package_number, Weight, Destination, Origin)
                    packageCrud.add(package)   
            elif CrudSelector == '2':
                packageCrud.show()
                packageEditNumber = int(input('witch package you want to edit(give me your package number) : '))
                packageCrud.target(packageEditNumber)
                packageEditParam = input('give me the number of param you want to change : ')
                while(True):
                    if packageEditParam == '1' or packageEditParam=='2' :
                        print('\nyou cant change package number or package type or !!! \n')
                        packageEditParam = input('give me the number of param you want to change : ')
                    elif packageEditParam >'6' :
                        print('\nwrong number !!!\n')
                        packageEditParam = input('give me the number of param you want to change : ')
                    else:
                        break
                packageEditParamValue= input('give me you param for change : ')
                packageCrud.update(packageEditParam,packageEditParamValue,packageEditNumber)
                packageCrud.save()
                
            elif CrudSelector == '3':
                packageCrud.show()
                DeletePackageNumber = int(input('witch package you want to delete : '))
                packageCrud.delete(DeletePackageNumber)
                packageCrud.save()
                
        elif AdminSelector =='2':
            for i in CrudContainersMenu:
                print(i)
            CrudSelector = input('enter you number : ')
            
            if CrudSelector == '1':
                type_ = ""
                for i in Container_type:
                    print(i)
                container_type            = input('enter you number : ')
                Maximum_weight            = input('Maximum_weight :')
                Maximum_package_number    = input('Maximum_package_number : ')
                file_name = "./Containers.json"
                try:
                    temp = 0
                    with open(file_name) as f:
                        data = json.load(f)
                        for i in range(len(data)):
                            if data[i-1]['container_number']>temp:
                                temp = data[i-1]['container_number']
                        container_number=temp +1
                except JSONDecodeError:
                    container_number = 1
                if container_type == '1':
                    type_ = "breakable"
                    Maximum_speed = input('Maximum_speed : ')
                    container = Transportation.Container.create_container(type_,container_number, Maximum_weight, Maximum_package_number, Maximum_speed)
                    containerCrud.add(container)
                    containerCrud.save()
                elif container_type =='2':
                    type_ = "freezer"
                    container_Minimum_temperature = input('Minimum_temperature : ')
                    container = Transportation.Container.create_container(type_,container_number, Maximum_weight, Maximum_package_number,container_Minimum_temperature)
                    containerCrud.add(container)
                    containerCrud.save()  
            elif CrudSelector == '2':
                containerCrud.show()
                ContainerEditNumber = int(input('witch container you want to edit(give me your container number) : '))
                containerCrud.target(ContainerEditNumber)
                ContainerEditParam = input('give me the number of param you want to change : ')
                while(True):
                    if ContainerEditParam == '1' or ContainerEditParam=='2' or ContainerEditParam=='5':
                        print('\nyou cant change container number or container type or container load package list!!! \n')
                        ContainerEditParam = input('give me the number of param you want to change : ')
                    elif ContainerEditParam >'6' :
                        print('\nwrong number !!!\n')
                        ContainerEditParam = input('give me the number of param you want to change : ')
                    else:
                        break
                ContainerEditParamValue= input('give me you param for change : ')
                containerCrud.update(ContainerEditParam,ContainerEditParamValue,ContainerEditNumber)
                containerCrud.save()
                
                
            elif CrudSelector == '3':
                containerCrud.show()
                DeleteContainerNumber = int(input('witch package you want to delete : '))
                containerCrud.delete(DeleteContainerNumber)
                containerCrud.save() 
        elif AdminSelector == '3':
            pass
        elif AdminSelector =='4':
            pass
        elif AdminSelector == '5':
            pass
        elif AdminSelector == '6':
            pass
    
    # package_type=input('package_type : ')
    # weight = input('weight : ')
    # destination = input('destination : ')
    # origin = input('origin : ')
    # crud = CRUD()
    # ##input package type
    # if package_type =='1':
    #     crud.package = Transportation.Breakabl_Packages(weight ,destination ,origin)
    # elif package_type == '2':
    #     Minimum_temperature = input('Minimum_temperature : ')
    #     crud.package = Transportation.cold_Packages(weight ,destination ,origin , Minimum_temperature)
    # else :
    #     crud.package = Transportation.Package(weight , destination ,origin)

    