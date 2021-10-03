#! /usr/bin/python3
import cgi
import os
text1 = ""
text2 = ""
table = ""
flag = 0
form = cgi.FieldStorage()
if os.environ["REQUEST_METHOD"] == "POST":
    if "text" in form:
        text = form["text"].value
        flag += 1
    else:
        text1 = "Status: 400 Bad Request"
        text2 = "The variables 'text' and 'size' are both required"
    if "size" in form:
        size = form["size"].value
        try:
            size = int(size)
            flag += 1
        except ValueError:
            text1 = "Status: 400 Bad Request"
            text2 = "The 'size' variable must be an integer"
    else:
        text1 = "Status: 400 Bad Request"
        text2 = "The variables 'text' and 'size' are both required"
else:
    text1 = "Status: 405 Method Not Allowed"
    text2 = "Allow: POST"
if flag==2:
    for i in range(size):
        table += "<tr>"
        if i%2==0:
            for e in range(size):
                if e%2 == 0:
                    table += "<td>" + text + "</td>"
                else:
                    table += "<td></td>"
        else:
            for e in range(size):
                if e%2 == 0:
                    table += "<td></td>"
                else:
                    table += "<td>" + text + "</td>"
        table += "</tr>"
print ("Content-type:text/html\r\n\r\n")
print ('<html>')
print ('<head>')
print ('<title>Random</title>')
print ('</head>')
print ('<body>')
print ('<table>')
print ('%s' % table)
print ('</table>')
print ('<p>%s</p>' % text1)
print ('<br>')
print ('<p>%s</p>' % text2)
print ('</body>')
print ('</html>')
