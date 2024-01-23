#parse through csv and sort information into dict 
import csv

class CourseManage: 

    def __init__(self):
        ''' #will come back to if nested dicts don't work
        self.gened = { #contains gened section information
            'A': [], #this list will contain another list of every class ex: A: [['A1', Oral Communication, COMM200, Public Speaking, None, 3]]
            'B': [],
            'C': [],
            'D': [],
            'E': [],
            'F': []
        }
        '''
        self.gened = { #contains gened section information
            'A': {'A1': [], #this list will contain another list of every class ex: A: {'A1': [[Oral Comm, Comm200, Pub Speaking, None, 3]]}
                  'A2': [],
                  'A3': []}, 
            'B': [],
            'C': [],
            'D': [],
            'E': [],
            'F': []
        }

    def parse_csv(self): #add all data to self.gened
        with open('courses.csv', 'r') as courses_file:
            csv_reader = csv.reader(courses_file)
            next(csv_reader)
            for line in csv_reader:
                print(line)

