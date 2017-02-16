import subprocess
import operator

host = "yahoo.com"

dict = {'us-east-1': '23.23.255.255', 'us-west-1': '50.18.56.1', 'us-east-2': '52.14.64.0', 'us-gov-west-1':'52.222.9.163', 'ca-central-1':'52.60.50.0', 'us-west-2':'35.160.63.253', 'eu-west-1':'34.248.60.213', 'eu-central-1':'35.156.63.252', 'eu-west-2':'52.56.34.0', 'ap-northeast-1':'13.112.63.251', 'ap-northeast-2':'52.78.63.252', 'ap-southeast-1':'46.51.216.14', 'ap-southeast-2':'13.54.63.252', 'ap-south-1':'35.154.63.252', 'sa-east-1':'52.67.255.254'}

resultSet = [];

for k, v in dict.items():
		ping = subprocess.Popen(
		["ping", "-c", "3", v],
		stdout = subprocess.PIPE,
		stderr = subprocess.PIPE
		)

		out, error = ping.communicate()
		resultSet.append((k+' ['+v+']',float(out.split('\n')[7].split('/')[4])));

resultSet.sort(key=operator.itemgetter(1))

print resultSet;

i = 1
for x in resultSet:
	print str(i) +'. '+ x[0]+' - ', x[1]
	i = i + 1
