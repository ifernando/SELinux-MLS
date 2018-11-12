#!/usr/bin/env python

s1_read_s2=0
s2_read_s1=0
can_write_to_eachother=0
has_category=0

#Validate user's input
#yes=1, no=0, other keyboard input=-1 
def validate_user_input(user_input):
	if user_input == "Y" or user_input == "y":
		return 1
	elif user_input == "N" or user_input == "n":
		return 0
	else:
		return -1

has_category = validate_user_input(input("Does S1 and S2 have categories?(Y/N) : "))
while has_category == -1:
	print("Invalid Input...")
	has_category = validate_user_input(input("Does S1 and S2 have categories?(Y/N) : "))

can_write_to_eachother=validate_user_input(input("Can S1 and S2 write to each other?(Y/N) : "))
while can_write_to_eachother == -1:
    print("Invalid Input...")
    can_write_to_eachother=validate_user_input(input("Can S1 and S2 write to each other?(Y/N) : "))

s1_read_s2=validate_user_input(input("Can S1 READ S2 content?(Y/N) : "))
while s1_read_s2 == -1:
    print("Invalid Input...")
    can_write_to_eachother=validate_user_input(input("Can S1 READ S2 content?(Y/N) : "))
 
s2_read_s1=validate_user_input(input("Can S2 READ S1 content?(Y/N) : "))
while s2_read_s1 == -1:
    print("Invalid Input...")
    s2_read_s1=validate_user_input(input("Can S2 READ S1 content?(Y/N) : "))
  
print("-----------------------------------------------------------------------")                
print("Your input is... ")
print("S1 READ S2 content : ")
print('YES' if s1_read_s2 else 'NO')
print("S2 READ S1 content : ")
print('YES' if s2_read_s1 else 'NO')
print("S1 WRITE S2 and S2 WRITE S1 content : ")
print('YES' if can_write_to_eachother else 'NO')
print("Does S1 and S2 has categories : ")
print('YES' if has_category else 'NO')
                
print("-----------------------------------------------------------------------")
print("Output is... ")
if (s2_read_s1 == 1) and (s1_read_s2 == 1):
	print("S1 = S2")
	if (has_category == 1):
		print("C1 ⊆ C2 or C2 ⊆ C1")
	exit(0)

if (can_write_to_eachother == 1):
	print("if S1WS2→ 1;\nthen S1=S2 (BLP write equal property)\nS1RS2→ 1 & S2RS1→ 1\n∴ skipping;")  
	exit(0) 
else:  
	if (s1_read_s2 == 0) and (s2_read_s1 == 0):
		print("S1 ∥  S2")
		if (has_category == 1):
			print("C1 <> C2")
		exit(0)
	elif (s1_read_s2 == 1) and (s2_read_s1 == 0):
		print("S1 > S2")
		if (has_category == 1):
			print("C2 ⊆ C1")
		exit(0)
	elif (s1_read_s2 == 0) and (s2_read_s1 == 1):
		print("S2 > S1")
		if (has_category == 1):
			print("C1 ⊆ C2")
		exit(0)
