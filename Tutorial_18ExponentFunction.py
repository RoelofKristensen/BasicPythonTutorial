#allow us to raise something to a certain power
print(2**3)

#but using a for loop

def raise_to_power(basse_num, pow_num):
    result = 1
    for x in range(pow_num):
        result = result * basse_num
    return result

print(raise_to_power(int(input("base number ")),int(input("power number "))))