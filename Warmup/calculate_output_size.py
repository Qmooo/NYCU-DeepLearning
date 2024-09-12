import math
size = int(input("Type input size of height or width: "))
convNumber = int(input("Number of convs: "))
output = size
for i in range(convNumber):
    kernel = int(input("kernel size: "))
    stride = int(input("stride size: "))
    padding = int(input("padding size: "))
    output = math.floor((output + 2*padding - kernel) / stride) + 1
    print(f'Output after conv layer: {output}')
    have_pool = bool(input("Have a pool layer?(Type 1 is yes, 0 is no): "))
    if have_pool:
        poolSize = int(input("Pool size: "))
        output /= poolSize
        print(f'Output after pool layer: {output}')
    