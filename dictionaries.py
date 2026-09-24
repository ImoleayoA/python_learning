student = {"name" : "Cia", "age" : 18, "course" : "Ai Native Engineering" }
print(student)

print(student["name"])
print(student["course"])

student["city"] = "Lagos"
student["age"] = 19
student.pop("course")
print(student)

for key, value in student.items():
    print(key, ":", value)

print("name" in student)
print("country" in student)

classroom = { "student1" : {"name" : "CiA", "age" : 18}, "student2" : {"name" : "cIa", "age" : 19} }
print(classroom["student1"]["name"])
print(classroom["student2"]["age"])
