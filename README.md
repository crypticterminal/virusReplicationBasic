Basic Python Virus Replication

Tutorial:
https://cranklin.wordpress.com/2012/05/10/how-to-make-a-simple-computer-virus-with-python/

How works

Search recurses through the current folder and finds .py files. If the file is already infected, it skips it. Otherwise, it adds it to the list of files to be infected.

Infect grabs the virus portion of the code from itself and prepends it to each of the victim files. This way, everytime each of the infected python files run, it runs the virus first.
