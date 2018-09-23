#!/usr/bin/python2

print("content-type: text/html")
print("")

#print("hello")

import cgi
import commands as sp

form=cgi.FormContent()
print(form)

master=[]
slave=[]
job=[]
task=[]
for i in form.keys():
	if 'm' in i:
		master.append(i)
	elif 'd' in i:
		slave.append(i)	
	elif 'j' in i:
		job.append(i)
	elif 't' in i:
		task.append(i)
sp.getoutput("sudo chown apache /ws_ansible")
fdir=open('/ws_ansible/dir_var.yml','w')
d=sp.getoutput("date +%F%T")
fdir.write("master: m{} \n".format(d))
fdir.write("slave: s{} \n".format(d))
fdir.write("mip1: {} \n".format(form.get('mip1')[0]))
fdir.write("jip: {} \n".format(form.get('jip')[0]))
fdir.close()



sp.getoutput("sudo chown apache /myhosts")
fhost=open('/myhosts/hosts','w')

fhost.write("[master]\n")
for i in master:
	fhost.write(form[i][0] + '\n')
fhost.write("[slave]\n")
for i in slave:
	fhost.write(form[i][0]+'\n')
fhost.write("[job]\n")
for i in job:
	fhost.write(form[i][0]+'\n')

fhost.write("[task]\n")
for i in task:
	fhost.write(form[i][0]+'\n')

fhost.close()

print("""
WE RECIEVED YOUR DATA SUCCESFULLY
<br/>
CLICK TO START:
<br/>
<form action='start-nn.py'>
NAMENODE:<input type='submit'/>

<br/>
</form>
<form action='start-jt.py'>
JOBTRACKER:<input type='submit'/> 
<br/>
</form>

<form action='start-dn.py'>
DATANODE:<input type='submit'/> 
<br/>
</form>

<form action='start-tt.py'>
TASKTRACKER:<input type='submit'/>
</form>
""")
