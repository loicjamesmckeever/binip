from binip.binip import *

subnetv4 = Subnet('192.168.1.0/22')
subnetv6 = Subnet('ac43:34f:45bc:2c::12/34')

pattern4 = subnetv4.toRegex()
pattern6 = subnetv6.toRegex()

ipv4 = IP('192.168.1.24')
print(ipv4.iptype)