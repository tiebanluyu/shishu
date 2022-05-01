class fenshu:
    def __init__(self,zi,mu=1):
        if str(type(zi))==str(type(0.1)):#float
            self.zi=zi*(10**9)
            self.mu=(10**9)                    
        elif str(type(zi))==str(type(1)):#int
            self.zi=zi
            self.mu=mu
        else:
            raise Exception("输入错误")
        self.yuefen()    
    def zhi(self):#计算
        if self.zi==0:
            self.mu=0
            return 0
        else:
            return self.zi/self.mu        
    def yuefen(self):#约分
        def zuidagongyueshu(a,b):#最大公约数之辗转相除法
            c=1
            while not c==0:
                c=a%b
                a=b
                b=c
                #print(1232)
            return a
        zi=self.zi
        mu=self.mu
        yue=zuidagongyueshu(zi,mu)
        zi=zi/yue
        mu=mu/yue
        #print(1,zi,mu)
        self.zi=int(zi)
        self.mu=int(mu)
    def __add__(self,shu):#加
        zi=self.zi*shu.mu+shu.zi*self.mu
        mu=self.mu*shu.mu
        
        a=fenshu(zi,mu)
        a.yuefen()
        return a
        
    def __sub__(self,shu):#减
        zi=self.zi*shu.mu-shu.zi*self.mu
        mu=self.mu*shu.mu
        a=fenshu(zi,mu)
        a.yuefen()
        return a
    def __eq__(self):
        return self.zhi()    
    
    __call__=__float__=__eq__  #多方法 
    def __mul__(self,shu):#乘
        zi=self.zi*shu.zi      
        mu=self.mu*shu.mu
        a=fenshu(zi,mu)
        a.yuefen()
        return a
    def __div__(self,shu):#除
        zi=self.zi*shu.mu     
        mu=self.mu*shu.zi
        a=fenshu(zi,mu)
        a.yuefen()
        return a   
    def __str__(self):#文本化
        return f"({self.zi}/{self.mu})"
    __repr__=__str__    
    def list(self,chang):
        zi=self.zi
        mu=self.mu
        a=list()
        chang=int(chang/4)*4
        b=int(self())#整数
        a.append(b)
        zi-=mu*b
        for i in range(chang//4):
            zi=zi*10000
            b=int(zi/mu)
            zi=zi-mu*b
            
            a.append(b)
            #
        return a    


         
    








#测试
a=fenshu(1123456789009876554465465334,1346879832412343134645243348) 
a.yuefen()
print(a)
print(a.list(2000))

"""
b=a*a
b=b+a
print(a())
#print(b.zi,b.mu)  
"""


