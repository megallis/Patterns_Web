from my_framework.templator import render
from patterns.creational_patterns import Engine, Logger
from patterns.structural_patterns import RouteAdd, Debug

site = Engine()
logger = Logger('main')
routes = {}

@RouteAdd(routes=routes,url="/")
class Index:
    @Debug(name="Index")
    def __call__(self, request):
        return "200 OK", render("index.html", objects_list=site.categories)

@RouteAdd(routes=routes,url="/about/")
class About:
    @Debug(name="About")
    def __call__(self, request):
        return "200 OK", render("about.html", data=request.get("", None))

@RouteAdd(routes=routes,url="/contact/")
class Contact_Form:
    @Debug(name="Contact_Form")
    def __call__(self, request):
        return "200 OK", render("contact.html", data=request.get("data", None))

@RouteAdd(routes=routes,url="/course-list/")
class CoursesList:
    @Debug(name="CoursesList")
    def __call__(self, request):
        logger.log("Список курсов")
        category_id = int(request['request_params']['id'])
        logger.log(f"ID категоии {category_id}")
        try:
            category = site.find_category_by_id(category_id)
            return '200 OK', render('course-list.html', objects_list=category.courses, name=category.name, id=category.id)
        except KeyError:
            return '200 OK', 'No curses'

@RouteAdd(routes=routes,url="/course-new/")
class CreateCourse:
    category_id = -1
    @Debug(name="CreateCourse")
    def __call__(self, request):
        print(request)
        if request['method'] == 'POST':
            # метод пост
            data = request['data']

            name = data['name']
            name = site.decode_value(name)

            category = None
            if self.category_id != -1:
                category = site.find_category_by_id(int(self.category_id))

                course = site.create_course('record', name, category)
                site.courses.append(course)

            return '200 OK', render('course-list.html', objects_list=category.courses,
                                    name=category.name, id=category.id)

        else:
            try:
                self.category_id = int(request['request_params']['id'])
                category = site.find_category_by_id(int(self.category_id))

                return '200 OK', render('create-course.html', name=category.name, id=category.id)
            except KeyError:
                return '200 OK', 'Empty category'


@RouteAdd(routes=routes,url="/category-new/")
class CreateCategory:
    @Debug(name="CreateCategory")
    def __call__(self, request):
        if request['method'] == 'POST':
            # метод пост
            print(request)
            data = request['data']

            name = data['name']
            name = site.decode_value(name)

            category_id = data.get('category_id')

            category = None
            if category_id:
                category = site.find_category_by_id(int(category_id))

            new_category = site.create_category(name, category)

            site.categories.append(new_category)

            return '200 OK', render('index.html', objects_list=site.categories)
        else:
            categories = site.categories
            return '200 OK', render('category-new.html', categories=categories)

@RouteAdd(routes=routes,url="/category-list/")
class CategoryList:
    @Debug(name="CategoryList")
    def __call__(self, request):
        logger.log('Список категорий')
        return '200 OK', render('category-list.html', objects_list=site.categories)

@RouteAdd(routes=routes,url="/copy-course/")
class CopyCourse:
    @Debug(name="CopyCourse")
    def __call__(self, request):
        request_params = request['request_params']

        try:
            name = request_params['name']
            old_course = site.get_course(name)
            if old_course:
                new_name = f'copy_{name}'
                new_course = old_course.clone()
                new_course.name = new_name
                site.courses.append(new_course)

            return '200 OK', render('course-list.html', objects_list=site.courses)
        except KeyError:
            return '200 OK', 'No courses have been added yet'