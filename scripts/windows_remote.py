import winrm
import sys
s = winrm.Session('192.168.99.1', auth=('manik','Rmani123'))
out = s.run_cmd('ipconfig')
print(out.std_out.decode('utf-8'))
# to run ps script >>>>  out= s.run_ps(ps_script)

