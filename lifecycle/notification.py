from datetime import datetime
from enum import Enum
import json
from json import JSONEncoder
import logging

dt = datetime.now()
ts = dt.isoformat()


class Encoder(JSONEncoder):
    """    Encoder for dict to json    """
    def default(self, obj):
        return obj.__dict__


class Status(str, Enum):
    """    Statuses list    """
    ACCEPTING = 'ACCEPTING'
    ACCEPTED = 'ACCEPTED'
    CLONED = 'CLONED'
    PROCESSING = 'PROCESSING'
    VALIDATING = 'VALIDATING'
    CURATING = 'CURATING'
    ENRICHING = 'ENRICHING'
    TRANSFORMING = 'TRANSFORMING'
    PREPARED = 'PREPARED'
    QUEUED = 'QUEUED'
    COMPLETED = 'COMPLETED'
    COMPLETED_WITH_ERROR = 'COMPLETED_WITH_ERROR'
    ERROR = 'ERROR'
    SENT = 'SENT'
    SENT_FOR_REPLAY = 'SENT_FOR_REPLAY'
    REPLAYED = 'REPLAYED'


class ErrorDetails:
    """

    recordId 	String 	Y 	This is to provide the errored recordId details.
    eventTime 	String 	Y 	This is time of error event generation in epoch time
    description 	String 	Y 	This is record id error description 	
    detailedDescription 	String 	N 	This is detailed error Description
    
    """
    def __init__(self, recordId: str, eventTime: float,
                 detailedDescription: str = ''):
        self.id = recordId
        self.detailedDescription = detailedDescription
        self.eventTime = eventTime

    def __str__(self):
        try:
            return json.dumps(dict(self), cls=Encoder, ensure_ascii=False)
        except Exception as e:
            logging.exception(e)

    def __repr__(self):
        try:
            return self.__str__()
        except Exception as e:
            logging.exception(e)

    def getErrorList(self):
        try:
            data = Encoder().encode(self)
            return json.dumps(data, cls=Encoder)
        except Exception as e:
            logging.exception(e)


class EventError:
    """

    summary 	String 	Y 	This is a summary for complete errors for the ingestion id
    errorCode 	String 	Y 	This is a combined error code for the ingestion id
    errorDetails 	Array 	N
    
    """
    def __init__(self, summary: str, errorCode: str, errorDetails: str = ''):
        self.summary = summary
        self.errorCode = errorCode
        self.errorMessage = errorDetails
        self.errors = []

    def addErrorDetails(self, err: ErrorDetails):
        try:
            self.errors.append(err)
            return self.errors
        except Exception as e:
            logging.exception(e)

    def __str__(self):
        try:
            return json.dumps(dict(self), cls=Encoder, ensure_ascii=False)
        except Exception as e:
            logging.exception(e)

    def __repr__(self):
        try:
            return self.__str__()
        except Exception as e:
            logging.exception(e)

    def __iter__(self):
        try:
            yield from {
                "summary": self.summary,
                "errorCode": self.errorCode,
                "errorMessage": self.errorMessage,
                "errors": self.errors
            }.items()
        except Exception as e:
            logging.exception(e)

    def getError(self):
        try:
            data = Encoder().encode(self)
            return json.dumps(data, cls=Encoder)
        except Exception as e:
            logging.exception(e)


class Event:
    """
    
    id 	String 	Y 	This is the unique id for the event e.g. ingestion Id,
    entityType 	String 	Y 	This defines blue yonder entity types	
    status 	ENUM 	Y 	This is the event status. Please see below table 	
    eventTime 	String 	Y 	This is time of event generation in epoch time 
    totalEvents 	Integer 	N
    processedEvents 	Integer 	N 	
    ignoredEvents 	Integer 	N 	
    erroredEvents 	Integer 	N 
    description 	String 	N 
    fileName 	String 	N 
    batchId 	String 	N
    workflowId 	String 	N
    error 	Object 	N
    
    """
    def __init__(self, identId: str, entityType: str, status: Status,
                 eventTime: float, totalEvents: int = 1,
                 processedEvents: int = 1,
                 ignoredEvents: int = 0, erroredEvents: int = 0,
                 description: str = '', fileName: str = '', batchId: str = '',
                 workflowId: str = '', error: EventError = None):
        self.id = identId
        self.entityType = entityType
        self.status = status
        self.eventTime = eventTime
        self.totalEvents = totalEvents
        self.processedEvents = processedEvents
        self.ignoredEvents = ignoredEvents
        self.erroredEvents = erroredEvents
        self.description = description
        self.fileName = fileName
        self.batchId = batchId
        self.workflowId = workflowId
        self.error = error

        try:
            if self.id is None or len(self.id) <= 0:
                raise ValueError('ID of the event should not be empty')

            if status not in [e.value for e in Status]:
                raise ValueError('Status of the event should not be empty')

            try:
                datetime.fromtimestamp(
                    eventTime)
            except Exception:
                raise ValueError('eventTime must be epoch timestamp')

        except Exception as e:
            logging.exception(e)
            raise

        logging.info('Event ID: ' + self.id)

    def __str__(self):
        try:
            return json.dumps(dict(self), cls=Encoder, ensure_ascii=False)
        except Exception as e:
            logging.exception(e)

    def __repr__(self):
        try:
            return self.__str__()
        except Exception as e:
            logging.exception(e)

    def __iter__(self):
        try:
            yield from {
                "id": self.id,
                "entityType": self.entityType,
                "status": self.status.value,
                "eventTime": self.eventTime,
                "totalEvents": self.totalEvents,
                "processedEvents": self.processedEvents,
                "ignoredEvents": self.ignoredEvents,
                "erroredEvents": self.erroredEvents,
                "description": self.description,
                "fileName": self.fileName,
                "batchId": self.batchId,
                "workflowId": self.workflowId,
                "error": self.error.getError(),
            }.items()
        except Exception as e:
            logging.exception(e)

    def getEvent(self):
        try:
            data = Encoder().encode(self)
            return json.dumps(data, cls=Encoder)
        except Exception as e:
            logging.exception(e)


class Header:
    """

    tenantId 	String 	Y 	Realm Id (per customer per environment) 	
    applicationName 	String 	Y 	This is highest level application demarcation,
    All PDC applications will have a default value of "PDC" ,
    end applications will have their own name. e.g. LCT, SAP . 
    serviceGroup 	String 	Y 	This categorizes service into groups,
    serviceName 	String 	Y 	This is pre-defined service name	
    kafkaTopic 	String 	Y 	This is the kafka topic. public.all.application.status
    isCompressed 	boolean 	Y 	This is the flag to compress the payload.
    
    """
    def __init__(self, tenantId: str, applicationName: str,
                 serviceGroup: str, serviceName: str, kafkaTopic: str):
        self.id = tenantId
        self.applicationName = applicationName
        self.serviceGroup = serviceGroup
        self.serviceName = serviceName
        self.kafkaTopic = kafkaTopic

        try:
            if self.id is None or len(self.id) <= 1:
                raise ValueError('Tenant ID should not be empty')
            
            if self.serviceName is None or len(self.serviceName) <= 1:
                raise ValueError('Service ID should not be empty')
            
            if self.kafkaTopic is None or len(self.kafkaTopic) <= 1:
                raise ValueError('Kafka Topic should not be empty')
            
            if self.applicationName is None or len(self.applicationName) <= 1:
                raise ValueError('applicationName should not be empty')
            
            if self.serviceGroup is None or len(self.serviceGroup) <= 1:
                raise ValueError('serviceGroup should not be empty')
        except Exception as e:
            logging.exception(e)
            raise

    def __iter__(self):
        try:
            yield from {
                "id": self.id,
                "applicationName": self.applicationName,
                "serviceGroup": self.serviceGroup,
                "serviceName": self.serviceName,
                "kafkaTopic": self.kafkaTopic,
            }.items()
        except Exception as e:
            logging.exception(e)

    def __str__(self):
        try:
            return json.dumps(dict(self), cls=Encoder, ensure_ascii=False)
        except Exception as e:
            logging.exception(e)

    def __repr__(self):
        try:
            return self.__str__()
        except Exception as e:
            logging.exception(e)

    def getHeader(self):
        try:
            data = Encoder().encode(self)
            return json.dumps(data, cls=Encoder)
        except Exception as e:
            logging.exception(e)


class Message:
    def __init__(self, header: Header):
        self.header = header
        self.id = header.id
        self.events = []

        logging.info('Notification ID: ' + self.id)

    def addEvent(self, event: Event):
        try:
            self.events.append(event)
            return self.events
        except Exception as e:
            logging.exception(e)

    def __iter__(self):
        try:
            yield from {
                "header": self.header,
                "events": self.events
            }.items()
        except Exception as e:
            logging.exception(e)

    def __str__(self):
        try:
            return json.dumps(dict(self), cls=Encoder, ensure_ascii=False)
        except Exception as e:
            logging.exception(e)

    def __repr__(self):
        try:
            return self.__str__()
        except Exception as e:
            logging.exception(e)

    def getMessage(self):
        try:
            data = Encoder().encode(self)
            return json.dumps(data, cls=Encoder)
        except Exception as e:
            logging.exception(e)
