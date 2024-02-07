class Archive:
    instanse = None
    archive_text = []
    archive_number = []

    text = None
    number = None

    def __new__(cls, text, number):
        cls.instanse = super().__new__(cls)
        cls.text = text
        cls.number = number
        cls.archive_text.append(cls.text)
        cls.archive_number.append(cls.number)
        return cls.instanse

    def __init__(self, text: str, number):
        self.text = text
        self.number = number

    def __str__(self):
        str_ = ""
        str_ = f"Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}"
        return str_

    def __repr__(self) -> str:
        str_ = f"Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}"
        return str_

archive1 = Archive("Запись 1", 42)
archive2 = Archive("Запись 2", 3.14)

print(archive1)
print(archive2)
