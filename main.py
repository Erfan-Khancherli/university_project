import json
import os
from json import JSONDecodeError
from Transportation import Transportation
from CrudPackages import CRUD
from CrudContainers import CRUD1
from CrudCars import CRUD2
from tkinter import *
from barname import barname
import sys

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
    packageCrud   = CRUD()
    containerCrud = CRUD1()
    carCrud       = CRUD2()
    barname       = barname()
    
    AdminMenu          = ['1-Crud packages' , '2-Crud Containers' , '3-Crud Cars' , '4-Loading' , '5-Send and Recive' , '6-Exit']
    CrudPackagesMenu   = ['1-Add package' , '2-edit package' , '3-Delete package']
    CrudContainersMenu = ['1-Add container' , '2-edit container' , '3-Delete container']
    CrudCarsMenu       = ['1-add car' , '2-edit car' , '3-delete car']
    Packages_type      = ['1-Breakable' , '2-Cold' , '3-Default']
    Container_type     = ['1-Breakable' , '2-Freezer']
    Car_type           = ['1-Simple' , '2-Container']
    LoadingList        = ['1-show packages' , '2-show containers' , '3-show cars' , '4-Loading packages to containers' , '5-Loading containers to cars']
    SendReciveMenu     = ['1-Ready cars' , '2-Recive','3-Send']
    
    
    packageCrud.load_from_file()
    containerCrud.load_from_file()
    carCrud.load_from_file()
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
                while(True):
                    try:
                        Weight   = int(input('Weight :'))
                        if type(Weight) is int:
                            break
                    except ValueError:
                        print('you can just give me numbers ! ')
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
                    while(True):
                        try:
                            Minimum_temperature = int(input('Minimum_temperature : '))
                            if type(Minimum_temperature) is int:
                                break
                        except ValueError:
                            print('you can just give me numbers ! ')
                    
                    package = Transportation.Package.create_package(type_,package_number, Weight, Destination, Origin , Minimum_temperature)
                    packageCrud.add(package)
                    packageCrud.save()
                    
                elif package_type =='3':
                    type_ = "Default"
                    package = Transportation.Package.create_package(type_,package_number, Weight, Destination, Origin)
                    packageCrud.add(package)
                    packageCrud.save()
                       
            elif CrudSelector == '2':
                packageCrud.show()
                while(True):
                    try:
                        packageEditNumber = int(input('witch package you want to edit(give me your package number) : '))
                        if type(packageEditNumber) is int:
                            break
                    except ValueError:
                        print('you can just give me numbers ! ')                
                
                packageCrud.target(packageEditNumber)
                packageEditParam = input('give me the number of param you want to change : ')
                while(True):
                    if packageEditParam == '1' or packageEditParam=='2' :
                        print('\nyou cant change package number or package type or !!! \n')
                        packageEditParam = input('give me the number of param you want to change : ')
                    elif packageEditParam >'6' :
                        print('\nwrong!!!\n')
                        packageEditParam = input('give me the number of param you want to change : ')
                    else:
                        break
                packageEditParamValue= input('give me you param for change : ')
                packageCrud.update(packageEditParam,packageEditParamValue,packageEditNumber)
                packageCrud.save()
                
            elif CrudSelector == '3':
                packageCrud.show()
                DeletePackageNumber = input('witch package you want to delete (if more that one seprate with (,)) : ')
                if type(DeletePackageNumber) is list:
                    packageCrud.delete(DeletePackageNumber)
                else:
                    DeletePackageNumber =DeletePackageNumber.split(',')
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
                    empty_list=[]
                    container = Transportation.Container.create_container(type_,container_number, Maximum_weight, Maximum_package_number, Maximum_speed ,empty_list )
                    containerCrud.add(container)
                    containerCrud.save()
                elif container_type =='2':
                    type_ = "freezer"
                    container_Minimum_temperature = input('Minimum_temperature : ')
                    empty_list=[]
                    container = Transportation.Container.create_container(type_,container_number, Maximum_weight, Maximum_package_number,container_Minimum_temperature,empty_list)
                    containerCrud.add(container)
                    containerCrud.save()
            elif CrudSelector == '2':
                x=containerCrud.show()
                if x == 0:
                    print('\nthere is no containers\n')
                else : 
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
                DeleteContainerNumber = input('witch container you want to delete (if more that one seprate with (,)) : ')
                if type(DeleteContainerNumber) is list:
                    containerCrud.delete(DeleteContainerNumber)
                else:
                    DeleteContainerNumber =DeleteContainerNumber.split(',')
                    containerCrud.delete(DeleteContainerNumber)
                containerCrud.save()
        elif AdminSelector == '3':
            for i in CrudCarsMenu:
                print(i)
            CrudSelector = input('enter you number : ')
            
            if CrudSelector == '1':
                type_ = ""
                for i in Car_type:
                    print(i)
                container_type             = input('enter you number : ')
                car_Maximum_portable_weight= input('car_Maximum_portable_weight :')

                file_name = "./Cars.json"
                try:
                    temp = 0
                    with open(file_name) as f:
                        data = json.load(f)
                        for i in range(len(data)):
                            if data[i-1]['cars_number']>temp:
                                temp = data[i-1]['cars_number']
                        cars_number=temp +1
                except JSONDecodeError:
                    cars_number = 1
                if container_type == '1':
                    empty_list1=[]
                    type_ = "simple"
                    Maximum_portable_weight    = input('Maximum_portable_weight : ')
                    Maximum_portable_number    = input('Maximum_portable_number : ')
                    car = Transportation.Cars.create_car(type_,cars_number, car_Maximum_portable_weight, Maximum_portable_weight, Maximum_portable_number,empty_list1)
                    carCrud.add(car)
                    carCrud.save()
                elif container_type =='2':
                    empty_list1=[]
                    type_ = "container"
                    Maximum_connectable_container = input('Maximum_connectable_container : ')
                    car = Transportation.Cars.create_car(type_,cars_number,car_Maximum_portable_weight, Maximum_connectable_container,empty_list1)
                    carCrud.add(car)
                    carCrud.save()  
            elif CrudSelector == '2':
                x=carCrud.show()
                if x == 0:
                    print('\nthere is no car\n')
                else : 
                    CarEditNumber = int(input('witch car you want to edit(give me your container number) : '))
                    carCrud.target(CarEditNumber)
                    CarEditParam = input('give me the number of param you want to change : ')
                    while(True):
                        if CarEditParam == '1' or CarEditParam=='2' or CarEditParam=='6':
                            print('\nyou cant change car number or car type or car package list list!!! \n')
                            CarEditParam = input('give me the number of param you want to change : ')
                        elif CarEditParam >'6' :
                            print('\nwrong number !!!\n')
                            CarEditParam = input('give me the number of param you want to change : ')
                        else:
                            break
                    CarEditParamValue= input('give me you param for change : ')
                    carCrud.update(CarEditParam,CarEditParamValue,CarEditNumber)
                    carCrud.save()   
            elif CrudSelector == '3':
                carCrud.show()
                DeleteCarNumber = input('witch car you want to delete (if more that one seprate with (,)) : ')
                if type(DeleteCarNumber) is list:
                    carCrud.delete(DeleteCarNumber)
                else:
                    DeleteCarNumber =DeleteCarNumber.split(',')
                    carCrud.delete(DeleteCarNumber)
                carCrud.save()    
        elif AdminSelector =='4':
            while(True):
                for i in LoadingList:
                    print(i)
                LoadingSelector = input('enter the number : ')
                if   LoadingSelector   == '1':
                    packageCrud.show()
                elif LoadingSelector == '2':
                    containerCrud.show()
                elif LoadingSelector == '3':
                    carCrud.show()
                elif LoadingSelector == '4':
                    packages_list = packageCrud.packages
                    containerCrud.show()
                    id = input('give me your container number : ')
                    selected_container = containerCrud.pack(id)
                    compatibles = selected_container.show_compatible(packages_list)
                    for i in compatibles:
                        print(str(i))
                    packages_id = input('give me your packages number and seprate with (,) : ')
                    if type(packages_id) is list:
                        selected_container.package_to_container(compatibles , packages_id)
                        packageCrud.save()
                    else:
                        packages_id =packages_id.split(',')
                        selected_container.package_to_container(compatibles , packages_id)
                        packageCrud.save()
                    containerCrud.save()   
                    break
                elif LoadingSelector == '5':
                    packages_list = packageCrud.packages
                    containers_list = containerCrud.containers
                    carCrud.show()
                    id = input('give me your Car number : ')
                    selected_car = carCrud.pack(id)
                    compatibles = selected_car.show_compatible(containers_list,packages_list)
                    if len(compatibles)<1:
                        print('there is no compatibles PackageList or ContainerList')
                        break
                    else:
                        print(compatibles)
                        if type(compatibles[0]) is Transportation.Package:
                            for i in compatibles:
                                print(str(i))
                            packages_id = input('give me your packages number and seprate with (,) : ')
                            if type(packages_id) is list:
                                selected_car.container_to_car(compatibles , packages_id)
                                packageCrud.save()
                            else:
                                packages_id =packages_id.split(',')
                                selected_car.container_to_car(compatibles , packages_id)
                                packageCrud.save()
                        elif type(compatibles[0]) is Transportation.Breakable_Container or Transportation.Breakable_Packages:
                            for i in compatibles:
                                print(str(i))
                            packages_id = input('give me your container numbers and seprate with (,) : ')
                            if type(packages_id) is list:
                                selected_car.container_to_car(compatibles , packages_id)
                                containerCrud.save()
                            else:
                                packages_id =packages_id.split(',')
                                selected_car.container_to_car(compatibles , packages_id)
                                containerCrud.save()
                        carCrud.save()
                        break
                    
        elif AdminSelector == '5':
            for i in SendReciveMenu:
                print(i)
            input1= input('enter the number  : ')
            if input1 == '1':
                send = carCrud.Ready_car()
                if len(send)>0:
                    for i in send:
                        print(i)
                else:
                    print('there is no Ready cars') 
                    break
            elif input1 == '2':
                packages_list = packageCrud.packages
                containers_list = containerCrud.containers
                car_list = carCrud.cars
                barname.load_barname(car_list,containers_list,packages_list)
                carCrud.save()
                packageCrud.save()
                containerCrud.save()  
            elif input1 == '3':
                send = carCrud.Ready_car()
                if len(send)>0:
                    for i in send:
                        print(i)
                else:
                    print('there is no Ready cars') 
                    break
                send_car_id = input('give me your car number that you want to send and seprate with (,): ')
                if type(send_car_id) is list: 
                    send = carCrud.send(send_car_id)
                else:
                    send_car_id =send_car_id.split(',')
                    send = carCrud.send(send_car_id)
                packages_list = packageCrud.packages
                containers_list = containerCrud.containers
                a,b,c=barname.barname1(send , packages_list,containers_list)
                packageCrud.delete(c)
                packageCrud.delete(b)
                containerCrud.delete(a)
                packageCrud.save()
                containerCrud.save()    
                carCrud.save()
                
        elif AdminSelector == '6':
            sys.exit()
    

    