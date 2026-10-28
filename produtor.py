import pika
import sys

parametros = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(parametros)
channel = connection.channel()

channel.queue_declare(queue='fila_pedidos', durable=True)

mensagem = ' '.join(sys.argv[1:]) or "Pedido padrão"

channel.basic_publish(exchange='', routing_key='fila_pedidos', body=mensagem, properties=pika.BasicProperties(delivery_mode=2))

print(f"[x] Enviado para a fila : {mensagem}")

connection.close()