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
            raise  TypeError("UnexceptType")#别的东西
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
        self.num=num
        self.den=den
    
    #输出数值
    def __float__(self):
        return self.value    
    __call__=__float__
    __int__=lambda self:int(self.value)


    #比较,fromat是为了接纳其他类型      
    __lt__=lambda self,number:self()<fromat(number)()#小于
    __gt__=lambda self,number:self()>fromat(number)()#大于
    __le__=lambda self,number:self()<=fromat(number)()#小于等于
    __ge__=lambda self,number:self()>=fromat(number)()#大于等于
    __eq__=lambda self,number:self()==fromat(number)()#等于
    __ne__=lambda self,number:self()!=fromat(number)()#不等于
            
    
    #四则运算      

    def __add__(self,number):#加
        number=format(number)#格式化，兼容int和float
        num=self.num*number.den+number.num*self.den
        den=self.den*number.den        
        return Fac(num,den)
        
    def __sub__(self,number):#减
        number=format(number)
        num=self.num*number.den-number.num*self.den
        den=self.den*number.den      
        return Fac(num,den)
     
    def __mul__(self,number):#乘
        number=format(number)
        num=self.num*number.num      
        den=self.den*number.den   
        return Fac(num,den)
   
    def __truediv__(self,number):#除
        number=format(number)
        num=self.num*number.den     
        den=self.den*number.num   
        return Fac(num,den)
        
    __div__=__floordiv__=__truediv__#n种除法    
    #反运算
    __radd__=__add__
    __rmul__=__mul__
    __rsub__=lambda self,number:fromat(number)-self

    __rtruediv__=lambda self,number:fromat(number)/self
    __rdiv__=__rfloordiv__=__rtruediv__#n种除法

     
    
    #迭代器
    
    def __iter__(self):
        self.iternum=self.num    
        b=int(self.num//self.den)       
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
    