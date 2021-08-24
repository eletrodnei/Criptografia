from cryptography.fernet import Fernet
 
str1 = "Meu Nome é Julio, futuro analista de sistemas"
key = Fernet.generate_key()
  
fernet = Fernet(key)
  
enctex = fernet.encrypt(str1.encode())
  
dectex = fernet.decrypt(enctex).decode()

print("Frase a ser Criptografada: ", str1)
print("Frase Criptograda: ", enctex)
print("Frase Descriptograda: ", dectex)