class fenshu:
    def __init__(self,zi,mu=1):
        if str(type(zi))==str(type(0.1)):#float
            self.zi=zi*(10**9)
            self.mu=mu*(10**9)                    
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
            return a
        zi=self.zi
        mu=self.mu
        yue=zuidagongyueshu(zi,mu)
        zi=zi/yue
        mu=mu/yue
        
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
    def __str__(self):
        return f"({self.zi}/{self.mu})"
    __repr__=__str__    
         
    








#测试
a=fenshu(435272) 
a.yuefen()
b=a*a
b=b-a
print(b)
print(b.zi,b.mu)  



