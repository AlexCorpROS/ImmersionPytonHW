import doctest


class Person:

    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int):
        '''
        >>> t5 = Employee("ivanov", "ivan", "ivanovich", 30, "manager", 50000)
        >>> t5.last_name
        'Ivanov'
        '''
        self.last_name = last_name.title()
        self.first_name = first_name.title()
        self.patronymic = patronymic.title()
        self._age = age

    def full_name(self):
        '''
        >>> t1 = Employee("Ivanov","Ivan","Ivanovich",30, 'a',2)
        >>> t1.full_name()
        'Ivanov Ivan Ivanovich'
        '''
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def birthday(self):
        '''
        >>> t2 = Employee("Ivanov","Ivan","Ivanovich",30, 'a',2)
        >>> t2.birthday()
        >>> t2._age
        31
        '''
        self._age += 1

    def get_age(self):
        return self._age


class Employee(Person):

    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int, position: str, salary: float):
        super().__init__(last_name, first_name, patronymic, age)
        self.position = position.title()
        self.salary = salary

    def raise_salary(self, percent: float):
        # '''
        # >>> t3 = Employee("Ivanov","Ivan","Ivanovich",30, "manager",50000)
        # >>> t3.raise_salary(10)
        # >>> t3.salary
        # 55000.0
        # '''
        self.salary = round(self.salary * (1 + percent / 100),2)

    def __str__(self):
        '''
        >>> t4 = Employee("Ivanov", "Ivan", "Ivanovich", 30, "manager", 50000)
        >>> print(t4)
        Ivanov Ivan Ivanovich (Manager)
        '''
        return f'{self.full_name()} ({self.position})'

def test_employee_raise_salary():
    '''
    >>> emp = Employee("Ivanov","Ivan","Ivanovich",30, "manager",50000)
    >>> emp.raise_salary(10)
    >>> emp.salary
    55000.0
    '''
    pass


if __name__ == '__main__':
    doctest.testmod(verbose=True)