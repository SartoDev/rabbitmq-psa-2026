import pika
import time

parametros = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(parametros)
channel = connection.channel()

channel.queue_declare(queue='fila_pedidos', durable=True)

def processar_pedido(ch, method, properties, body):
    mensagem = body.decode()
    print(f"[x] Recebido: {mensagem}")
    tempo_processamento = body.count(b'.')
    time.sleep(tempo_processamento)
    print("[x] Processamento concluído")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue='fila_pedidos', on_message_callback=processar_pedido)

channel.start_consuming()