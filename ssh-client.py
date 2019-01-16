import paramiko

host=raw_input("Digite o ip: ")
user=raw_input("Digite o usuario: ")
password=raw_input("Digite a senha: ")

client=paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host,username=user,password=password)

while True:
    comando=raw_input("Comando: ")
    entrada, saida, erros = client.exec_command(comando)
    print saida.readlines()
    continuar=raw_input("\nDeseja continuar? [s/n] ")
    if continuar=='n':
        break