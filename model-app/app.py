from eventpy.eventdispatcher import EventDispatcher
from lifecycle import notification
import asyncio
from kafka import KafkaProducer, KafkaConsumer
from kafka.errors import KafkaError, KafkaTimeoutError
from dotenv import load_dotenv
from json import loads
from datetime import datetime
import ssl

sasl_mechanism = 'PLAIN'
security_protocol = 'SASL_SSL'
topic = 'public.all.ingestion.status'

load_dotenv()

dt = datetime.now()
ts = dt.isoformat()

context = ssl.create_default_context()
context.options &= ssl.OP_NO_TLSv1
context.options &= ssl.OP_NO_TLSv1_1


def publish_event(message):
    producer = KafkaProducer(bootstrap_servers='',
                             sasl_plain_username='',
                             sasl_plain_password='',
                             security_protocol=security_protocol,
                             ssl_context=context,
                             sasl_mechanism=sasl_mechanism,
                             api_version=(0, 10),
                             retries=50)
    future = producer.send(topic, value=message.encode('utf-8'))
    try:
        record_metadata = future.get(timeout=1000)
        print(record_metadata)
    except KafkaError as kke:
        print(kke)
    except KafkaTimeoutError as kte:
        print("KafkaLogsConsumer timeout sending log to Kafka: %s", kte)
    except KafkaError as ke:
        print("KafkaLogsConsumer error sending log to Kafka: %s", ke)
    except Exception as e:
        print("KafkaLogsConsumer exception sending log to Kafka: %s", e)


def read_event():
    try:
        consumer = KafkaConsumer(
            topic,
            bootstrap_servers='',
            sasl_plain_username='',
            sasl_plain_password='',
            security_protocol=security_protocol,
            ssl_context=context,
            sasl_mechanism=sasl_mechanism,
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='my-group',
            value_deserializer=lambda x: loads(x.decode('utf-8')))
        for message in consumer:
            message = message.value
            print('msg {}'.format(message))
    except KafkaTimeoutError as kte:
        print("KafkaLogsConsumer timeout sending log to Kafka: %s", kte)
    except KafkaError as ke:
        print("KafkaLogsConsumer error sending log to Kafka: %s", ke)
    except Exception as e:
        print("KafkaLogsConsumer exception sending log to Kafka: %s", e)


async def main():
    header = notification.Header('a1b6b9a3-130f-430a-8aba-60b5c45a862f',
                         'LifecycleService_PY', 'serviceGroup', 'serviceName',
                         topic)

    errOne = notification.EventError('my summary', 'errCode', 'the message')
    errEvent = notification.ErrorDetails('recordId', datetime.timestamp(
        datetime.utcnow()), 'just some more details')
    errEventTwo = notification.ErrorDetails('recordId2', datetime.timestamp(
        datetime.utcnow()), 'another event of the same error')
    errOne.addErrorDetails(errEvent)
    errOne.addErrorDetails(errEventTwo)
    event = notification.Event('id', 'entityType', notification.Status.ACCEPTING,
                       datetime.timestamp(datetime.utcnow()), 1, 1, 0, 1,
                       'my description', 'filename', 'batchId', 'workflowId',
                       errOne)
    event_ii = notification.Event('id2', 'entityType', notification.Status.ACCEPTING,
                          datetime.timestamp(datetime.utcnow()), 1, 1, 0, 1,
                          'my description', 'filename', 'batchId',
                          'workflowId', errOne)
    msg = notification.Message(header)
    msg.addEvent(event)
    msg.addEvent(event_ii)
    message = msg
    # create an EventDispatcher
    dispatcher = EventDispatcher()

    dispatcher.appendListener(5, lambda: print(message))
    dispatcher.appendListener(6, lambda: publish_event(message))
    dispatcher.appendListener(6, read_event())

    # Dispatch the events
    dispatcher.dispatch(5)

    # Publish to kafka
    dispatcher.dispatch(6)

asyncio.run(main())
