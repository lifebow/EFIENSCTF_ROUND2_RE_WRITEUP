import random
import string

flag = 'hidden'

lines = []
plaintext = open('plaintext.txt', 'w')
for f in flag:
    lines += [''.join([f] + [random.choice(string.ascii_letters) for i in range(4 * 256 - 1)] + ['\n'])]

print(lines)
plaintext.writelines(lines)
plaintext.close()
