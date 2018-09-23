#!/usr/bin/python2

import commands as sp
import cgi
print("content-type: text/html")
print("")

f=cgi.FieldStorage()
dn=f.getvalue('dn')
tt=f.getvalue('tt')


print("Enter ip of following:")
print("<br/>")
print("<form action='final_setup.py'>")
i=1
print("MN <input type='text' name=mip1 />")
print("<br/>")
while i <= int(dn):
	print("DN{0} <input type='text' name=dip{0} />".format(i))
	print("<br/>")
	i+=1
i=1
while i <= int(tt):
	print("TT{0} <input type='text' name=tip{0} />".format(i))
	print("<br/>")
        i+=1

print("JT <input type='text' name=jip />")
print("""
<br/>
<input type='submit'/>
</form>
""")
