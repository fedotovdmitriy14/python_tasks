import os
from array import array
from random import random
from sys import path

floats = array('d', (random() for i in range(10**7)))


print(floats[-1])

if os.path.exists('./floats.bin') == False:
    fp = open('floats.bin', 'wb')
    floats.tofile(fp)
    fp.close()
    print("created")
else:
    print("file exists")

floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)   # read 10**7 numbers from fp file
fp.close()
print(floats[-1])

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

fedotovdmitriy14ghp_aAb0