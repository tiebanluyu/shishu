#导入deepcopy
from copy import deepcopy
#方便对格式进行比较
isin=isinstance
#将各种格式转为分数
def geshihua(shu):
        if isin(shu,fenshu):#fenshu
            return shu                   
        elif isin(shu,int) or isin(shu,float):
            return fenshu(shu)
        else: 
            raise Exception("输入错误") 

#分数模块
class fenshu:
    def __init__(self,zi=0,mu=1):#初始化        
        if isin(zi,float):#float格式
            self.zi=zi*(10**15)
            self.mu=(10**15)                    
        elif isin(zi,int):#int格式
            self.zi=zi
            self.mu=mu
        else:
            raise Exception("输入错误,暂不支持文本")#别的东西
        self.yuefen()    
        
    @property #将方法访问转换成属性访问
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
        zi=zi//yue
        mu=mu//yue      
        self.zi=int(zi)
        self.mu=int(mu)
    
    #输出数值
    def __float__(self):
        return self.zhi    
    __call__=__float__
    __int__=lambda self:int(self.zhi)


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
        a=fenshu(zi,mu)     
        return a
        
    def __sub__(self,shu):#减
        shu=geshihua(shu)#兼容
        zi=self.zi*shu.mu-shu.zi*self.mu
        mu=self.mu*shu.mu
        a=fenshu(zi,mu)      
        return a
     
    def __mul__(self,shu):#乘
        shu=geshihua(shu)#兼容
        zi=self.zi*shu.zi      
        mu=self.mu*shu.mu
        a=fenshu(zi,mu)   
        return a
   
    def __truediv__(self,shu):#除
        shu=geshihua(shu)#兼容
        zi=self.zi*shu.mu     
        mu=self.mu*shu.zi
        a=fenshu(zi,mu)#       
        return a
        
    __div__=__floordiv__=__truediv__#n种除法    
     
    
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
    #转换成列表
    def list(self,chang=100):
        self.__iter__()
        list1=[]
        for linshi in range(int(chang/4)):
            list1.append(self.__next__())
        return list1   
            
    
    #文本化    
    __repr__=__str__=lambda self:f"fenshu({self.zi}/{self.mu})"
    __hash__=lambda self:hash((self.zi,self.mu))	  
    
#实数             
class shishu:
    
    def __init__(self,shu=0,dishu=1):      
        if  isin(shu,shishu):#实数格式
            self.xinxi=deepcopy(shu.xinxi)
            return
        elif isin(shu,dict):#dict格式
            self.xinxi=shu
            return    
        else:
            shu=geshihua(shu)#int float 分数
            self.xinxi={}
            self.xinxi[dishu]=shu
        a=self.huajian()
        self.xinxi.clear()       
        for i in a:
            self.xinxi[i]=a[i]
                
    
    def jiashu(self,shu,beikaifangshu=1):#添加一个数
        if not self.xinxi.get(beikaifangshu) is None:#已存在，get方法存在则返回切片值，否则返回None
            self.xinxi[beikaifangshu]+=geshihua(shu)
        else:                                        #不存在
            self.xinxi[beikaifangshu]=geshihua(shu)
    #四则运算（除法有bug）
    
    #加法    
    def __add__(self,shu):
        linshi=shishu(self)
        if isin(shu,shishu):#实数格式
            for i in shu.xinxi:
                linshi.jiashu(shu.xinxi[i],i)
                
        else:#分数，小数
            shu=geshihua(shu)    
            linshi.jiashu(shu)
        return linshi
    
    #减法    
    def __sub__(self,shu):
        linshi=shishu(self)#复制一份       
        if isin(shu,shishu):#实数格式
            for i in shu.xinxi:
                linshi.jiashu(shu.xinxi[i]*(-1),i)        
        else:#分数，小数
            shu=geshihua(shu*(-1))    
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
        fuzhi2=dict(fuzhi)
        for linshi in fuzhi:
            
            
            if fuzhi[linshi].zi==0:
                del fuzhi2[linshi]
        return fuzhi2          
       
    def __mul__(self,shu):#乘法
        linshi=shishu()
        xinxi1=self.xinxi
        xinxi2=shu.xinxi
        for jia in xinxi1:
            for yi in xinxi2:
                linshi.jiashu(xinxi1[jia]*xinxi2[yi],beikaifangshu=jia*yi)          
        return shishu(linshi.huajian())       
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
            c=shishu(d)              
            a=a*c
            b=b*c    
        c=shishu(a)        
        for i in a.xinxi:
            c.xinxi[i]=a.xinxi[i]/b.xinxi[1]    
        return c    
    
    #文本化    
    __str__=(lambda self : "shishu"+str(self.xinxi).
    	                replace("{","[").replace("}","]") ) 
    __repr__=(lambda self : "shishu("+str(self.xinxi)+")")