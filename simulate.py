# Name: 
# SID:
# unikey:

import math
import sys
from sim_config import sim_config
from sim_results import sim_results
from sim_loader import *
from sim_particle import *
from sim_particles2d import *

''' 
    simulate.py

    Student is to complete the functions:
        summarise_sim_data
        summarise_soil_data
        check_simulation_data
        calculate_applicable_load
        calculate_current_load
        simulation_start

    No modification is needed for functions, or sections:
        find_leak_points
        find_leak_points_r
        setup_config
        simulate_main
        main
        if __name__ == "__main__":

'''

def summarise_sim_data(config):
    ''' print the summary of the simulation parameter data 
        input:  config variables load_location, load_width, load_weight, load_type, load_timing, load_custom_data
        output: list of strings
    '''
    strs_out = []

    return strs_out
    
def summarise_soil_data(config):
    ''' print the summary of the soil data 
        input:  config variables soil_width, soil_depth, soil_key_desc, soil_data
        output: list of strings
    '''
    strs_out = []

    return strs_out

def check_simulation_data(config):
    ''' 
        check the simulation parameters and soil data are compatible
        - load location must be within the columns of soil defined
        - load width cannot overhang last soil column
        input: config variables for simulation parameters and soil
        output: on success, return True, otherwise return False
    '''
    return True 
    pass



def find_leak_points_r(start, fluid_body_particles):
# DO NOT MODIFY
    ''' Given '''
    leak_points = []

    p = start

    if p == None:
        return []

    if p.processed:
        return []

    if p.type == 'B':
        return []

    if p.type == 'V':
        p.processed = True
        return [p]

    p.processed = True
    fluid_body_particles.append(p)

    for i in range(4):
        if p.n[i] != None:
            leak_points += find_leak_points_r(p.n[i], fluid_body_particles)

    return leak_points

def find_leak_points(start):
# DO NOT MODIFY
    ''' Given '''
    fluid_body_particles = []
    leak_points = find_leak_points_r(start, fluid_body_particles)
    return (leak_points, fluid_body_particles)


def calculate_applicable_load(config, particles2d, current_load):
    '''
        Calculate how much of the load will be applied based on whether there are bedrock columns. When there are no bedrock columns, there is no change to the actual load. When there are all bedrock columns, the actual load is zero. For all other cases, the actual load is load - all load bearing bedrock columns

        Formula for your idea:
        load = load * ( #non-bedrock-cols / width + #bedrock-cols / width )

        input: 
                current_load, the number of kN for the given time instance (externally calculated based on non constant load type)
                config data with Load location and dimensions.
                particle2d - 2D grid of particles at present
        output: the kN (single float) applied to the body of water
    '''
    pass


def calculate_current_load(config, hours_passed):
    '''
    caclulate the amount of weight to be applied at hours_passed time.

    - Where the load type is constant. config.load_weight is returned.  

    - Where the load type is linear, a calculation is needed based on
hours_passed and load_timing. If the hours_passed exceeds load_timing,
then the full load_weight is used 
    
    - Where the load type is custom, the calculation follows the pairs
of time,load values in config.load_custom_data. config.load_custom_data
is assumed to be in time sorted order with no duplicates. The
intermediate values of custom data use the last known time's load value.
If the hours_passed is before all time/load pairs, then the load is zero.

    input: 
        config information config.load_weight, config.load_type, config.load_timing, config.load_custom_data
        hours_passed - representing the current time in the simulation. must be a positive integer
    output:
        on success, the load applied (single float) is returned (without considering the soil information)
        on failure, -1.0 is returned
    '''
    pass




def simulation_start(config, results):
    ''' Partially given

        run the simulation
        input: using the already loaded 
            - config variables
            - particles2d, leak_points, fluid_body_particles

        output: 
            - fill in the results object with information about the simulation and the outcome
            - list of strings for any output to be printed
    '''
    strs_out = []

    particles2d = create_2d_particle_array(config.soil_width, config.soil_depth, config.soil_data)
    print(particles2d)

    start_particles = []
    start_loc = [0, config.load_location]
    
    start_particles.append(particles2d)
    print(start_particles)
    print(start_loc[0])
    print(start_loc[1])
    
    for j in range(config.load_width):
        start_particles.append(particles2d[start_loc[0]][start_loc[1] + j] )
    print(start_particles)

    reset_particles2d(particles2d)
    visualise_particles2d(particles2d)

    load_connected_to_body = False
    found_water_body = False
    leak_points_ever_found = False
    leak_points = []
    fluid_body_particles = []
    for start in start_particles:
        leak_points, fluid_body_particles = find_leak_points(start)

        # check that the load is adjacent to a body of water (only one needed)
        load_connected_to_body = False
        for load_index in range(config.load_width):
            if particles2d[0][config.load_location+load_index].type == 'C':
                load_connected_to_body = True
                break

        if load_connected_to_body:
            found_water_body = True
            if len(leak_points) != 0:
                leak_points_ever_found = True
                break


    # CHECK if the simulation can be run
    #  - is there a water body?
    #  - are there leak points?
    #  - is the load connected to the body?


    total_water_removed = 0
    hours_passed = 0
    heights = []

    # REPEAT until consolidated

        # update the number of hours passed

        # calculate the current load 
        # calculate the applicable/final load 
        # add the final load for this timestep to results

        # calculate the water moved 

        # calculate the amount of water to remove from each particle

        # remove water from all fluid_body_particles only if they continue to hold water
        # Note: you must modify the .water attribute to reflect the water remaining in this particle 

        # update the total amount of water removed so far

        # calculate the heights of all columns for this hour

        # add the height information for this timestep to results

        #visualise_particles2d_water(particles2d)

        # test if consolidated


    # set the results for consolidation information

    visualise_particles2d(particles2d)
    print_heights(config.soil_depth, heights, 4,4)

    # return 
    return strs_out

def setup_config(sim_param_file, soil_data_file, output_file):
# DO NOT MODIFY
    ''' Given
        input: three file names
        output:
            on success, return a sim_config object with all variables filled in using the functions parse_sim_parameters and parse_soil_data
            on any failure, raise an exception with appropriate message
    '''
    config = sim_config()

    config.sim_param_file = sim_param_file
    config.soil_data_file = soil_data_file
    config.output_file = output_file

    parse_success = False
    try:
        f = open(config.sim_param_file, 'r')
        parse_success = parse_sim_parameters(f, config)
    except FileNotFoundError:
        raise Exception('sim params: could not find file: {}'.format(sim_param_file))
    except OSError:
        raise Exception('sim params: error encountered when reading file: {}'.format(sim_param_file))

    if not parse_success:
        raise Exception('sim params: parsing simulation parameters failed')
    else:
        print('OK parsed simulation parameters successfully')

    parse_success = False
    try:
        f = open(config.soil_data_file, 'r')
        parse_success = parse_soil_data(f, config)
    except FileNotFoundError:
        raise Exception('soil data: could not find file: {}'.format(config.soil_data_file))
    except OSError:
        raise Exception('soil data: error encountered when reading file: {}'.format(config.soil_data_file))

    if not parse_success:
        raise Exception('soil data: parsing soil data failed')
    else:
        print('OK parsed soil data successfully')


    sim_data_ok = check_simulation_data(config)
    if not sim_data_ok:
        raise Exception('simulation data incompatible')
    else:
        print('OK simulation data compatible')

    return config



def simulate_main(argv):
# DO NOT MODIFY
    ''' Given
        input: list of string as arguments to the program (do not use sys.argv, use argv)
        load data, run the simulation
        output: 
            save the results in the output file
            on success, return sim_results object 
            on failure return the Exception object:
                - for lacking command line arguments
                - for failing to setup configuration
                - for failing to run the simulation
                - for failing to write the output data
    '''
    if len(argv) < 4:
        print("Usage: python3 simulate.py <sim parameters file> <soil data file> <output file>")
        print("python3 simulate.py block01_config.txt clay1.txt block01_output.txt")
        raise Exception('error: not enough parameters')

    config = setup_config(argv[1], argv[2], argv[3])

    for l in summarise_sim_data(config):
        print(l)

    for l in summarise_soil_data(config):
        print(l)

    results = sim_results()
    strs = simulation_start(config, results)
    for line in strs:
        print(line)

    try:
        f = open(config.output_file, 'w')

        f.write('sim_param: {}\n'.format(config.sim_param_file))
        f.write('soil_data: {}\n'.format(config.soil_data_file))

        for l in summarise_sim_data(config):
            f.write("{}\n".format(l))

        for l in summarise_soil_data(config):
            f.write("{}\n".format(l))

        f.write('Consolidation time: {}\n'.format(results.get_consolidation_time()))
        f.write('Total water removed: {}\n'.format(results.get_total_water_removed()))
        for t in range(results.get_consolidation_time()):
            load = results.get_load_data(t)
            heights = results.get_height_data(t)
            f.write("t={}. load: {} heights: {}\n".format(t, load, heights))

        f.close()
    except:
        raise Exception('writing results: error encountered when writing file: {}', config.output_file)

    return results

def main(argv):
# DO NOT MODIFY
    print('--------------------')
    print('-START -------------')
    print('--------------------')
    simulate_main(argv)
    print('--------------------')
    print('-END ---------------')
    print('--------------------')


# DO NOT MODIFY
if __name__ == "__main__":
# DO NOT MODIFY
    main(sys.argv)
# DO NOT MODIFY
