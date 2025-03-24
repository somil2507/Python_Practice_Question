def print_otp():

    input_mobile_number = input("Please enter your mobile number : ", )

    otp = input_mobile_number[-4:]

    print("OTP is : ", otp)

#print_otp()    

def alternate_method_otp():

    input_mobile_number = input("Please enter your mobile number : ", )
    otp = []

    for i in input_mobile_number[-4:]:
        otp.append(i)

    print("OTP is : ",''.join(otp))

alternate_method_otp()        
