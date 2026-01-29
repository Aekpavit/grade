class GradeCalculator:
    def __init__(self, score):
        self.score = score

    def get_grade(self):
        if self.score >= 80:
            return "A"
        elif self.score >= 70:
            return "B"
        elif self.score >= 60:
            return "C"
        elif self.score >= 50:
            return "D"
        else:
            return "F"


def show_result(score):
    print("\n===== หน้าแสดงผล =====")
    calc = GradeCalculator(score)
    print("คะแนน:", score)
    print("เกรด:", calc.get_grade())
