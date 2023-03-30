import re

from binip.binip import IP

#Test IP address
def test_address():
    '''Test the address attribute of the IP class.'''
    ipv4 = IP('192.168.1.24')
    expected = '192.168.1.24'
    actual = ipv4.address
    assert actual == expected, "IP address is incorrect."