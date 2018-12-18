'''
Author          : Bijan R.Rofoee
Email           : bijan.rofoee@sky.uk
Version         : 0.1
'''

from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader('.')

file = open('../list_lab.txt', 'r')
file_lines = file.readlines()

ip_dict = {}
port_dict = {}

for i in file_lines:
    name = str(i).split()[0]
    ip_dict[name] = str(i).split()[1]
    port_dict[name] = str(i).split()[2]


env = Environment(loader=file_loader)


jumphost = "10.246.65.138"

template = env.get_template('tunnel_gen_template.j2')
tunnel_gen_output = template.render(jumphost=jumphost, ip_dict=ip_dict, port_dict=port_dict)
print(tunnel_gen_output)

output_gen_file = open('tunnel_gen.sh', 'w')
output_gen_file.write(tunnel_gen_output)
output_gen_file.close()


template = env.get_template('tunnel_test_template.j2')
tunnel_test_output = template.render(port_dict=port_dict)
print(tunnel_test_output)

output_test_file = open('tunnel_test.sh', 'w')
output_test_file.write(tunnel_test_output)
output_test_file.close()


template = env.get_template('tunnel_kill_template.j2')
tunnel_kill_output = template.render(port_dict=port_dict)
print(tunnel_kill_output)

output_kill_file = open('tunnel_kill.sh', 'w')
output_kill_file.write(tunnel_kill_output)
output_kill_file.close()

type_dict = {}
for i in port_dict:
    if 'sr' in str(i):
        type_dict[i] = 'ALUSR_Device'
    else:
        type_dict[i] = 'XRDevice'


template = env.get_template('tunnel_python_template.j2')
tunnel_python_output = template.render(port_dict=port_dict, type_dict=type_dict)
print(tunnel_python_output)

output_python_file = open('tunnel_python.py', 'w')
output_python_file.write(tunnel_python_output)
output_python_file.close()


