# from socket import *
# serverPort = 12500
# serverSocket = socket(AF_INET, SOCK_DGRAM)
# serverSocket.bind(("",serverPort))
# print ("UDP server\n")
# while 1:
#     message, clientAddress = serverSocket.recvfrom(2048)
#     text = str(message,"utf-8") #cp1252 #utf-8
#     print ("Received from Client: ", text)

from socket import *

# Caesar cipher encryption function
def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        encrypted_char = chr((ord(char) + shift) % 256)
        encrypted_text += encrypted_char
    return encrypted_text

# Caesar cipher decryption function
def caesar_decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        decrypted_char = chr((ord(char) - shift) % 256)
        decrypted_text += decrypted_char
    return decrypted_text

serverPort = 12500
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))
print("UDP server\n")

shift = 3  # Caesar cipher shift value

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    encrypted_text = str(message, "utf-8")
    print("Received from Client (encrypted):", encrypted_text)
    
    decrypted_text = caesar_decrypt(encrypted_text, shift)
    print("Decrypted message:", decrypted_text)