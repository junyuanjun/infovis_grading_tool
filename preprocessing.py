import os
import subprocess
import json

'''initialize to_view folder'''
subprocess.run(['rm', '-r', 'to_view'])
subprocess.run(['mkdir', 'to_view'])

'''move all the student submission file to the to_view folder'''
submission_folder = "./raw_submission"
id_arr = []
for student in os.listdir(submission_folder):
	if (student == '.DS_Store'):
		continue
	bracket_pos = student.index('(')
	student_name = student[:bracket_pos]
	net_id = student[bracket_pos+1:-1]
	id_arr.append(net_id)

	source = submission_folder + "/" + student + "/Submission attachment(s)/index.html"
	target = "./to_view/" + net_id + "_index.html"
	process = subprocess.run(['cp', source, target])

'''output the all submission ids'''
to_output = {"ids": id_arr}
with open('./to_view/ids.json', 'w') as json_output:
	json_output.write(json.dumps(to_output))

'''move the data file to to_view folder'''
subprocess.run(['cp', 'routes.csv', './to_view/'])
subprocess.run(['cp', 'contries.geo.json', './to_view/'])
subprocess.run(['cp', 'contries.geo.json', './to_view/countries.geo.json'])
subprocess.run(['cp', 'd3.js', './to_view/'])