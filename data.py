import json
import time

courlist = []
faclist = []
schllist = []

def findInData(strings):

	with open ('database.json') as database:
		response = json.loads(database.read())

	datalenght = len(response)
	print(datalenght)


	for i in range (0, datalenght):
		data = response[i]
		utme = data['UTME']
		school = data['SCHOOL']
		course = data['COURSE']
		faculty = data['FACULTY']

		data = sortdata(strings, utme, school, course, faculty)

		if data == 'None':
			pass

		else:
			cors = data[0]
			facs = data[1]
			schs = data[2]
			courlist.append(cors)
			faclist.append(facs)
			schllist.append(schs)


	return (courlist, schllist, faclist)


def sortdata(waec, utme, school, course, faculty):
	countlist = []
	for i in waec:
		if i in utme and len(countlist)< 3:
			countlist.append(i)

		else:
			pass

	if len(countlist) == 3:
		return (course, faculty, school)


	else:
		return "None"


waec = waec = ["Chemistry","Biology","Mathematics","Economics","Government"]
findInData(waec)