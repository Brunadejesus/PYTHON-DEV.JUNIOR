import os ## Importa o módulo ou biblioteca OS (Integra os programas e recursos do S.O)

print("#" * 60) ## Imprimir  60 vezes

ip_ou_host = input("Digite o ip ou host a ser verificado: ") ## Criamos uma variavel que recebar o endereço IP

print("#" * 60)

os.system('ping -n 3 {}'.format(ip_ou_host))##Chamando system da biblioteca OS - Comando ping
## -n -numero de pacotes que serão apresentados (6)