# Define the subnetting table (in reverse order, starting from bottom to top)
subnet_masks = {
    30: "255.255.255.252", #4
    29: "255.255.255.248", #8
    28: "255.255.255.240", #16
    27: "255.255.255.224",   #32
    26: "255.255.255.192",   #64
    25: "255.255.255.128",   #128
    24: "255.255.255.0"       #256
}

# Define the number of bits for host and network
host_bits = 8  # The default number of host bits for Class C
network_bits = 24  # The default number of network bits for Class C

# Function to calculate subnetting
def subnet_calculation(required_host):
    # Calculate the converted network bits (8 - required_host)
    converted_network_bits = required_host - host_bits
    # Calculate the total new bits (24 + converted_network_bits)
    total_new_bits = network_bits + converted_network_bits

    # Display the converted network bits and total new bits
    print(f"Converted Network Bits: {converted_network_bits}")
    print(f"Total New Bits: {total_new_bits}")

    # Get the subnet mask for the new network bits
    subnet_mask = subnet_masks.get(total_new_bits)

    # Display the subnet mask
    print(f"Full Network Bits means: {subnet_mask}")

    # Calculate the number of blocks (2^converted_network_bits)
    number_of_blocks = 2 ** converted_network_bits
    print(f"Number of Blocks: {number_of_blocks}")

    # Calculate the block size (2^H where H is required host + 2)
    block_size = 2 ** required_host
    print(f"Block Size: {block_size}")

    # Display the usable IP ranges
    print("\nUsable IP Ranges:")
    for i in range(number_of_blocks):
        start_ip = i * block_size
        end_ip = start_ip + block_size - 1
        print(f"{{{start_ip}, {end_ip}}}", end=" ")
    print()

# Main program
if __name__ == "__main__":
    # Input the required host from the user
    required_host = int(input("Enter the required number of hosts: "))

    # Perform subnet calculation
    subnet_calculation(required_host)