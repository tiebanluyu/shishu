from collections import namedtuple
Radical=namedtuple("Radical",["rute","indexoftheroot"])
class Surd():
    def __init__(self,*args):
        self.data:dict
        self.confficient:int
        if type(args[0])==dict:
            self.data=args[0].copy()
        else:
            self.data={}
            for value,key in args:
                self.data[key]=value
        if 1 in list(self.data):
            self.confficient=self.data[1]
            del self.data[1]
        else:
            self.confficient=1

    def __mul__(self,others):
        def decompose(a,index):
            b=1
            c=1
            while c**index<a:
                c+=1                
                if a%(c**index)==0:
                    b=c
            print(b)        
            return b
        data={}
        confficient=self.confficient*others.confficient
        sd=self.data
        od=others.data
        for i in sd:
            if i in od.keys():
                data[i]=sd[i]*od[i]
            else:
                data[i]=sd[i]
        for i in od:
            if i in sd.keys():
                data[i]=sd[i]
        for key,value in data.items():
            temp=decompose(value,key)
            confficient*=temp
            data[key]=data[key]/(temp**key)
            
            





                
        data[1]=confficient
        return Surd(data)        







class Polymerization:
    pass




