"""
Record Api Payload Provider
"""
class RecordPayloadProvider:
    """
    Wraps JSON for record api
    """
    def generate_createrecordayload(self):
        """
        generate record paylad-create
        :return: create payload
        """
        payload = {
            "name": "string",
            "allowed": ["null"],
            "trackingId": 0,
            "trackingFull": "string",
            "applicationId": "string",
            "referencedRecordIds": ["null"],
            "referencedByIds": ["null"],
            "matches": ["null"],
            "isNew": "true",
            "values": {},
            "repeatFieldCurrentValues": {},
            "valuesDocument": {},
            "actionsExecuted": {},
            "visualizations": {
                "additionalProp1": ["null"],
                "additionalProp2": ["null"],
                "additionalProp3": ["null"],
            },
            "applicationRevision": 0,
            "coeditSession": {
                "editors": ["null"],
                "recordId": "string",
                "applicationId": "string",
                "values": {},
                "createdDate": "string",
                "modifiedDate": "string",
                "id": "string",
                "name": "string",
                "disabled": "true",
            },
            "locked": "true",
            "lockingUser": {"id": "string", "name": "string"},
            "lockedDate": "string",
            "comments": {
                "additionalProp1": ["null"],
                "additionalProp2": ["null"],
                "additionalProp3": ["null"],
            },
            "createdDate": "string",
            "modifiedDate": "string",
            "createdByUser": {"id": "string", "name": "string"},
            "modifiedByUser": {"id": "string", "name": "string"},
            "sessionTimeSpent": 0,
            "totalTimeSpent": 0,
            "timeTrackingEnabled": "null",
            "hangfireJobId": "string",
            "isHangfireCreatedAndUnpersisted": "null",
            "infiniteLoopFlag": "null",
            "latestWorkflowRun": ["null"],
            "id": "string",
            "disabled": "null",
        }
        return payload
