import numpy

from serialize_images import __version__
from serialize_images.core import MainArraySerializable


def test_version():
    assert __version__ == '0.1.2'

def test_core_encode():
    result = MainArraySerializable.encode_to_string(numpy.ndarray([0]))
    print(result)
    assert type(result) == str

def test_core_decode():
    result = MainArraySerializable.decode_to_ndarray(
        "\x93NUMPY\x01\x00v\x00{'descr': '<f8', 'fortran_order': False, 'shape': (0,), }                                                            \n"
    )
    assert type(result) == numpy.ndarray
