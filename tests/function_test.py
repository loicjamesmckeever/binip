import re

from binip.binip import *

#Test ip_type function
def test_ip_type():
    '''Test the ip_type() function.'''
    ipv4 = ip_type('192.168.1.24')
    ipv6 = ip_type('ac43:34f:45bc:2c::12')
    neither = ip_type('gobbledeegook')
    expected = ['v4', 'v6', None]
    actual = [ipv4, ipv6, neither]
    assert expected == actual, 'ip_type function fails.'