import pytest

from binip.functions import *

def test_ip_type():
    '''Test the ip_type() function.'''
    ipv4 = ip_type('192.168.1.24')
    ipv6 = ip_type('ac43:34f:45bc:2c::12')
    subnetv4 = ip_type('192.168.1.24/24')
    subnetv6 = ip_type('ac43:34f:45bc:2c::12/32')
    expected = ['v4', 'v6', 'v4', 'v6']
    actual = [ipv4, ipv6, subnetv4, subnetv6]
    assert expected == actual, 'ip_type function fails.'

def test_ip_type_errors():
    '''Test that the ip_type function raises the correct errors.'''
    with pytest.raises(ValueError):
        test = ip_type('192.168.1')
    with pytest.raises(ValueError):
        test = ip_type('192.168.1.24.48')
    with pytest.raises(ValueError):
        test = ip_type('192.168.1.300')
    with pytest.raises(ValueError):
        test = ip_type('ac43::45bc:2c::12')
    with pytest.raises(ValueError):
        test = ip_type('ac43:34f:45bc:2c:0:12')
    with pytest.raises(ValueError):
        test = ip_type('ac43:34f:45bc:2c:0:0:0:0:12')
    with pytest.raises(ValueError):
        test = ip_type('ac43:34f:45bc:2c:fffk:0:0:12')
    with pytest.raises(ValueError):
        test = ip_type('Nonesense')
    with pytest.raises(TypeError):
        test = ip_type(123)

def test_bin2ip():
    '''Test the bin2ip function.'''
    ipv4_bin = bin2ip('11000000101010000000000100011000')
    ipv6_bin = bin2ip('10101100010000110000001101001111010001011011110000000000001011000000000000000000000000000000000000000000000000000000000000010010')
    expected = ['192.168.1.24', 'ac43:34f:45bc:2c:0:0:0:12']
    actual = [ipv4_bin, ipv6_bin]
    assert expected == actual, 'bin2ip function fails conversion from binary to decimal/hexadecimal.'

def test_bin2ip_error():
    '''Test that the bin2ip function raises the correct errors for using a binary value not 32 or 128 bits long and for using a non binary input.'''
    with pytest.raises(ValueError):
        bin2ip('100100')
    with pytest.raises(ValueError):
        bin2ip('1234')
    with pytest.raises(TypeError):
        bin2ip(1234)