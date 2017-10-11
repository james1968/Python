#!/bin/bash

# sysinfo_page - A script to produce an HTML file

title="My System Infotmation for $HOSTNAME"
RIGHT_NOW=$(date +"%x %r %Z")
TIME_STAMP="Updated on $RIGHT_NOW by $USER"

cat <<-_EOF_
<html>
<head>
	<title>
	$title
	</title>
</head>

<body>
<h1>$title</h1>
<p>$TIME_STAMP</p>
</body>
</html>
_EOF_
