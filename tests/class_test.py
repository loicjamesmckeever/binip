import pytest

from binip.classes import IP

#Test IP address
def test_address():
    '''Test the address attribute of the IP class.'''
    ipv4 = IP('192.168.1.24')
    ipv6 = IP('ac43:34f:45bc:2c::12')
    expected = ['192.168.1.24', 'ac43:34f:45bc:2c::12']
    actual = [ipv4.address, ipv6.address]
    assert actual == expected, "IP address is incorrect."

#Test IP address errors
def test_address_errors():
    '''Test that the IP class raises the proper errors given invalid inputs.'''
    with pytest.raises(ValueError):
        test = IP('192.168.1')
    with pytest.raises(ValueError):
        test = IP('192.168.1.24.48')
    with pytest.raises(ValueError):
        test = IP('192.168.1.300')
    with pytest.raises(ValueError):
        test = IP('ac43::45bc:2c::12')
    with pytest.raises(ValueError):
        test = IP('ac43:34f:45bc:2c:0:12')
    with pytest.raises(ValueError):
        test = IP('ac43:34f:45bc:2c:0:0:0:0:12')
    with pytest.raises(ValueError):
        test = IP('ac43:34f:45bc:2c:fffk:12')