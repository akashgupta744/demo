class Bank:
    bank_Name='lena-dena'
    bank_ifsc='l@d1234'
    bank_branch='gwalior'
    bank_manager='mr.Akash Gupta'
    bank_roi=7.7
    def __init__(self,n,ac,ad,g,b=10):
        self.name=n
        self.account=ac
        self.adhar=ad
        self.gender=g
        self.balance=b

    @classmethod
    def display_bank_details(cls):
        print('bank name is',cls.bank_Name)
        print('bank ifsc is',cls.bank_ifsc)
        print('bank branch is',cls.bank_branch)
        print('bank manager is',cls.bank_manager)
        print('bank roi is',cls.bank_roi)

    @staticmethod
    def get_int_data(s):
        data=int(input(f'enter int data for {s}'))
        return data

    @classmethod
    def modify_roi(cls):
        newroi=cls.get_int_data('newroi')
        cls.bank_roi=newroi
        print(newroi,'roi is modified')
        
    def withdraw(self):
        amount=self.get_int_data('withdraw amount')
        if self.balance>=amount:
            self.balance-=amount
            print(amount,'withdrwal is successful')
            print(f'your balance is {self.balance}')
        else:
            print('low balance')
            print(f'your balance is {self.balance}')

akash=Bank('Akash Gupta',2334,9890,'Male',1123344)
itii=Bank('itishree',236764,3456544,'female',123456789)
akash.modify_roi()
akash.withdraw()
Bank.display_bank_details()

