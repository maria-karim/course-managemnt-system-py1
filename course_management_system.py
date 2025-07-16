class User:
    def __init__(self, name):
        self.name = name

    def dashboard(self):
        pass

class Student(User):
    def __init__(self, name):
        super().__init__(name)
        self.__selected_courses = []
        self.__fees_paid = name.lower() in ["sara", "saad", "ali", "arsal", "maria"]

    def select_course(self, course):
        courses = ["Data Analysis", "Web Design", "Cyber Security", "Digital Marketing", "ML"]
        if course in courses and course not in self.__selected_courses:
            self.__selected_courses.append(course)

    def get_selected_courses(self):
        return self.__selected_courses

    def get_fee_status(self):
        return "Paid" if self.__fees_paid else "Unpaid"

class Teacher(User):
    def __init__(self, name, subjects):
        super().__init__(name)
        self.subjects = subjects

class Admin(User):
    def __init__(self, name):
        super().__init__(name)

    def view_all(self, student_list, teacher_list):
        data = []
        for s in student_list:
            data.append({
                'Name': s.name,
                'Courses': s.get_selected_courses(),
                'Fees': s.get_fee_status()
            })
        return data
