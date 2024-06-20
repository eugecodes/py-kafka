correct_header = '"{\\"id\\": \\"a1b6b9a3-130f-430a-8aba-60b5c45a862f\\", \\"applicationName\\": \\"LifecycleService_PY\\", \\"serviceGroup\\": \\"serviceGroup\\", \\"serviceName\\": \\"serviceName\\", \\"kafkaTopic\\": \\"public.all.ingestion.status\\"}"'
message_example = '"{\\"header\\": {\\"id\\": \\"a1b6b9a3-130f-430a-8aba-60b5c45a862f\\", \\"applicationName\\": \\"LifecycleService_PY\\", \\"serviceGroup\\": \\"serviceGroup\\", \\"serviceName\\": \\"serviceName\\", \\"kafkaTopic\\": \\"public.all.ingestion.status\\"}, \\"events\\": [{\\"id\\": \\"id\\", \\"entityType\\": \\"entityType\\", \\"status\\": \\"ACCEPTING\\", \\"eventTime\\": 1694752440.22695, \\"totalEvents\\": 1, \\"processedEvents\\": 1, \\"ignoredEvents\\": 0, \\"erroredEvents\\": 1, \\"description\\": \\"my description\\", \\"fileName\\": \\"filename\\", \\"batchId\\": \\"batchId\\", \\"workflowId\\": \\"workflowId\\", \\"error\\": null}]}"'
message_only_mandatory_values = '"{\\"header\\": {\\"id\\": \\"a1b6b9a3-130f-430a-8aba-60b5c45a862f\\", \\"applicationName\\": \\"LifecycleService_PY\\", \\"serviceGroup\\": \\"serviceGroup\\", \\"serviceName\\": \\"serviceName\\", \\"kafkaTopic\\": \\"public.all.ingestion.status\\"}, \\"events\\": [{\\"id\\": \\"id\\", \\"entityType\\": \\"entityType\\", \\"status\\": \\"ACCEPTING\\", \\"eventTime\\": 1694752440.22695, \\"totalEvents\\": {\\"summary\\": \\"my summary\\", \\"errorCode\\": \\"errCode\\", \\"errorMessage\\": \\"\\", \\"errors\\": []}, \\"processedEvents\\": 1, \\"ignoredEvents\\": 0, \\"erroredEvents\\": 0, \\"description\\": \\"\\", \\"fileName\\": \\"\\", \\"batchId\\": \\"\\", \\"workflowId\\": \\"\\", \\"error\\": null}]}"'
dict_header = {
    "id": "a1b6b9a3-130f-430a-8aba-60b5c45a862f", 
    "applicationName": "LifecycleService_PY", 
    "serviceGroup": "serviceGroup", 
    "serviceName": "serviceName", 
    "kafkaTopic": "public.all.ingestion.status"
}
java_sdk_header = {
    "application": "testApplication", 
    "service": "serviceName", 
    "tenantId": "testTenant", 
    "serviceGroup": "testGroup", 
    "kafka_topic": "public.all.application.status", 
    "id": "9ed9b49f-b4f9-559c-234e-aa47d21be1d2", 
    "version": "_v1", 
    "isCompressed": False, 
    "timestamp": 1695785780031
}
java_sdk_mandatory_fields = {"events":[
    {
        "id":"ingestion_egress_uuid",
        "entityType":"entityName",
        "status":"COMPLETED",
        "eventTime":1694752440.22695
    }
],
"headers":{
    "application":"testApplication", 
    "service":"serviceName", 
    "tenantId":"testTenant", 
    "serviceGroup":"testGroup", 
    "kafka_topic":"public.all.application.status", 
    "id":"2f75f20d-7989-d1b9-4c91-819a7c8c31d6", 
    "version":"_v1", 
    "isCompressed":False, 
    "timestamp":1695785780084
}}
java_sdk_all_fields = {
    "events":[
        {
            "id":"ingestion_egress_uuid",
            "entityType":"entityName",
            "status":"COMPLETED",
            "description":"long Description",
            "eventTime":1689912000000,
            "batchId":"batchId",
            "workflowId":"business Process Id/WorkflowId",
            "totalEvents":0,"processedEvents":0,
            "ignoredEvents":0,"erroredEvents":0,
            "fileName":"ingestedFile",
            "error":{"summary":"This is error summary",
                    "errorCode":"PDC-001",
                    "details":[
                        {"recordId":"recordId","eventTime":1689912000000,"description":"This is short error desc","detailedDescription":"This is detailed error Message"}
                    ]
                }
        }
    ],
    "headers":{
        "application":"testApplication", 
        "service":"serviceName", 
        "tenantId":"testTenant", 
        "serviceGroup":"testGroup", 
        "kafka_topic":"public.all.application.status", 
        "id":"14ed92f9-e984-8c6b-260d-322089ca0de0", 
        "version":"_v1", "isCompressed":False, 
        "timestamp":1695785780102
    }
}
