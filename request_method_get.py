#! /usr/bin/python3
import cgi
import os
form = cgi.FieldStorage()
text1 = ""
text2 = ""
if os.environ["REQUEST_METHOD"] == "GET":
    if "asdf" in form:
        asdf = form["asdf"].value
        for i in range(20):
            text1+=asdf
    else:
        text1 = "Status: 400 Bad Request"
        text2 = "The variables 'asdf' and 'jkl' are both required"
    if "jkl" in form:
        jkl = form["jkl"].value
        for i in range(20):
            text2+=jkl
    else:
        text1 = "Status: 400 Bad Request"
        text2 = "The variables 'asdf' and 'jkl' are both required"
else:
        text1 = "Status: 405 Method Not Allowed"
        text2 = "Allow: GET"
print ("Content-type:text/html\r\n\r\n")
print ('<html>')
print ('<head>')
print ('<title>request method get</title>')
print ('</head>')
print ('<body>')
print ('<p>%s</p>' % text1)
print ('<br>')
print ('<p>%s</p>' % text2)
print ('</body>')
print ('</html>')
