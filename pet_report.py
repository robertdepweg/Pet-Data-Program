"""
MODULE: pet_report.py
contains CLASS: CIS216
used by PROJECT: RobertDPgm7.py
DESCRIPTION: This module contains several functions for use in Program 7
AUTHOR: Robert Depweg
"""
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - FUNCTIONS

def report_header(outfile):
    '''Writes the report's header into the .txt file'''
    outfile.write(f'{"Pet Report":>35}\n')
    outfile.write('\n')
    outfile.write(f'{"Name":<15}{"Symbol":<12}{"Count"}{"US Households":>18}\n')
    outfile.write('\n')

def process_records(infile, outfile):
    '''Splits the line into elements that are then calculated further
    and written down in .txt file, then given to report_footer'''
    counter: int = 0        # Counts each loop iteration, 
                            # and divides avg at end
    high_count: int = 0     # Max count value
    low_count: int = 99     # Min count value
    high_pop: int = 0       # Max population value
    low_pop: int = 99999999 # Min population value
    values: str = 0         # Holds the line's elements
    ave_count: float = 0    # Average count
    ave_pop: float = 0      # Average population
    line = infile.readline()
    while line != '':

        # splits elements into named variables
        values: list = line.split(',')
        name: str  = values[0]
        symbol: str  = values[1]
        count: int = int(values[2])

        # Tests if count is max or min
        if count > high_count:
            high_count = count
        if count < low_count:
            low_count = count
        population: int = int(values[3])

        # Tests if population is max or min
        if population > high_pop:
            high_pop = population
        if population < low_pop:
            low_pop = population
        
        counter += 1
        ave_count += count
        ave_pop += population
        outfile.write(f'{name:<15}{symbol:<14}{count:<5}{population:>16,.0f}\n')
        line = infile.readline()
    ave_count = round(ave_count / counter)
    ave_pop = ave_pop / counter
    report_footer(outfile, high_count, low_count, ave_count, high_pop, low_pop, ave_pop)

def report_footer(outfile, high_count, low_count, ave_count, high_pop, low_pop, ave_pop):
    '''Writes the final stats at bottom of .txt file'''
    outfile.write(f'{"-" * 53}\n')
    outfile.write(f'{"High":>26}{"Low":>12}{"Average":>15}\n')
    outfile.write(f'{"Count:"}{high_count:>20,.0f}{low_count:>12,.0f}{ave_count:>15,.2f}\n')
    outfile.write(f'{"US Households:"}{high_pop:>12,.0f}{low_pop:>12,.0f}{ave_pop:>15,.2f}\n')
