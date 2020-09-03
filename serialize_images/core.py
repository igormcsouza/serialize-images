""" Core Classes

Author: Igor Souza
Version: 0.0.1






"""

import numpy
import io


class MainArraySerializable:
    """Serialize Numpy.Ndarray to string like objects which may be dumps through Json"""
    
    @staticmethod
    def encode_to_string(arr):
        """Encode the array to a Json Serializable string"""
        
        memfile = io.BytesIO()
        numpy.save(memfile, arr)
        memfile.seek(0)
        return memfile.read().decode('latin-1')
    
    @staticmethod
    def decode_to_ndarray(text):
        """Decode the string from MainArraySerializable.encode_to_string to an Numpy.Ndarry"""
        
        memfile = io.BytesIO()
        memfile.write(text.encode('latin-1'))
        memfile.seek(0)
        return numpy.load(memfile)