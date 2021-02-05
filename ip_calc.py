"""tool for calculate ipV4 address parameters for network equipment"""

ip = input('Input ip-address: ')


def decimal_to_four_octet(arg):
    """ if: mask like /1 - /32 convert to four-octet format
        else: mask like 0.0.0.0 convert to four-octet format
    """
    if len(str(arg)) < 3:
        bit_notation = f'{"1" * 32}'
        convert = f'{bit_notation[:arg]}{"0" * (32 - arg)}'
        new_binary_mask = [convert[_:_ + 8] for _ in range(0, len(convert), 8)]
        return '.'.join(new_binary_mask)
    else:
        separated_ip = arg.split('.')
        octet_ip_list = [f'{"0" * (8 - len(bin(int(_))[2:]))}{bin(int(_))[2:]}'
                         for _ in separated_ip]
        dec_ip = '.'.join(octet_ip_list)
        return dec_ip


def four_octet_to_decimal(arg):
    """convert four-octet binary format to decimal format (0.0.0.0)"""
    separated_octet = arg.split('.')
    dec_ip_list = [f'{int(_, 2)}' for _ in separated_octet]
    dec_ip = '.'.join(dec_ip_list)
    return dec_ip


def octet_to_list_unpac(arg):
    return list(''.join(arg).replace('.', ''))


def network_generator(octet_1, octet_2):
    first_octet = octet_to_list_unpac(octet_1)
    second_octet = octet_to_list_unpac(octet_2)
    mapping_list = list(map(lambda x, y: int(x) * int(y), first_octet, second_octet))
    mapped_string = ''.join(map(str, mapping_list))
    octetting = [mapped_string[_:_ + 8] for _ in range(0, len(mapped_string), 8)]
    return '.'.join(octetting)


def wildcard(arg):
    arg = arg.split('.')
    return f'{255 - int(arg[0])}.' \
           f'{255 - int(arg[1])}.' \
           f'{255 - int(arg[2])}.' \
           f'{255 - int(arg[3])}'


def broad(octet_1, octet_2):
    first_octet = octet_to_list_unpac(decimal_to_four_octet(octet_1))
    second_octet = octet_to_list_unpac(octet_2)
    mapping_list = list(map(lambda x, y: int(x) + int(y), first_octet, second_octet))
    mapped_string = ''.join(map(str, mapping_list))
    octetting = [mapped_string[_:_ + 8] for _ in range(0, len(mapped_string), 8)]
    return '.'.join(octetting)


def host_min(arg):
    arg = arg.split('.')
    return f'{arg[0]}.' \
           f'{arg[1]}.' \
           f'{arg[2]}.' \
           f'{1 + int(arg[3])}'


def host_max(arg):
    arg = four_octet_to_decimal(arg)
    arg = arg.split('.')
    return f'{arg[0]}.' \
           f'{arg[1]}.' \
           f'{arg[2]}.' \
           f'{int(arg[3]) - 1}'


if '/' in ip:
    mask = int(ip[(ip.index('/')) - (len(ip) - 1):])
    ip = ip[:(ip.index('/')) - len(ip)]
else:
    mask = input('Input mask: ')
    # transform to short format
    if len(str(mask)) > 3:
        long = decimal_to_four_octet(mask)
        short = list(map(int, octet_to_list_unpac(long)))
        mask = sum(short)
    else:
        mask = int(mask)


octet_ip = decimal_to_four_octet(ip)  # '11000000.10101010. ...'
octet_mask = decimal_to_four_octet(mask)  # '11111111.11111110. ...'
# map '*' octet_ip and octet_mask
network = network_generator(octet_ip, octet_mask)  # '11000000.10101010. ...'
wildcard_decimal = wildcard(four_octet_to_decimal(octet_mask))  # '0.1.255.255'
# map '+' wildcard and network
broadcast = broad(wildcard_decimal, network)  # '11000000.10101010. ...'
host_min_decimal = host_min(four_octet_to_decimal(network))  # '192.168.0.1'
host_max_decimal = host_max(broadcast)  # 192.169.255.254'

# indent setting for correct output align
mask_indent = 17 - len(four_octet_to_decimal(octet_mask))
network_indent = 17 - len(four_octet_to_decimal(network))

print(
    f'\nAddress:    {ip:<20} {octet_ip:<20}'
    f'\nNetmask:    {four_octet_to_decimal(octet_mask):<8} = {mask:<{mask_indent}} {octet_mask:<20}'
    f'\nWildcard:   {wildcard_decimal:<20} {decimal_to_four_octet(wildcard_decimal):<20}'
    f'\n=>'
    f'\nNetwork:    {four_octet_to_decimal(network):<8} / {mask:<{network_indent}} {network:<20}'
    f'\nBroadcast:  {four_octet_to_decimal(broadcast):<20} {broadcast:<20}'
    f'\nHostMin:    {host_min_decimal:<20} {decimal_to_four_octet(host_min_decimal):<20}'
    f'\nHostMax:    {host_max_decimal:<20} {decimal_to_four_octet(host_max_decimal):<20}'
)
