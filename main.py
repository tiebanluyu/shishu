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
#将各种格式转为分数
def format(number):
        if isin(number,Fac):#分数
            return number                   
        elif isin(number,int) or isin(number,float):
            return Fac(number)
        else: 
            raise Exception("输入错误") 

#分数模块
class Fac:
    def __init__(self,num=0,den=1):#初始化        
        if isin(num,float):#float格式
            self.num=num*(10**15)
            self.den=(10**15)                    
        elif isin(num,int):#int格式
            self.num=num
            self.den=den
        else:
            raise Exception("输入错误,暂不支持文本")#别的东西
        self.divide()    
        
    @property #将方法访问转换成属性访问
    def value(self):#计算
        if self.num==0:
            self.den=1
            return 0
        else:
            return self.num/self.den 
    
    
            
                   
    def divide(self):#约分
        def GCD(a,b):
            #最大公约数之辗转相除法
            c=1
            while not c==0:
                c=a%b
                a=b
                b=c               
            return a
        if self.num==0:#万一分子是零
            self.den=1
            return
        num=self.num
        den=self.den
        yue=GCD(num,den)
        num=num//yue
        den=den//yue      
        self.num=int(num)
        self.den=int(den)
    
    #输出数值
    def __float__(self):
        return self.value    
    __call__=__float__
    __int__=lambda self:int(self.value)


    #比较      
    __lt__=lambda self,number:self()<number()#小于
    __gt__=lambda self,number:self()>number()#大于
    __le__=lambda self,number:self()<=number()#小于等于
    __ge__=lambda self,number:self()>=number()#大于等于
    __eq__=lambda self,number:self()==number()#等于
    __ne__=lambda self,number:self()!=number()#不等于
            
    
    #四则运算      

    def __add__(self,number):#加
        number=format(number)#格式化，兼容int和float
        num=self.num*number.den+number.num*self.den
        den=self.den*number.den    
        a=Fac(num,den)     
        return a
        
    def __sub__(self,number):#减
        number=format(number)#兼容
        num=self.num*number.den-number.num*self.den
        den=self.den*number.den
        a=Fac(num,den)      
        return a
     
    def __mul__(self,number):#乘
        number=format(number)#兼容
        num=self.num*number.num      
        den=self.den*number.den
        a=Fac(num,den)   
        return a
   
    def __truediv__(self,number):#除
        number=format(number)#兼容
        num=self.num*number.den     
        den=self.den*number.num
        a=Fac(num,den)#       
        return a
        
    __div__=__floordiv__=__truediv__#n种除法    
     
    
    #迭代器
    
    def __iter__(self):
        self.iternum=self.num    
        b=int(self())       
        self.iternum-=self.den*b
        self.iterb=b
        self.itercount=1
        return self
    def __next__(self):
        if self.itercount==1:
            self.itercount=0
            return self.iterb            
        self.iternum=self.iternum*10000
        b=int(self.iternum/self.den)
        self.iternum=self.iternum-self.den*b
            
        return b
    #转换成列表
    def list(self,length=100):
        self.__iter__()
        list1=[]
        for temp in range(int(length/4)):
            list1.append(self.__next__())
        return list1   
            
    
    #文本化    
    __repr__=__str__=lambda self:f"Fac({self.num}/{self.den})"
    __hash__=lambda self:hash((self.num,self.den))	  
    
#实数             
class AlgNum:
    
    def __init__(self,number=0,dishu=1):      
        if  isin(number,AlgNum):#实数格式
            self.imformation=deepcopy(number.imformation)
            return
        elif isin(number,dict):#dict格式
            self.imformation=number
            return    
        else:
            number=format(number)#int float 分数
            self.imformation={}
            self.imformation[dishu]=number
        a=self.simplifications()
        self.imformation.clear()       
        for i in a:
            self.imformation[i]=a[i]
                
    
    def jiashu(self,number,beikaifangshu=1):#添加一个数
        if not self.imformation.get(beikaifangshu) is None:#已存在，get方法存在则返回切片值，否则返回None
            self.imformation[beikaifangshu]+=format(number)
        else:                                        #不存在
            self.imformation[beikaifangshu]=format(number)
    #四则运算（除法有bug）
    
    #加法    
    def __add__(self,number):
        temp=AlgNum(self)
        if isin(number,AlgNum):#实数格式
            for i in number.imformation:
                temp.jiashu(number.imformation[i],i)
                
        else:#分数，小数
            number=format(number)    
            temp.jiashu(number)
        return temp
    
    #减法    
    def __sub__(self,number):
        temp=AlgNum(self)#复制一份       
        if isin(number,AlgNum):#实数格式
            for i in number.imformation:
                temp.jiashu(number.imformation[i]*(-1),i)        
        else:#分数，小数
            number=format(number*(-1))    
            temp.jiashu(number)
        return temp
    
    def simplifications(self):#化简
        def fenjie(a):
            b=1
            c=1
            while c**2<a:
                c+=1                
                if a%(c**2)==0:
                    b=c
            return b
            
        copy0={}
        for temp in self.imformation:
            temp2=temp
            temp3=self.imformation[temp2]
            temp4=fenjie(temp)
            temp2=temp2//(temp4**2)
            temp3=temp3*temp4           
            if  copy0.get(temp2) is None:
                copy0[temp2]=format(temp3)                
            else:
                copy0[temp2]+=format(temp3)
        copy1=dict(copy0)
        for temp in copy0:
            
            
            if copy0[temp].num==0:
                del copy1[temp]
        return copy1          
       
    def __mul__(self,number):#乘法
        temp=AlgNum()
        imformation1=self.imformation
        imformation2=number.imformation
        for jia in imformation1:
            for yi in imformation2:
                temp.jiashu(imformation1[jia]*imformation2[yi],beikaifangshu=jia*yi)          
        return AlgNum(temp.simplifications())       
    def __truediv__(self,number):#除法有BUG
        if len(list(number))>4:
            raise Exception("理论问题，除数项数不得大于4")
        a=self
        b=number    
        if (b.imformation.get(1) is None):
            a=a*b
            b=b*b        
        while not (len(b.imformation)==1):           
            d=b.imformation.copy()
            d[1]=d[1]*-1
            c=AlgNum(d)              
            a=a*c
            b=b*c    
        c=AlgNum(a)        
        for i in a.imformation:
            c.imformation[i]=a.imformation[i]/b.imformation[1]    
        return c    
    
    #文本化    
    __str__=(lambda self : "AlgNum"+str(self.imformation).
    	                replace("{","[").replace("}","]") ) 
    __repr__=(lambda self : "AlgNum("+str(self.imformation)+")")