"""ระบบลงทะเบียนเรียนและข้อมูล"""
class student:
    def __init__(self,name,id):
        self.name = name
        self.studentid = id
        self.course = [] #self.course ถ้าเป็น string จะจัดการยากเมื่อมีหลายวิชา (ควรใช้ list) ถ้าจะเพิ่มต่อยใช้ append()
    def enroll(self,course):
        print(f"you have enroll {course}")
        if course in self.course:
            print("You have already enrol this course")
        elif course not in self.course:
            self.course.append(course)
            print(f"Susscesfull enroll this {course} course")
    def show_course(self):
        print("All subject you have enroll")
        for i in self.course:
            print(f"{i}")

class teacher:
    def __init__(self,name,id):
        self.name = name
        self.teacherid = id
        self.subject_tech = []
    def assign_subject(self,subject):
        if subject not in self.subject_tech:
            self.subject_tech.append(subject)
            print(f"{self.name} can now tecach {subject}")
        else:
            print(f"You have already enroll this {subject}")

class course:
    def __init__(self,course_id,course_name,teacher):
        self.course_id = course_id
        self.course_name = course_name
        self.teacher =  teacher
        self.list_student = []

    def add_student(self, student):
        if student.name not in self.list_student:
            self.list_student.append(student.name) #เอาชื่อนักเรียนไปเก็บใน list ของ class course
            #เรียกใช้ method ข้ามคลาสได้อย่างถูกต้อง (เช่น student.enroll()) เงื่อนไขส่ง obj ของclassนั้นมาด้วย
            student.enroll(self.course_name) # ทำการเพิ่มวิชาให้กับ object นั้นๆ
            # ทำการเรียกใช้ class student ฟังชั่นก์ enroll โดยส่ง self.coursename ("Math") เข้าไป
        else:
            print(f"{student.name} already enroll this {self.course_name}")
    def showinfo(self):
        print(f"course name: {self.course_name} couse id: {self.course_id}")
        print(f"teach by {self.teacher.name}")
        print("Enroll student:")
        for i in self.list_student:
            print(f"{i}")

# การใช้งาน
# การกำหนด attribute |  variable = class_name(argument1,argument2,........)
t1 = teacher("ครูบีม", "T001")

# การเรียกใช้งาน variable.func_name(argument1,argument2,......)
t1.assign_subject("Math")

s1 = student("น้องเอ", "S001")
s2 = student("น้องบี", "S002")

c1 = course("C001", "Math", t1)

#เราสามารถ เอาข้อมูลจาก class อื่นมาใช้ใน classตัวเอง ได้รวมถึงฟังชั่น
#วิธี แค่ส่ง object ของclassนั้นๆ ไปในparameterด้วย ก็จะสามารถใช้ฟังชั่นของclassนั้นได้เลย
c1.add_student(s1)
c1.add_student(s2)

c1.showinfo()
s1.show_course()
