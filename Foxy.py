import random



class Foxy_Move:
    def __init__(self, xhase0):
        self.xhase0 = xhase0
        
    
    def init(self):
                
        if self.xhase0:
            self.xhase1 = True
            self.xhase0 = False
            
            self.foxy_timer = random.randint(1, 5) * 1000
            
                
                
                
        elif self.xhase1:
            self.xhase2 = True
            self.xhase1 = False
            
            self.foxy_timer = random.randint(1, 5) * 1000
            
                
            
        elif self.xhase2:
            self.xhase3 = True
            self.xhase2 = False
            
            self.foxy_timer = random.randint(1, 5) * 1000
                    
        
        elif self.xhase3:
            self.xlast = True
            self.xhase3 = False
            
            self.foxy_timer = random.randint(1, 2) * 1000
            
            
        elif self.xlast:
            self.xjump = True
            
            
            
    
    def reset_ai(self):
        self.xhase0 = True
        self.xhase1 = False
        self.xhase2 = False
        self.xhase3 = False
        self.xlast = False
        self.xjump = False
        self.foxy_timer = (random.randint(1, 3) * 1000)
