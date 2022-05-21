def prep_input(input):
    # convert input to binary and pad with 1 
    binInput =   (' '.join(format(ord(x), 'b').rjust(8, '0') for x in input) + " 1").replace(" ","")
    input_length_bin = len(binInput)-1 # get length of the bin version of the input
    return pad_zeros(binInput) + add_big_end_length(input_length_bin)

# helper methods 
def pad_zeros(input):
    five_twelve_multiple = (len(input) // 512 + 1) * 512 # length of the highest string
    if(five_twelve_multiple - len(input)< 64):
        five_twelve_multiple += 512
    five_twelve_multiple -= 64
    return input.ljust(five_twelve_multiple, '0')

def add_big_end_length(input_bin_length):
    big_end_num = bin(input_bin_length).rjust(65, '0').replace('b', '')
    return big_end_num

