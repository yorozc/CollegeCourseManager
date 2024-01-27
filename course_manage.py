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
        self.completed_courses = { #will hold completed courses that can be used to calc gpa or units
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

    def print_dict(self): #make it print elegantly not ugly
        return self.gened

    def web_scrape(self):
        pass


    def parse_csv(self): #add all data to self.gened
        with open('courses.csv', 'r') as courses_file:
            csv_reader = csv.reader(courses_file, delimiter=',')
            next(csv_reader)
            for line in csv_reader:
                if line[0] in self.gened.keys() and line[1] in self.gened[line[0]].keys():
                    self.gened[line[0]][line[1]].append([line[2], line[3], line[4], line[5], line[6]])  
                else:
                    print('Keys do not exist, try again')

        return self.gened

    def removed(self): #once removed, it will go to completed_courses
        #ask user what classes they have taken 
        #have it take the class_section_number or course_name
        #1/27/2024 Note to self: give capability of erasing with section # or name of class
        taken = input('What section/class have you completed: ') #have it search through the dict and rem from self.gened but move to self.completed
        for key in self.gened:
            if self.gened[key]:
                self.completed_courses[key][taken]  = self.gened[key].pop(taken, None) 
                return self.completed_courses
            
            else: 
                print('That class was not found, you maybe mispelled it?')
                break
        
    def check_eligibility(self): 
        #checks if eligible for class by checking prereqs from completed courses
        pass
