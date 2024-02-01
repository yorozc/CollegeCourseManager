from course_manage import *

def main():
    manage = CourseManage()
    data = manage.parse_csv()
    #print(data)
    print(manage.print_dict())
    print('++++++++++++++++++++++++++++++++++++')
    print(manage.removed())
    print('+++++++++++++++++++++++++++++++++++')
    print(manage.gened)
    print('+++++++++++++++++++++++++++++++++++')
    manage.check_eligibility()

    #print(manage.completed_courses)
if __name__ == "__main__":
    main()
