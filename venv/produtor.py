import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='fila_mensagens')

print("Digite mensagens. Para sair, digite 'sair'.")

while True:
    mensagem = input("Mensagem: ")
    if mensagem.lower() == 'sair':
        break
    channel.basic_publish(exchange='', routing_key='fila_mensagens', body=mensagem.encode())
    print(f"Mensagem enviada: {mensagem}")

connection.close()
