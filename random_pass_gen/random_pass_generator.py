#!/usr/bin/env python3
# encoding: utf-8
import secrets
import string
import sys
import argparse
import os
from tqdm import tqdm #progress bar
# import time
# from datetime import timedelta



#check python version
if sys.version_info<(3,0,0):
    sys.stderr.write("Get Python 3 you idiot : https://www.python.org/downloads/ \n")
def argumentValidator(arguments) :
    #todo : propose a min length and a maxlength ? max words ? 

"""
Random Password generator that generates passwords of a min length of 8.
The password contains ASCII letters, punctuation and digits

"""
#generate a password string
def passwordGenerator(passwordLength):

    return ''.join(generator.choice(alphabet) for _ in range(passwordLength))

#generate a list of passwords and then write them to a txt
def generatePasswords(arguments):
    numPass = arguments.number
    passwordLength = arguments.length
    if numPass == 1 :
        password = passwordGenerator(passwordLength)
        print(password)
        return passwords # not very clean
    else :
        passwords = [passwordGenerator(passwordLength) for password in tqdm(range(numPass))]
        set(passwords) #making extra sure they are unique
        with open('passwords.txt','w') as txtfile :
            txtfile.write("\n".join(passwords))

    return passwords

"""

Generates a passphrase from an EFF wordfile : https://www.eff.org/fr/deeplinks/2016/07/new-wordlists-random-passphrases

"""

# loctes the wordfile -- maybe should add a selection of wordfiles (eff-short for example, maybe different languages ?)
def locateFile():
    #todo

#generate the worldfile from the provided txt
def createFile():
    wordfile = []
    with open('eff-long.txt','r') as file:
        for line in file :
            word = line.strip()
            wordfile.append(word)

    return wordfile


#choose words from a worldfile
def chooseWords(wordfile,numWords):
    words = [generator.choice(wordfile) for x in range(numWords)]
    return words



#generate a passphrase based on the number of words in it
def passphraseGenerator(numWords,wordfile):
    password = None
    seperator = " " #words separated by a space #todo : implement other seperators ?
    password = seperator.join(chooseWords(wordfile,numWords))
    return password




# generate a list of passphrases , if numPass == 1 we just print a single string
def generatePassphrases(arguments):
    numWords = arguments.words
    numPass = arguments.number
    passphrases = set()
    if numPass == 1 : #if only one passphrase we print it
        passphrase= passphraseGenerator(numWords,wordfile)
        print(passphrase)
        return(passphrases) # this isnt very clean

    else : #else we append it to a li
        passphrases = [passphraseGenerator(numWords,wordfile) for passphrase in tqdm(range(numPass))]
        set(passphrases)
        with open('passwords.txt','w') as txtfile :
            txtfile.write("\n".join(passphrases))

    return passphrases







#parser class for the arguments
class Argparser(argparse.ArgumentParser) :

    def __init__(self, *args, **kwargs):
        super(Argparser,self).__init__(*args,**kwargs)
        self.addArgs()
        #creation of the arguments
    def addArgs(self):
        #todo : add argument for a different seperator
        self.add_argument('-pw','--password',dest='action',action='store_const',const=generatePasswords, help = "Generate a password with 16 characters")
        self.add_argument('-pp','--passphrase',dest='action',action='store_const',const=generatePassphrases,help = 'Generate a passphrase with 4 words')
        self.add_argument("-w","--words", dest = "words", type = int, default = 4,   help = "Generate a passphrase with WORDS words")
        self.add_argument("-l","--length",dest = "length", type = int, default = 16,  help = "Generate a password with LENGTH characters")
        self.add_argument('-n','--number',dest = "number" ,type = int, default = 1,  help = "Generate NUMBER number of passwords or passphrases.")


def main() :
    parser = Argparser(prog=os.path.basename(sys.argv[0]),description="Generator for random Passwords/Passphrases.")
    arguments = parser.parse_args(sys.argv[1:])
    if arguments.action is None :
        parser.print_help()
    else :
        arguments.action(arguments)





#call the shit

if __name__ == '__main__' :
    #initalizing the generator
    generator = secrets.SystemRandom() #SystemRandom is secure : https://docs.python.org/3/library/os.html#os.urandom
    #initalizing the alphabet
    alphabet = string.ascii_lowercase +string.ascii_uppercase + string.digits + string.punctuation
    #creation a list from the txt wordfile
    wordfile = createFile()
    #call the program
    main()


################        testing        ###########################

#generateUsernames(5,8)
#print(string.punctuation)
#generator(100,20)

# start_time = time.monotonic()
# print(start_time)
# for i in tqdm(range(2000000)):
#     passwordGenerator(16)
#
# end_time = time.monotonic()
# print(timedelta(seconds=end_time - start_time))
