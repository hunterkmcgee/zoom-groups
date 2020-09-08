## by HUNTER MCGEE
## use to generate csv for zoom breakout rooms.
## refer to documentation for an easy guide.

import csv
import requests
from bs4 import BeautifulSoup

## UPDATE PATHs FOR DIFFERENT GROUP LISTS
classlistPage = 'classlist.html'    # Classlist D2L page for this course, used to pull in emails
path = 'groups.txt'                 # Text file that specifies groups and names of group members
outPath = 'breakout-groups.csv'     # Output file, used to populate zoom breakout rooms
emailDomain = '@mtmail.mtsu.edu'

## CLASS DEFINITIONS
class Course:
    
    def __init__(self):
        self.groups = []

    def addGroup(self, group):
        self.groups.append(group)

    def getGroups(self):
        return self.groups


class Group:

    def __init__(self, name):
        self.name = name
        self.students = []

    def addStudent(self, student):
        self.students.append(student.info)

    def getStudents(self):
        return self.students
    
    def getName(self):
        return self.name


class Student:

    def __init__(self, name, emailTable):
        self.info = (name, self.emailLookup(name, emailTable))

    def emailLookup(self, name, emailTable):
        try:
            email = emailTable[name]
        except KeyError:
            return ('**' + name.strip().replace(',', ' -') + '**')
        return email

    def getEmail(self):
        return self.info[1]

    def getName(self):
        return self.info[0]

## Gets list of emails and corresponding student names
def getEmailTable(webpageFile):
    emailTable = []

    soup = BeautifulSoup(open(webpageFile), 'html.parser')

    for row in soup.find_all('tr'):
        for nameCell in row.find_all('th', {'class' : 'd_ich'}):
            studentName = nameCell.get_text().strip()

            # Get MTMAIL username
            parent = nameCell.parent()
            label = parent[-4].find('label').get_text()
            email = label + emailDomain

            # append to Email Table
            emailTable.append((studentName, email))

    return emailTable

## GET TEXT BLOCK FOR EACH GROUP
## FIRST ROW OF EACH GROUP = GROUP NAME
## EVERY SUBSEQUENT ROW = NAME OF GROUP MEMBERS
## NEW LINE SHOULD SIGNIFY END OF GROUP
emails = dict(getEmailTable(classlistPage))
#print(emails)

course = Course()
f = open(path, 'r', newline='')
f_lines = f.read().split('\n')

group_text_block = []
for line in f_lines:
    if line[0] != '\r':
        group_text_block.append(line)
    else:
        groupName = group_text_block[0].strip()
        group = Group(groupName)
        course.addGroup(group)

        for student in group_text_block[1:]:
            s = Student(student.strip(), emails)
            group.addStudent(s)

        group_text_block = []

# GENERATE CSV
with open(outPath, 'w', newline='') as csvFile:
    groupWriter = csv.writer(csvFile, delimiter=',', quotechar='', quoting=csv.QUOTE_NONE)

    # WRITE HEADER
    groupWriter.writerow(['Pre-assign Room Name', 'Email Address'])

    for group in course.getGroups():
        groupName = group.getName()

        for student in group.getStudents():
            groupWriter.writerow([groupName, student[1]])

csvFile.close()

f.close()
        