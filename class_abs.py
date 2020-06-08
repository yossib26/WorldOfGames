class employee:

    raise_amt = 1.04
    num_of_emps = 0

    def __init__(self, first, email, pay):
        self.first = first
        self.email = email
        self.pay = pay
        self.test = first + "@" + email
        employee.num_of_emps +=1

    def full_name(self):
        return "{} {}".format(self.first, self.email)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


# inheritense
class developer(employee):
    raise_amt = 1.10

    def __init__(self, first, email, pay, prog):
       super().__init__(first, email, pay)
       self.prog = prog


class manager(employee):
    def __init__(self, first, email, pay, employees=None):
       super().__init__(first, email, pay)
       if employees is None:
           self.employees = []
       else:
           self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print(" -->", emp.fullname())


dev_1 = developer("dev-1", "ddddd", 5000, "python")
dev_2 = developer("dev-2", "ddddd", 90000, "java")

# mgr_1 = manager("Sue, ""aaaaa", 1000000, [dev_1])

#print(dev_1.pay)
#print(dev_1.prog)

#dev_1.apply_raise()
#print(dev_1.pay)


#emp_1 = employee("aaaa", "ddddd", 50000)
#emp_2 = employee("vvvvv", "dgfgfdgfd", 6000)
#print(help(developer))





#print(dev_1.test)

#print(dev_2.test)

