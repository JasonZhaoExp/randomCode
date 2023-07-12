def denToBin(den):
    output = []
    outputStr = f"{den} in binary is "
    while den%2==0 or den%2==1:
        bin = den%2
        den = den//2
        output.append(bin)
        if den == 0:
            break
        else:
            continue
    for i in range(1, len(output)+1):
        outputStr +=  str(output[-i])
    return outputStr

print(denToBin(26))