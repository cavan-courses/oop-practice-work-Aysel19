class Worker:
    def __init__(self,name,profession,department):
        self.name=name
        self.profession=profession
        self.department=department

    def show(self):
            print("Name:",self.name,"Profession:",self.profession,"Department:",self.department)

class Other(Worker):
    def __init__(self,name,profession,position,department):
            super().__init__(name,profession,department)
            self.position=position
    def show(self):
            print("Name:",self.name,"Profession:",self.profession,"Department:",self.department,"Position:",self.position,)


Other =Other("Jack Williams","Web Developer","Intern","IT")
Worker =Worker("Jane Roberts","HR","IR")
Other.show()
Worker.show()







