import sys,os
print(os.getcwd())
f=open(os.path.join("F:/","python","paramiko","mk.txt"),'a')
#print(mk)
sys.stdout=f
print("manikanta")