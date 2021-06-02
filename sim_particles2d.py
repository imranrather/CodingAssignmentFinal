# Name: 
# SID:
# unikey:
from sim_config import sim_config as config
from sim_particle import *

''' 
    sim_particles2d.py

    Student is to complete the functions:
        calculate_heights
        get_bedrock_columns

    No modification is needed for functions:
        create_2d_particle_array
        reset_particles2d
        count_particles2d
        visualise_particles2d
        visualise_particles2d_water
        print_heights
'''

def calculate_heights(particles2d):
    ''' calculate the height of each column     
    input: 2D grid of particles (list of lists)
    output: a list of heights for each column
    '''
    
    return [heights]



def get_bedrock_columns(particles2d):
    ''' returns a list of boolean values to represent whether the column is entirely bedrock
    input: 2D grid of particles (list of lists)
    output: a list of bool, where the list length is the number of columns'''
    
    column=[]
    bedrock=[]
    for col in range (3):
        for row in range (3):
            column.append(particles2d[col][row].type)
            
            
    for row in range(3):
        #print(column[row: :config.soil_width])
        if column[row: : 3].count("B") == 3:
            bedrock.append(True)
        else: 
            bedrock.append(False)
            
        
    return bedrock



def create_2d_particle_array(soil_width, soil_depth, soil_data):
    ''' Given : row order traversal '''
    particles2d = []

    i = 0
    while i < soil_depth:
        particles2d.append([])
        j = 0
        while j < soil_width:
            ttype = soil_data[i][j]
            p = particle(j,i)
            p.type = ttype
            if ttype == 'C':
                p.water = 0.4
                p.capacity = 0.4
            elif ttype == 'H':
                p.water = 0.03
                p.capacity = 0.05
            elif ttype == 'R':
                p.water = 0
                p.capacity = 0.001
            elif ttype == 'B':
                p.water = 0
                p.capacity = 0
            elif ttype == 'V':
                p.water = 0
                p.capacity = 1000

            particles2d[i].append(p)

            # create links
            if i > 0:
                particles2d[i-1][j].set_south(p)
                p.set_north(particles2d[i-1][j])
            if j > 0:
                particles2d[i][j-1].set_east(p)
                p.set_west(particles2d[i][j-1])

            j += 1

        i += 1

    return particles2d



def reset_particles2d(particles2d):
    i = 0
    while i < len(particles2d):
        j = 0
        while j < len(particles2d[0]):
            p = particles2d[i][j]
            p.processed = False
            p.passes = False
            j += 1
        i += 1

def count_particles2d(particles2d):
    count = 0
    i = 0
    while i < len(particles2d):
        j = 0
        while j < len(particles2d[0]):
            p = particles2d[i][j]
            if p.processed:
                count += 1
            j += 1
        i += 1

    print(count)


def visualise_particles2d(particles2d):
    i = 0
    while i < len(particles2d):
        j = 0
        lines = [[], [], [], [], []]

        while j < len(particles2d[0]):
            p = particles2d[i][j]

            hpad = 4
            lines[0].append(str(p).center(hpad, ' '))
            j += 1

        print(lines[0])
        i += 1


def visualise_particles2d_water(particles2d):
    i = 0
    while i < len(particles2d):
        j = 0
        lines = [[], [], [], [], []]

        while j < len(particles2d[0]):
            p = particles2d[i][j]

            hpad = 4
            lines[0].append(str(round(p.water,3)).center(hpad, ' '))
            j += 1

        print(lines[0])
        i += 1


def print_heights(max_height, heights, chars_for_1h, chars_for_1w, guide=False):
    ''' Given '''
    print("Heights: ")
    print()
    maxh = int(max_height * chars_for_1h)

    # create empty data
    strs = []
    strs += [ '-'*len(heights)*chars_for_1w ]
    for i in range(maxh):
        strs += [ list(' '*len(heights)*chars_for_1w) ]
    strs += [ '-'*len(heights)*chars_for_1w ]

    # set the levels
    for i in range(len(heights)):
        h = max(0, min(maxh,  (maxh - (int(round(heights[i], 0)) * chars_for_1h)) + 1))
        row = i*chars_for_1w
        for j in range(chars_for_1w):
            strs[h][row+j] = '*'

    # print
    if guide:
        for i in range(len(strs)):
            s = '  '
            if i != 0:
                h = (maxh-i+1)//chars_for_1h
                s = '{0:<2} '.format(str(h))
            print(s, end='')
            for j in range(len(strs[i])):
                print(strs[i][j], end='')
            print()
    else:
        for line in strs:
            for ch in line:
                print(ch, end='')
            print()