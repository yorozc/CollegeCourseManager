from course_manage import *

def main():
    manage = CourseManage()
    data = manage.parse_csv()
    #print(data)
    print(manage.print_dict())
    print('++++++++++++++++++++++++++++++++++++')
    manage.removed()
    print(manage.print_dict())
if __name__ == "__main__":
    main()
