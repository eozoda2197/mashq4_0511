class Student:
    def __init__(self, score):
        self._score = score

    @property
    def grade(self):
        if self._score >= 90:
            return "A"
        elif self._score >= 80:
            return "B"
        elif self._score >= 70:
            return "C"
        elif self._score >= 60:
            return "D"
        else:
            return "F"

    @grade.setter
    def grade(self, value):
        grades = {"A": 95, "B": 85, "C": 75, "D": 65, "F": 50}
        if value in grades:
            self._score = grades[value]
        else:
            raise ValueError("Noto‘g‘ri baho kiritildi!")


student1 = Student(87)
print(f"Talaba bahosi: {student1.grade}")

student1.grade = "A"
print(f"Yangilangan score: {student1._score}")
print(f"Yangi baho: {student1.grade}")
