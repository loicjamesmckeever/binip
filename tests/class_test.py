import pytest

from binip.classes import IP, Subnet

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
        test = IP('ac43:34f:45bc:2c:fffk:0:0:12')
    with pytest.raises(ValueError):
        test = IP('Nonesense')
    with pytest.raises(TypeError):
        test = IP(123)

#Test Subnet address errors
def test_subnet_address_errors():
    '''Test that the Subnet class raises the proper errors given invalid inputs.'''
    with pytest.raises(ValueError):
        test = Subnet('192.168.1.24')
    with pytest.raises(ValueError):
        test = Subnet('192.168.1/24')
    with pytest.raises(ValueError):
        test = Subnet('192.168.1.0/33')
    with pytest.raises(ValueError):
        test = Subnet('192.168.1.24.48/24')
    with pytest.raises(ValueError):
        test = Subnet('192.168.1.300/24')
    with pytest.raises(ValueError):
        test = Subnet('ac43:34f:45bc:2c::12')
    with pytest.raises(ValueError):
        test = Subnet('ac43:34f:45bc:2c:3:12/48')
    with pytest.raises(ValueError):
        test = Subnet('ac43:34f:45bc:2c::12/129')
    with pytest.raises(ValueError):
        test = Subnet('ac43:34f:45bc:2c:fffk:0:0:0:12/48')
    with pytest.raises(ValueError):
        test = Subnet('ac43:34f:45bc:2c:fffk:0:0:12/48')
    with pytest.raises(ValueError):
        test = Subnet('Nonesense')
    with pytest.raises(TypeError):
        test = Subnet(123)