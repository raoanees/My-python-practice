import json
import pickle

f = open("newfile.txt",'w');
f.write("Hello World to files and directories")
f.close()

f = open("jsonfile.txt",'w')
json.dump([1,'Ali',3.45],f)
json.dump([2,'Ahmed',3.21],f)
f.close()

f.close()
