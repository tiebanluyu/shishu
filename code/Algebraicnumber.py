


#import something 导入东西
from collections import namedtuple
import logging
from math import isclose

class frozendict(dict):#冻结字典，MappingProxyType很难用，不可哈希的
    """make dictionary hashable and immuntable

    """
    #from types import MappingProxyType
    def __hash__(self):
        return hash(str(self))
    def nonefunc(*args,**kws):
        """clean the function"""
        return None
    __clear__=__delitem__=__pop__=__setitem__=nonefunc


Radical=namedtuple("Radical",["rute","indexoftheroot"])
class Surd():#单项式
    def __init__(self,*args):
        self.data:dict
        self.confficient:int
        
        if type(args[0])==dict:
            
            data=args[0].copy()
        else:
            data={}
            for value,key in args:
                data[key]=value
        if 1 in list(data):
            self.confficient=data[1]
            del data[1]
        else:
            self.confficient=1
        self.data=frozendict(data)
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
            
            if isclose(value,1.0):
                del data[key]
        data[1]=confficient
        return Surd(data)        
    def __repr__(self):
        return str((self.data,self.confficient))

    def __hash__(self):
        return hash(self.data)*hash(self.confficient)




class Polymerization:#多项式
    def __init__(self,*args):
        data={}
        if type(args[0])==dict:
           self.data=args[0]
           for i in self.data.copy():
               if type(i)==Surd:
                   j=self.data[i]
                   del self.data[i]
                   self.data[i.data]=i.confficient*j
           return
        for i in args:
            data[i.data]=i.confficient
        self.data=frozendict(data)    
    def __add__(self,others):
        sd=self.data
        od=self.data
        data={}
        for key,value in sd.items():
            if data.get(key) is None:
                data[key]=value
            else:
                data[key]=data[key]+value
        for key,value in od.items():
            if data.get(key) is None:
                data[key]=value
            else:
                data[key]=data[key]+value
        return Polymerization(data)
    def __sub__(self,others):
        sd=self.data
        od=self.data
        data={}
        for key,value in sd.items():
            if data.get(key) is None:
                data[key]=value*(-1)
            else:
                data[key]=data[key]-value
        for key,value in od.items():
            if data.get(key) is None:
                data[key]=value*(-1)
            else:
                data[key]=data[key]-value
        return Polymerization(data)
    def __mul__(self,others):
        data=Polymerization({})
        for key1,value1 in self.data.items():
            i=Surd(dict(key1))*Surd({1:value1})
            for key2,value2 in others.data.items():
                j=Surd(dict(key1))*Surd({1:value2})
                data=data+Polymerization(i*j)
        return data         
                
            
        
    
    
        
        



