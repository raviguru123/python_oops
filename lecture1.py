import  datetime;

class Employee:
    no_of_emps=0;
    raise_amount=1.04;
    def __init__(self,first,last,salary):
        self.first=first;
        self.last=last;
        self.salary=salary;
        Employee.no_of_emps+=1;
    def fullname(self):
        return self.first+' '+self.last;
    def apply_raise(self):
        return self.salary*self.raise_amount;
    @classmethod
    def change_raise_amount(cls,value):
        cls.raise_amount=value;

    @classmethod
    def from_string(cls,emp_string):
        first,last,email=emp_string.split('-');
        return cls(first,last,email);
    @staticmethod
    def is_weekday(day):
        if(day.weekday()==5 or day.weekday()==6):
            return False;
        return True;

# emp_1=Employee('ravi','guru',100000);
# emp_2=Employee('sunil','raghav',50000);
# print(emp_1.fullname());
# print(Employee.fullname(emp_1));
# Employee.raise_amount=1.05;
# emp_1.raise_amount=1.05;
# print(emp_1.raise_amount);
# print(emp_2.raise_amount);
# print(emp_1.__dict__);
# print(Employee.__dict__);
# print(emp_1.apply_raise());
# print(emp_1.no_of_emps);

# emp_string='ravi-guru-100000';
# emp_1=Employee.from_string(emp_string);
# print(emp_1.__dict__);
date=datetime.date(2017,10,23);
print(Employee.is_weekday(date));

        
