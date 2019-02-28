shenfenzhen_number=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

shenfenzhen_number_str=input()

if len(shenfenzhen_number_str)!=18:

    print("请输入正确的身份证号码。")

else:
    for i in shenfenzhen_number:

        shenfenzhen_number[i]=shenfenzhen_number_str[i]

        #print(shenfenzhen_number[i])
        #[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]