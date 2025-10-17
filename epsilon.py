maths=float(input("Enter maths mark out of 200:"))
physics=float(input("Enter physics mark out of 200:"))
chemistry=float(input("Enter chemistry mark out of 200:"))
maths_half=maths/2
physics_quarter=physics/4
chemistry_quarter=chemistry/4
cutoff=maths_half+physics_quarter+chemistry_quarter
print("Your cutoff mark:",cutoff)
total_possible=100
lost_marks=total_possible-cutoff
print("Your lost",lost_marks,"marks from full cutoff.")
