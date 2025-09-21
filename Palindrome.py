given_string = input().strip()
string_length = len(given_string)
longest = ""

for i in range(string_length):
    #先處理奇數回文
    left, right = i, i #奇數回文的中間的字母
    while(left >= 0 and right < string_length and given_string[left] == given_string[right]):
        if(right - left + 1 > len(longest)): #如果right和left的長度大於longest的長度，那就將longest更新為left到right
            longest = given_string[left:right+1]
        left -= 1
        right += 1
    #處理偶數回文
    left, right = i, i+1 #偶數回文的中間字母 ex:accbbcca就是中間兩個b
    while(left >= 0 and right < string_length and given_string[left] == given_string[right]):
        if(right - left + 1 > len(longest)):
            longest = given_string[left:right+1]
        left -= 1
        right += 1
if(len(longest) >= 2):
    print(longest)
else:
    print("No Palindrome")
