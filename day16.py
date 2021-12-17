filename = 'puzzle_input/day16.txt'


with open(filename) as file:
    transmission = file.readline().strip()
    

def to_binary(hex_str):
    # Convert hex to binary
    # Don't laugh at me
    # I had a real algorithm here but the leading zeroes were a nightmare
    
    # I am not accepting criticism at this time!!!!!!!!!!
    # :-)
    
    bin_str = ''
    for c in hex_str:
        if c == '0':
            bin_str += '0000'
        elif c == '1':
            bin_str += '0001'
        elif c == '2':
            bin_str += '0010'
        elif c == '3':
            bin_str += '0011'
        elif c == '4':
            bin_str += '0100'
        elif c == '5':
            bin_str += '0101'
        elif c == '6':
            bin_str += '0110'
        elif c == '7':
            bin_str += '0111'
        elif c == '8':
            bin_str += '1000'
        elif c == '9':
            bin_str += '1001'
        elif c == 'A':
            bin_str += '1010'
        elif c == 'B':
            bin_str += '1011'
        elif c == 'C':
            bin_str += '1100'
        elif c == 'D':
            bin_str += '1101'
        elif c == 'E':
            bin_str += '1110'
        elif c == 'F':
            bin_str += '1111'
        else:
            print("unexpected hex found:", c)
            break
    return bin_str
    
    
def to_number(bin_str):
    # Convert binary to decimal
    return int(bin_str, 2)
    

def str_pop(s, n):
    # This is a helper function that splits a string at position n
    # I do this because my method is to consume the transmission from
    # front to back and I don't want to bother keeping track of the index.
    
    # Also I hate typing brackets
    return [s[:n], s[n:]]

    
class Packet:
    def __init__(self, version, type_id):
        self.version = version
        self.type_id = type_id
        self.value = None
        self.length_type_id = None
        self.sub_packets = []
    
    def set_value(self, bin_str=None):
        # For operators, it calculates the value based on the sub-packets.
        # For values, it takes a binary string and determines the decimal
        # value, then returns the binary string.
        if self.type_id == 0:
            temp = 0
            for sub in self.sub_packets:
                temp += sub.value
            self.value = temp
        elif self.type_id == 1:
            temp = 1
            for sub in self.sub_packets:
                temp *= sub.value
            self.value = temp
        elif self.type_id == 2:
            self.value = min([p.value for p in self.sub_packets])
        elif self.type_id == 3:
            self.value = max([p.value for p in self.sub_packets])
        elif self.type_id == 5:
            if self.sub_packets[0].value > self.sub_packets[1].value:
                self.value = 1
            else:
                self.value = 0
        elif self.type_id == 6:
            if self.sub_packets[0].value < self.sub_packets[1].value:
                self.value = 1
            else:
                self.value = 0
        elif self.type_id == 7:
            if self.sub_packets[0].value == self.sub_packets[1].value:
                self.value = 1
            else:
                self.value = 0
        elif self.type_id == 4:
            v = ''
            while True:
                cont, this_chunk, bin_str = bin_str[0], \
                                            bin_str[1:5], bin_str[5:]
                v += this_chunk
                if cont == '0':
                    break
            self.value = int(v, 2)
            return bin_str
        

def get_next_packet(msg, p):
    # This is a giant mess of a recursive function!
    
    # Get the version and type ID
    ver, msg = str_pop(msg, 3)
    t_id, msg = str_pop(msg, 3)
    ver = to_number(ver)
    t_id = to_number(t_id)
    
    # Store this packet in the list
    this_packet = Packet(ver, t_id)
    p.append(this_packet)
    
    # Determine the type
    # Type 4: Literal values
    if this_packet.type_id == 4:
        msg = this_packet.set_value(msg)
        
    # Anything else: Operators
    else:
        # Determine the length type
        l_t_id, msg = str_pop(msg, 1)
        this_packet.length_type_id = to_number(l_t_id)
        
        # Type 0 -> sub-packets are in a sub-string of given length
        # We will look for sub-packets until the sub-string is exhausted
        if this_packet.length_type_id == 0:
            sub_length, msg = str_pop(msg, 15)
            sub_length = to_number(sub_length)
            
            sub_transmission, msg = str_pop(msg, sub_length)
            
            while len(sub_transmission) > 0:
                # Find all our sub-packets
                sub_transmission, sub_packet = \
                    get_next_packet(sub_transmission, p)
                this_packet.sub_packets.append(sub_packet)
        
        # Type 1 -> A number of sub-packets are given but not the length
        elif this_packet.length_type_id == 1:
            sub_count, msg = str_pop(msg, 11)
            sub_count = to_number(sub_count)
            
            # Get a specific number of subpackets from the remaining msg string
            for i in range(sub_count):
                msg, sub_packet = get_next_packet(msg, p)
                this_packet.sub_packets.append(sub_packet)
                
        # At this point, we have retrieved all the sub-packets for an operator
        # so we can now set the values.
        this_packet.set_value()
    
    return [msg, this_packet]

#transmission = '880086C3E88112'
bin_transmission = to_binary(transmission)
packets = []

bin_transmission, _ = get_next_packet(bin_transmission, packets)

version_sum = 0
for packet in packets:
    version_sum += packet.version
    
print("Part 1:", version_sum)
print("Part 2:", packets[0].value)

