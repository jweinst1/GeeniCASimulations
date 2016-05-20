#this simulation is a basic one, without consideration for neighborhoods of students, run under discrete time instances
#it does not take cash into account
import sys

#student class
class Student:

    def __init__(self):
        self.sessions = 0
        self.generations = 0
        self.locked = False
    def __repr__(self):
        if self.locked:
            return "??"
        return str([self.sessions, self.generations])
    def incrementgen(self):
        self.generations += 1

#tutor class
class Tutor:

    def __init__(self):
        self.taught = 0
    def __repr__(self):
        return str(self.taught)



#generator for simulation
#for every generation a flag amount of tutors  are selected to schedule a session or teach it
#a tutor can only teach one student per generation
#if a student doesn't
def tutorStudentSim(students, tutors, flag):
    #you cannot select more tutors than you actually have
    assert tutors >= flag
    import random
    s = [Student() for i in range(students)]
    t = [Tutor() for i in range(tutors)]
    while True:
        selected_tutors = random.sample(t, flag)
        selected_students = random.sample(s, flag)
        for elem in selected_tutors:
            elem.taught += 1
        for student in selected_students:
            if student.sessions == 0 and student.generations == 2:
                student.locked = True
            else:
                if student.locked:
                    student.incrementgen()
                else:
                    student.incrementgen()
                    student.sessions += 1
        for std in s:
            if std.sessions == 0 and std.generations == 2:
                std.locked = True
            elif not std.locked:
                std.incrementgen()
        yield str(t) + "\n" + str(s)

studcount = int(sys.argv[1])
tutorcount = int(sys.argv[2])
flagcount = int(sys.argv[3])
times = int(sys.argv[4])

gen = tutorStudentSim(studcount, tutorcount, flagcount)

for i in range(times):
    print(next(gen))
