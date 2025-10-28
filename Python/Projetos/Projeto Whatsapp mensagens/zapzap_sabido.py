import pywhatkit as kit
import pyautogui
from time import sleep
import os

sair = 0

while(sair == 0):
    saudação =" "
    generoDoCliente = " "
    nomeDoCliente = " "
    nomeDaConsultora = " "
    mensagem = " "
    
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    print("                                                                                     Mensagens prontas            \n")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")                                                                                                    

    print("                                                                                     1- Boas Vindas")
    print("                                                                                     2- Apresentação da loja")
    print("                                                                                     3- O cliente está se sentindo confortável com o óculos")
    print("                                                                                     4- Avaliação do atendimento")
    print("                                                                                     5- Mensagem de como a consultora pode auxiliar o cliente hoje ")
    print("                                                                                     6- Fechar a aplicação \n")

    escolha = int(input("                                                                                     Selecione qual mensagem mandar: "))
    if (escolha <=0 or escolha >= 7):
        print("                                                                                     Número incorreto!")
    if(escolha == 6):
        sair = 10
        print("                                                                                     Sessão encerrada...")
    else:  
        if (escolha == 1):
            print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            print("                                                                                     Defina a saudação: ")
            print("                                                                                     1- Bom dia ")
            print("                                                                                     2- Boa Tarde")
            print("                                                                                     3- Boa noite \n")
            saudação = int(input("                                                                                     Digite aqui: "))
            if(saudação == 1):
                saudação = "Bom dia"
            if(saudação == 2):
                saudação = "Boa tarde"
            if(saudação == 3):
                saudação = "Boa noite"
            mensagem = f"""{saudação}!
Seja bem-vindo(a) ao ZEISS Vision Center, a loja conceito da marca ZEISS.
Oferecemos as melhores soluções em saúde visual, com tecnologia de ponta, precisão alemã e um atendimento totalmente personalizado.

Conte conosco para encontrar a lente ideal para o seu estilo de vida e garantir a melhor experiência visual possível."""
        if (escolha == 2): 
            mensagem = """ZEISS VISION CENTER RECIFE, uma ótica totalmente diferente das outras. Aqui o cliente encontra a inovação e a tecnologia exclusiva das lentes ZEISS, somada às melhores marcas mundiais de armações. Qualidade, precisão e personalização para saúde dos seus olhos, seja para óculos de grau ou solar.
Venha conhecer nossa loja no Shopping Recife e tenha muito mais que uma ótica, tenha uma ZEISS VISION CENTER ao seu dispor."""
        if (escolha == 3):
            ("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            print("                                                                                     Defina a saudação: ")
            print("                                                                                     1- Bom dia ")
            print("                                                                                     2- Boa Tarde")
            print("                                                                                     3- Boa noite \n")
            saudação = int(input("                                                                                     Digite aqui: "))
            if(saudação == 1):
                saudação = "Bom dia"
            if(saudação == 2):
                saudação = "Boa tarde"
            if(saudação == 3):
                saudação = "Boa noite"
            ("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            print("                                                                                     Defina o sexo:")
            print("                                                                                     1- Feminino")
            print("                                                                                     2- Masculino")
            generoDoCliente = int(input("                                                                                     Digite aqui: "))
            if (generoDoCliente == 1):
                generoDoCliente = "Sra."
                nomeDoCliente = input("                                                                                     Nome da cliente: ")
            if(generoDoCliente == 2):
                generoDoCliente = "Sr."
                nomeDoCliente = input("                                                                                     Nome do cliente: ")
            nomeDaConsultora = input("                                                                                     Nome da consultora: ")

            mensagem = f"""{saudação}, {generoDoCliente} {nomeDoCliente}!
Aqui é a {nomeDaConsultora} da Zeiss Vision Center Recife.
Estou entrando em contato para saber como o senhor está se adaptando aos seus óculos e se eles estão precisando de algum ajuste ou manutenção.
Esse serviço é totalmente gratuito e bem rapidinho, enquanto cuidamos dos seus óculos, o senhor pode aproveitar um delicioso cappuccino por nossa conta.Estamos à disposição!"""
        if (escolha == 4):
            nomeDaConsultora = input("                                                                                     Nome da consultora: ")
            mensagem = f"""*Obrigado por escolher a Zeiss Vision Center!*

Estaremos sempre disponíveis para lhe atender, conte com os nossos consultores especializados. 

Se puder avaliar o meu atendimento no link a seguir, me deixaria muito feliz! 

https://g.page/r/CeKPP2Z4BfaUEB0/review

Segue abaixo algumas dicas importantes para você aproveitar ao máximo o seu produto!

Atenciosamente, 
*{nomeDaConsultora}*"""
        if(escolha == 5):
            ("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            print("                                                                                     Defina a saudação: ")
            print("                                                                                     1- Bom dia ")
            print("                                                                                     2- Boa Tarde")
            print("                                                                                     3- Boa noite \n")
            saudação = int(input("                                                                                     Digite aqui: "))
            if(saudação == 1):
                saudação = "Bom dia"
            if(saudação == 2):
                saudação = "Boa tarde"
            if(saudação == 3):
                saudação = "Boa noite"
            nomeDaConsultora = input("                                                                                     Digite o seu nome: ")
            mensagem = f"""{saudação}!
Sou {nomeDaConsultora}, a consultora responsável pelo seu atendimento e estou à disposição para ajudá-la no que for necessário. Como posso te auxiliar hoje?"""
        numero = input("                                                                                     Digite o número de telefone do cliente: ")
        
        kit.sendwhatmsg_instantly(f'+{numero}',mensagem)
        pyautogui.hotkey('enter')
        sleep(2)
        pyautogui.hotkey('ctrl','w')
        pyautogui.hotkey('enter')
        pyautogui.hotkey('alt', 'tab')
        os.system("cls")