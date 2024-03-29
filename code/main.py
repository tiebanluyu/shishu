"""
Copyright (c) 2022 铁板烤鲈鱼
shishu is licensed under Mulan PSL v2.
You can use this software according to the terms and conditions of the Mulan PSL v2.
You may obtain a copy of Mulan PSL v2 at:
         http://license.coscl.org.cn/MulanPSL2
THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
See the Mulan PSL v2 for more details.
"""
#导入deepcopy
from copy import deepcopy
#方便对格式进行比较
isin=isinstance
from fractions import Fraction 

#实数             
class AlgNum:
    
    def __init__(self,number:any=0,base:int=1):      
        if  isin(number,AlgNum):#实数格式
            self.__data=deepcopy(number.__data)
            return
        elif isin(number,dict):#dict格式
            self.__data=number
            return    
        else:
            number=format(number)#其他
            self.__data={}
            self.__data[base]=number
        a=self.simplifications()
        self.__data.clear()       
        for i in a:
            self.__data[i]=a[i]
                
    
    def toadd(self,number,root=1):#添加一个数
        if self.__data.get(root) is None:#已存在，get方法存在则返回切片值，否则返回None
            self.__data[root]=format(number)
        else:                                        #不存在
            self.__data[root]+=format(number)
    
    #四则运算
    
    #加法    
    def __add__(self,number):
        temp=AlgNum(self)
        if isin(number,AlgNum):#实数格式
            for i in number.__data:
                temp.toadd(number.__data[i],i)
                
        else:#分数，小数
            number=format(number)    
            temp.toadd(number)
        return temp
    
    #减法    
    def __sub__(self,number):
        temp=AlgNum(self)#复制一份       
        if isin(number,AlgNum):#实数格式
            for i in number.__data:
                temp.toadd(number.__data[i]*(-1),i)        
        else:#分数，小数
            number=format(number*(-1))    
            temp.toadd(number)
        return temp
    
    def simplifications(self):#化简，暂时不动
        def decompose(a):
            b=1
            c=1
            while c**2<a:
                c+=1                
                if a%(c**2)==0:
                    b=c
            return b
            
        copy0={}
        for temp in self.__data:
            temp2=temp
            temp3=self.__data[temp2]
            temp4=decompose(temp)
            temp2=temp2//(temp4**2)
            temp3=temp3*temp4           
            if  copy0.get(temp2) is None:
                copy0[temp2]=format(temp3)                
            else:
                copy0[temp2]+=format(temp3)
        copy1=dict(copy0)
        for temp in copy0:
            if copy0[temp].numerator==0:####
                del copy1[temp]
        return copy1          
       
    def __mul__(self,number):#乘法
        temp=AlgNum()
        data1=self.__data
        data2=number.__data
        for jia in data1:
            for yi in data2:
                temp.toadd(data1[jia]*data2[yi],root=jia*yi)          
        return AlgNum(temp.simplifications()) 

    def __truediv__(self,number):#除法
        if len(list(number.__data))>=4:
            raise Exception("理论问题，除数项数不得大于3")
        a=self
        b=number    
        if (b.__data.get(1) is None):
            a=a*b
            b=b*b            
        while not (len(b.__data)==1):                     
            d=b.__data.copy()
            d[1]=d[1]*-1
            c=AlgNum(d)              
            a=a*c
            b=b*c
                
        c=AlgNum(a)        
        for i in a.__data:
            c.__data[i]=a.__data[i]/b.__data[1]    
        return c    
    
    #反运算
    __radd__=lambda self,number:AlgNum(number)+self#加

    __rmul__=lambda self,number:AlgNum(number)*self#乘

    __rsub__=lambda self,number:AlgNum(number)-self#减

    __rtruediv__=lambda self,number:AlgNum(number)/self#除

    __rdiv__=__rfloordiv__=__rtruediv__#n种除法
    
    #文本化    
    __str__=(lambda self : "AlgNum"+str(self.__data).
    	                replace("{","[").replace("}","]") ) 
    __repr__=(lambda self : "AlgNum("+str(self.__data)+")")

    @property
    def data(self):
        return self.__data

#将各种格式转为分数
def format(number):
    return Fraction(number)
    
def sqrt(num):
    """开平方

       可以这么写
        a=1*sqrt(13)+2*sqrt(5)
        方便人工生成
     """
    return AlgNum(number=1,base=num)


