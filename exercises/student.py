#Save each student into a list
studs = []

class Student():


   def __init__(self, name, age, gender):
       self.name = name
       self.age = age
       self.gender = gender

       #Add student to the studs list
       studs.append(self)

   def getName(self):
        return self.name


   def getAge(self):
        return self.age


   def getGender(self):
        return self.gender


   def setAge(self, age):
        self.age = age


   def __str__(self):
       return str(self.name) + ', ' + str(self.age)


john = Student('John', 24, 'male')
will = Student('Will', 18, 'male')
zoe = Student('Zoe', 26, 'female')
patrick = Student('Patrick', 19, 'male')
sarah = Student('Sarah', 21, 'female')


#Prints out every student in the list
for students in studs:
    print(students)