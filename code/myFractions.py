#����ģ��
class Fac:
    def __init__(self,num=0,den=1):#��ʼ��        
        if isin(num,float):#float��ʽ
            self.num=num*(10**15)
            self.den=(10**15)                    
        elif isin(num,int):#int��ʽ
            self.num=num
            self.den=den
        else:
            raise  TypeError("UnexceptType")#��Ķ���
        self.divide()    
        
    @property #����������ת�������Է���
    def value(self):#����
        if self.num==0:
            self.den=1
            return 0
        else:
            return self.num/self.den 
    
    
            
                   
    def divide(self):#Լ��
        def GCD(a,b):
            #���Լ��֮շת�����
            c=1
            while not c==0:
                c=a%b
                a=b
                b=c               
            return a
        if self.num==0:#��һ��������
            self.den=1
            return
        num=self.num
        den=self.den
        yue=GCD(num,den)
        num=num//yue
        den=den//yue      
        self.num=num
        self.den=den
    
    #�����ֵ
    def __float__(self):
        return self.value    
    __call__=__float__
    __int__=lambda self:int(self.value)


    #�Ƚ�,fromat��Ϊ�˽�����������      
    __lt__=lambda self,number:self()<fromat(number)()#С��
    __gt__=lambda self,number:self()>fromat(number)()#����
    __le__=lambda self,number:self()<=fromat(number)()#С�ڵ���
    __ge__=lambda self,number:self()>=fromat(number)()#���ڵ���
    __eq__=lambda self,number:self()==fromat(number)()#����
    __ne__=lambda self,number:self()!=fromat(number)()#������
            
    
    #��������      

    def __add__(self,number):#��
        number=format(number)#��ʽ��������int��float
        num=self.num*number.den+number.num*self.den
        den=self.den*number.den        
        return Fac(num,den)
        
    def __sub__(self,number):#��
        number=format(number)
        num=self.num*number.den-number.num*self.den
        den=self.den*number.den      
        return Fac(num,den)
     
    def __mul__(self,number):#��
        number=format(number)
        num=self.num*number.num      
        den=self.den*number.den   
        return Fac(num,den)
   
    def __truediv__(self,number):#��
        number=format(number)
        num=self.num*number.den     
        den=self.den*number.num   
        return Fac(num,den)
        
    __div__=__floordiv__=__truediv__#n�ֳ���    
    #������
    __radd__=__add__
    __rmul__=__mul__
    __rsub__=lambda self,number:fromat(number)-self

    __rtruediv__=lambda self,number:fromat(number)/self
    __rdiv__=__rfloordiv__=__rtruediv__#n�ֳ���

     
    
    #������
    
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
    #ת�����б�
    def list(self,length=100):
        self.__iter__()
        list1=[]
        for temp in range(int(length/4)):
            list1.append(self.__next__())
        return list1   
            
    
    #�ı���    
    __repr__=__str__=lambda self:f"Fac({self.num}/{self.den})"
    __hash__=lambda self:hash((self.num,self.den))	  
    