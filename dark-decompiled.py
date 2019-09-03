import os
merah = '\x1b[1;91m'
lime = '\x1b[1;92m'
kuning = '\x1b[1;93m'
biru = '\x1b[1;94m'
ungu = '\x1b[1;95m'
blue = '\x1b[1;96m'
putih = '\x1b[1;97m'
tutup = '\x1b[0m'
os.system('clear')
print tutup + '               [ Dark-FB ]v1.8               '
print ' Ingin membeli api-key bisa hubungi kami melalui : '
print ' Wa : ' + lime + '+62 89620134992'
print '      +62 895340174061' + tutup
print
raw_input('[>] Masukkan API KEY : ')
raw_input('Enter untuk hubungi saya ...')
os.system('xdg-open https://wa.me/6289620134992?text=I%20want%20to%20buy%20api-key%20Dark-FB')
