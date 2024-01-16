def copy_func():
	with open('plot2.png', 'rb') as rf:
		with open('plot5.png', 'wb') as wf:
			for line in rf:
				wf.write(line)



copy_func()




