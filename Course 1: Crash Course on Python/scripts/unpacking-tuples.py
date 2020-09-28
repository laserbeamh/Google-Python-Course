def guest_list(guests):
	for guest in guests:
		(name, age, job) = guest
		print("{name} is {age} years old and works as a {job}".format(name=name,age=age,job=job))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])
