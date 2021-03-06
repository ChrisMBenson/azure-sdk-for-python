# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class JobRelationshipProperties(Model):
    """Job relationship information properties including pipeline information,
    correlation information, etc.

    All required parameters must be populated in order to send to Azure.

    :param pipeline_id: The job relationship pipeline identifier (a GUID).
    :type pipeline_id: str
    :param pipeline_name: The friendly name of the job relationship pipeline,
     which does not need to be unique.
    :type pipeline_name: str
    :param pipeline_uri: The pipeline uri, unique, links to the originating
     service for this pipeline.
    :type pipeline_uri: str
    :param run_id: The run identifier (a GUID), unique identifier of the
     iteration of this pipeline.
    :type run_id: str
    :param recurrence_id: Required. The recurrence identifier (a GUID), unique
     per activity/script, regardless of iterations. This is something to link
     different occurrences of the same job together.
    :type recurrence_id: str
    :param recurrence_name: The recurrence name, user friendly name for the
     correlation between jobs.
    :type recurrence_name: str
    """

    _validation = {
        'pipeline_name': {'max_length': 260},
        'recurrence_id': {'required': True},
        'recurrence_name': {'max_length': 260},
    }

    _attribute_map = {
        'pipeline_id': {'key': 'pipelineId', 'type': 'str'},
        'pipeline_name': {'key': 'pipelineName', 'type': 'str'},
        'pipeline_uri': {'key': 'pipelineUri', 'type': 'str'},
        'run_id': {'key': 'runId', 'type': 'str'},
        'recurrence_id': {'key': 'recurrenceId', 'type': 'str'},
        'recurrence_name': {'key': 'recurrenceName', 'type': 'str'},
    }

    def __init__(self, *, recurrence_id: str, pipeline_id: str=None, pipeline_name: str=None, pipeline_uri: str=None, run_id: str=None, recurrence_name: str=None, **kwargs) -> None:
        super(JobRelationshipProperties, self).__init__(**kwargs)
        self.pipeline_id = pipeline_id
        self.pipeline_name = pipeline_name
        self.pipeline_uri = pipeline_uri
        self.run_id = run_id
        self.recurrence_id = recurrence_id
        self.recurrence_name = recurrence_name
