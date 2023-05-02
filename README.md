# Binip

### Description:

Library for IP networking and subnetting.

### Installation:

Download .whl file and run:

    pip install binip-0.0.1-py3-none-any.whl

### Documentation:

**Classes:**

IP:

Input: IPv4 or IPv6 address.

Attributes:

- address: str, IP address.
- iptype: str, 'v4' or 'v6'.
- expanded(for IPv6 only):str, expanded IPv6 address.
- contracted(for IPv6 only):str, contracted IPv6 address.

Methods:

- validate_address: Validates a given IP address, works for both IPv4 and IPv6.
- ip_type: Returns either 'v4' or 'v6'.
- ipv6_expand: Given a shortened IPv6 address will return the unshortened version.
- ipv6_contract: Returns shortened IPv6 address.  Removes leading zeros and contracts largest set of repeating zero hexadecatets.
- binip: Given an IP will return the IP in binary format.  Works for both IPv4 and IPv6.
- in_subnet Given a subnet will return True if the IP is in that subnet, will return False if otherwise.  Works for both IPv4 and IPv6.

Subnet:

Input: IPv4 or IPv6 subnet address, CIDR notation.

Attributes:

- address: str, subnet address.
- network: str, network address for subnet.
- mask: str, subnet mask.
- iptype: str, 'v4' or 'v6'.
- info: dict, info on subnet.

Methods:

- validate_address: Validates a given IP address, works for both IPv4 and IPv6.
- ip_type: Returns either 'v4' or 'v6'.
- ipv6_expand: Given a shortened IPv6 address will return the unshortened version.
- ipv6_contract: Returns shortened IPv6 address.  Removes leading zeros and contracts largest set of repeating zero hexadecatets.
- binip: Given an IP will return the IP in binary format.  Works for both IPv4 and IPv6.
- in_subnet: Given an IP will return True if the IP is in the subnet, will return False if otherwise.  Works for both IPv4 and IPv6.
- subnet_info: Returns the network address, broadcast address and number of client IPs available for the subnet.
- toRegexv4: Returns a RegEx pattern to match the given IPv4 subnet.
- toRegexv6: Returns a RegEx pattern to match the given IPv6 subnet.
    
**Functions:**

- ip_type: Returns either 'v4' or 'v6'.  Works for both IP and subnet addresses.

        ip_type('192.168.1.24')
        v4

- ipv6_expand: Given a shortened IPv6 address will return the unshortened version.

        ipv6_expand('ac43:34f:45bc:2c::12')
        'ac43:034f:45bc:002c:0000:0000:0000:0012'
    
- ipv6_contract: Returns shortened IPv6 address.  Removes leading zeros and contracts largest set of repeating zero hexadecatets.

        ipv6_contract('ac43:034f:45bc:002c:0000:0000:0000:0012')
        'ac43:34f:45bc:2c::12'
    
- ip2bin: Given an IP address, in either decimal or hexadecimal format, returns the same IP address in binary format.

        ip2bin('192.168.1.24')
        '11000000101010000000000100011000'
    
- bin2ip: Given an IP address in binary format returns the same IP address in either decimal or hexadecimal format.

        bin2ip('11000000101010000000000100011000')
        '192.168.1.24'
    
- in_subnet: Given a subnet and an IP will return True if the IP is in that subnet, will return False if otherwise.  Works for both IPv4 and IPv6.

        in_subnet('192.168.1.24', '192.168.1.0/24')
        True
        in_subnet('192.168.1.24', '192.168.2.0/24')
        False
    
- toRegexv4: Returns a RegEx pattern to match the given IPv4 subnet.

        toRegexv4('192.168.1.0/14')
        '192.[1][6][8-9].[0-9]{1,3}.[0-9]{1,3}|192.[1][7][0-1].[0-9]{1,3}.[0-9]{1,3}'
    
- toRegexv6: Returns a RegEx pattern to match the given IPv6 subnet.

        toRegexv6('ac43:34f:45bc:2c::12/56')
        'ac43:34f:45bc:[0-9a-f]{0,1}:.*|ac43:34f:45bc:[0-9a-f]{0,1}[0-9a-f]{0,1}:.*|ac43:34f:45bc:[1-9a-e]{1}[0-9a-f]{0,1}:.*|ac43:34f:45bc:f[0-9a-f]{0,1}:.*'

### License:

Basic MIT license.
