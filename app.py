from flask import Flask, jsonify, request, render_template, redirect
from datetime import datetime
from data import *

waec_data = []


app = Flask(__name__)


@app.route('/')
def index():
	course = response[0] if len(response) >= 1
	schools = response[1] if len(response) >= 1
	faculties = response[2] if len(response) >= 1


	if len(course) == 6:
		pass

	elif len(course) < 6:
		smcourse = 6 - len(course)
		for i in range(0, smcourse):
			course.append('No Data')

	else:
		del course[5:]

		pass


	return render_template('index.html', 
		cors1=course[0], cors2=course[1], cors3=course[2], cors4=course[3], cors5=course[4], cors6=course[5],
		schs1=schools[0],schs2=schools[1], schs3=schools[2], schs4=schools[3], schs5=schools[4], schs6=schools[5],
		facs1=faculties[0], facs2=faculties[1], facs3=faculties[2], facs4=faculties[3], facs5=faculties[4], facs6=faculties[5])


@app.route('/recommend', methods=['POST'])
def getData():

	sub1 = waec_data.append(request.form['waec1'])
	sub2 = waec_data.append(request.form['waec2'])
	sub3 = waec_data.append(request.form['waec3'])
	sub4 = waec_data.append(request.form['waec4'])
	sub5 = waec_data.append(request.form['waec5'])


	response = findInData(waec_data)


	return redirect('/')





if __name__ == '__main__':
	app.run(host="localhost", port=4000, debug=True)