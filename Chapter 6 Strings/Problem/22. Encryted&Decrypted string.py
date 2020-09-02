# A program picks out the characters at even indixes
# put them first in the encrypted string, and follow them by the odd characters
# 
#       message
#index: 0123456 
#       msaeesg
#index: 0123456 
#       message

# Visit: https://stackoverflow.com/questions/61340298/python-program-to-print-the-odd-and-even
# indices-of-an-string-not-taking-the-fir

# Visit: https://stackoverflow.com/questions/60645336/when-i-try-to-decrypt
# my-message-in-python-it-says-string-index-out-of-range-i

# def encrypt_char(s):
#    result_even = '' 
#    result_odd  = ''
#    for i in range(len(s)):
#        if i%2 == 0:
#            result_even = result_even + s[i]
#        else:
#            result_odd = result_odd + s[i]
#   
#   return (result_even+result_odd)
    

s = input('Enter a string:')
# Encryption
s = s[::2] + s[1::2]
print(s)

# Decryption
s += ' '
d = ''
half = int(len (s) /2) 
for i in range(half):
    d += s[i] + s[i + half]
print (d)
