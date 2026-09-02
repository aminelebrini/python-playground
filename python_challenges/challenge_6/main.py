str = str(input("enter your String ! :"))

new_str = ""

for i in range(len(str) -1 , -1, -1):

    new_str += str[i]

print(new_str)