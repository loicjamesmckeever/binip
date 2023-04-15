#from binip.functions import *
from binip.classes import *
from datetime import datetime

import re

ipv4 = IP('192.168.1.24')
subnet = Subnet('ac43:34f:45bc:2c::12/48')

print(ipv4, subnet)

# test = '34c'
# start = datetime.now()
# regex = r'[0-9a-f]{1,4}'
# comp = re.compile(regex)
# if not comp.fullmatch(test):
#     print('Fail.')
# end = datetime.now()
# print(end - start)
# start = datetime.now()
# if int(test, 16) not in range(0,65536):
#     print('Fail.')
# end = datetime.now()
# print(end - start)