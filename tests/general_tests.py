from binip.functions import *
from binip.classes import *

subnetv4 = Subnet('192.168.1.0/22')
subnetv6 = Subnet('ac43:34f:45bc:2c::12/34')

pattern4 = subnetv4.toRegex()
pattern6 = subnetv6.toRegex()

ipv4 = IP('192.168.1.24')
ipv6 = 'ac43:0:2c:2b:2a:34:0:12'

ipv6_expanded = ipv6_expand(ipv6)

#print(ipv6_contract(ipv6))
#print(ipv6_contract(ipv6_expanded))

test = ipv6_contract(ipv6)

print(test)