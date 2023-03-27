import re

def ip_type(ip):
    '''Given an IP will return 'v4' if IPv4 or 'v6' if IPv6.'''
    if '.' in ip:
        iptype = 'v4'
    elif ':' in ip:
        iptype = 'v6'
    return iptype

def ipv6_expand(ipv6):
    '''Given a shortened IPv6 address will return the unshortened version.'''
    split = ipv6.split(':')
    zeros = ['0000' for i in range(0,9-len(split))]
    new_split = []
    for octet in split:
        if octet == '':
            new_split += zeros
        elif octet == '0':
            new_split.append('0000')
        elif len(octet) < 4:
            for i in range(0,4-len(octet)):
                octet = '0' + octet
            new_split.append(octet)
        else:
            new_split.append(octet)
    new_ipv6 = ':'.join(new_split)
    return new_ipv6

def ip2bin(ip):
    '''Given an IP split will return the IP in binary format.  Works for both IPv4 and IPv6.'''
    iptype = ip_type(ip)
    bin_ip = ''
    if iptype == 'v4':
        split_ip = ip.split('.')
        for octet in split_ip:
            octet = format(int(octet), '08b')
            bin_ip += octet
    elif iptype == 'v6':
        ip = ipv6_expand(ip)
        split_ip = ip.split('.')
        for octet in split_ip:
            octet = format(int(octet, 16), '016b')
            bin_ip += octet
    return bin_ip

def subnet2bin(subnet):
    '''Given a subnet will split it into the subnet mask(decimal) and the network IP(binary).  Works for both IPv4 and IPv6.'''


def in_subnet(ip, subnet):
    '''Given an IP and a subnet will return True if that IP is in that subnet, will return False if otherwise.  Works for both IPv4 and IPv6.'''
    #Determine if the IP and subnet are v4 or v6 and then split the IP and subnet by octet and get the mask from the subnet.
    split_ip = ip.split('.')
    split_subnet = subnet.split('/')
    mask = int(split_subnet[1])
    split_network = split_subnet[0].split('.')
    if len(split_ip) == 1 and len(split_network) == 1:
        mode = 'v6'
        ip = ipv6_expand(ip)
        split_ip = ip.split(':')
        network = ipv6_expand(split_subnet[0])
        split_network = network.split(':')
    elif len(split_ip) != len(split_subnet): #This is the case if the function is given an IP and a subnet of different versions.
        return False
    else:
        mode = 'v4'
    #Convert the IP to binary
    bin_ip = ip2bin(split_ip, mode)
    #Convert the subnet to binary
    bin_network = ip2bin(split_network, mode)
    #Compare the network portion of the IP and the subnet to see if they match.
    if bin_ip[:mask] == bin_network[:mask]:
        return True
    else:
        return False
    
class IP:
    def __init__(self, address):
        self.address = self.validate_address(address)
        self.iptype = self.ip_type()
        
    def validate_address(self, address):
        '''Validate the submitted IP, works for both v4 and v6.'''
        val_err = 'This is not a valid IP address.'
        if '.' in address:
            ip_split = address.split('.')
            if len(ip_split) != 4:
                raise ValueError(val_err)
            regex = r'1?\d{,2}|2[0-4]\d|25[0-5]'
            comp = re.compile(regex)
            for octet in ip_split:
                if comp.fullmatch(octet):
                    return address
                else:
                    raise ValueError(val_err)
        elif ':' in address:
            expanded = ipv6_expand(address)
            ip_split = expanded.split(':')
            if len(ip_split) != 8:
                raise ValueError(val_err)
            regex = r'[0-9a-f]{,4}'
            comp = re.compile(regex)
            for hexadecatet in ip_split:
                if comp.fullmatch(hexadecatet):
                    return address
                else:
                    raise ValueError(val_err)
        else:
            raise ValueError(val_err)

    def __str__(self):
        return f'{self.address}'
        
    def ip_type(self):
        '''Given an IP will return 'v4' if IPv4 or 'v6' if IPv6.'''
        if '.' in self.address:
            iptype = 'v4'
        elif ':' in self.address:
            iptype = 'v6'
        return iptype
    
    def ipv6_expand(self):
        '''Given a shortened IPv6 address will return the unshortened version.'''
        split = self.address.split(':')
        zeros = ['0000' for i in range(0,9-len(split))]
        new_split = []
        for hexadecatet in split:
            if hexadecatet == '':
                new_split += zeros
            elif hexadecatet == '0':
                new_split.append('0000')
            elif len(hexadecatet) < 4:
                for i in range(0,4-len(hexadecatet)):
                    hexadecatet = '0' + hexadecatet
                new_split.append(hexadecatet)
            else:
                new_split.append(hexadecatet)
        expanded = ':'.join(new_split)
        return expanded
    
    def binip(self):
        '''Given an IP will return the IP in binary format.  Works for both IPv4 and IPv6.'''
        iptype = self.ip_type()
        ip = self.address
        bin_ip = ''
        if iptype == 'v4':
            split_ip = ip.split('.')
            for octet in split_ip:
                octet = format(int(octet), '08b')
                bin_ip += octet
        elif iptype == 'v6':
            ip = self.ipv6_expand()
            split_ip = ip.split(':')
            for hexadecatet in split_ip:
                hexadecatet = format(int(hexadecatet, 16), '016b')
                bin_ip += hexadecatet
        return bin_ip
    
    def in_subnet(self, subnet):
        '''Given a subnet will return True if the IP is in that subnet, will return False if otherwise.  Works for both IPv4 and IPv6.'''
        #Determine if the IP and subnet are v4 or v6 and then split the IP and subnet by octet and get the mask from the subnet.
        network = Subnet(subnet)
        iptype = self.ip_type()
        subnettype = network.ip_type()
        if subnettype != iptype:
            raise ValueError('IP and subnet are not the same version.')
        else:
            bin_ip = self.binip()
            bin_network = network.binip()[0]
            mask = int(network.mask)
            if bin_ip[:mask] == bin_network[:mask]:
                return True
            else:
                return False
            
class Subnet:
    def __init__(self, address):
        self.address = self.validate_address(address)
        self.network = self.address.split('/')[0]
        self.mask = self.address.split('/')[1]
        
    def validate_address(self, address):
        '''Validate the submitted IP, works for both v4 and v6.'''
        val_err = 'This is not a valid Subnet address.'
        split_subnet = address.split('/')
        if len(split_subnet) == 2:
            network = split_subnet[0]
            mask = split_subnet[1]
            if '.' in network:
                if int(mask) not in range(0,33):
                    raise ValueError(val_err)
                ip_split = network.split('.')
                if len(ip_split) != 4:
                    raise ValueError(val_err)
                regex = r'1?\d{,2}|2[0-4]\d|25[0-5]'
                comp = re.compile(regex)
                for octet in ip_split:
                    if comp.fullmatch(octet):
                        return address
                    else:
                        raise ValueError(val_err)
            elif ':' in network:
                if int(mask) not in range(0,129):
                    raise ValueError(val_err)
                expanded = ipv6_expand(address)
                ip_split = expanded.split(':')
                if len(ip_split) != 8:
                    raise ValueError(val_err)
                regex = r'[0-9a-f]{,4}'
                comp = re.compile(regex)
                for hexadecatet in ip_split:
                    if comp.fullmatch(hexadecatet):
                        return address
                    else:
                        raise ValueError(val_err)
            else:
                raise ValueError(val_err)
        else:
            raise ValueError(val_err)
    
    def __str__(self):
        return f'{self.address}'
    
    def ip_type(self):
        '''Given a subnet address will return 'v4' if IPv4 or 'v6' if IPv6.'''
        if '.' in self.address:
            iptype = 'v4'
        elif ':' in self.address:
            iptype = 'v6'
        return iptype
    
    def ipv6_expand(self):
        '''Given a shortened IPv6 subnet address will return the unshortened version.'''
        split = self.network.split(':')
        zeros = ['0000' for i in range(0,9-len(split))]
        new_split = []
        for hexadecatet in split:
            if hexadecatet == '':
                new_split += zeros
            elif hexadecatet == '0':
                new_split.append('0000')
            elif len(hexadecatet) < 4:
                for i in range(0,4-len(hexadecatet)):
                    hexadecatet = '0' + hexadecatet
                new_split.append(hexadecatet)
            else:
                new_split.append(hexadecatet)
        expanded = ':'.join(new_split) + '/' + self.mask
        return expanded
    
    def binip(self):
        '''Given a subnet will return the subnet address and subnet mask in binary format.  Works for both IPv4 and IPv6.'''
        iptype = self.ip_type()
        network = self.network
        mask = self.mask
        bin_network = ''
        if iptype == 'v4':
            split_network = network.split('.')
            for octet in split_network:
                octet = format(int(octet), '08b')
                bin_network += octet
            bin_mask = ''.join(['1' if i < int(mask) else '0' for i in range(0,33)])
        elif iptype == 'v6':
            network = self.ipv6_expand().split('/')[0]
            split_network = network.split(':')
            for hexadecatet in split_network:
                hexadecatet = format(int(hexadecatet, 16), '016b')
                bin_network += hexadecatet
            bin_mask = ''.join(['1' if i < int(mask) else '0' for i in range(0,129)])
        return bin_network, bin_mask
    
    def in_subnet(self, ip):
        '''Given an IP will return True if that IP is in the subnet, will return False if otherwise.  Works for both IPv4 and IPv6.'''
        #Determine if the IP and subnet are v4 or v6 and then split the IP and subnet by octet and get the mask from the subnet.
        ip = IP(ip)
        iptype = ip.ip_type()
        subnettype = self.ip_type()
        if subnettype != iptype:
            raise ValueError('IP and subnet are not the same version.')
        else:
            bin_ip = ip.binip()
            bin_network = self.binip()[0]
            mask = int(self.mask)
            if bin_ip[:mask] == bin_network[:mask]:
                return True
            else:
                return False
