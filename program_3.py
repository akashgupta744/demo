class Player:
    def __init__(self,n,co,a,nom,nor,now):
        self.pname=n
        self.pcountry=co
        self.page=a
        self.pmatches=nom
        self.pruns=nor
        self.pwickets=now

class Team:
    def __init__(self,n):
        self.nop=n
        self.player_list=[]
        for i in range(1,self.nop+1):
            pn=input(f'{i} player name') #Virat
            pc=input(f'{i} player country') #india
            pa=input(f'{i} player age') #34
            pnm=int(input(f'{i} player no. of matches'))
            pnr=int(input(f'{i} player no. of Runs'))
            pnw=int(input(f'{i} player no. of Wickets'))
            pao=Player(pn,pc,pa,pnm,pnr,pnw)
            self.player_list.append(pao)

    
    def total_score(self):
        total_run=0
        for i in self.player_list:
            total_run+=i.pruns
        print('Total score =',total_run)

    def max_run(self):
        max=0
        obj=''
        for i in self.player_list:
            if i.pruns>max:
                max=i.pruns
                obj=i
        print(f'max runs of {obj.pname} = {max}')

    def max_wickets(self):
        max=0
        obj=''
        for i in self.player_list:
            if i.pwickets>max:
                max=i.pwickets
                obj=i
        print(f'max wickets of {obj.pname} = {max}')
    
    def max_matches(self):
        max=0
        obj=''
        for i in self.player_list:
            if i.pmatches>max:
                max=i.pmatches
                obj=i
        print(f'max matches played by {obj.pname} = {max}')


        
india=Team(int(input('no_players')))       
india.total_score() 
india.max_run()
india.max_wickets()
india.max_matches()           
