def add_binary(a, b):
    '''
    Given two strings perform binary addition and return the result as a string
    '''
    if a[:2]=="0b" and b[:2]=="0b":   
        a=a[2:]
        b=b[2:]
    sum_a=0
    power=len(a)-1
    for i in a:
        if i=="1":
            sum_a+=1*(2**power)
            power-=1
        elif i=="0":
            sum_a+=0*(2**power)
            power-=1
    sum_b=0
    power_b=len(b)-1
    for j in b:
        if j=="1":
            sum_b+=1*(2**power_b)
            power_b-=1
        elif j=="0":
            sum_b+=0*(2**power_b)
            power_b-=1
    total_sum=sum_a+sum_b
    res=""
    while total_sum>0:
        if total_sum%2==1:
            res+="1"
            total_sum=total_sum//2
        elif total_sum%2==0:
            res+="0"
            total_sum=total_sum//2    
    res+="b0"
    return res[::-1]
