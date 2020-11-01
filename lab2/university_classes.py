class Person:

    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email
        self.inbox = []

    def send_mail(self, content):
        self.inbox.append(content)

    def __str__(self):
        return self.name + " " + self.surname + " " + self.email + " Messages:" + str(self.inbox)


class Student(Person):

    def __init__(self, name, surname, email, index_no, **grades):
        super().__init__(name, surname, email)
        self.index_no = index_no
        self.grades = grades
        self.box = []

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def __str__(self):
        return super().__str__() + " Index number: " + str(self.index_no) + " Grades:" + str(self.grades)


class Worker(Person):

    def __init__(self, name, surname, email, room_no):
        super().__init__(name, surname, email)
        self.room_no = room_no

    def __str__(self):
        return super().__str__() + " Room number: " + str(self.room_no)


class Researcher(Worker):
    status = "researcher"

    def __init__(self, name, surname, email, room_no, publications_list):
        super().__init__(name, surname, email, room_no)
        self.publications_list = publications_list

    def add_publication(self, content):
        self.publications_list.append(content)

    def __str__(self):
        return super().__str__() + " Publications: " + str(self.publications_list)


class TeachingWorker(Worker):
    status = "teaching_worker"

    def __init__(self, name, surname, email, room_no, subjects, information_hours):
        super().__init__(name, surname, email, room_no)
        self.information_hours = information_hours
        self.subjects = subjects

    def __str__(self):
        return super().__str__() + " Subjects: " + str(self.subjects) + " Information hours: " + self.information_hours


if __name__ == "__main__":
    student1 = Student("Tomasz", "Kowalski", "tomk@gmail.com", 399, Math=5)
    researcher1 = Researcher("Adam", "Kowalski", "ak@gmail.com", 233, ["publication1", "publication2"])
    tw1 = TeachingWorker("Adrian", "Kowalski", "ak2@gmail.com", 233, ["math", "history"], "Friday 15-16")
    print("{}\n{}\n{}".format(student1, researcher1, tw1))

    student1.add_grade("IT", 4)
    student1.add_grade("Music", 2)
    tw1.send_mail("Hello")
    tw1.send_mail("Goodbye")
    researcher1.add_publication("publication3")
    print("After changes: ")
    print("{}\n{}\n{}".format(student1, researcher1, tw1))

