Family = {}
Family["tata"] = "Mihai"
Family["mama"] = "Ana"
print(Family)
print(Family.get("mama"))
print(Family.pop("mama"))
print(Family)
new_f = Family.copy()
print('Original one: ', Family)
print('New one: ', new_f)

ref_new = Family
ref_new.clear()
print('Referinta: ', ref_new)
print('Original: ', Family)

ref_new["copil_1"] = "Octav"
ref_new["copil_2"] = "Ioan"
ref_new["copil_3"] = "Mihai"
ref_new["copil_4"] = "Costel"

print('Referinta: ', ref_new)
print('Original: ', Family)

# ?
marks = {}.fromkeys(['copil_2', 'copil_3', 'copil_4'], "test")
print(marks.items())

for item in Family.items():
	print(item)

another_family = {x_member:x_member+x_member for x_member in range(20)}

print(another_family)
print(30 not in another_family)


for i in another_family:
	print(another_family[i])

sort_fam = sorted(Family, reverse = False)
print(sort_fam)