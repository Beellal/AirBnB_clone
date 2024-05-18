AirBnB Clone - The Console

This project is a command-line console clone of the AirBnB website. Currently, it functions as an independent console but is intended to be integrated with other components of the website in the future, including HTML, databases, and API integrations using Flask and other software.

Description of the Command Interpreter

The command interpreter is designed for testing and developer use. It operates as a shell-like interpreter that accepts commands, executes them, and performs specific tasks. The interpreter utilizes the Cmd class from the cmd module for its functionality.

Start It
To start the command interpreter, run the console.py file. Ensure that this file cannot be imported directly; it can only be executed.

To Use It

//Interactive Mode:

$ ./console.py
(hbnb) help
Documented commands (type help):
========================================
EOF  help  quit
(hbnb) quit
$

//Non-Interactive Mode (similar to the Shell project in C):

$ echo "help" | ./console.py
(hbnb)
Documented commands (type help):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)
Documented commands (type help):
========================================
EOF  help  quit
(hbnb)
$