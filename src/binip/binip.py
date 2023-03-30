import re

def hex_range(first, last):
    ranges = []
    if first[0] == last[0]:
        if first[1]==last[1]:
            if first[2]==last[2]:
                #Section if the first threee values match
                if first[3].isdigit() and last[3].isalpha():
                    first_range = f'{first[:3].lstrip("0")}[{first[3]}-9a-{last[3]}]'+'{0,1}'
                else:
                    first_range = f'{first[:3].lstrip("0")}[{first[3]}-{last[3]}]'+'{0,1}'
                ranges.append(first_range)
            else:
                #Section if the first two values match
                if first[3].isdigit():
                    first_range = f'{first[:3].lstrip("0")}[{first[3]}-9a-f]' + '{0,1}'
                elif first[3].isalpha():
                    first_range = f'{first[:3].lstrip("0")}[{first[3]}-f]' + '{0,1}'
                ranges.append(first_range)
                if first[2].isdigit():
                    second_range = f'{first[:2].lstrip("0")}[{first[2]}-9a-f]' + '{0,1}[0-9a-f]{0,1}'
                elif first[2].isalpha():
                    second_range = f'{first[:2].lstrip("0")}[{first[2]}-f]' + '{0,1}[0-9a-f]{0,1}'
                ranges.append(second_range)
                first_plus = int(first[2],16)+1
                first_plus = f'{first_plus:01x}'
                last_minus = int(last[2],16)-1
                last_minus = f'{last_minus:01x}'
                if first_plus.isdigit() and last_minus.isalpha():
                    fourth_range = f'{first[:2].lstrip("0")}[{first_plus}-9a-{last_minus}]'+'{1}[0-9a-f]{0,1}'
                else:
                    fourth_range = f'{first[:2].lstrip("0")}[{first_plus}-{last_minus}]'+'{1}[0-9a-f]{0,1}'
                ranges.append(fourth_range)
                if last[3].isdigit():
                    fifth_range = f'{last[:3].lstrip("0")}[0-{last[3]}]' + '{0,1}'
                elif last[3].isalpha():
                    fifth_range = f'{last[:3].lstrip("0")}[0-9a-{last[3]}]' + '{0,1}'
                ranges.append(fifth_range)
        else:
            #section if the first values match
            if first[3].isdigit():
                first_range = f'{first[:3].lstrip("0")}[{first[3]}-9a-f]' + '{0,1}'
            elif first[3].isalpha():
                first_range = f'{first[:3].lstrip("0")}[{first[3]}-f]' + '{0,1}'
            ranges.append(first_range)
            if first[2].isdigit():
                second_range = f'{first[:2].lstrip("0")}[{first[2]}-9a-f]' + '{1}[0-9a-f]{0,1}'
            elif first[2].isalpha():
                second_range = f'{first[:2].lstrip("0")}[{first[2]}-f]' + '{1}[0-9a-f]{0,1}'
            ranges.append(second_range)
            first_plus = int(first[1],16)+1
            first_plus = f'{first_plus:01x}'
            last_minus = int(last[1],16)-1
            last_minus = f'{last_minus:01x}'
            if first_plus.isdigit() and last_minus.isalpha():
                fourth_range = f'{first[:1].lstrip("0")}[{first_plus}-9a-{last_minus}]'+'{1}[0-9a-f]{0,2}'
            else:
                fourth_range = f'{first[:1].lstrip("0")}[{first_plus}-{last_minus}]'+'{1}[0-9a-f]{0,2}'
            ranges.append(fourth_range)
            if last[3].isdigit():
                fifth_range = f'{last[:3].lstrip("0")}[0-{last[3]}]' + '{0,1}'
            elif last[3].isalpha():
                fifth_range = f'{last[:3].lstrip("0")}[0-9a-{last[3]}]' + '{0,1}'
            ranges.append(fifth_range)
            if last[2].isdigit():
                sixth_minus = str(int(last[2])-1)
                sixth_range = f'{last[:2].lstrip("0")}[0-{sixth_minus}]' + '{0,1}[0-9a-f]{0,1}'
            elif last[2].isalpha():
                sixth_minus = int(last[2],16)-1
                sixth_minus = f'{sixth_minus:01x}'
                sixth_range = f'{last[:2].lstrip("0")}[0-9a-{sixth_minus}]' + '{0,1}[0-9a-f]{0,1}'
            ranges.append(sixth_range)
    else:
        #Section if all four values are different
        if first[3].isdigit():
            first_range = f'{first[:3].lstrip("0")}[{first[3]}-9a-f]' + '{0,1}'
        elif first[3].isalpha():
            first_range = f'{first[:3].lstrip("0")}[{first[3]}-f]' + '{0,1}'
        ranges.append(first_range)
        if first[2].isdigit():
            second_range = f'{first[:2].lstrip("0")}[{first[2]}-9a-f]' + '{0,1}[0-9a-f]{0,1}'
        elif first[2].isalpha():
            second_range = f'{first[:2].lstrip("0")}[{first[2]}-f]' + '{1}[0-9a-f]{0,1}'
        ranges.append(second_range)
        if first[1].isdigit():
            third_range = f'{first[:1].lstrip("0")}[{first[1]}-9a-f]' + '{1}[0-9a-f]{0,2}'
        elif first[1].isalpha():
            third_range = f'{first[:1].lstrip("0")}[{first[1]}-f]' + '{1}[0-9a-f]{0,2}'
        ranges.append(third_range)
        first_plus = int(first[0],16)+1
        first_plus = f'{first_plus:01x}'
        last_minus = int(last[0],16)-1
        last_minus = f'{last_minus:01x}'
        if first_plus.isdigit() and last_minus.isalpha():
            fourth_range = f'[{first_plus}-9a-{last_minus}]'+'{0,1}[0-9a-f]{0,3}'
        else:
            fourth_range = f'[{first_plus}-{last_minus}]'+'{0,1}[0-9a-f]{0,3}'
        ranges.append(fourth_range)
        if last[3].isdigit():
            fifth_range = f'{last[:3].lstrip("0")}[0-{last[3]}]' + '{0,1}'
        elif last[3].isalpha():
            fifth_range = f'{last[:3].lstrip("0")}[0-9a-{last[3]}]' + '{0,1}'
        ranges.append(fifth_range)
        if last[2].isdigit():
            sixth_minus = str(int(last[2])-1)
            sixth_range = f'{last[:2].lstrip("0")}[0-{sixth_minus}]' + '{0,1}[0-9a-f]{0,1}'
        elif last[2].isalpha():
            sixth_minus = int(last[2],16)-1
            sixth_minus = f'{sixth_minus:01x}'
            sixth_range = f'{last[:2].lstrip("0")}[0-9a-{sixth_minus}]' + '{1}[0-9a-f]{0,1}'
        ranges.append(sixth_range)
        if last[1].isdigit():
            seventh_minus = str(int(last[1])-1)
            seventh_range = f'{last[:1].lstrip("0")}[0-{seventh_minus}]' + '{1}[0-9a-f]{0,2}'
        elif last[1].isalpha():
            seventh_minus = int(last[1],16)-1
            seventh_minus = f'{seventh_minus:01x}'
            seventh_range = f'{last[:1].lstrip("0")}[0-9a-{seventh_minus}]' + '{1}[0-9a-f]{0,2}'
        ranges.append(seventh_range)
    return ranges

def toRegexv6(subnet, or_logic='|'):
    '''Returns a RegEx pattern to match the given IPv6 subnet.'''
    subnet_split = subnet.split('/')
    ipv6, mask = subnet_split[0], int(subnet_split[1])
    ipv6 = ipv6_expand(ipv6)
    ipv6_split = ipv6.split(':')
    bin_ipv6 = ''
    for item in ipv6_split:
        item = int(item, 16)
        item = f'{item:016b}'
        bin_ipv6 += item
    #Find which hexadecatet, and at which bit of the hexadecatet, is being divided by the mask
    hexadecatet, bit = divmod(mask, 16)
    #Build the RegEx pattern
    regex = ''
    base_pattern = ''
    for i in range(0,hexadecatet):
        if ipv6_split[i] == '0000':
            base_pattern += '[0]{0,1}' + ':'
        else:
            hexadecatet_stripped = ipv6_split[i].lstrip('0')
            base_pattern += hexadecatet_stripped + ':'
    #If bit=0 then no hexadecatet is divided and we can build the RegEx pattern
    if bit == 0:
        base_pattern += '.*/'
        regex = '/' + base_pattern
    else:
        #Get the first and last values of the hexadecatet that is divided
        divided = ipv6_split[hexadecatet+1]
        divided = int(divided, 16)
        divided = f'{divided:016b}'
        unchanged = divided[:bit]
        changed = divided[bit-16:]
        first = unchanged
        last = unchanged
        for i in range(0, len(changed)):
            first += '0'
            last += '1'
        first = int(first, 2)
        first = f'{first:04x}'
        last = int(last, 2)
        last = f'{last:04x}'
        #Get the RegEx ranges for the divided octet
        ranges = hex_range(first, last)
        full_ranges = ['/' + base_pattern + range + ':.*/' for range in ranges]
        regex = f' {or_logic} '.join(full_ranges)
    return regex

def toRegexv4(subnet, or_logic='|'):
    '''Returns a RegEx pattern to match the given IPv4 subnet.  Written by Zephyr Zink.'''
    subnet_split=subnet.split('.')
    mask=int(subnet_split[3].split('/')[1])
    first_octet=int(subnet_split[0])
    second_octet=int(subnet_split[1])
    third_octet=int(subnet_split[2])
    fourth_octet=int(subnet_split[3].split('/')[0])

    start=0
    final=0

    expressions_list=[]
    if mask == 8:
        expressions_list.append(str(first_octet)+'.*')

    if mask == 16:
        expressions_list.append(str(first_octet)+'.'+str(second_octet)+'.*')

    if mask == 24:
        expressions_list.append(str(first_octet)+'.'+str(second_octet)+'.'+str(third_octet)+'.*')

    if mask in (9,10,11,12,13,14,15):
        begin_ex='/'+str(first_octet)+'.'
        end_ex='.[0-9]{1,3}.[0-9]{1,3}/'
        start=second_octet

    if mask in (17,18,19,20,21,22,23):
        begin_ex='/'+str(first_octet)+'.'+str(second_octet)+'.'
        end_ex='.[0-9]{1,3}/'
        start=third_octet

    if mask in (25,26,27,28,29,30,31,32):
        begin_ex='/'+str(first_octet)+'.'+str(second_octet)+'.'+str(third_octet)+'.'
        end_ex='/'
        start=fourth_octet

    if mask in (9,17,25):
        final=start+127
    elif mask in (10,18,26):
        final=start+63
    elif mask in (11,19,27):
        final=start+31
    elif mask in (12,20,28):
        final=start+15
    elif mask in (13,21,29):
        final=start+7
    elif mask in (14,22,30):
        final=start+3
    elif mask in (15,23,31):
        final=start+1
    elif mask in (16,24,32):
        final=start

    one_p=[]
    ten_p=[]
    hund_p=[]
    twohun_p=[]
    list_of_searches=[]

    for i in range(start,final+1):
        if i < 10:
            one_p.append(i)
        elif i >= 10 and i <100:
            ten_p.append(i)
        elif i >=100 and i < 200:
            hund_p.append(i)
        elif i>=200:
            twohun_p.append(i)

    if len(one_p)>0:
        list_of_searches.append('['+str(one_p[0])+'-'+str(one_p[len(one_p)-1])+']')

    if len(ten_p)>0:
        if int(ten_p[len(ten_p)-1]/10)-int(ten_p[0]/10)==0:
            list_of_searches.append('['+str(int(ten_p[0]/10))+']['+str(ten_p[0]%10)+'-'+str(ten_p[len(ten_p)-1]%10)+']')
        elif int(ten_p[len(ten_p)-1]/10)-int(ten_p[0]/10)==1:
            list_of_searches.append('['+str(int(ten_p[0]/10))+']['+str(ten_p[0]%10)+'-9]')
            list_of_searches.append('['+str(int(ten_p[len(ten_p)-1]/10))+'][0-'+str(ten_p[len(ten_p)-1]%10)+']')
        elif int(ten_p[len(ten_p)-1]/10)-int(ten_p[0]/10)==2:
            list_of_searches.append('['+str(int(ten_p[0]/10))+']['+str(ten_p[0]%10)+'-9]')
            list_of_searches.append('['+str(int(ten_p[0]/10)+1)+'][0-9]')
            list_of_searches.append('['+str(int(ten_p[len(ten_p)-1]/10))+'][0-'+str(ten_p[len(ten_p)-1]%10)+']')
        elif int(ten_p[len(ten_p)-1]/10)-int(ten_p[0]/10)>=3:
            list_of_searches.append('['+str(int(ten_p[0]/10))+']['+str(ten_p[0]%10)+'-9]')
            list_of_searches.append('['+str(int(ten_p[0]/10)+1)+'-'+str(int(ten_p[len(ten_p)-1]/10)-1)+'][0-9]')
            list_of_searches.append('['+str(int(ten_p[len(ten_p)-1]/10))+'][0-'+str(ten_p[len(ten_p)-1]%10)+']')

    if len(hund_p)>0:
        for i in range(0,len(hund_p)):
            hund_p[i]=hund_p[i]-100
        if int(hund_p[len(hund_p)-1]/10)-int(hund_p[0]/10)==0:
            list_of_searches.append('[1]['+str(int(hund_p[0]/10))+']['+str(hund_p[0]%10)+'-'+str(hund_p[len(hund_p)-1]%10)+']')
        elif int(hund_p[len(hund_p)-1]/10)-int(hund_p[0]/10)==1:
            list_of_searches.append('[1]['+str(int(hund_p[0]/10))+']['+str(hund_p[0]%10)+'-9]')
            list_of_searches.append('[1]['+str(int(hund_p[len(hund_p)-1]/10))+'][0-'+str(hund_p[len(hund_p)-1]%10)+']')
        elif int(hund_p[len(hund_p)-1]/10)-int(hund_p[0]/10)==2:
            list_of_searches.append('[1]['+str(int(hund_p[0]/10))+']['+str(hund_p[0]%10)+'-9]')
            list_of_searches.append('[1]['+str(int(hund_p[0]/10)+1)+'][0-9]')
            list_of_searches.append('[1]['+str(int(hund_p[len(hund_p)-1]/10))+'][0-'+str(hund_p[len(hund_p)-1]%10)+']')
        elif int(hund_p[len(hund_p)-1]/10)-int(hund_p[0]/10)>=3:
            list_of_searches.append('[1]['+str(int(hund_p[0]/10))+']['+str(hund_p[0]%10)+'-9]')
            list_of_searches.append('[1]['+str(int(hund_p[0]/10)+1)+'-'+str(int(hund_p[len(hund_p)-1]/10)-1)+'][0-9]')
            list_of_searches.append('[1]['+str(int(hund_p[len(hund_p)-1]/10))+'][0-'+str(hund_p[len(hund_p)-1]%10)+']')

    if len(twohun_p)>0:
        for i in range(0,len(twohun_p)):
            twohun_p[i]=twohun_p[i]-200
        if int(twohun_p[len(twohun_p)-1]/10)-int(twohun_p[0]/10)==0:
            list_of_searches.append('[2]['+str(int(twohun_p[0]/10))+']['+str(twohun_p[0]%10)+'-'+str(twohun_p[len(twohun_p)-1]%10)+']')
        elif int(twohun_p[len(twohun_p)-1]/10)-int(twohun_p[0]/10)==1:
            list_of_searches.append('[2]['+str(int(twohun_p[0]/10))+']['+str(twohun_p[0]%10)+'-9]')
            list_of_searches.append('[2]['+str(int(twohun_p[len(twohun_p)-1]/10))+'][0-'+str(twohun_p[len(twohun_p)-1]%10)+']')
        elif int(twohun_p[len(twohun_p)-1]/10)-int(twohun_p[0]/10)==2:
            list_of_searches.append('[2]['+str(int(twohun_p[0]/10))+']['+str(twohun_p[0]%10)+'-9]')
            list_of_searches.append('[2]['+str(int(twohun_p[0]/10)+1)+'][0-9]')
            list_of_searches.append('[2]['+str(int(twohun_p[len(twohun_p)-1]/10))+'][0-'+str(twohun_p[len(twohun_p)-1]%10)+']')
        elif int(twohun_p[len(twohun_p)-1]/10)-int(twohun_p[0]/10)>=3:
            list_of_searches.append('[2]['+str(int(twohun_p[0]/10))+']['+str(twohun_p[0]%10)+'-9]')
            list_of_searches.append('[2]['+str(int(twohun_p[0]/10)+1)+'-'+str(int(twohun_p[len(twohun_p)-1]/10)-1)+'][0-9]')
            list_of_searches.append('[2]['+str(int(twohun_p[len(twohun_p)-1]/10))+'][0-'+str(twohun_p[len(twohun_p)-1]%10)+']')

    for items in list_of_searches:
        if mask in (8,16,24):
            pass
        else:
            expressions_list.append(begin_ex+items+end_ex)
    expressions_list_full =f'{or_logic}'.join([ranget for ranget in expressions_list])
    return expressions_list_full

def ip_type(ip):
    '''Given an IP will return 'v4' if IPv4 or 'v6' if IPv6.'''
    if '.' in ip:
        iptype = 'v4'
    elif ':' in ip:
        iptype = 'v6'
    else:
        iptype = None
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
    
def ipbin(bin_ip):
        '''Given an IP in binary for returns decimal form for IPv4 and hexadecimal form for IPv6.'''
        if len(bin_ip) == 32:
            octets = [bin_ip[i:i+8] for i in range(0,32,8)]
            ip_address = '.'.join([str(int(octet,2)) for octet in octets])
        elif len(bin_ip) == 128:
            hexadecatets = [bin_ip[i:i+16] for i in range(0,128, 16)]
            ip_address = ':'.join([format(int(hexadecatet, 2), 'x') for hexadecatet in hexadecatets])
        else:
            raise ValueError(f'{bin_ip} is not a valid binary IP address.')
        return ip_address
    
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
    
    @staticmethod
    def ipv6_expand(address):
        '''Given a shortened IPv6 address will return the unshortened version.'''
        split = address.split(':')
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
            ip = self.ipv6_expand(ip)
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
        self.mask = int(self.address.split('/')[1])
        
    def validate_address(self, address):
        '''Validate the submitted IP, works for both v4 and v6.'''
        val_err = 'This is not a valid Subnet address.'
        split_subnet = address.split('/')
        if len(split_subnet) == 2:
            network = split_subnet[0]
            mask = int(split_subnet[1])
            if '.' in network:
                if mask not in range(0,33):
                    raise ValueError(val_err + '1')
                ip_split = network.split('.')
                if len(ip_split) != 4:
                    raise ValueError(val_err)
                regex = r'1?\d{,2}|2[0-4]\d|25[0-5]'
                comp = re.compile(regex)
                for octet in ip_split:
                    if comp.fullmatch(octet):
                        return address
                    else:
                        raise ValueError(val_err + '2')
            elif ':' in network:
                if mask not in range(0,129):
                    raise ValueError(val_err + '3')
                expanded = ipv6_expand(address)
                ip_split = expanded.split(':')
                if len(ip_split) != 8:
                    raise ValueError(val_err + '4')
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
    
    @staticmethod
    def ipv6_expand(subnet):
        '''Given a shortened IPv6 subnet address will return the unshortened version.'''
        split = subnet.split(':')
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
        expanded = ':'.join(new_split) + '/' + str(self.mask)
        return expanded
    
    def binip(self):
        '''Given a subnet will return the subnet network address, broadcast address and subnet mask in binary format.  Works for both IPv4 and IPv6.'''
        iptype = self.ip_type()
        network = self.network
        mask = self.mask
        bin_network = ''
        if iptype == 'v4':
            split_network = network.split('.')
            for octet in split_network:
                octet = format(int(octet), '08b')
                bin_network += octet
            bin_mask = ''.join(['1' if i < mask else '0' for i in range(0,32)])
        elif iptype == 'v6':
            network = ipv6_expand(self.network)
            split_network = network.split(':')
            for hexadecatet in split_network:
                hexadecatet = format(int(hexadecatet, 16), '016b')
                bin_network += hexadecatet
            bin_mask = ''.join(['1' if i < mask else '0' for i in range(0,128)])
        bin_broadcast = ''.join([bin_network[:mask],''.join(['1' for bit in bin_network[mask:]])])
        bin_network = ''.join([bin_network[:mask],''.join(['0' for bit in bin_network[mask:]])])
        return bin_network, bin_broadcast, bin_mask
    
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
            
    def subnet_info(self):
        '''Returns the network address, broadcast address and number of client IPs available for the subnet.'''
        bin_network, bin_broadcast, bin_mask = self.binip()
        clients = sum([2**bit for bit in range(0,bin_mask.count('0'))]) - 1
        network = ipbin(bin_network)
        broadcast = ipbin(bin_broadcast)
        first_ip = ipbin(bin_network[:-1]+'1')
        last_ip = ipbin(bin_broadcast[:-1]+'0')
        client_range = first_ip + ' - ' + last_ip
        info = {"Network address:":network, "Broadcast address":broadcast, "Number of client IPs:":clients, "Client IP range:":client_range}
        return info
    
    @staticmethod
    def hex_range(first, last):
        ranges = []
        if first[0] == last[0]:
            if first[1]==last[1]:
                if first[2]==last[2]:
                    #Section if the first threee values match
                    if first[3].isdigit() and last[3].isalpha():
                        first_range = f'{first[:3].lstrip("0")}[{first[3]}-9a-{last[3]}]'+'{0,1}'
                    else:
                        first_range = f'{first[:3].lstrip("0")}[{first[3]}-{last[3]}]'+'{0,1}'
                    ranges.append(first_range)
                else:
                    #Section if the first two values match
                    if first[3].isdigit():
                        first_range = f'{first[:3].lstrip("0")}[{first[3]}-9a-f]' + '{0,1}'
                    elif first[3].isalpha():
                        first_range = f'{first[:3].lstrip("0")}[{first[3]}-f]' + '{0,1}'
                    ranges.append(first_range)
                    if first[2].isdigit():
                        second_range = f'{first[:2].lstrip("0")}[{first[2]}-9a-f]' + '{0,1}[0-9a-f]{0,1}'
                    elif first[2].isalpha():
                        second_range = f'{first[:2].lstrip("0")}[{first[2]}-f]' + '{0,1}[0-9a-f]{0,1}'
                    ranges.append(second_range)
                    first_plus = int(first[2],16)+1
                    first_plus = f'{first_plus:01x}'
                    last_minus = int(last[2],16)-1
                    last_minus = f'{last_minus:01x}'
                    if first_plus.isdigit() and last_minus.isalpha():
                        fourth_range = f'{first[:2].lstrip("0")}[{first_plus}-9a-{last_minus}]'+'{1}[0-9a-f]{0,1}'
                    else:
                        fourth_range = f'{first[:2].lstrip("0")}[{first_plus}-{last_minus}]'+'{1}[0-9a-f]{0,1}'
                    ranges.append(fourth_range)
                    if last[3].isdigit():
                        fifth_range = f'{last[:3].lstrip("0")}[0-{last[3]}]' + '{0,1}'
                    elif last[3].isalpha():
                        fifth_range = f'{last[:3].lstrip("0")}[0-9a-{last[3]}]' + '{0,1}'
                    ranges.append(fifth_range)
            else:
                #section if the first values match
                if first[3].isdigit():
                    first_range = f'{first[:3].lstrip("0")}[{first[3]}-9a-f]' + '{0,1}'
                elif first[3].isalpha():
                    first_range = f'{first[:3].lstrip("0")}[{first[3]}-f]' + '{0,1}'
                ranges.append(first_range)
                if first[2].isdigit():
                    second_range = f'{first[:2].lstrip("0")}[{first[2]}-9a-f]' + '{1}[0-9a-f]{0,1}'
                elif first[2].isalpha():
                    second_range = f'{first[:2].lstrip("0")}[{first[2]}-f]' + '{1}[0-9a-f]{0,1}'
                ranges.append(second_range)
                first_plus = int(first[1],16)+1
                first_plus = f'{first_plus:01x}'
                last_minus = int(last[1],16)-1
                last_minus = f'{last_minus:01x}'
                if first_plus.isdigit() and last_minus.isalpha():
                    fourth_range = f'{first[:1].lstrip("0")}[{first_plus}-9a-{last_minus}]'+'{1}[0-9a-f]{0,2}'
                else:
                    fourth_range = f'{first[:1].lstrip("0")}[{first_plus}-{last_minus}]'+'{1}[0-9a-f]{0,2}'
                ranges.append(fourth_range)
                if last[3].isdigit():
                    fifth_range = f'{last[:3].lstrip("0")}[0-{last[3]}]' + '{0,1}'
                elif last[3].isalpha():
                    fifth_range = f'{last[:3].lstrip("0")}[0-9a-{last[3]}]' + '{0,1}'
                ranges.append(fifth_range)
                if last[2].isdigit():
                    sixth_minus = str(int(last[2])-1)
                    sixth_range = f'{last[:2].lstrip("0")}[0-{sixth_minus}]' + '{0,1}[0-9a-f]{0,1}'
                elif last[2].isalpha():
                    sixth_minus = int(last[2],16)-1
                    sixth_minus = f'{sixth_minus:01x}'
                    sixth_range = f'{last[:2].lstrip("0")}[0-9a-{sixth_minus}]' + '{0,1}[0-9a-f]{0,1}'
                ranges.append(sixth_range)
        else:
            #Section if all four values are different
            if first[3].isdigit():
                first_range = f'{first[:3].lstrip("0")}[{first[3]}-9a-f]' + '{0,1}'
            elif first[3].isalpha():
                first_range = f'{first[:3].lstrip("0")}[{first[3]}-f]' + '{0,1}'
            ranges.append(first_range)
            if first[2].isdigit():
                second_range = f'{first[:2].lstrip("0")}[{first[2]}-9a-f]' + '{0,1}[0-9a-f]{0,1}'
            elif first[2].isalpha():
                second_range = f'{first[:2].lstrip("0")}[{first[2]}-f]' + '{1}[0-9a-f]{0,1}'
            ranges.append(second_range)
            if first[1].isdigit():
                third_range = f'{first[:1].lstrip("0")}[{first[1]}-9a-f]' + '{1}[0-9a-f]{0,2}'
            elif first[1].isalpha():
                third_range = f'{first[:1].lstrip("0")}[{first[1]}-f]' + '{1}[0-9a-f]{0,2}'
            ranges.append(third_range)
            first_plus = int(first[0],16)+1
            first_plus = f'{first_plus:01x}'
            last_minus = int(last[0],16)-1
            last_minus = f'{last_minus:01x}'
            if first_plus.isdigit() and last_minus.isalpha():
                fourth_range = f'[{first_plus}-9a-{last_minus}]'+'{0,1}[0-9a-f]{0,3}'
            else:
                fourth_range = f'[{first_plus}-{last_minus}]'+'{0,1}[0-9a-f]{0,3}'
            ranges.append(fourth_range)
            if last[3].isdigit():
                fifth_range = f'{last[:3].lstrip("0")}[0-{last[3]}]' + '{0,1}'
            elif last[3].isalpha():
                fifth_range = f'{last[:3].lstrip("0")}[0-9a-{last[3]}]' + '{0,1}'
            ranges.append(fifth_range)
            if last[2].isdigit():
                sixth_minus = str(int(last[2])-1)
                sixth_range = f'{last[:2].lstrip("0")}[0-{sixth_minus}]' + '{0,1}[0-9a-f]{0,1}'
            elif last[2].isalpha():
                sixth_minus = int(last[2],16)-1
                sixth_minus = f'{sixth_minus:01x}'
                sixth_range = f'{last[:2].lstrip("0")}[0-9a-{sixth_minus}]' + '{1}[0-9a-f]{0,1}'
            ranges.append(sixth_range)
            if last[1].isdigit():
                seventh_minus = str(int(last[1])-1)
                seventh_range = f'{last[:1].lstrip("0")}[0-{seventh_minus}]' + '{1}[0-9a-f]{0,2}'
            elif last[1].isalpha():
                seventh_minus = int(last[1],16)-1
                seventh_minus = f'{seventh_minus:01x}'
                seventh_range = f'{last[:1].lstrip("0")}[0-9a-{seventh_minus}]' + '{1}[0-9a-f]{0,2}'
            ranges.append(seventh_range)
        return ranges

    @staticmethod
    def toRegexv6(subnet, or_logic='|'):
        '''Returns a RegEx pattern to match the given IPv6 subnet.'''
        subnet_split = subnet.split('/')
        ipv6, mask = subnet_split[0], int(subnet_split[1])
        ipv6 = ipv6_expand(ipv6)
        ipv6_split = ipv6.split(':')
        bin_ipv6 = ''
        for item in ipv6_split:
            item = int(item, 16)
            item = f'{item:016b}'
            bin_ipv6 += item
        #Find which octet, and at which bit of the octet, is being divided by the mask
        octet, bit = divmod(mask, 16)
        #Build the RegEx pattern
        regex = ''
        base_pattern = ''
        for i in range(0,octet):
            if ipv6_split[i] == '0000':
                base_pattern += '[0]{0,1}' + ':'
            else:
                octet_stripped = ipv6_split[i].lstrip('0')
                base_pattern += octet_stripped + ':'
        #If bit=0 then no octet is divided and we can build the RegEx pattern
        if bit == 0:
            base_pattern += '.*/'
            regex = '/' + base_pattern
        else:
            #Get the first and last values of the octet that is divided
            divided = ipv6_split[octet+1]
            divided = int(divided, 16)
            divided = f'{divided:016b}'
            unchanged = divided[:bit]
            changed = divided[bit-16:]
            first = unchanged
            last = unchanged
            for i in range(0, len(changed)):
                first += '0'
                last += '1'
            first = int(first, 2)
            first = f'{first:04x}'
            last = int(last, 2)
            last = f'{last:04x}'
            #Get the RegEx ranges for the divided octet
            ranges = hex_range(first, last)
            full_ranges = ['/' + base_pattern + range + ':.*/' for range in ranges]
            regex = f'{or_logic}'.join(full_ranges)
        return regex

    @staticmethod
    def toRegexv4(subnet, or_logic='|'):
        '''Returns a RegEx pattern to match the given IPv4 subnet.  Written by Zephyr Zink.'''
        subnet_split=subnet.split('.')
        mask=int(subnet_split[3].split('/')[1])
        first_octet=int(subnet_split[0])
        second_octet=int(subnet_split[1])
        third_octet=int(subnet_split[2])
        fourth_octet=int(subnet_split[3].split('/')[0])

        start=0
        final=0

        expressions_list=[]
        if mask == 8:
            expressions_list.append(str(first_octet)+'.*')

        if mask == 16:
            expressions_list.append(str(first_octet)+'.'+str(second_octet)+'.*')

        if mask == 24:
            expressions_list.append(str(first_octet)+'.'+str(second_octet)+'.'+str(third_octet)+'.*')

        if mask in (9,10,11,12,13,14,15):
            begin_ex='/'+str(first_octet)+'.'
            end_ex='.[0-9]{1,3}.[0-9]{1,3}/'
            start=second_octet

        if mask in (17,18,19,20,21,22,23):
            begin_ex='/'+str(first_octet)+'.'+str(second_octet)+'.'
            end_ex='.[0-9]{1,3}/'
            start=third_octet

        if mask in (25,26,27,28,29,30,31,32):
            begin_ex='/'+str(first_octet)+'.'+str(second_octet)+'.'+str(third_octet)+'.'
            end_ex='/'
            start=fourth_octet

        if mask in (9,17,25):
            final=start+127
        elif mask in (10,18,26):
            final=start+63
        elif mask in (11,19,27):
            final=start+31
        elif mask in (12,20,28):
            final=start+15
        elif mask in (13,21,29):
            final=start+7
        elif mask in (14,22,30):
            final=start+3
        elif mask in (15,23,31):
            final=start+1
        elif mask in (16,24,32):
            final=start

        one_p=[]
        ten_p=[]
        hund_p=[]
        twohun_p=[]
        list_of_searches=[]

        for i in range(start,final+1):
            if i < 10:
                one_p.append(i)
            elif i >= 10 and i <100:
                ten_p.append(i)
            elif i >=100 and i < 200:
                hund_p.append(i)
            elif i>=200:
                twohun_p.append(i)

        if len(one_p)>0:
            list_of_searches.append('['+str(one_p[0])+'-'+str(one_p[len(one_p)-1])+']')

        if len(ten_p)>0:
            if int(ten_p[len(ten_p)-1]/10)-int(ten_p[0]/10)==0:
                list_of_searches.append('['+str(int(ten_p[0]/10))+']['+str(ten_p[0]%10)+'-'+str(ten_p[len(ten_p)-1]%10)+']')
            elif int(ten_p[len(ten_p)-1]/10)-int(ten_p[0]/10)==1:
                list_of_searches.append('['+str(int(ten_p[0]/10))+']['+str(ten_p[0]%10)+'-9]')
                list_of_searches.append('['+str(int(ten_p[len(ten_p)-1]/10))+'][0-'+str(ten_p[len(ten_p)-1]%10)+']')
            elif int(ten_p[len(ten_p)-1]/10)-int(ten_p[0]/10)==2:
                list_of_searches.append('['+str(int(ten_p[0]/10))+']['+str(ten_p[0]%10)+'-9]')
                list_of_searches.append('['+str(int(ten_p[0]/10)+1)+'][0-9]')
                list_of_searches.append('['+str(int(ten_p[len(ten_p)-1]/10))+'][0-'+str(ten_p[len(ten_p)-1]%10)+']')
            elif int(ten_p[len(ten_p)-1]/10)-int(ten_p[0]/10)>=3:
                list_of_searches.append('['+str(int(ten_p[0]/10))+']['+str(ten_p[0]%10)+'-9]')
                list_of_searches.append('['+str(int(ten_p[0]/10)+1)+'-'+str(int(ten_p[len(ten_p)-1]/10)-1)+'][0-9]')
                list_of_searches.append('['+str(int(ten_p[len(ten_p)-1]/10))+'][0-'+str(ten_p[len(ten_p)-1]%10)+']')

        if len(hund_p)>0:
            for i in range(0,len(hund_p)):
                hund_p[i]=hund_p[i]-100
            if int(hund_p[len(hund_p)-1]/10)-int(hund_p[0]/10)==0:
                list_of_searches.append('[1]['+str(int(hund_p[0]/10))+']['+str(hund_p[0]%10)+'-'+str(hund_p[len(hund_p)-1]%10)+']')
            elif int(hund_p[len(hund_p)-1]/10)-int(hund_p[0]/10)==1:
                list_of_searches.append('[1]['+str(int(hund_p[0]/10))+']['+str(hund_p[0]%10)+'-9]')
                list_of_searches.append('[1]['+str(int(hund_p[len(hund_p)-1]/10))+'][0-'+str(hund_p[len(hund_p)-1]%10)+']')
            elif int(hund_p[len(hund_p)-1]/10)-int(hund_p[0]/10)==2:
                list_of_searches.append('[1]['+str(int(hund_p[0]/10))+']['+str(hund_p[0]%10)+'-9]')
                list_of_searches.append('[1]['+str(int(hund_p[0]/10)+1)+'][0-9]')
                list_of_searches.append('[1]['+str(int(hund_p[len(hund_p)-1]/10))+'][0-'+str(hund_p[len(hund_p)-1]%10)+']')
            elif int(hund_p[len(hund_p)-1]/10)-int(hund_p[0]/10)>=3:
                list_of_searches.append('[1]['+str(int(hund_p[0]/10))+']['+str(hund_p[0]%10)+'-9]')
                list_of_searches.append('[1]['+str(int(hund_p[0]/10)+1)+'-'+str(int(hund_p[len(hund_p)-1]/10)-1)+'][0-9]')
                list_of_searches.append('[1]['+str(int(hund_p[len(hund_p)-1]/10))+'][0-'+str(hund_p[len(hund_p)-1]%10)+']')

        if len(twohun_p)>0:
            for i in range(0,len(twohun_p)):
                twohun_p[i]=twohun_p[i]-200
            if int(twohun_p[len(twohun_p)-1]/10)-int(twohun_p[0]/10)==0:
                list_of_searches.append('[2]['+str(int(twohun_p[0]/10))+']['+str(twohun_p[0]%10)+'-'+str(twohun_p[len(twohun_p)-1]%10)+']')
            elif int(twohun_p[len(twohun_p)-1]/10)-int(twohun_p[0]/10)==1:
                list_of_searches.append('[2]['+str(int(twohun_p[0]/10))+']['+str(twohun_p[0]%10)+'-9]')
                list_of_searches.append('[2]['+str(int(twohun_p[len(twohun_p)-1]/10))+'][0-'+str(twohun_p[len(twohun_p)-1]%10)+']')
            elif int(twohun_p[len(twohun_p)-1]/10)-int(twohun_p[0]/10)==2:
                list_of_searches.append('[2]['+str(int(twohun_p[0]/10))+']['+str(twohun_p[0]%10)+'-9]')
                list_of_searches.append('[2]['+str(int(twohun_p[0]/10)+1)+'][0-9]')
                list_of_searches.append('[2]['+str(int(twohun_p[len(twohun_p)-1]/10))+'][0-'+str(twohun_p[len(twohun_p)-1]%10)+']')
            elif int(twohun_p[len(twohun_p)-1]/10)-int(twohun_p[0]/10)>=3:
                list_of_searches.append('[2]['+str(int(twohun_p[0]/10))+']['+str(twohun_p[0]%10)+'-9]')
                list_of_searches.append('[2]['+str(int(twohun_p[0]/10)+1)+'-'+str(int(twohun_p[len(twohun_p)-1]/10)-1)+'][0-9]')
                list_of_searches.append('[2]['+str(int(twohun_p[len(twohun_p)-1]/10))+'][0-'+str(twohun_p[len(twohun_p)-1]%10)+']')

        for items in list_of_searches:
            if mask in (8,16,24):
                pass
            else:
                expressions_list.append(begin_ex+items+end_ex)
        expressions_list_full =f'{or_logic}'.join([ranget for ranget in expressions_list])
        return expressions_list_full
    
    def toRegex(self, or_logic='|'):
        if self.ip_type() == 'v4':
            regex_pattern = self.toRegexv4(self.address, or_logic)
        elif self.ip_type() == 'v6':
            regex_pattern = self.toRegexv6(self.address, or_logic)
        return regex_pattern