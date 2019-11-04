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
from msrest.exceptions import HttpOperationError


class CanceledSubscriptionId(Model):
    """The ID of the canceled subscription.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar value: The ID of the canceled subscription
    :vartype value: str
    """

    _validation = {
        'value': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(CanceledSubscriptionId, self).__init__(**kwargs)
        self.value = None


class CloudError(Model):
    """CloudError.
    """

    _attribute_map = {
    }


class EnabledSubscriptionId(Model):
    """The ID of the subscriptions that is being enabled.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar value: The ID of the subscriptions that is being enabled
    :vartype value: str
    """

    _validation = {
        'value': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(EnabledSubscriptionId, self).__init__(**kwargs)
        self.value = None


class ErrorResponse(Model):
    """Describes the format of Error response.

    :param code: Error code
    :type code: str
    :param message: Error message indicating why the operation failed.
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ErrorResponse, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.message = kwargs.get('message', None)


class ErrorResponseException(HttpOperationError):
    """Server responsed with exception of type: 'ErrorResponse'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ErrorResponseException, self).__init__(deserialize, response, 'ErrorResponse', *args)


class Operation(Model):
    """REST API operation.

    :param name: Operation name: {provider}/{resource}/{operation}
    :type name: str
    :param display: The object that represents the operation.
    :type display: ~azure.mgmt.subscription.models.OperationDisplay
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
    }

    def __init__(self, **kwargs):
        super(Operation, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.display = kwargs.get('display', None)


class OperationDisplay(Model):
    """The object that represents the operation.

    :param provider: Service provider: Microsoft.Subscription
    :type provider: str
    :param resource: Resource on which the operation is performed: Profile,
     endpoint, etc.
    :type resource: str
    :param operation: Operation type: Read, write, delete, etc.
    :type operation: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = kwargs.get('provider', None)
        self.resource = kwargs.get('resource', None)
        self.operation = kwargs.get('operation', None)


class OperationListResult(Model):
    """Result of the request to list operations. It contains a list of operations
    and a URL link to get the next set of results.

    :param value: List of operations.
    :type value: list[~azure.mgmt.subscription.models.Operation]
    :param next_link: URL to get the next set of operation list results if
     there are any.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Operation]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(OperationListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)


class OperationName(Model):
    """The operation Name parameter.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar value: The operation Name
    :vartype value: str
    """

    _validation = {
        'value': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(OperationName, self).__init__(**kwargs)
        self.value = None


class PurchaseSupportResponseResult(Model):
    """A list of containing support plan result.

    :param purchase_record_id: the purchase record Id
    :type purchase_record_id: str
    :param status: the status
    :type status: str
    :param result: the result
    :type result: str
    :param detailed_error_code: the detailed error code
    :type detailed_error_code: str
    :param billing_total: the billing total
    :type billing_total: str
    """

    _attribute_map = {
        'purchase_record_id': {'key': 'purchaseRecordId', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'result': {'key': 'result', 'type': 'str'},
        'detailed_error_code': {'key': 'detailedErrorCode', 'type': 'str'},
        'billing_total': {'key': 'billingTotal', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(PurchaseSupportResponseResult, self).__init__(**kwargs)
        self.purchase_record_id = kwargs.get('purchase_record_id', None)
        self.status = kwargs.get('status', None)
        self.result = kwargs.get('result', None)
        self.detailed_error_code = kwargs.get('detailed_error_code', None)
        self.billing_total = kwargs.get('billing_total', None)


class PurchaseSupportStatusResponseResult(Model):
    """A list of containing Purchase Records.

    :param created_timestamp: Created timestamp
    :type created_timestamp: str
    :param quote_id: the Quotation Id
    :type quote_id: str
    :param self_url: SelfUrl
    :type self_url: str
    """

    _attribute_map = {
        'created_timestamp': {'key': 'createdTimestamp', 'type': 'str'},
        'quote_id': {'key': 'quoteId', 'type': 'str'},
        'self_url': {'key': 'selfUrl', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(PurchaseSupportStatusResponseResult, self).__init__(**kwargs)
        self.created_timestamp = kwargs.get('created_timestamp', None)
        self.quote_id = kwargs.get('quote_id', None)
        self.self_url = kwargs.get('self_url', None)


class RenamedSubscriptionId(Model):
    """The ID of the subscriptions that is being renamed.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar value: The ID of the subscriptions that is being renamed
    :vartype value: str
    """

    _validation = {
        'value': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(RenamedSubscriptionId, self).__init__(**kwargs)
        self.value = None


class SubscriptionName(Model):
    """The new name of the subscription.

    :param subscription_name: New subscription name
    :type subscription_name: str
    """

    _attribute_map = {
        'subscription_name': {'key': 'subscriptionName', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SubscriptionName, self).__init__(**kwargs)
        self.subscription_name = kwargs.get('subscription_name', None)


class SupportPlanResponseResult(Model):
    """A list of containing support plan result.

    :param id: the Asset Id
    :type id: str
    :param offer_id: the support plan
    :type offer_id: str
    :param start_date: the start date
    :type start_date: str
    :param end_date: the end date
    :type end_date: str
    :param product_id: the productId
    :type product_id: str
    :param sku_id: the skuId
    :type sku_id: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'offer_id': {'key': 'offerId', 'type': 'str'},
        'start_date': {'key': 'startDate', 'type': 'str'},
        'end_date': {'key': 'endDate', 'type': 'str'},
        'product_id': {'key': 'productId', 'type': 'str'},
        'sku_id': {'key': 'skuId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SupportPlanResponseResult, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.offer_id = kwargs.get('offer_id', None)
        self.start_date = kwargs.get('start_date', None)
        self.end_date = kwargs.get('end_date', None)
        self.product_id = kwargs.get('product_id', None)
        self.sku_id = kwargs.get('sku_id', None)
