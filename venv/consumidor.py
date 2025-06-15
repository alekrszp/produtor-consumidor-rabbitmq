import pika
from datetime import datetime

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='fila_mensagens')

def callback(ch, method, properties, body):
    mensagem = body.decode()
    data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('mensagens_recebidas.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f"[{data_hora}] {mensagem}\n")
    print(f"Recebido e salvo: [{data_hora}] {mensagem}")

channel.basic_consume(queue='fila_mensagens', on_message_callback=callback, auto_ack=True)

print("Aguardando mensagens... Pressione CTRL+C para sair.")
channel.start_consuming()
