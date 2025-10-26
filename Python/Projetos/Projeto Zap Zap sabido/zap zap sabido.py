import pywhatkit as kit
import pyautogui as autogui

print("------------------------------------------")
print("             Mensagens prontas            ")
print("------------------------------------------\n")

print("")
numero = input("Digite o numero de telefone: ")
mensagem = input("Digite a mensagem: ")

kit.sendwhatmsg_instantly(numero,mensagem)