from lifecycle import notification
import pytest
from . import mock_data

@pytest.mark.asyncio
async def test_build_header(): # validate header test
    header = notification.Header('a1b6b9a3-130f-430a-8aba-60b5c45a862f',
                         'LifecycleService_PY', 'serviceGroup', 'serviceName',
                         'public.all.ingestion.status')
    assert header.getHeader() == mock_data.correct_header


@pytest.mark.asyncio
async def test_validation_id():
    with pytest.raises(ValueError,
                       match="ID of the event should not be empty"):
        notification.Event('', 'entityType', notification.Status.ACCEPTING,
                   1694752440.22695, 0, 1, 0, 0, 'my description',
                   'filename', 'batchId', 'workflowId', None)


@pytest.mark.asyncio
async def test_event_with_error():
    errOne = notification.EventError('my summary', 'errCode', 'the message')
    notification.Event('id', 'entityType', notification.Status.ACCEPTING,
               1694752440.22695, 1, 1, 0, 1, 'my description',
               'filename', 'batchId', 'workflowId', errOne)


@pytest.mark.asyncio
async def test_timeevent_no_epoch():
    with pytest.raises(ValueError, match="eventTime must be epoch timestamp"):
        notification.Event('idaaa', 'entityType', notification.Status.ACCEPTING,
                   'datetime.timestamp(datetime.utcnow())',
                   1, 1, 0, 1, 'my description', 'filename',
                   'batchId', 'workflowId', None)


@pytest.mark.asyncio
async def test_create_message():
    header = notification.Header('a1b6b9a3-130f-430a-8aba-60b5c45a862f',
                         'LifecycleService_PY', 'serviceGroup',
                         'serviceName', 'public.all.ingestion.status')
    event = notification.Event('id', 'entityType', notification.Status.ACCEPTING,
                       1694752440.22695, 1, 1, 0, 1, 'my description',
                       'filename', 'batchId', 'workflowId', None)
    msg = notification.Message(header)
    msg.addEvent(event)
    assert msg.getMessage() == mock_data.message_example


@pytest.mark.asyncio
async def test_only_mandatory_values():
    header = notification.Header('a1b6b9a3-130f-430a-8aba-60b5c45a862f',
                         'LifecycleService_PY', 'serviceGroup',
                         'serviceName', 'public.all.ingestion.status')
    errOne = notification.EventError('my summary', 'errCode')
    event = notification.Event('id', 'entityType', notification.Status.ACCEPTING,
               1694752440.22695, errOne)
    msg = notification.Message(header)
    msg.addEvent(event)
    assert msg.getMessage() == mock_data.message_only_mandatory_values


@pytest.mark.asyncio
async def test_empty_tenant_id():
    with pytest.raises(ValueError, match="Tenant ID should not be empty"):
        notification.Header('',
                         'LifecycleService_PY', 'serviceGroup', 'serviceName',
                         'public.all.ingestion.status')


@pytest.mark.asyncio
async def test_null_tenant_id():
    with pytest.raises(ValueError, match="Tenant ID should not be empty"):
        notification.Header(None,
                         'LifecycleService_PY', 'serviceGroup', 'serviceName',
                         'public.all.ingestion.status')


@pytest.mark.asyncio
async def test_empty_service_id():
    with pytest.raises(ValueError, match="Service ID should not be empty"):
        notification.Header('a1b6b9a3-130f-430a-8aba-60b5c45a862f',
                         'LifecycleService_PY', 'serviceGroup', '',
                         'public.all.ingestion.status')


@pytest.mark.asyncio
async def test_null_service_id():
    with pytest.raises(ValueError, match="Service ID should not be empty"):
        notification.Header('a1b6b9a3-130f-430a-8aba-60b5c45a862f',
                         'LifecycleService_PY', 'serviceGroup', None,
                         'public.all.ingestion.status')


@pytest.mark.asyncio
async def test_empty_kafka_topic():
    with pytest.raises(ValueError, match="Kafka Topic should not be empty"):
        notification.Header('a1b6b9a3-130f-430a-8aba-60b5c45a862f',
                         'LifecycleService_PY', 'serviceGroup', 'serviceName',
                         '')


@pytest.mark.asyncio
async def test_null_kafka_topic():
    with pytest.raises(ValueError, match="Kafka Topic should not be empty"):
        notification.Header('a1b6b9a3-130f-430a-8aba-60b5c45a862f',
                         'LifecycleService_PY', 'serviceGroup', 'serviceName',
                         None)


@pytest.mark.asyncio
async def test_empty_mandatory_values_in_event():
    with pytest.raises(ValueError, match="Status of the event should not be empty"):
        notification.Event('id', 'entityType', '',
               1694752440.22695, None)
    with pytest.raises(ValueError, match="ID of the event should not be empty"):
        notification.Event('', 'entityType', notification.Status.ACCEPTING,
               1694752440.22695, None)
    with pytest.raises(ValueError, match="eventTime must be epoch timestamp"):
        notification.Event('id', 'entityType', notification.Status.ACCEPTING,
               '', None)


@pytest.mark.asyncio
async def test_null_mandatory_values_in_event():
    with pytest.raises(ValueError, match="Status of the event should not be empty"):
        notification.Event('id', 'entityType', None,
               1694752440.22695, None)
    with pytest.raises(ValueError, match="ID of the event should not be empty"):
        notification.Event(None, 'entityType', notification.Status.ACCEPTING,
               1694752440.22695, None)
    with pytest.raises(ValueError, match="eventTime must be epoch timestamp"):
        notification.Event('id', 'entityType', notification.Status.ACCEPTING,
               None, None)


@pytest.mark.asyncio
async def test_valid_notification_event():
    notification.Event('id', 'entityType', notification.Status.ACCEPTING,
                       1694752440.22695, 1, 1, 0, 1, 'my description',
                       'filename', 'batchId', 'workflowId', None)


@pytest.mark.asyncio
async def test_valid_notification_event_with_defaults():
    notification.Event('id', 'entityType', notification.Status.ACCEPTING,
               1694752440.22695)


@pytest.mark.asyncio
async def test_build_notification_error_details():
    err = notification.EventError('my summary', 'errCode')
    detail1 = notification.ErrorDetails('recordId', 1694752440.22695)
    err.addErrorDetails(detail1)
