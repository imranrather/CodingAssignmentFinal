# Name: 
# SID:
# unikey:

''' 
    sim_particle.py

    Given. No modification required by student.  
'''

class particle:
    ''' Given '''
    ''' north, east, south, west '''

    def __init__(self, x, y):
        self.passes = 0
        self.processed = False

        # identify within the grid
        self.x = x
        self.y = y

        # neighbours
        self.n = [ None, None, None, None ]

        self.type = 'C'
        self.water = 0.4
        self.capacity = 0.4


    def north(self):
        return self.n[0]
    def east(self):
        return self.n[1]
    def south(self):
        return self.n[2]
    def west(self):
        return self.n[3]

    def set_north(self, p):
        self.n[0] = p
    def set_east(self, p):
        self.n[1] = p
    def set_south(self, p):
        self.n[2] = p
    def set_west(self, p):
        self.n[3] = p

    def __str__(self):
        return '({},{}) {}'.format(self.x, self.y,self.type)

    def __repr__(self):
        return '({},{}) {}'.format(self.x, self.y,self.type)

