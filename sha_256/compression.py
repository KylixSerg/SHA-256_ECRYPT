'''
compression:
for every word in the 64-32bit long chunk perform:

Initialize variables a, b, c, d, e, f, g, h and set them equal to the current hash values respectively. h0, h1, h2, h3, h4, h5, h6, h7
Run the compression loop. The compression loop will mutate the values of a…h. The compression loop is as follows:
for i from 0 to 63
S1 = (e rightrotate 6) xor (e rightrotate 11) xor (e rightrotate 25)
ch = (e and f) xor ((not e) and g)
temp1 = h + S1 + ch + k[i] + w[i]
S0 = (a rightrotate 2) xor (a rightrotate 13) xor (a rightrotate 22)
maj = (a and b) xor (a and c) xor (b and c)
temp2 := S0 + maj
h = g
g = f
f = e
e = d + temp1
d = c
c = b
b = a
a = temp1 + temp2
'''

from sha_256.message_schedule import *
from sha_256.consts import *

'''
params: -512bit long chunck in binary.
        -working variables, working variables a list of vars from a-h, intialized with 
        hard-coded constants that represent the first 32 bits of the fractional parts 
        of the square roots of the first 8 primes: 2, 3, 5, 7, 11, 13, 17, 19
returns: compressed 512bit chunk into mutated working variables
'''
def perform_chunk_compression(chunk_message, workign_variables):
    a = workign_variables[0]
    b = workign_variables[1]
    c = workign_variables[2]
    d = workign_variables[3]
    e = workign_variables[4]
    f = workign_variables[5]
    g = workign_variables[6]
    h = workign_variables[7]
    chunk = chunk_message

    for i in range(len(chunk)):
       S1 = perform_xor_3(right_rotate(e,6),right_rotate(e,11),right_rotate(e,25)) 
       ch = perform_xor_2(perform_and(e,f), perform_and(perform_negation(e),g))
       to_sum = [h, S1, ch, bin(int(ROUND_CONSTS[i], 16)).replace('0b', '').rjust(32, '0'), chunk[i]]
       temp1 = perform_modular_addition(to_sum)
       S0 = perform_xor_3(right_rotate(a,2),right_rotate(a,13),right_rotate(a,22))
       maj = perform_xor_3(perform_and(a,b),perform_and(a,c),perform_and(b,c))
       to_sum2 = [S0, maj] 
       temp2 = perform_modular_addition(to_sum2)

       h = g
       g = f
       f = e
       e = perform_modular_addition([d, temp1])
       d = c
       c = b
       b = a
       a = perform_modular_addition([temp1, temp2])
    
    
    return [a,b,c,d,e,f,g,h]

'''
params: working values after compression
return: concatenated hexadecimal digest represeting the sha256 output
'''
def perform_hash(elements):
    final_hash = "" 
    for i in range(len(elements)):
        final_hash+=(hex(int(elements[i], 2)).replace("0x", '')).rjust(8, '0')
    return final_hash
 

