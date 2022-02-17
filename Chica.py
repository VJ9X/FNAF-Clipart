import random

class Chica_Move:
    def __init__(self, chase0):
        self.chase0 = chase0
    
    def init(self):
        
        if self.chase0:
            self.chase0 = False
            self.chase1 = True
            
        elif self.chase1:
            
            choice1 = random.randint(1, 3)
            
            if choice1 == 1:
                self.chase01 = True
                self.chase1 = False
            
            elif choice1 == 2:
                self.chase02 = True
                self.chase1 = False
            
            elif choice1 == 3:
                self.chase2 = True
                self.chase1 = False
                
            
        
        
        elif self.chase01:
            
            choice2 = random.randint(1, 2)
            
            if choice2 == 1:
                self.chase02 = True
                self.chase01 = False
                
            if choice2 == 2:
                self.chase2 = True
                self.chase01 = False
            
            
            
        elif self.chase02:
            
            choice3 = random.randint(1, 2)
            
            if choice3 == 1:
                self.chase2 = True
                self.chase02 = False
                
            if choice3 == 2:
                self.choice01 = True
                self.chase02 = False
            
            
        elif self.chase2:
            
            self.chase3 = True
            self.chase2 = False
            
            
        elif self.chase3:
            
            self.clast = True
            self.chase3 = False
            self.bonnie_timer = random.randint(1, 5) * 1000
            
        elif self.clast:
            
            self.cjump = True
            self.clast = False
        
        
        
        if not self.clast:
            self.chica_timer = (random.randint(1, 5) * 1000)
            
    def reset_ai(self):
        
        self.chase0 = True
        self.chase1 = False
        self.chase01 = False #chica bathroom
        self.chase02 = False #chica kitchen
        self.chase2 = False
        self.chase3 = False
        self.clast = False
        self.cjump = False
        self.chica_timer = (random.randint(1, 10) * 1000)

            
                
            
            
