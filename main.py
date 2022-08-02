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
def fromat(shu):
        if isin(shu,Fac):#分数
            return shu                   
        elif isin(shu,int) or isin(shu,float):
            return Fac(shu)
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
    __lt__=lambda self,shu:self()<shu()#小于
    __gt__=lambda self,shu:self()>shu()#大于
    __le__=lambda self,shu:self()<=shu()#小于等于
    __ge__=lambda self,shu:self()>=shu()#大于等于
    __eq__=lambda self,shu:self()==shu()#等于
    __ne__=lambda self,shu:self()!=shu()#不等于
            
    
    #四则运算      

    def __add__(self,shu):#加
        shu=fromat(shu)#格式化，兼容int和float
        num=self.num*shu.den+shu.num*self.den
        den=self.den*shu.den    
        a=Fac(num,den)     
        return a
        
    def __sub__(self,shu):#减
        shu=fromat(shu)#兼容
        num=self.num*shu.den-shu.num*self.den
        den=self.den*shu.den
        a=Fac(num,den)      
        return a
     
    def __mul__(self,shu):#乘
        shu=fromat(shu)#兼容
        num=self.num*shu.num      
        den=self.den*shu.den
        a=Fac(num,den)   
        return a
   
    def __truediv__(self,shu):#除
        shu=fromat(shu)#兼容
        num=self.num*shu.den     
        den=self.den*shu.num
        a=Fac(num,den)#       
        return a
        
    __div__=__floordiv__=__truediv__#n种除法    
     
    
    #迭代器
    
    def __iter__(self):
        self.iternum=self.num    
        b=int(self())       
        self.iternum-=self.den*b
        self.iterb=b
        self.iterjishu=1
        return self
    def __next__(self):
        if self.iterjishu==1:
            self.iterjishu=0
            return self.iterb            
        self.iternum=self.iternum*10000
        b=int(self.iternum/self.den)
        self.iternum=self.iternum-self.den*b
            
        return b
    #转换成列表
    def list(self,chang=100):
        self.__iter__()
        list1=[]
        for linshi in range(int(chang/4)):
            list1.append(self.__next__())
        return list1   
            
    
    #文本化    
    __repr__=__str__=lambda self:f"Fac({self.num}/{self.den})"
    __hash__=lambda self:hash((self.num,self.den))	  
    
#实数             
class AlgNum:
    
    def __init__(self,shu=0,dishu=1):      
        if  isin(shu,AlgNum):#实数格式
            self.xinxi=deepcopy(shu.xinxi)
            return
        elif isin(shu,dict):#dict格式
            self.xinxi=shu
            return    
        else:
            shu=fromat(shu)#int float 分数
            self.xinxi={}
            self.xinxi[dishu]=shu
        a=self.huajian()
        self.xinxi.clear()       
        for i in a:
            self.xinxi[i]=a[i]
                
    
    def jiashu(self,shu,beikaifangshu=1):#添加一个数
        if not self.xinxi.get(beikaifangshu) is None:#已存在，get方法存在则返回切片值，否则返回None
            self.xinxi[beikaifangshu]+=fromat(shu)
        else:                                        #不存在
            self.xinxi[beikaifangshu]=fromat(shu)
    #四则运算（除法有bug）
    
    #加法    
    def __add__(self,shu):
        linshi=AlgNum(self)
        if isin(shu,AlgNum):#实数格式
            for i in shu.xinxi:
                linshi.jiashu(shu.xinxi[i],i)
                
        else:#分数，小数
            shu=fromat(shu)    
            linshi.jiashu(shu)
        return linshi
    
    #减法    
    def __sub__(self,shu):
        linshi=AlgNum(self)#复制一份       
        if isin(shu,AlgNum):#实数格式
            for i in shu.xinxi:
                linshi.jiashu(shu.xinxi[i]*(-1),i)        
        else:#分数，小数
            shu=fromat(shu*(-1))    
            linshi.jiashu(shu)
        return linshi
    
    def huajian(self):#化简
        def fenjie(a):
            b=1
            c=1
            while c**2<a:
                c+=1                
                if a%(c**2)==0:
                    b=c
            return b
            
        copy0={}
        for linshi in self.xinxi:
            linshi2=linshi
            linshi3=self.xinxi[linshi2]
            linshi4=fenjie(linshi)
            linshi2=linshi2//(linshi4**2)
            linshi3=linshi3*linshi4           
            if  copy0.get(linshi2) is None:
                copy0[linshi2]=fromat(linshi3)                
            else:
                copy0[linshi2]+=fromat(linshi3)
        copy1=dict(copy0)
        for linshi in copy0:
            
            
            if copy0[linshi].num==0:
                del copy1[linshi]
        return copy1          
       
    def __mul__(self,shu):#乘法
        linshi=AlgNum()
        xinxi1=self.xinxi
        xinxi2=shu.xinxi
        for jia in xinxi1:
            for yi in xinxi2:
                linshi.jiashu(xinxi1[jia]*xinxi2[yi],beikaifangshu=jia*yi)          
        return AlgNum(linshi.huajian())       
    def __truediv__(self,shu):#除法有BUG
        if len(list(shu))>4:
            raise Exception("理论问题，除数项数不得大于4")
        a=self
        b=shu    
        if (b.xinxi.get(1) is None):
            a=a*b
            b=b*b        
        while not (len(b.xinxi)==1):           
            d=b.xinxi.copy()
            d[1]=d[1]*-1
            c=AlgNum(d)              
            a=a*c
            b=b*c    
        c=AlgNum(a)        
        for i in a.xinxi:
            c.xinxi[i]=a.xinxi[i]/b.xinxi[1]    
        return c    
    
    #文本化    
    __str__=(lambda self : "AlgNum"+str(self.xinxi).
    	                replace("{","[").replace("}","]") ) 
    __repr__=(lambda self : "AlgNum("+str(self.xinxi)+")")