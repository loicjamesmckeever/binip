from binip.functions import *
from binip.classes import *

def ipv6_contract(ipv6):
    ipv6_split = ipv6.split(':')
    ipv6_contracted = []
    for hexadecatet in ipv6_split:
        while hexadecatet[0] == '0' and len(hexadecatet) > 1:
                hexadecatet = hexadecatet[1:]
        ipv6_contracted.append(hexadecatet)
    return ipv6_contracted

subnetv4 = Subnet('192.168.1.0/22')
subnetv6 = Subnet('ac43:34f:45bc:2c::12/34')

pattern4 = subnetv4.toRegex()
pattern6 = subnetv6.toRegex()

ipv4 = IP('192.168.1.24')
ipv6 = 'ac43:0:0:2c:0:0:0:12'

ipv6_expanded = ipv6_expand(ipv6)

#print(ipv6_contract(ipv6))
#print(ipv6_contract(ipv6_expanded))

test_split =ipv6.split(':')

i=0
replacing_zeros = []
while i < 8:
    zeros = []
    if test_split[i] == '0':
        zeros.append(i)
        j=1
        while test_split[i+j] == '0':
            zeros.append(i+j)
            j+=1
        i+=j
        replacing_zeros.append(zeros)
    else:
        i+=1

zeros_to_replace = max(replacing_zeros)
new_test_split = []
for i in range(0,len(test_split)):
    if i in zeros_to_replace:
        new_test_split.append('')
    else:
        new_test_split.append(test_split[i])
     
print(':'.join(new_test_split))