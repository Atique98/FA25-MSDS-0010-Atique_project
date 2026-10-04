class Student:
    def __init__(self, id, name, program, semester, marks):
        self.id = id
        self.name = name
        self.program = program
        self.semester = semester
        self.marks = marks
        self.grade = None

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["name"],
            data["program"],
            data["semester"],
            data["marks"],
        )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "program": self.program,
            "semester": self.semester,
            "marks": self.marks,
            "grade": self.grade,
        }

    def __str__(self):
        return f"{self.name} ({self.id}) - {self.program}"
