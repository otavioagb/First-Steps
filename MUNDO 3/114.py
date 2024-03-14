import urllib.request


try:
    site=urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('There was an error!')
else:
    print('All very well!')