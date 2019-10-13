#Replace Quality Scores
#This program replaces the quality scores of any Thymine base in the first, second, next to last, or last
#position in the read, and makes them lower for a
# specific kind of quality control
#A program by Tyler Serio
#Python 3.7
#Circa June 2019

#import relevant libraries
import numpy
import os.path
from os import path

#create variables
running = 1

#define the functions
def split(word):
    return[char for char in word]

def replace_quality_scores():
    #define the variables
    readcount = 0
    totalreadcount = 0
    milreadcount = 0
    linecount = 0
    badbasecount = 0

    #FASTQ files have four lines, thus four variables are created
    line1 = "blah"
    line2 = "blah"
    line3 = "blah"
    line4 = "blah"
    opening = 1

    #ask the user what file they want to open
    while opening == 1:
        print ("What file would you like to replace quality scores in?")
        print ("Example: 'pear_1_2.fastq'")
        print ("Type the exact name of the file you would like to remove low quality reads from,")
        ofile = input ("or type [0] to retrun to the menu. ")
        print ("")
        
        if ofile == "0":
            naming = 0
            removing = 0
            opening = 0
            break

        #check to see if the file exists
        path.exists(ofile)

        #if the file exists move on to the next step
        if path.exists(ofile) == True:
            print ("I will retrieve your file.")
            print ("I have found your file.")
            ofile = open(ofile, "r")
            cutoff = 0
            opening = 0
            replacing = 0
            naming = 1
            break

        #if the file does not exist, ask the user for another file
        if path.exists(ofile) == False:
            print("I will retrieve your file.")
            print("I cannot find this file. Make sure to type the file name exactly,")
            print("Try again, or type [0] to return to the menu.")
            print("")
            opening = 1
            replacing = 0
            naming = 0

    #ask the user what they would like to name their output file  
    while naming == 1:
        outputfilename = input ("The high-quality reads will be written to an output file. What would you like to name your output file? ")
        outputfilename =str(outputfilename)
        outputfilename = (outputfilename + ".txt.")
        outputfile = open (outputfilename, "w")
        print ("Your new file name is " + outputfilename)
        naming = 0
        replacing = 1
        break

    #begin replacing quality scores
    while replacing == 1:
        cutoff += 1

        #if all lines in the input file have been read, finish this part of the program
        if cutoff == 2:
            ofile.close()
            outputfile.close()
            print ("That's it!")
            print ("We're done!")
            print ("Total numbers of reads examined: " + str(totalreadcount))
            replacing = 0
            break

        #read every line of the input file
        for line in ofile:
            #let the user know something is happening
            if readcount == 1000000:
                readcount = 0
                milreadcount = milreadcount + 1000000
                print (str(milreadcount) + " reads examined.")
            linecount += 1

            #read and record the lines
            if linecount == 1:
                line1 = str(line)
            if linecount == 2:
                line2 = str(line)
                base_characters = split(line2)
            if linecount == 3:
                line3 = str(line)
            if linecount == 4:
                line4 = str(line)
                readcount += 1
                totalreadcount += 1
                quality_characters = split(line4)

                #if the quality score is a 'T' reduce it to a '#'
                if base_characters[0] == "T":
                    quality_characters[0] = "#"
                if base_characters[1] == "T":
                    quality_characters[1] = "#"
                if base_characters[len(base_characters) - 2] == "T":
                    quality_characters[len(base_characters) - 2] = "#"
                if base_characters[len(base_characters) - 3] == "T":
                    quality_characters[len(base_characters) - 3] = "#"
                line4 = ''.join(quality_characters)

                #write the lines to an output file
                outputfile.write(line1)
                outputfile.write(line2)
                outputfile.write(line3)
                outputfile.write(line4)

                #reset the variables
                line1 = "blah"
                line2 = "blah"
                line3 = "blah"
                line4 = "blah"
                linecount = 0    

#begin the program
while running == 1:
    #ask the user what they would like to do
    print ("Hello, what would you like to do?")
    print ("")
    print ("[1] - Replace quality scores.")
    print ("[2] - Exit")
    print ("")
    selecting = 1

    #select an option
    while selecting == 1:
        selection = 0
        selection = input ("Which do you choose? ")
        print ("")
        
        if selection != "1" and selection != "2":
            if selection == "":
                selection == ("Nothing")
                
            print ("You have chosen [" + selection + "].")
            print ("That is not a proper selection.")
            print ("Please choose from the list of selections.")
            
        else:
            selecting = 0

        #run the function
        if selection == "1":
            replace_quality_scores()
            selection = 0

        #exit the program
        if selection == "2":
            selecting = 2
            selection = 0

            #begin exiting the program
            while selecting == 2:
                print ("Goodbye. Are you sure you want to exit?")
                print ("")
                print ("[y] - Yes")
                print ("[n] - No")
                print ("")
                selection = input ("Which do you choose? ")
                print ("")

                #ask the user if they really want to exit
                if (selection != "y" and selection != "n"):
                    if selection == "":
                        selection == ("Nothing")
                        
                    print ("You have chosen [" + selection + "].")
                    print ("That is not a proper selection.")
                    print ("Please choose from the list of selections.")
                    
                if selection == "y":
                    exit()
                    
                if selection == "n":
                    print ("Oops. Nevermind then.")
                    selecting = 0
                
    
