A form that targets request_method_get.py (make sure to include the correct path, which will include
/cgi-bin/) uses the GET method, and has two text fields for the variables.
	"curl -d asdf=text -d jkl=ok -G http://127.0.0.1:80/cgi-bin/request_method_get.py"
A form that targets the same page, but uses the POST method.
	"curl -X POST -d “asdf=text&jkl=ok” http://127.0.0.1:80/cgi-bin/request_method_get.py"
A form that targets request_method_post.py and uses the POST method. It must have a type=text
field for the variable text and a type=number field for the variable size.
	"curl -X POST -d "text=text&size=3" http://127.0.0.1:80/cgi-bin/request_method_post.py"
A form that targets the same page with the same method, but has an error because it doesn’t mention
the right variables.
	"curl -X POST -d "text=text&size=ok” http://127.0.0.1:80/cgi-bin/request_method_post.py"