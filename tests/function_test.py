import pytest

from binip.functions import *

#Test ip_type function
def test_ip_type():
    '''Test the ip_type() function.'''
    ipv4 = ip_type('192.168.1.24')
    ipv6 = ip_type('ac43:34f:45bc:2c::12')
    neither = ip_type('gobbledeegook')
    expected = ['v4', 'v6', None]
    actual = [ipv4, ipv6, neither]
    assert expected == actual, 'ip_type function fails.'

#Test bin2ip function
def test_bin2ip():
    '''Test the bin2ip() function.'''
    ipv4_bin = bin2ip('11000000101010000000000100011000')
    ipv6_bin = bin2ip('10101100010000110000001101001111010001011011110000000000001011000000000000000000000000000000000000000000000000000000000000010010')
    expected = ['192.168.1.24', 'ac43:34f:45bc:2c:0:0:0:12']
    actual = [ipv4_bin, ipv6_bin]
    assert expected == actual, 'bin2ip function fails conversion from binary to decimal/hexadecimal.'

#Test bin2ip function errors
def test_bin2ip_error():
    '''Test that bin2ip function raises the correct errors for using a binary value not 32 or 128 bits long and for using a non binary input.'''
    with pytest.raises(ValueError):
        bin2ip('100100')
    with pytest.raises(ValueError):
        bin2ip('1234')
    with pytest.raises(TypeError):
        bin2ip(1234)