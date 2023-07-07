import json
import os
from Transportation import Transportation
from json.decoder import JSONDecodeError
from json.decoder import JSONDecodeError
class barname():
    def __init__(self):
        self.barname = []
        
        
    #loading barnameh
    def load_barname(self , car_list , containers_list , packages_list):
        
        file_name = "./barname.json"
        json_list=[]
        try:
            with open(file_name) as f:
                data = json.load(f)
                q=[]
                q.append(data[0]['container_list']['container_number'])
                w=[]
                # wthis is for make packages(object) from barnameh
                for i in data:
                    if i["CarType"] == 'container':
                        if i['container_list']['load_package_list']['package_type'] == 'breakable':
                            packages_list.append(Transportation.Package.create_package(i['container_list']['load_package_list']['package_type'],i['container_list']['load_package_list']['package_number'],i['container_list']['load_package_list']['weight'], i['container_list']['load_package_list']['destination'], i['container_list']['load_package_list']['origin']))
                        elif i['container_list']['load_package_list']['package_type'] == 'cold':
                            packages_list.append(Transportation.Package.create_package(i['container_list']['load_package_list']['package_type'],i['container_list']['load_package_list']['package_number'],i['container_list']['load_package_list']['weight'], i['container_list']['load_package_list']['destination'], i['container_list']['load_package_list']['origin'] , i['container_list']['load_package_list']['Minimum_temperature']))
                    elif i["CarType"] == 'simple':
                        if i['package_list']['package_type'] =='Default':
                            packages_list.append(Transportation.Package.create_package(i['package_list']['package_type'],i['package_list']['package_number'],i['package_list']['weight'], i['package_list']['destination'], i['package_list']['origin']))
                
                
                #this is for make container(object) from barnameh  
                for i in data :
                    if i["CarType"] == 'container':
                        if int((i['container_list']['container_number'])) in q:
                            temp = w
                            w=[]
                            w.append(i['container_list']['load_package_lists'])
                            if temp == w:
                                pass
                            else:
                                if i['container_list']['ContainerType'] == 'breakable':
                                    containers_list.append(Transportation.Container.create_container(i['container_list']['ContainerType'],q[0],i['container_list']['Maximum_weight'], i['container_list']['Maximum_package_number'], i['container_list']['Maximum_speed'],w))
                                elif i['container_list']['ContainerType'] == 'freezer':
                                    containers_list.append(Transportation.Container.create_container(i['container_list']['ContainerType'],q[0],i['container_list']['Maximum_weight'], i['container_list']['Maximum_package_number'], i['container_list']['container_Minimum_temperature'],w))
                        
                        else:
                            q=[]
                            q.append(i['container_list']['container_number'])
                    elif i["CarType"] == 'simple':
                        pass      
                q=[]
                w=[]
                q.append(data[0]['cars_number'])        
                for i in data:
                    if i["CarType"] == 'container':
                        if int((i['cars_number'])) in q:
                            temp = w
                            w=[]
                            w.append(i['container_lists'])
                            if temp ==w:
                                pass
                            else:
                                if i['CarType'] == 'container':
                                    car_list.append(Transportation.Cars.create_car(i['CarType'],q[0],i['car_Maximum_portable_weight'] ,i['Maximum_connectable_container'],w ))
                        else:
                            q=[]
                            q.append(i['cars_number'])
                    elif i["CarType"] == 'simple':
                        if int((i['cars_number'])) in q:
                            temp = w
                            w=[]
                            w.append(i['package_lists'])
                            if temp ==w:
                                pass
                            else:
                                if i["CarType"] == 'simple':
                                    print(i)
                                    car_list.append(Transportation.Cars.create_car(i['CarType'],q[0],i['car_Maximum_portable_weight'] ,i['Maximum_portable_weight'], i['Maximum_portable_number'],w))
                        else:
                            q=[]
                            q.append(i['cars_number'])
                                
        except JSONDecodeError:
            print('-------\nthere is no barnameh\n-------')
    #making barnameh        
    def barname1(self , send , package_list , container_list):
        print(send)
        file_name = "./barname.json"
        a=[]
        b=[]
        c=[]
        json_list=[]
        with open(file_name) as f:
            for i in send:
                if type(i) is Transportation.Simple_Cars:
                    d={
                        "cars_number": i.cars_number,
                        "car_Maximum_portable_weight": i.car_Maximum_portable_weight,
                        "Maximum_portable_weight": i.Maximum_portable_weight,
                        "CarType" : i.CarType,
                        'Maximum_portable_number':i.Maximum_portable_number,
                        "package_lists" : i.package_list,
                        }
                    print('im here now')
                    for j in i.package_list:
                        for k in package_list:
                            print('this is here')
                            if j==k.package_number:
                                d['package_list']={"package_number": k.package_number,
                                                   "weight": k.weight,
                                                   "destination": k.destination,
                                                   "origin" : k.origin,
                                                   "package_type" : k.PackageType,
                                                   }
                                c.append(j)
                                print('im here')
                                json_list.append(d)
                                try:
                                    with open(file_name) as f:
                                        listObj = json.load(f)
                                        listObj.append(d)
                                        with open(file_name, 'w') as f:
                                            json.dump(listObj, f, indent=4)
                                except JSONDecodeError:
                                    with open(file_name, 'a') as f:
                                        json.dump(json_list, f, indent=4)
                elif type(i) is Transportation.Container_Cars:
                    d={
                        "cars_number": i.cars_number,
                        "car_Maximum_portable_weight": i.car_Maximum_portable_weight,
                        "Maximum_connectable_container": i.Maximum_connectable_container,
                        "CarType" : i.CarType,
                        "container_lists" : i.container_list,
                        }
                    for j in i.container_list:
                        for k in container_list:
                            if j==k.container_number:
                                a.append(j)
                                if type(k) is Transportation.Breakable_Container:
                                    d['container_list']={"container_number": k.container_number,
                                                        "Maximum_weight": k.Maximum_weight,
                                                        "Maximum_package_number": k.Maximum_package_number,
                                                        "ContainerType"     : k.ContainerType,
                                                        'Maximum_speed'     :k.Maximum_speed,
                                                        "load_package_lists" : k.load_package_list,
                                                        }
                                    for q in k.load_package_list:
                                        for w in package_list:
                                            if q == w.package_number:
                                                b.append(q)
                                                d['container_list']['load_package_list']={"package_number": w.package_number,
                                                                                          "weight": w.weight,
                                                                                          "destination": w.destination,
                                                                                          "origin" : w.origin,
                                                                                          "package_type" : w.PackageType,
                                                                                          }
                                                
                                                json_list.append(d)
                                                try:
                                                    with open(file_name) as f:
                                                        listObj = json.load(f)
                                                        listObj.append(d)
                                                        with open(file_name, 'w') as f:
                                                            json.dump(listObj, f, indent=4)
                                                except JSONDecodeError:
                                                    with open(file_name, 'a') as f:
                                                        json.dump(json_list, f, indent=4)    
                                elif type(k) is Transportation.FreezerـContainer:
                                    d['container_list']={"container_number": k.container_number,
                                                         "Maximum_weight": k.Maximum_weight,
                                                         "Maximum_package_number": k.Maximum_package_number,
                                                         "ContainerType"     : k.ContainerType,
                                                         'container_Minimum_temperature':k.container_Minimum_temperature,
                                                         "load_package_lists" : k.load_package_list,
                                                         }
                                    for q in k.load_package_list:
                                        for w in package_list:
                                            if q == w.package_number:
                                                b.append(q)
                                                d['container_list']['load_package_list']={"package_number": w.package_number,
                                                                                          "weight": w.weight,
                                                                                          "destination": w.destination,
                                                                                          "origin" : w.origin,
                                                                                          "package_type" : w.PackageType,
                                                                                          'Minimum_temperature':w.Minimum_temperature,
                                                                                          }
                                                json_list.append(d)
                                                try:
                                                    with open(file_name) as f:
                                                        listObj = json.load(f)
                                                        listObj.append(d)
                                                        with open(file_name, 'w') as f:
                                                            json.dump(listObj, f, indent=4)
                                                except JSONDecodeError:
                                                    with open(file_name, 'a') as f:
                                                        json.dump(json_list, f, indent=4)
            return a,b,c                                           
    