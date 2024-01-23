from course_manage import *

def main():
    manage = CourseManage()
    data = manage.parse_csv()
    print(data)

if __name__ == "__main__":
    main()
