﻿class fenshu:
    def __init__(self,zi=0,mu=1):
        if str(type(zi))==str(type(0.1)):#float
            self.zi=zi*(10**15)
            self.mu=(10**15)                    
        elif str(type(zi))==str(type(1)):#int
            self.zi=zi
            self.mu=mu
        else:
            raise Exception("输入错误")
        self.yuefen()    
    def zhi(self):#计算
        if self.zi==0:
            self.mu=1
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
        if self.zi==0:
            self.mu=1
            return
        zi=self.zi
        mu=self.mu
        yue=zuidagongyueshu(zi,mu)
        zi=zi/yue
        mu=mu/yue
        #print(1,zi,mu)
        self.zi=int(zi)
        self.mu=int(mu)
    
    #输出数值
    def __float__(self):
        return self.zhi()    
    value=__call__=__float__ #多方法
    
    #比较
    def __lt__(self,shu):
        return self()<shu()
    def __gt__(self,shu):
        return self()>shu()  
    def __eq__(self,shu):
        return self()==shu() 
    def __ne__(self,shu):
        return self()!=shu()     
    
    #四则运算
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
     
    def __mul__(self,shu):#乘
        zi=self.zi*shu.zi      
        mu=self.mu*shu.mu
        a=fenshu(zi,mu)
        a.yuefen()
        return a
    def __truediv__(self,shu):#除
        zi=self.zi*shu.mu     
        mu=self.mu*shu.zi
        a=fenshu(zi,mu)
        a.yuefen()
        return a
        
    __div__=__floordiv__=__truediv__    
    #文本化
    def __str__(self):
        return f"({self.zi}/{self.mu})"
    __repr__=__str__    
    
    #转换成列表
    def list(self,chang=100):
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
    #文本化
    def __str__(self):
        return f"({self.zi}/{self.mu})"
    __repr__=__str__    
    
    #转换成列表
    def list(self,chang=100):
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
if __name__=="__main__":
    
    a=fenshu(100)
    b=fenshu(144)

    print(...)
