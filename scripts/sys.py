import os
import sys
cwd=os.getcwd()
s=sys.stdout
e=sys.stderr
f=open(os.path.join("F:/","python","paramiko","out.log"),'a')
f1=open(os.path.join("F:/","python","paramiko","err.txt"),'a')
sys.stdout=f
sys.stderr=f1
print(os.getlogin())
print(os.name())
sys.stdout=s
sys.stderr=e


