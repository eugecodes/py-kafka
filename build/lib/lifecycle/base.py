from datetime import datetime

""" 
# Base Input Class
class Model:
    id: str = ''
    entity_type: str = ''
    status: str = ''
    description: str = ''
    event_time: datetime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    batch_id: str = ''
    total_events: int = 0
    processed_events: int = 0
    ignored_events: int = 0
    errored_events: int = 0

# Error Details Class that specifies the structure of an error
class ErrorDetails:
    record_id: str = ''
    event_time: datetime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    description: str = ''
    error_message: str = ''

# Error Class that has a collection of Error Details per each Error
class Error:
    error_desc: str = ''
    error_details: dict[ErrorDetails] = {}

# Extension of the Base Input Class
class Initial(Model):
    filename: str = ''
    error: dict[Error] = {}

# Output Event Class
class OutputModel:
    events: list[Model] = []

# Input Event Class
class InputModel:
    events: list[Initial] = [] """


async def build_message(data):
    res = {'events': []}
    for input in data.events:
        model = {
            'id': input['id'],
            'entityType': input['entityType'],
            'status': input['status'],
            'description': input['description'],
            'eventTime': input['eventTime'],
            'batchId': input['batchId'],
            'totalEvents': input['totalEvents'],
            'processedEvents': input['processedEvents'],
            'ignoredEvents': input['ignoredEvents'],
            'erroredEvents': input['erroredEvents']
        }
        res.events.append(model)
    return res
