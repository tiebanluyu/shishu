from collections import namedtuple
import logging,math
Radical=namedtuple("Radical",["rute","indexoftheroot"])
class Surd():
    def __init__(self,*args):
        self.data:dict
        self.confficient:int
        #logging.error(args)
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
            if not (i in sd.keys()):
                data[i]=sd[i]
                
        for key,value in data.items():
            temp=decompose(value,key)
            #print(temp)
            confficient=temp*confficient
            data[key]=data[key]/(temp**key)
        for key,value in list(data.items()):
            
            if math.isclose(value,1.0):
                del data[key]
        data[1]=confficient
        return Surd(data)        







class Polymerization:
    pass




