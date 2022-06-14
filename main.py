from copy import deepcopy#导入deepcopy
bigeshi=lambda a,b:type(a)==type(b)#对格式进行比较
def geshihua(shu):#将各种格式转为分数
        if bigeshi(shu,fenshu()):#fenshu
            return shu                   
        elif bigeshi(shu,1) or bigeshi(shu,0.1):
            return fenshu(shu)
        else: 
            raise Exception("输入错误") 

#分数模块
class fenshu:
    def __init__(self,zi=0,mu=1):#初始化
        if bigeshi(zi,0.1):#float格式
            self.zi=zi*(10**15)
            self.mu=(10**15)                    
        elif bigeshi(zi,1):#int格式
            self.zi=zi
            self.mu=mu
        else:
            raise Exception("输入错误")#别的奇怪东西
        self.yuefen()    
    
    @property
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
        return self.zhi    
    __call__=__float__
    __int__=lambda self:int(self.zi)
    
    
     
    
    #比较
      
    __lt__=lambda self,shu:self()<shu()#小于
    __gt__=lambda self,shu:self()>shu()#大于
    __le__=lambda self,shu:self()<=shu()#小于等于
    __ge__=lambda self,shu:self()>=shu()#大于等于
    __eq__=lambda self,shu:self()==shu()#等于
    __ne__=lambda self,shu:self()!=shu()#不等于
            
    
    #四则运算
      
    def __add__(self,shu):#加
        shu=geshihua(shu)#格式化，兼容int和float
        zi=self.zi*shu.mu+shu.zi*self.mu
        mu=self.mu*shu.mu    
        a=fenshu(zi,mu)#包装       
        return a
        
    def __sub__(self,shu):#减
        shu=geshihua(shu)#格式化，兼容int和float
        zi=self.zi*shu.mu-shu.zi*self.mu
        mu=self.mu*shu.mu
        a=fenshu(zi,mu)#包装
        
        return a
     
    def __mul__(self,shu):#乘
        shu=geshihua(shu)#格式化，兼容int和float
        zi=self.zi*shu.zi      
        mu=self.mu*shu.mu
        a=fenshu(zi,mu)#包装
        
        return a
    def __truediv__(self,shu):#除
        shu=geshihua(shu)#格式化，兼容int和float
        zi=self.zi*shu.mu     
        mu=self.mu*shu.zi
        a=fenshu(zi,mu)#包装
        
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
            
    #文本化
    
    __repr__=__str__=lambda self: f"fenshu({self.zi}/{self.mu})"
    	  
    
    #转换成列表
    def list(self,chang=100):
        self.__iter__()
        list1=[]
        for linshi in range(int(chang/4)):
            list1.append(self.__next__())
        return list1             
class shishu:
    
    def __init__(self,shu=0,dishu=1):
        
        if shu!=0 and bigeshi(shu,shishu()):
            self.xinxi=deepcopy(shu.xinxi)
            return
        if bigeshi(shu,dict()):
            self.xinxi=shu
            return    
        shu=geshihua(shu)
        self.xinxi={}
        self.xinxi[dishu]=shu
    def jiashu(self,shu,beikaifangshu=1):
        if not self.xinxi.get(beikaifangshu) is None:
            self.xinxi[beikaifangshu]+=geshihua(shu)
        else:
            self.xinxi[beikaifangshu]=geshihua(shu)
        
    def __add__(self,shu):
        linshi=shishu(self)
        
        if bigeshi(self,shu):#实数格式
            for i in shu.xinxi:
                linshi.jiashu(shu.xinxi[i],i)
                
        else:#分数，小数
            shu=geshihua(shu)    
            linshi.jiashu(shu)
        return linshi
    def __sub__(self,shu):#减法
        linshi=shishu(self)#复制一份
        
        if bigeshi(self,shu):#实数格式
            for i in shu.xinxi:
                linshi.jiashu(shu.xinxi[i]*(-1),i)
                
        else:#分数，小数
            shu=geshihua(shu*(-1))    
            linshi.jiashu(shu)
        return linshi
    def huajian(self,*,gai=True):
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
                fuzhi[linshi2]=geshihua(linshi3)
                
            else:
                fuzhi[linshi2]+=geshihua(linshi3)
        
        del linshi,linshi2,linshi3,linshi4
        if not gai:
            return shishu(fuzhi)        
        else:
            self.xinxi=fuzhi    
            return self
    def __mul__(self,shu):
        linshi=shishu()
        xinxi1=self.xinxi
        xinxi2=shu.xinxi
        for jia in xinxi1:
            for yi in xinxi2:
                linshi.jiashu(xinxi1[jia]*xinxi2[yi],beikaifangshu=jia*yi)
                
        return linshi.huajian()       
            
            
        
    __str__=__repr__=(lambda self : 
    	                "shishu"+str(self.xinxi).
    	                replace("{","[").
                    	replace("}","]")  
    	             )         
if __name__=="__main__":    
       
    from cProfile import run
    a=shishu({
    	1:fenshu(0.02437643522627294),
    	91:fenshu(0.15373848453),
    	817:fenshu(4.0263),
    	257:fenshu(731636183651316736136.63613136),
    1964858457:fenshu(35361851371.361531531631838),
    41396137:fenshu(2.5),
    597139761:fenshu(17.579)
    
    
    
    	}
    	)
    #run("print(a*a*a*a*a+a*a*a*a*a)")  
    
    
    a=fenshu(100,91)
    a.zhi=1  
    print(a.zhi)