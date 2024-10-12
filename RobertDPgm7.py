# PROJECT:  RobertDPgm7.py
# AUTHOR:  Robert Depweg                                    DESIGNER:  clc
# DESCRIPTION:  This project writes a report to a file based on data from an
#      input .csv data file.
# INPUT:  PetData.csv file already in project folder.
#      Each person's data record contains name, picture, count per household, population US households
#      (Assume no errors in data file - i.e.,
#          - number & population always numeric values
#          - records always have 4 fields
#          - 4 fields always in correct order)
# OUTPUT:  PetReport.txt - includes:
#       - REPORT HEADER:
#           - a descriptive title, then a blank line
#           - a column header line (with labels for 4 fields) then a blank line
#                  [with labels aligned over the data fields]
#       - DETAIL LINES:  (1 line per pet)
#           Fields must be be nicely spaced across and formatted
#               - 2 numeric fields Count center justified and pop RIGHT-justified - all aligned
#               - 2 alphanumeric fields LEFT-justified - all aligned
#               - population has commas
#       - REPORT FOOTER:
#           - a line of dashes (exactly as wide as the report - repeat operator should be used)
#           - final stats, nicely formatted with labels, on 2 lines:
#                  largest count, lowest count , average count (comma and decimal)
#                  highest pop, lowest pop, average pop (comma and decimal)
#       - See EXPECTED OUTPUT
#       - Format output using f-string  field width, alignment, and precision specifiers.  
#         Do not align output using spaces.
# MAIN PROCESSING ALGORITHM:  Input data file is treated as a STREAM of data,
#       not a STORAGE BIN of data.  So program never needs data for > 1 pet
#       at a time.  So program:
#          - only has a SINGLE set of variables to accommodate ONE data set
#          - does whatever processing is needed for THAT data set
#          - then reads in NEXT data set (for NEXT pet) into the SAME
#              variables (which over-writes the previous pet's data).
# MODULARITY:
#       1) main function in THIS .py file:
#           - opens the 2 data files
#           - calls report_header in another module
#           - calls process_records in the other module
#           - closes the 2 data files
#           - prints ending message to report file and to console:
#       2) the other module (pet_report.py) contains 3 functions:
#           - report_header() (called by main)
#           - process_records() (called by main)
#           - report_footer() (called by process_records, at the end)
# NOTES:
#       - YOU have to create the other module in this project
#       - since the 2 files are opened/closed in THIS main program, but are
#           read/written to in functions in the OTHER module, the file objects
#           (e.g., infile and outfile) have to be passed as parameters to
#           those functions which need file access
#       - process_records includes:
#               setting up and initializing variables needed for the stats
#               the IPO functionality in its WHILE loop whose body includes:
#                       read a record
#                       split it into fields#
#                       do the stats using this record's data
#                       write a detail line in the report
#               call report_footer providing it with the stats data
#                       (& outfile object) as parameters
# ----------------------------------------------------------------------------
# INPUT: PetData.csv, The fields: name, symbol, count, population
# OUTPUT: PetData.txt
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
import pet_report

def main():
        try:
                user_file = input()
                infile_cvs = open(user_file, 'r')
                outfile_txt = open('PetData.txt', 'w')

                pet_report.report_header(outfile_txt)

                pet_report.process_records(infile_cvs, outfile_txt)
                
                outfile_txt.write('\n\nEND OF REPORT')
                infile_cvs.close()
                outfile_txt.close()

                print("OK, Report created - see PetData.txt in project folder")
        except:
                print('OS Error')


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Conditional call to main()
if __name__ == '__main__':
    main()