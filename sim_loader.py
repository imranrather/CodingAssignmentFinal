# Name: Imran Rather 
# SID: 510462233
# unikey: irat3510


#importing modules 

import math
import sys
from sim_config import sim_config

def parse_sim_parameters(file_obj, config):
    #https://docs.python.org/3/library/io.html#io.IOBase.readlines (documentation)
    #https://www.codegrepper.com/code-examples/python/how+to+strip+a+list+in+python (documentation)
    
    test_file = file_obj.read(); #opening and reading the file_object 
    file_objsplit = test_file.split("\n") #splitting the contents into a list, every new line is a new list object 
    
    if (len(file_objsplit)) != 15: #this is the number of lines in test cases that arent missing information
        print('config file invalid, should be 15 lines long')
        return False #this will return early if the config file is not valid (not enough information)
    location_width = (file_objsplit[1].split(', ')) #splitting the 2nd element into another list
    location = location_width[0] 
    config.load_location = int(location) #reassigning the config variable for location
    print('this is the load location: ' + str(config.load_location))
    width = location_width[1]
    config.load_width = int(width) #reassigning the config variable for width
    print('this is the load width: ' + str(config.load_width))
    load_weight = file_objsplit[4]
    config.load_weight = int(load_weight) #reassigning the config variable for weight
    print('this is the load weight: ' + str(load_weight))
    load_type = file_objsplit[7]
    config.load_type = load_type #reassigning the config variable for load type
    print('this is the load type: ' + load_type)
    load_timing = file_objsplit[10]
    config.load_timing = int(load_timing) #reassigning the config variable for load timing 
    print('the load timing is: ' + str(config.load_timing))
    custom_data = file_objsplit[13]
    custom_data = custom_data.split(',')
    custom_data = [i.strip() for i in custom_data] #stripping away whitespaces 
    config.load_custom_data = custom_data  #reassigning the config variable for custom data 
    print('the custom data for this test case is: ' + str(config.load_custom_data))

    #load location/width --> must be integers, from 0-100 (inclusive)
    #load weight --> 1 integer, from 0-1,000,000 (inclusive)
    #load type --> must be string, default is constant, either constant, linear or custom
    #load timing --> 1 integer, not used for constant or custom load types, 0-1,000,000
    #load custom data --> pairs of int values, comma seperated, used when custom load type is selected otherwise ignored,
    #even number of values, no duplicate time values, 
    
    return True
    


def parse_soil_data(file_obj, config):
    ''' input: open file object
        output: 
            set the config variables soil_width, soil_depth, soil_key_desc, soil_data
            close the file_obj
            return True on success, otherwise False
    '''
    test_file = file_obj.read(); #opening and reading the file_object 
    file_objsplit = test_file.split("\n") #splitting the contents into a list, every new line is a new list object 
    width_depth = (file_objsplit[1].split(', '))
    
    width = width_depth[0]
    config.soil_width = int(width )
    print('the soil width is: ' + str(width))
    depth = width_depth[1]
    config.soil_depth = int(depth)
    print('the depth of soil is: ' + str(config.soil_depth))
    soil_keys = (file_objsplit[4])
    soil_keys = (soil_keys.split(','))
    soil_keys = [i.strip() for i in soil_keys] #strips elements of whitespaces (this was preventing the code passing test cases)
    config.soil_key_desc.extend(soil_keys) #adding the elements of the list form the test file to the list in soil_keys_desc
    print('the soil keys are: ' + str(config.soil_key_desc))
    soil_data1 = str(file_objsplit[7])
    soil_data1 = list(soil_data1)
    config.soil_data.append(soil_data1)
    print(config.soil_data)
    soil_data2 = str(file_objsplit[8])
    soil_data2 = list(soil_data2)
    config.soil_data.append(soil_data2)
    soil_data3 = str(file_objsplit[9])
    soil_data3 = list(soil_data3)
    config.soil_data.append(soil_data3)
    print(config.soil_data)

    #since soil data always changes, you can do a for loop or something to check len of testfile
    
    
    
    
    return True 
