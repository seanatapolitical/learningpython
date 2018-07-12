# hi Sean, hashtags mark 'comments' that are ignored when the code runs, so
# you'll only be able to read this when you succeed in opening this script
# for editing. Codeword 1 is 'Mongoose'

rot13cipher = {}
for c in (65, 97):
    for i in range(26):
        rot13cipher[chr(i+c)] = chr((i+13) % 26 + c)

# the cipher I just built can be used to decode the gobbledegook below when
# you run this code!

ciphered_text = "Uryyb jbeyq! V'ir pvcurerq gur grkg va gur fpevcg fb gung lbh pna'g whfg ernq vg va gur rqvgbe. Vs lbh'er ernqvat guvf lbh znantrq gb eha gur pbqr! Jryy qbar - pbqrjbeq 2 vf 'Pnagnaxrebhf'."

print(
    ''.join([rot13cipher.get(x,x) for x in ciphered_text])
)

print('Success!')
