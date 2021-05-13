from datetime import date
from views import Index, About, Home, Contact_Form, CreateCourse, CoursesList, CreateCategory, CategoryList, CopyCourse

routes = {
    "/": Index(),
    "/about/": About(),
    "/home/": Home(),
    "/contact/": Contact_Form(),
    "/course-new/": CreateCourse(),
    "/course-list/": CoursesList(),
    "/category-new/": CreateCategory(),
    "/category-list/": CategoryList(),
    "/copy-course/": CopyCourse()
}


def date_front(request):
    request["date"] = date.today()


def key_front(request):
    request["user"] = "Petr"


fronts = [key_front, date_front]
