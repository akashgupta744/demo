class School:
    school_name='DPS'
    school_location='Gwalior'
    school_principal='miss.peter'
    school_fees={'1th':12000,'2nd':13000,'3rd':14000,'4th':15000,'5th':16000,
                '6th':17000,'7th':18000,'8th':19000,'9th':20000,'10th':21000,'11th':22000,'12th':23000,}
    def __init__ (self,n,a,c,id,am):
        self.stud_Name=n
        self.stud_Age=a
        self.stud_Class=c
        self.stud_ID=id
        self.paid_amount=am
        self.remaining_amount=School.school_fees.get(self.stud_Class)-self.paid_amount

    def student_details(self):
        print(f'Name of Student is {self.stud_Name}')
        print(f'Age is {self.stud_Age}')
        print(f'class is {self.stud_Class}')
        print(f'Student ID is {self.stud_ID}')
        print('student fees',School.school_fees.get(self.stud_Class))
        print(f'amount paid by the student {self.paid_amount}')
        print(f'remaining amount is {self.remaining_amount}')

Akash=School('akash gupta',23,'10th',592418,10000)
Akku=School('akash',23,'11th',592418,13000)


School.student_details(Akash) # Akash.student_details()
School.student_details(Akku)

