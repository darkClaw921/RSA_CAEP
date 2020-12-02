from Crypto.PublicKey import RSA

keyFilePub = open('/Users/igorgerasimov/Desktop/', 'rb')
keyFilePriv = open('/Users/igorgerasimov/Desktop/', 'rb')

PUBLICK_KEY_FILE = keyFilePub.read()
PUBLICK_KEY = RSA.importKey(PUBLICK_KEY_FILE)

PRIVATE_KEY_FILE = keyFilePriv.read() 
PRIVATE_KEY = RSA.importKey(PRIVATE_KEY_FILE)

keyFilePub.close()
keyFilePriv.close()

def encrypt_message(message):
    """[summary]
    Кодирует сообщение с использование RSA 

    Args:
        message ([str]): [Сообщение которое нобходими закодировать]

    Returns:
        [bytes]: [Закодированое сообщение ]
    """
    encryptMessage = PUBLICK_KEY.encrypt(message.encode('utf8'),1)
    return encryptMessage[0]

def decrypt_message(message):
    """[summary]
    Декодирует сообщение с использование RSA 

    Args:
        message ([str]): [Сообщение которое нобходими декодировать]

    Returns:
        [str]: [Декодированное сообщение ]
    """

    decryptMessage = PRIVATE_KEY.decrypt(eval(message))
    return decryptMessage.decode('utf8')

