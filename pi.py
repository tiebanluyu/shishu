def pi(num):
    pi=fenshu()
    for i in range(num):
        pi+=fenshu(4,(2*i-1)*(-1)**(i+1))
    return pi