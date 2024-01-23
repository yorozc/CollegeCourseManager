#parse through csv and sort information into dict 
import csv

class CourseManage: 

    def __init__(self):

        self.gened = { #contains gened section information
            'A': {'A1': [], #this list will contain another list of every class ex: A: {'A1': [[Oral Comm, Comm200, Pub Speaking, None, 3]]}
                  'A2': [],
                  'A3': []}, 
            'B': {'B1': [],
                  'B2': [],
                  'B3': [],
                  'B4': [],
                  'UD-B': []},
            'C': {'C1': [],
                  'C2': [],
                  'UD-C': []},
            'D': {'D1': [],
                  'D2': [],
                  'UD-D': []},
            'E': {'E1': []},
            'F': {'F1': []}
        }
        self.completed = { #will hold completed courses that can be used to calc gpa or units
            'A': {'A1': [], 
                  'A2': [],
                  'A3': []}, 
            'B': {'B1': [],
                  'B2': [],
                  'B3': [],
                  'B4': [],
                  'UD-B': []},
            'C': {'C1': [],
                  'C2': [],
                  'UD-C': []},
            'D': {'D1': [],
                  'D2': [],
                  'UD-D': []},
            'E': {'E1': []},
            'F': {'F1': []}
        }

    def web_scrape(self):
        pass


    def parse_csv(self): #add all data to self.gened
        with open('courses.csv', 'r') as courses_file:
            csv_reader = csv.reader(courses_file, delimiter=',')
            headers = next(csv_reader)
            for line in csv_reader:
                if line[0] in self.gened.keys() and line[1] in self.gened[line[0]].keys():
                    self.gened[line[0]][line[1]].append([line[2], line[3], line[4], line[5], line[6]])  
                else:
                    print('Keys do not exist, try again')

        return self.gened

    def completed(self): #will allow user to remove courses they have completed into a completed list
        #will display classes that are left to take once they complete a section
        pass



