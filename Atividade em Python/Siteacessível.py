import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com/@arlaxy6946')
    print('O site pode ser acessado tranquilamente!')
except:
    print('O site não está disponivel')
