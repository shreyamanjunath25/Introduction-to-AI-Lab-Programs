def main():
    a=False
    b=True
    print("not operation of a= ",not(a))
    print("or operation of a and b= ",(a or b))
    print("and operation of a and b= ", (a and b))
    print("xor operation of a and b= ", (a ^ b))
    print("xnor operation of a and b= ", not(a ^ b))
    print("implication of a and b= ", imp(a,b))
    print("Bidirectional operation of a and b= ",bidir(a,b))


def imp(a,b):
   return (not(a)) or b

def bidir(a,b):
    return (imp(a,b) and imp(b,a))

if __name__ == '__main__':
    main()