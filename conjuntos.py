class Conjunto:
    def __init__(self, *args):
        if type(args[0]) == list:
            self.elementos = tuple(args[0])
        elif type(args[0]) == Conjunto:
            self.elementos = args[0].elementos    
        else:
            self.elementos = args
            
    
