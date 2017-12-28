f = open('output10.txt','r')
fr = open('anss10.txt' , 'r')
while 1:
	try:
		y = f.readline()
		u = fr.readline()
		if y != u:
			print y,'ans',
			print u,'my ans'
	except:
		f.close()
		fr.close()
		quit()
