# Name: 
# SID:
# unikey:

'''
    sim_results.py

    Student is to complete all the functions. They may choose the name of the instance variables, or follow suggested.
'''
class sim_results:

    def __init__(self):
        ''' set initial values of the simulation state '''
        # suggested 
        self.consolidation_time = 0
        self.total_water_removed = 0
        self.heights_data = [ [0] ] # multiple per time step
        self.load_data = [0] # one per time step
        pass

    def get_consolidation_time(self):
        return self.get_consolidation_time
        pass

    def get_total_water_removed(self):
        return self.total_water_removed
        pass

    def get_height_data(self, time):
        '''
        return the list of heights for each column at the given time. 
        The time value must be between 0 and consolidation_time
        
        input: time (hours since start simulation)
        output: 
            on success, list of height values for the given time
            on failure, return an empty list
        '''
        return self.heights_data
        pass

    def get_load_data(self, time):
        '''
        return the final load value applied to the water body at the given time. 
        The final load value is after all calculations involving timing and bedrock columns. 
        The time value must be between 0 and consolidation_time
        
        input: time (hours since start simulation)
        output: 
            on success, load value (single float) for the given time
            on failure, return -1.0
        '''
        return self.load_data
        pass
        


