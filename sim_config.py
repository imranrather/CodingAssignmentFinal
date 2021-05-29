# Name: Imran Rather 
# SID: 510462233
# unikey: irat3510

'''
    sim_config.py

    Given. No modification required by student 
'''
class sim_config:

    def __init__(self):
        ''' Given '''
        self.sim_param_file = 'undefined'
        self.soil_data_file = 'undefined'
        self.output_file = 'undefined'

        self.load_location = -1
        self.load_width = -1
        self.load_weight = 0
        self.load_type = None
        self.load_timing = -1
        self.load_custom_data = [0,0] # flat 1D list

        self.soil_width = 0
        self.soil_depth = 0
        self.soil_key_desc = []
        self.soil_data = [] # 2D. row major. list of lists

        # Soil compressibility. Water volume moved per 100kN per hour
        self.CLAY_COMPRESSIBILITY_RATE = 0.001
        self.SHALE_COMPRESSIBILITY_RATE = 0.0005

    def get_ith_custom_time_and_load(self,i):
        '''
            Given
            return a 2 tuple of (time, load) for the ith pair

            pair i: 0     1     2      3       4       5
            data :  4,44, 7,68, 14,77, 20,119, 24,104, 29,98

            get_ith_custom_time_and_load(3) returns (20,119)
        '''
        return (self.load_custom_data[2*i], self.load_custom_data[2*i+1])
        
    def get_soil_data(self, x,y):
        '''
            Given
            return the soil type at location x,y
            
              0123
            0 ABCD
            1 EFGH
            2 IJKL

            get_soil_data(1,2) returns 'K', which is row 2, column 1
        '''
        return self.soil_data[y][x]
