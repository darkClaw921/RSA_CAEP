
from Crypto.PublicKey import RSA

keyFilePub = open('/Users/igorgerasimov/Desktop/', 'wb')
keyFilePriv = open('/Users/igorgerasimov/Desktop/', 'wb')

key = RSA.generate(1024)
keyFilePub.write(key.publickey().exportKey('PEM'))
keyFilePriv.write(key.exportKey('PEM'))

keyFilePub.close() 
keyFilePriv.close()

