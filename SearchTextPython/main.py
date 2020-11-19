from user import masuk
from document import filetext
import sys
ulang = ''
while ulang != 'n':
    doc = input('Tampilkan urutan list dokumen text ? y/n \n')
    if doc == 'y':
        filetext()
    masuk()
    ulang = input('Ulangi program ? y/n \n')
exit()
