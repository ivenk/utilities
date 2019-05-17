import sys


print "Running clickjacker !!!"
url = sys.argv[1]
f = open(str(url.split(".")[0]) + ".html","w+")
template = '<html>' + '\n'\
'<head>'+ '\n'\
'<title>Clickjack test page</title>'+ '\n'\
'</head>'+'\n'\
'<body>'+'\n'\
'<p>Website is vulnerable to clickjacking!</p>'+'\n'\
'<iframe src="http://www.'+ url + '" width="500" height="500"></iframe>'+'\n'\
'</body>'+'\n'\
'</html>'+'\n'
f.write(template)
f.close()
print "Html file generated."
