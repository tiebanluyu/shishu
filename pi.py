class Pi:
    @staticmethod
    def f1(num):
        Pi=fenshu()  
        for i in range(num):
            Pi+=fenshu(4,(2*i+1)*(-1)**(i))
        return Pi    
    @staticmethod
    def f2(num):
        pi = fenshu()
        for k in range(num):
            pi += fenshu(1,pow(16, k) * (4 / (8 * k + 1) - 2 /(8 * k + 4) - 1/(8 * k + 5) - 1 /(8 * k + 6)))
        return pi
    pi=fenshu(355,113)