# creating object of adress class inside the constructor of trainer class
class Car:
    def __init__(self,cn,cc,cm):
        self.Cname=cn
        self.Ccolour=cc
        self.Cmodel=cm
    
    def car_started(self):
        print(self.Cname,'is started')
    def car_accelerated(self):
        print(self.Cname,'is accelerated')
    def car_stop(self):
        print(self.Cname,'is stop')


    
class Driver:
    def __init__(self,n,ag,e):
        self.Dname=n
        self.Dage=ag
        self.Dexperince=e
        N=input('enter Car Name')
        C=input('enter Car colour')
        M=input('enter Car Model')
        ACO=Car(N,C,M)
        self.Dcar=ACO

    def car_driving(self):
        print(self.Dname,'has started the car')
        self.Dcar.car_started()
        self.Dcar.car_accelerated()
        self.Dcar.car_stop()
        print(self.Dname,'has started the car')

Akash=Driver('Akash Gupta',23,'2yr')
Akash.car_driving()
        
