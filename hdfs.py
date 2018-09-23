#!/usr/bin/python2

print("content-type: text/html")
print("")

print("Welcome to HDFS Cluster")
print("<br/>")


print("""
<form action='hdfs_setup.py'>
Enter  no of DataNode: <input type='text' name='dn' />
<br/>
Enter  no of TaskTrackers: <input type='text' name='tt' />

<input type='submit' />
</form>

""")

