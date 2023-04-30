Binip
Description:
Library for IP networking and subnetting.

Installation:
Download .whl file and run:
pip install binip-0.0.1-py3-none-any.whl


Documentation:
    Classes:
        IP:
            Init: str
                IPv4 or IPv6 address.
            Str: str
                Returns IP address.
            Repr: str
                Returms IP address and IP type.
            Methods:
                validate_address:
                    Validates a given IP address, works for both IPv4 and IPv6.


            Examples:
        Subnet:
            Input: str
                IPv4 or IPv6 subnet address, CIDR notation.
            Methods:

    Functions:
        ip_type:
            Input:
            Returns:
        ipv6_expand:
            Input:
            Returns:
        ipv6_contract:
            Input:
            Returns:
        ip2bin:
            Input:
            Returns:
        bin2ip:
            Input:
            Returns:
        in_subnet:
            Input:
            Returns:
        toRegexv4:
            Input:
            Returns:
        toRegexv6:
            Input:
            Returns:

License:
Basic MIT license.
