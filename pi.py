class Pi:
    @staticmethod
    def f1(num):
        Pi=Fac()  
        for i in range(num):
            Pi+=Fac(4,(2*i+1)*(-1)**(i))
        return Pi    
    @staticmethod
    def f2(num):
        pi = Fac()
        for k in range(num):
            pi += Fac(1,pow(16, k) * (4 / (8 * k + 1) - 2 /(8 * k + 4) - 1/(8 * k + 5) - 1 /(8 * k + 6)))
        return pi
    pi=Fac(355,113)