class Human:
    def __init__(self, name, age, surname):
        self.name = name
        self.age = age
        self.surname = surname


class Work(Human):
    def __init__(self, name, age, surname, salary: float, industry: str, job_title: str):
        super().__init__(name, age, surname)
        self.salary = salary
        self.industry = industry
        self.job_title = job_title


class Taxes(Work):
    def __init__(self, salary, industry, job_title, PIT, PT, LT, TX, CPF):  #personal income tax/ property tax/ land tax/
        super().__init__(salary, industry, job_title)                       # transport tax/ contribution to the pension fund
        self.PIT = PIT
        self.PT = PT
        self.LT = LT
        self.TX = TX
        self.CPF = CPF
        self.GT = PIT + PT + LT + TX + CPF

    @staticmethod
    def general_tax(GT, salary):
        income = salary - GT
        return income



