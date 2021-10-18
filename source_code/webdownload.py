import wget

print('Beginning file download process')

url='http://www.vulnweb.com/acunetix-logo.png'

wget.download(url,'D:\\acunetix1.png')