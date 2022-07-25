def pi(num):
    Pi=fenshu()  
    for i in range(num):
        Pi+=fenshu(4,(2*i+1)*(-1)**(i))
    return Pi    