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
    input = parse_512_chunks(prep_input(string_to_hash))
    h0,h1,h2,h3,h4,h5,h6,h7 = H0,H1,H2,H3,H4,H5,H6,H7

    for chunk in input:
        current_chunk = parse_32bit_words(chunk)
        # convert chunk to message shedule
        current_chunk = convert_chunk_to_message_schedule(current_chunk)

        # initalize working variables
        a = bin(int(H0, 16)).replace('0b', '').rjust(32, '0')
        b = bin(int(H1, 16)).replace('0b', '').rjust(32, '0')
        c = bin(int(H2, 16)).replace('0b', '').rjust(32, '0')
        d = bin(int(H3, 16)).replace('0b', '').rjust(32, '0')
        e = bin(int(H4, 16)).replace('0b', '').rjust(32, '0')
        f = bin(int(H5, 16)).replace('0b', '').rjust(32, '0')
        g = bin(int(H6, 16)).replace('0b', '').rjust(32, '0')
        h = bin(int(H7, 16)).replace('0b', '').rjust(32, '0')

        compressed_chunk = perform_chunk_compression(current_chunk, [a,b,c,d,e,f,g,h])

        # Add the compressed chunk to the current hash value:
        h0 = perform_modular_addition([bin(int(h0, 16)).replace('0b', '').rjust(32, '0'), compressed_chunk[0]])
        h1 = perform_modular_addition([bin(int(h1, 16)).replace('0b', '').rjust(32, '0'), compressed_chunk[1]])
        h2 = perform_modular_addition([bin(int(h2, 16)).replace('0b', '').rjust(32, '0'), compressed_chunk[2]])
        h3 = perform_modular_addition([bin(int(h3, 16)).replace('0b', '').rjust(32, '0'), compressed_chunk[3]])
        h4 = perform_modular_addition([bin(int(h4, 16)).replace('0b', '').rjust(32, '0'), compressed_chunk[4]])
        h5 = perform_modular_addition([bin(int(h5, 16)).replace('0b', '').rjust(32, '0'), compressed_chunk[5]])
        h6 = perform_modular_addition([bin(int(h6, 16)).replace('0b', '').rjust(32, '0'), compressed_chunk[6]])
        h7 = perform_modular_addition([bin(int(h7, 16)).replace('0b', '').rjust(32, '0'), compressed_chunk[7]])


    return perform_hash([h0,h1,h2,h3,h4,h5,h6,h7])