# from socket import *
# serverName = "10.1.70.19" # IPv4 // ::1 IPv6
# serverPort = 12500
# clientSocket = socket(AF_INET, SOCK_DGRAM) # AF_INET6
# print("UDP Client\n")
# while 1:
#     message = input("Input message: ")
#     if message == "exit":
#             break
#     clientSocket.sendto(bytes(message,"utf-8"), (serverName, serverPort))
# clientSocket.close()

from socket import *

# Caesar cipher encryption function
def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        encrypted_char = chr((ord(char) + shift) % 256)
        encrypted_text += encrypted_char
    return encrypted_text

serverName = "127.0.0.1"  # IPv4 // ::1 IPv6
serverPort = 12500
clientSocket = socket(AF_INET, SOCK_DGRAM)  # AF_INET6
print("UDP Client\n")

shift = 3  # Caesar cipher shift value

while True:
    message = input("Input message: ")
    if message == "exit":
        break
    
    encrypted_message = caesar_encrypt(message, shift)
    
    clientSocket.sendto(bytes(encrypted_message, "utf-8"), (serverName, serverPort))
    print("Encrypted message sent:", encrypted_message)

    # Receive and decrypt the response
    response, serverAddress = clientSocket.recvfrom(2048)
    decrypted_response = caesar_decrypt(response.decode("utf-8"), shift)
    print("Decrypted response:", decrypted_response)

clientSocket.close()