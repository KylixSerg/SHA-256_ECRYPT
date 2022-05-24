from sha_256.compression import perform_chunk_compression, perform_hash
from sha_256.input_prep import prep_input
from sha_256.message_schedule import parse_512_chunks, parse_32bit_words, convert_chunk_to_message_schedule, perform_modular_addition
from sha_256.consts import *

'''
param: input to hash, any alpha numeric value letter upper/lower, 
       number 0-9, special chars @,#,$...
       
returns: hashed value of the input, 256-bit (32 bytes) hash value. 
         represented as a hexadecimal number of 64 digits.
'''
def perform_sha256(string_to_hash):
    input = prep_input(string_to_hash)
    input = parse_512_chunks(input)
    
    h0= bin(int(H0, 16)).replace('0b', '').rjust(32, '0')
    h1= bin(int(H1, 16)).replace('0b', '').rjust(32, '0')
    h2= bin(int(H2, 16)).replace('0b', '').rjust(32, '0')
    h3= bin(int(H3, 16)).replace('0b', '').rjust(32, '0')
    h4= bin(int(H4, 16)).replace('0b', '').rjust(32, '0')
    h5= bin(int(H5, 16)).replace('0b', '').rjust(32, '0')
    h6= bin(int(H6, 16)).replace('0b', '').rjust(32, '0')
    h7= bin(int(H7, 16)).replace('0b', '').rjust(32, '0')

    for chunk in input:
        # convert chunk to message shedule
        current_chunk = convert_chunk_to_message_schedule(parse_32bit_words(chunk))

        # initalize working variables
        

        compressed_chunk = perform_chunk_compression(current_chunk, [h0,h1,h2,h3,h4,h5,h6,h7])
        # bug with the second iteration h0 becomes binary, when exptected hex
        # Add the compressed chunk to the current hash value:
        h0 = perform_modular_addition([h0, compressed_chunk[0]])
        h1 = perform_modular_addition([h1, compressed_chunk[1]])
        h2 = perform_modular_addition([h2, compressed_chunk[2]])
        h3 = perform_modular_addition([h3, compressed_chunk[3]])
        h4 = perform_modular_addition([h4, compressed_chunk[4]])
        h5 = perform_modular_addition([h5, compressed_chunk[5]])
        h6 = perform_modular_addition([h6, compressed_chunk[6]])
        h7 = perform_modular_addition([h7, compressed_chunk[7]])

        
    return perform_hash([h0,h1,h2,h3,h4,h5,h6,h7])

