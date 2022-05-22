'''
params: hash-input
returns: return binary of the hash-input with length multiple to 512.
'''
import math
from typing import MutableMapping
def prep_input(input):
    # convert input to binary and pad with 1 
    bin_input =   (' '.join(format(ord(x), 'b').rjust(8, '0') for x in input) + " 1").replace(" ","")
    input_length_bin = len(bin_input)-1 # get length of the bin version of the input
    return pad_zeros(bin_input) + add_big_end_length(input_length_bin)

# helper methods
'''
params: initial binary version of the input + (1 as a bit), length varies depending on the input
returns: retuns input padded with zeros where the length is the nearest multiple of 512
         or the one after it in case the prev one has length diff with input < 64
'''
def pad_zeros(input):    
    multiple = math.floor(len(input) /512) + 1
    multiple *= 512
    end = len(input)
    if(len(input) + 64 > multiple):
        multiple += 512
    output = input.ljust(multiple - 64, '0')
    return output

# helper methods
'''
params: binary representation of the hash-input length
return: big_endian representation of the input, 64bit long
'''
def add_big_end_length(input_bin_length):
    big_end_num = bin(input_bin_length).rjust(65, '0').replace('b', '')
    return big_end_num

