#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Script to parse Standard Resume """

import re
import os
import glob
from db_setup import resume




def save_to_db(key, value):
    resume.update({'_id': 'info'}, {'$set':{key:value}}, upsert=True)


def parse_resume(file):
    '''
    This will take single input as resume with pdf format and parse it to
    get the Name, Email, Gender, Contact Number, Experience, Technical Skills,
    Strength etc. which are defined as per standard format defined in Readme.md
    '''
    ''' Initial heading variable which store list of tuples with line no. and
    heading in the tuples. e.g. [(1, 'Name')] '''
    headings = []

    with open('{0}.txt'.format(file)) as fl:
        lines = fl.readlines()

    for i, line in enumerate(lines):
        if re.search(r' : ?', line):
            headings.append((i, line.split(':')[0].strip()))

    ''' Parse the details against the headings and store them into the MongoDB
    database named '''

    for i, val in enumerate(headings):
        try:
            key = val[1]
            value = lines[val[0]:headings[i+1][0]]
            if len(value) == 1:
                value = value[0].split(':')[1]
            else:
                value.pop(0)
                value = ' '.join(str(item) for item in value)
            save_to_db(key, value)
        except (IndexError,) as e:
            value = lines[val[0]].split(':')[1]
            save_to_db(key, value)

def main():
    '''
    This will take pdf resume as input and parse it if it is designed as per
    Standard defined in Readme.md
    '''
    file = raw_input("Please Enter the name of Pdf resume : ")
    pdf_files = glob.glob('*.pdf')
    if '{0}.pdf'.format(file) in pdf_files:
        ''' Convert pdf file into text file '''
        os.system('pdftotext {0}.pdf'.format(file))

        # Call the parser
        parse_resume(file)
    else:
        print '''PDF FileName passed to this module is not Present in this.
                folder. Please move it to current directory of script.'''
        return


if __name__ == '__main__':
    main()
