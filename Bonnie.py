import random


class Bonnie_Move:
    def __init__(self, bhase0):
        self.bhase0 = bhase0
    
        
    
    def init(self):
        
        if self.bhase0:
            self.bhase1 = True
            self.bhase0 = False
                
            
        elif self.bhase1:
            
            choice1 = random.randint(1, 2)
            
            if choice1 == 1:
                self.bhase01 = True
                self.bhase0 = False
                self.bhase1 = False
                    
            elif choice1 == 2:
                self.bhase2 = True
                self.bhase1 = False
                        
        elif self.bhase01:
            self.bhase1 = True
            self.bhase01 = False
                    
        elif self.bhase2:
            choice2 = random.randint(1, 2)
            if choice2 == 1:
                self.bhase02 = True
                self.bhase2 = False
                
            if choice2 == 2:
                self.bhase3 = True
                self.bhase2 = False
                        
        elif self.bhase02:
            self.bhase2 = True
            self.bhase02 = False
                    
        elif self.bhase3:
            self.blast = True
            self.bhase3 = False
            self.bonnie_timer = random.randint(1, 5) * 1000
                    
        elif self.blast:  
            self.bjump = True
        
        else:
            self.bhase0 = True
            
        
        if not self.blast:
            self.bonnie_timer = random.randint(1, 10) * 1000
        
    def reset_ai(self):
        self.bhase0 = True
        self.bhase1 = False
        self.bhase01 = False
        self.bhase2 = False
        self.bhase02 = False
        self.bhase3 = False
        self.blast = False
        self.bjump = False
        self.bonnie_timer = random.randint(1, 10) * 1000
