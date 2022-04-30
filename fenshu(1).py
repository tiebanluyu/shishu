class fenshu:
    def __init__(self,zi,mu=1):
        if str(type(zi))==str(type(0.1)):
            self.zi=zi*(10**9)
            self.mu=mu*(10**9)
            self.yuefen()
            
        
        
        else:
            self.zi=zi
            self.mu=mu
    def zhi(self):
        if self.zi==0:
            return 0
        else:
            return self.zi/self.mu        
    def yuefen(self):
        def zuidagongyueshu(a,b):
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
    def __add__(self,shu):
        zi=self.zi*shu.mu+shu.zi*self.mu
        mu=self.mu*shu.mu
        #print(1273635)
        a=fenshu(zi,mu)
        a.yuefen()
        return a
        
    def __sub__(self,shu):
        zi=self.zi*shu.mu-shu.zi*self.mu
        mu=self.mu*shu.mu
        a=fenshu(zi,mu)
        a.yuefen()
        return a
    def __eq__(self):
        return self.zhi()    
    def __call__(self):
        return self.zhi()
    def __mul__(self,shu):
        zi=self.zi*shu.zi      
        mu=self.mu*shu.mu
        a=fenshu(zi,mu)
        a.yuefen()
        return a
         
    









a=fenshu(0.1138625254435272) 
a.yuefen()
b=a*a
b=b-a
print(b())
print(b.zi,b.mu)  



