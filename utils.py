# coding: utf8
# LBE - Lite Block Explorer
# Author: Ondrej Sika <ondrej@ondrejsika.com>
# License: MIT <http://ondrejsika.com/license/mit.txt>

import struct


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


def var_int_serialize(i, f):
    """
    VariableInt serializer
    """
    if i < 0:
        raise ValueError('varint must be non-negative integer')
    elif i < 0xfd:
        f.write(chr(i))
    elif i <= 0xffff:
        f.write(chr(0xfd))
        f.write(struct.pack(b'<H', i))
    elif i <= 0xffffffff:
        f.write(chr(0xfe))
        f.write(struct.pack(b'<I', i))
    else:
        f.write(chr(0xff))
        f.write(struct.pack(b'<Q', i))


def var_int_deserialize(f):
    """
    VariableInt deserializer
    """
    r = ord(f.read(1))
    if r < 0xfd:
        return r
    elif r == 0xfd:
        return struct.unpack(b'<H', f.read(2))[0]
    elif r == 0xfe:
        return struct.unpack(b'<I', f.read(4))[0]
    else:
        return struct.unpack(b'<Q', f.read(8))[0]
