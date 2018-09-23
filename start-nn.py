#!/usr/bin/python2

print("content-type: text/html")
print("")

import commands as sp

a=sp.getstatusoutput("sudo ansible-playbook /ws_ansible/master.yml -i /myhosts/hosts")

if a[0]==0:
	print "done"
else:
	print a
