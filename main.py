def reverseBits(n):
    
    x=str(bin(n))
    m=x[2::].zfill(32)
    return int(m[::-1],2)