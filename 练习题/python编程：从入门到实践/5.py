import time
def menu():
	print "please input you choose"
	print "1. add"
	print "2. del"
	print "3. select"
	print "4. update"
	print "5. print all" 
	print "6. exit"
	print "-----------------------"
student=[]
name=""
while(1):
	menu()
	a=int(input("you choose:"))

	if a==6:
		print "exiting .",
		time.sleep(0.5)
		print ".",
		time.sleep(0.5)
		print "."
		time.sleep(0.5)
		exit()
	elif a==1:
		print "please input student name"
		name=str(raw_input())
		student.append(name)
		print "success!"
	elif a==5 :
		for i in student:
			print i
	elif a==2:
		print "please input del student name"
		name=str(raw_input())
		j=0
		for i in student:
			if i==name:
				j=1
				student.remove(i)
		if j==0:
			print "no this student!"
		else:
			print "success!"
	elif a==3:
		print "please input select student name"
		j=0
		name=raw_input()
		for i in student:
			if i==name:
				j=1
		if j==0:
			print "no this student!"
		else:
			print "select success!"
	elif a==4:
		print "please input update student name"
		name=raw_input()
		j=0
		k=0
		for i in student:
			if i==name:
				j=1
				print "please input you upadte"
				student[k]=raw_input()
			k=k+1
		if j==0:
			print "no this student "
	a=raw_input("Press any key to continue")
	print "-----------------------"
	