def compare(a, b):
    len_a, len_b = len(a), len(b)
    result = ""

    for i in range(len_a):
        for j in range(len_b):
            k=0
            while i + k < len_a and j + k < len_b and a[i + k] == b[j + k]:
                k += 1
            
            if k > len(result):
                result = a[i:i + k]
    return result 

if __name__ == '__main__':
    print(compare("AKA", "AKASHI")) # AKA
    print(compare("KANGOORO", "KANG")) # KANG
    print(compare("KI", "KIJANG")) # KI
    print(compare("KUPU-KUPU", "KUPU")) # KUPU
    print(compare("ILALANG", "ILA")) # ILA