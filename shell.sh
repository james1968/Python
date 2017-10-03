#!/bin/bash

# sysinfo_page - A script to produce an HTML file

title="My System Infotmation"

cat <<-_EOF_
<html>
<head>
	<title>
	$title $HOSTNAME
	</title>
</head>

<body>
<h1>$title $HOSTNAME</h1>
<p>Updated on $(date +"%x %r %Z") by $USER</p>
</body>
</html>
_EOF_
