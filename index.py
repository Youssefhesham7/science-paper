# Creating the HTML file
file_html = open("demo.html", "w")

# Adding the input data to the HTML file
file_html.write('''<html>
<head>
<title>HTML File</title>
</head> 
<body>
<h1>Welcome Finxters</h1>           
<p>Example demonstrating How to generate HTML Files in Python</p> 
</body>
</html>''')

# Saving the data into the HTML file
file_html.close()