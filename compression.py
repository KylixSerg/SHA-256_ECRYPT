from message_schedule import *
from consts import *

def perform_chunk_compression(chunk, workign_variables):
    a = workign_variables[0]
    b = workign_variables[1]
    c = workign_variables[2]
    d = workign_variables[3]
    e = workign_variables[4]
    f = workign_variables[5]
    g = workign_variables[6]
    h = workign_variables[7]

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

def perform_hash(elements):
    final_hash = "" 
    for i in range(len(elements)):
        final_hash+=(hex(int(elements[i], 2)).replace("0x", '')).rjust(8, '0')
    return final_hash
 

