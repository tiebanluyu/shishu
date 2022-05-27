from copy import deepcopy
bigeshi=lambda a,b:type(a)==type(b)#对格式进行比较
class fenshu:
    def __init__(self,zi=0,mu=1):
        if bigeshi(zi,0.1):#float
            self.zi=zi*(10**15)
            self.mu=(10**15)                    
        elif bigeshi(zi,1):#int
            self.zi=zi
            self.mu=mu
        else:
            raise Exception("输入错误")'
        self.yuefen()    
    def zhi(self):#计算
        if self.zi==0:
            self.mu=1
            return 0
        else:
            return self.zi/self.mu        
    def yuefen(self):#约分
        def zuidagongyueshu(a,b):
            #最大公约数之辗转相除法
            c=1
            while not c==0:
                c=a%b
                a=b
                b=c
                
            return a
        if self.zi==0:#万一分子是零
            self.mu=1
            return
        zi=self.zi
        mu=self.mu
        yue=zuidagongyueshu(zi,mu)
        zi=zi/yue
        mu=mu/yue
        
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
    def geshihua(self,shu):
        if bigeshi(shu,fenshu()):#fenshu
            return shu                   
        elif bigeshi(shu,1) or bigeshi(shu,0.1):
            return fenshu(shu)
        else: 
            raise Exception("输入错误")   
    def __add__(self,shu):#加
        shu=self.geshihua(shu)
        zi=self.zi*shu.mu+shu.zi*self.mu
        mu=self.mu*shu.mu
    
        a=fenshu(zi,mu)
        a.yuefen()
        return a
        
    def __sub__(self,shu):#减
        shu=self.geshihua(shu)
        zi=self.zi*shu.mu-shu.zi*self.mu
        mu=self.mu*shu.mu
        a=fenshu(zi,mu)
        a.yuefen()
        return a
     
    def __mul__(self,shu):#乘
        shu=self.geshihua(shu)
        zi=self.zi*shu.zi      
        mu=self.mu*shu.mu
        a=fenshu(zi,mu)
        a.yuefen()
        return a
    def __truediv__(self,shu):#除
        shu=self.geshihua(shu)
        zi=self.zi*shu.mu     
        mu=self.mu*shu.zi
        a=fenshu(zi,mu)
        a.yuefen()
        return a
        
    __div__=__floordiv__=__truediv__    
     
    
    #迭代器
    
    def __iter__(self):
        self.iterzi=self.zi
        
        
        
        b=int(self())
        
        self.iterzi-=self.mu*b
        self.iterb=b
        self.iterjishu=1
        return self
    def __next__(self):
        if self.iterjishu==1:
            self.iterjishu=0
            return self.iterb
            
        self.iterzi=self.iterzi*10000
        b=int(self.iterzi/self.mu)
        self.iterzi=self.iterzi-self.mu*b
            
        return b
            #
    #文本化
    def __str__(self):
        return f"fenshu({self.zi}/{self.mu})"
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
class shishu:
    geshihua=fenshu.geshihua
    def __init__(self,shu=0,dishu=1):
        
        if shu!=0 and bigeshi(shu,shishu()):
            self.xinxi=deepcopy(shu.xinxi)
            return
        shu=self.geshihua(shu)
        self.xinxi={}
        self.xinxi[dishu]=shu
    def jiashu(self,shu,beikaifangshu=1):
        if not self.xinxi.get(beikaifangshu) is None:
            self.xinxi[beikaifangshu]+=self.geshihua(shu)
        else:
            self.xinxi[beikaifangshu]=self.geshihua(shu)
        
    def __add__(self,shu):
        linshi=shishu(self)
        
        if bigeshi(self,shu):#实数格式
            for i in shu.xinxi:
                linshi.jiashu(shu.xinxi[i],i)
                
        else:#分数，小数
            shu=linshi.geshihua(shu)    
            linshi.jiashu(shu)
        return linshi
    def __sub__(self,shu):
        linshi=shishu(self)
        
        if bigeshi(self,shu):#实数格式
            for i in shu.xinxi:
                linshi.jiashu(shu.xinxi[i]*(-1),i)
                
        else:#分数，小数
            shu=linshi.geshihua(shu*(-1))    
            linshi.jiashu(shu)
        return linshi
    def huajian(self):
        def fenjie(a):
            b=1
            c=1
            while c**2<a:
                c+=1
                if a%(c**2)==0:
                    b=c
            return b
            
        fuzhi={}
        for linshi in self.xinxi:
            linshi2=linshi
            linshi3=self.xinxi[linshi2]
            linshi4=fenjie(linshi)
            linshi2=linshi2//(linshi4**2)
            linshi3=linshi3*linshi4
            
            if  fuzhi.get(linshi2) is None:
                fuzhi[linshi2]=self.geshihua(linshi3)
                
            else:
                fuzhi[linshi2]+=self.geshihua(linshi3)
                
        self.xinxi=fuzhi    
            
            
            
        
    __str__=__repr__=(lambda self : 
    	                "shishu"+str(self.xinxi).
    	                replace("{","[").
                    	replace("}","]")  
    	             )         
if __name__=="__main__":    
       
    
    a=shishu(12,3)
   
    c=shishu(13,120)
    c=c-a
    c.huajian()
    print(c)
        