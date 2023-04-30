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

Methods:

- validate_address: Validates a given IP address, works for both IPv4 and IPv6.

- ip_type: Returns either 'v4' or 'v6'.

- ipv6_expand: Given a shortened IPv6 address will return the unshortened version.

- ipv6_contract: Returns shortened IPv6 address.  Removes leading zeros and contracts largest set of repeating zero hexadecatets.

- binip: Given an IP will return the IP in binary format.  Works for both IPv4 and IPv6.

- in_subnet Given a subnet will return True if the IP is in that subnet, will return False if otherwise.  Works for both IPv4 and IPv6.

Subnet:

Input: IPv4 or IPv6 subnet address, CIDR notation.

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

        >>>ip_type('192.168.1.24')
        >>>v4

- ipv6_expand: Given a shortened IPv6 address will return the unshortened version.
    
- ipv6_contract: Returns shortened IPv6 address.  Removes leading zeros and contracts largest set of repeating zero hexadecatets.
    
- ip2bin: Given an IP address, in either decimal or hexadecimal format, returns the same IP address in binary format.
    
- bin2ip: Given an IP address in binary format returns the same IP address in either decimal or hexadecimal format.
    
- in_subnet: Given a subnet and an IP will return True if the IP is in that subnet, will return False if otherwise.  Works for both IPv4 and IPv6.
    
- toRegexv4: Returns a RegEx pattern to match the given IPv4 subnet.
    
- toRegexv6: Returns a RegEx pattern to match the given IPv6 subnet.

### License:

Basic MIT license.
