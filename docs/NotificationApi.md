# swagger_client.NotificationApi

All URIs are relative to *https://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notification_get**](NotificationApi.md#notification_get) | **GET** /notification | Get your current notifications.


# **notification_get**
> list[Notification] notification_get()

Get your current notifications.

This is an upcoming feature and currently does not return data.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationApi()

try: 
    # Get your current notifications.
    api_response = api_instance.notification_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->notification_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Notification]**](Notification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

