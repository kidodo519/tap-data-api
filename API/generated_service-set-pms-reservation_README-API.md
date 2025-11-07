---
title: Tap Hub API - Front API v1.1
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
highlight_theme: darkula
headingLevel: 2

---

<!-- Generator: Widdershins v4.0.1 -->

<h1 id="tap-hub-api-front-api">Tap Hub API - Front API v1.1</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

API References

Base URLs:

* <a href="http://localhost:3000">http://localhost:3000</a>

* <a href="https://api.sbox.tap-ic.co.jp:8443/taphubapi-front-v1">https://api.sbox.tap-ic.co.jp:8443/taphubapi-front-v1</a>

* <a href="http://18.183.133.247:8080/taphubapi-front-v1">http://18.183.133.247:8080/taphubapi-front-v1</a>

Web: <a href="https://www.tap-ic.co.jp/">TAP Co.,Ltd.</a> 

# Authentication

* API Key (AccessToken)
    - Parameter Name: **X-API-Key**, in: header. 

<h1 id="tap-hub-api-front-api-facility">Facility</h1>

## Facility

<a id="opIdget-searchqueries-search_query-prefecture-names-prefecture_name-facilities"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:3000/searchqueries/{search_query}/prefecture-names/{prefecture_name}/facilities \
  -H 'Accept: application/json' \
  -H 'X-API-Key: API_KEY'

```

```http
GET http://localhost:3000/searchqueries/{search_query}/prefecture-names/{prefecture_name}/facilities HTTP/1.1
Host: localhost:3000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'API_KEY'
};

fetch('http://localhost:3000/searchqueries/{search_query}/prefecture-names/{prefecture_name}/facilities',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'X-API-Key' => 'API_KEY'
}

result = RestClient.get 'http://localhost:3000/searchqueries/{search_query}/prefecture-names/{prefecture_name}/facilities',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'API_KEY'
}

r = requests.get('http://localhost:3000/searchqueries/{search_query}/prefecture-names/{prefecture_name}/facilities', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'X-API-Key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','http://localhost:3000/searchqueries/{search_query}/prefecture-names/{prefecture_name}/facilities', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://localhost:3000/searchqueries/{search_query}/prefecture-names/{prefecture_name}/facilities");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:3000/searchqueries/{search_query}/prefecture-names/{prefecture_name}/facilities", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /searchqueries/{search_query}/prefecture-names/{prefecture_name}/facilities`

施設情報取得

<h3 id="facility-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|search_query|query|string|false|Search Query|
|prefecture_name|query|string|false|Name of prefecture|
|search_query|path|string|true|none|
|prefecture_name|path|string|true|none|

> Example responses

> 400 Response

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "errors": [
    {
      "parameter": "start_date",
      "detail": "invalid date",
      "code": "INVALID_PARAMETER",
      "value": "2021-13-32",
      "message": "Expected valid date, but got '2021-13-32' for start_date"
    }
  ]
}
```

<h3 id="facility-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[ApiFacilityResponse](#schemaapifacilityresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[ApiErrorResponseBadRequest](#schemaapierrorresponsebadrequest)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ApiErrorResponseUnauthorized](#schemaapierrorresponseunauthorized)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ApiErrorResponseNotFound](#schemaapierrorresponsenotfound)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[ApiErrorResponseInternalError](#schemaapierrorresponseinternalerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AccessToken
</aside>

<h1 id="tap-hub-api-front-api-provisions">Provisions</h1>

## Provisions

<a id="opIdget-hotels-hotel_id-provisions"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:3000/hotels/{hotel_id}/provisions \
  -H 'Accept: application/json' \
  -H 'X-API-Key: API_KEY'

```

```http
GET http://localhost:3000/hotels/{hotel_id}/provisions HTTP/1.1
Host: localhost:3000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'API_KEY'
};

fetch('http://localhost:3000/hotels/{hotel_id}/provisions',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'X-API-Key' => 'API_KEY'
}

result = RestClient.get 'http://localhost:3000/hotels/{hotel_id}/provisions',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'API_KEY'
}

r = requests.get('http://localhost:3000/hotels/{hotel_id}/provisions', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'X-API-Key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','http://localhost:3000/hotels/{hotel_id}/provisions', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://localhost:3000/hotels/{hotel_id}/provisions");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:3000/hotels/{hotel_id}/provisions", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /hotels/{hotel_id}/provisions`

手配品・貸出備品一覧取得

<h3 id="provisions-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|hotel_id|path|string|true|none|

> Example responses

> 400 Response

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "errors": [
    {
      "parameter": "start_date",
      "detail": "invalid date",
      "code": "INVALID_PARAMETER",
      "value": "2021-13-32",
      "message": "Expected valid date, but got '2021-13-32' for start_date"
    }
  ]
}
```

<h3 id="provisions-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|User Found|[ApiProvisionsResponse](#schemaapiprovisionsresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[ApiErrorResponseBadRequest](#schemaapierrorresponsebadrequest)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ApiErrorResponseUnauthorized](#schemaapierrorresponseunauthorized)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ApiErrorResponseNotFound](#schemaapierrorresponsenotfound)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[ApiErrorResponseInternalError](#schemaapierrorresponseinternalerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AccessToken
</aside>

## ProvisionRequests

<a id="opIddelete-hotels-hotel_id-reservations-reservation_id-provision-requests"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE http://localhost:3000/hotels/{hotel_id}/provision-requests/{provision_request_id} \
  -H 'Accept: application/json' \
  -H 'X-API-Key: API_KEY'

```

```http
DELETE http://localhost:3000/hotels/{hotel_id}/provision-requests/{provision_request_id} HTTP/1.1
Host: localhost:3000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'API_KEY'
};

fetch('http://localhost:3000/hotels/{hotel_id}/provision-requests/{provision_request_id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'X-API-Key' => 'API_KEY'
}

result = RestClient.delete 'http://localhost:3000/hotels/{hotel_id}/provision-requests/{provision_request_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'API_KEY'
}

r = requests.delete('http://localhost:3000/hotels/{hotel_id}/provision-requests/{provision_request_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'X-API-Key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','http://localhost:3000/hotels/{hotel_id}/provision-requests/{provision_request_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://localhost:3000/hotels/{hotel_id}/provision-requests/{provision_request_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "http://localhost:3000/hotels/{hotel_id}/provision-requests/{provision_request_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /hotels/{hotel_id}/provision-requests/{provision_request_id}`

手配品・貸出備品削除

<h3 id="provisionrequests-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|hotel_id|path|string|true|none|
|provision_request_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "provision_requests": {
    "id": "string",
    "provision": {
      "code": "string",
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    },
    "from_date": "2019-08-24",
    "to_date": "2019-08-24",
    "stock_control": true,
    "quantity": 0,
    "note": "string",
    "reservation_ref": {
      "reservation_id": "string",
      "room_id": "string",
      "stay_id": "string",
      "reservation_number": "string",
      "room_number": "string"
    }
  }
}
```

<h3 id="provisionrequests-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[ApiProvisionRequestResponse](#schemaapiprovisionrequestresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[ApiErrorResponseBadRequest](#schemaapierrorresponsebadrequest)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ApiErrorResponseUnauthorized](#schemaapierrorresponseunauthorized)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ApiErrorResponseNotFound](#schemaapierrorresponsenotfound)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[ApiErrorResponseInternalError](#schemaapierrorresponseinternalerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AccessToken
</aside>

<h1 id="tap-hub-api-front-api-extra-services">Extra Services</h1>

## ExtraServices

<a id="opIdDeleteExtraServiceReservation"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE http://localhost:3000/hotels/{hotel_id}/extra-service-reservations/{extra_service_reservation_id} \
  -H 'Accept: application/json' \
  -H 'X-API-Key: API_KEY'

```

```http
DELETE http://localhost:3000/hotels/{hotel_id}/extra-service-reservations/{extra_service_reservation_id} HTTP/1.1
Host: localhost:3000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'API_KEY'
};

fetch('http://localhost:3000/hotels/{hotel_id}/extra-service-reservations/{extra_service_reservation_id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'X-API-Key' => 'API_KEY'
}

result = RestClient.delete 'http://localhost:3000/hotels/{hotel_id}/extra-service-reservations/{extra_service_reservation_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'API_KEY'
}

r = requests.delete('http://localhost:3000/hotels/{hotel_id}/extra-service-reservations/{extra_service_reservation_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'X-API-Key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','http://localhost:3000/hotels/{hotel_id}/extra-service-reservations/{extra_service_reservation_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://localhost:3000/hotels/{hotel_id}/extra-service-reservations/{extra_service_reservation_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "http://localhost:3000/hotels/{hotel_id}/extra-service-reservations/{extra_service_reservation_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /hotels/{hotel_id}/extra-service-reservations/{extra_service_reservation_id}`

付帯施設削除

<h3 id="extraservices-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|hotel_id|path|string|true|none|
|extra_service_reservation_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "extra_reservation": {
    "id": "string",
    "service_item": {
      "code": "string",
      "name": "string",
      "kana_name": "string",
      "short_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    },
    "service_period": {
      "arrival_date": "2019-08-24",
      "arrival_time": "14:15:22Z",
      "departure_date": "2019-08-24",
      "departure_time": "14:15:22Z",
      "late_out": true
    },
    "person_count": 0,
    "note": "string",
    "reservation_ref": {
      "reservation_id": "string",
      "room_id": "string",
      "stay_id": "string",
      "reservation_number": "string",
      "room_number": "string"
    }
  }
}
```

<h3 id="extraservices-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[DeleteExtraServiceReservationResponse](#schemadeleteextraservicereservationresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[ApiErrorResponseBadRequest](#schemaapierrorresponsebadrequest)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ApiErrorResponseUnauthorized](#schemaapierrorresponseunauthorized)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ApiErrorResponseNotFound](#schemaapierrorresponsenotfound)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[ApiErrorResponseInternalError](#schemaapierrorresponseinternalerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AccessToken
</aside>

## List Extra Services

<a id="opIdListExtraServices"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:3000/hotels/{hotel_id}/extra-service-reservations?reservation_date=string \
  -H 'Accept: application/json' \
  -H 'X-API-Key: API_KEY'

```

```http
GET http://localhost:3000/hotels/{hotel_id}/extra-service-reservations?reservation_date=string HTTP/1.1
Host: localhost:3000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'API_KEY'
};

fetch('http://localhost:3000/hotels/{hotel_id}/extra-service-reservations?reservation_date=string',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'X-API-Key' => 'API_KEY'
}

result = RestClient.get 'http://localhost:3000/hotels/{hotel_id}/extra-service-reservations',
  params: {
  'reservation_date' => 'string'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'API_KEY'
}

r = requests.get('http://localhost:3000/hotels/{hotel_id}/extra-service-reservations', params={
  'reservation_date': 'string'
}, headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'X-API-Key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','http://localhost:3000/hotels/{hotel_id}/extra-service-reservations', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://localhost:3000/hotels/{hotel_id}/extra-service-reservations?reservation_date=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:3000/hotels/{hotel_id}/extra-service-reservations", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /hotels/{hotel_id}/extra-service-reservations`

付帯施設一覧取得

<h3 id="list-extra-services-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|service|query|string|false|Extra Service Code|
|reservation_date|query|string|true|reservation date|
|hotel_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "total_pages": 0,
  "total_records": 0,
  "extra_reservations": [
    {
      "id": "string",
      "service_item": {
        "code": "string",
        "name": "string",
        "kana_name": "string",
        "short_name": "string",
        "foreign_name": "string",
        "foreign_short_name": "string"
      },
      "service_period": {
        "arrival_date": "2019-08-24",
        "arrival_time": "14:15:22Z",
        "departure_date": "2019-08-24",
        "departure_time": "14:15:22Z",
        "late_out": true
      },
      "person_count": 0,
      "note": "string",
      "reservation_ref": {
        "reservation_id": "string",
        "room_id": "string",
        "stay_id": "string",
        "reservation_number": "string",
        "room_number": "string"
      }
    }
  ]
}
```

<h3 id="list-extra-services-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[ListExtraServiceReservationsResponse](#schemalistextraservicereservationsresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[ApiErrorResponseBadRequest](#schemaapierrorresponsebadrequest)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ApiErrorResponseUnauthorized](#schemaapierrorresponseunauthorized)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ApiErrorResponseNotFound](#schemaapierrorresponsenotfound)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[ApiErrorResponseInternalError](#schemaapierrorresponseinternalerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AccessToken
</aside>

## UpdateExtraServiceReservation

<a id="opIdUpdateExtraServiceReservation"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT http://localhost:3000/hotels/{hotel_id}/extra-service-reservations/{extra_service_reservation_id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'X-API-Key: API_KEY'

```

```http
PUT http://localhost:3000/hotels/{hotel_id}/extra-service-reservations/{extra_service_reservation_id} HTTP/1.1
Host: localhost:3000
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "extra_reservation": {
    "service_item_code": "str",
    "note": "string",
    "service_period": {
      "arrival_date": "2019-08-24",
      "arrival_time": "14:15:22Z",
      "departure_date": "2019-08-24",
      "departure_time": "14:15:22Z",
      "late_out": true
    },
    "person_count": 0
  }
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'X-API-Key':'API_KEY'
};

fetch('http://localhost:3000/hotels/{hotel_id}/extra-service-reservations/{extra_service_reservation_id}',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'X-API-Key' => 'API_KEY'
}

result = RestClient.put 'http://localhost:3000/hotels/{hotel_id}/extra-service-reservations/{extra_service_reservation_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'X-API-Key': 'API_KEY'
}

r = requests.put('http://localhost:3000/hotels/{hotel_id}/extra-service-reservations/{extra_service_reservation_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'X-API-Key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','http://localhost:3000/hotels/{hotel_id}/extra-service-reservations/{extra_service_reservation_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://localhost:3000/hotels/{hotel_id}/extra-service-reservations/{extra_service_reservation_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "http://localhost:3000/hotels/{hotel_id}/extra-service-reservations/{extra_service_reservation_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /hotels/{hotel_id}/extra-service-reservations/{extra_service_reservation_id}`

付帯施設修正

> Body parameter

```json
{
  "extra_reservation": {
    "service_item_code": "str",
    "note": "string",
    "service_period": {
      "arrival_date": "2019-08-24",
      "arrival_time": "14:15:22Z",
      "departure_date": "2019-08-24",
      "departure_time": "14:15:22Z",
      "late_out": true
    },
    "person_count": 0
  }
}
```

<h3 id="updateextraservicereservation-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[UpdateExtraServiceReservationRequest](#schemaupdateextraservicereservationrequest)|false|none|
|hotel_id|path|string|true|none|
|extra_service_reservation_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "extra_reservation": {
    "id": "string",
    "service_item": {
      "code": "string",
      "name": "string",
      "kana_name": "string",
      "short_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    },
    "service_period": {
      "arrival_date": "2019-08-24",
      "arrival_time": "14:15:22Z",
      "departure_date": "2019-08-24",
      "departure_time": "14:15:22Z",
      "late_out": true
    },
    "person_count": 0,
    "note": "string",
    "reservation_ref": {
      "reservation_id": "string",
      "room_id": "string",
      "stay_id": "string",
      "reservation_number": "string",
      "room_number": "string"
    }
  }
}
```

<h3 id="updateextraservicereservation-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[UpdateExtraServiceReservationResponse](#schemaupdateextraservicereservationresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[ApiErrorResponseBadRequest](#schemaapierrorresponsebadrequest)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ApiErrorResponseUnauthorized](#schemaapierrorresponseunauthorized)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ApiErrorResponseNotFound](#schemaapierrorresponsenotfound)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[ApiErrorResponseInternalError](#schemaapierrorresponseinternalerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AccessToken
</aside>

<h1 id="tap-hub-api-front-api-meals">Meals</h1>

## Meals

<a id="opIddelete-hotels-hotel_id-reservations-reservation_id-meal-reservation"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE http://localhost:3000/hotels/{hotel_id}/meal-reservations/{meal_reservation_id} \
  -H 'Accept: application/json' \
  -H 'X-API-Key: API_KEY'

```

```http
DELETE http://localhost:3000/hotels/{hotel_id}/meal-reservations/{meal_reservation_id} HTTP/1.1
Host: localhost:3000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'API_KEY'
};

fetch('http://localhost:3000/hotels/{hotel_id}/meal-reservations/{meal_reservation_id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'X-API-Key' => 'API_KEY'
}

result = RestClient.delete 'http://localhost:3000/hotels/{hotel_id}/meal-reservations/{meal_reservation_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'API_KEY'
}

r = requests.delete('http://localhost:3000/hotels/{hotel_id}/meal-reservations/{meal_reservation_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'X-API-Key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','http://localhost:3000/hotels/{hotel_id}/meal-reservations/{meal_reservation_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://localhost:3000/hotels/{hotel_id}/meal-reservations/{meal_reservation_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "http://localhost:3000/hotels/{hotel_id}/meal-reservations/{meal_reservation_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /hotels/{hotel_id}/meal-reservations/{meal_reservation_id}`

食事予約削除

<h3 id="meals-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|hotel_id|path|string|true|none|
|meal_reservation_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "meal_reservation": {
    "id": "string",
    "meal_place": {
      "id": "string",
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    },
    "meal_type": {
      "id": "string",
      "meal_place_code": "string",
      "meal_time_code": "string",
      "start_time": "14:15:22Z",
      "end_time": "14:15:22Z",
      "person_count": 0,
      "table_count": 0
    },
    "meal_time_frame": {
      "id": "string",
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    },
    "use_date": "2019-08-24",
    "meal_kana_name": "string",
    "meal_name": "string",
    "meal_short_name": "string",
    "meal_item": {
      "code": "string",
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    },
    "person_count": 0,
    "person_type": "ADULT",
    "unit_price": 0,
    "pricing_type": "INCLUDED",
    "start_time": "14:15:22Z",
    "end_time": "14:15:22Z",
    "valid": true,
    "note": "string",
    "reservation_ref": {
      "reservation_id": "string",
      "room_id": "string",
      "stay_id": "string",
      "reservation_number": "string",
      "room_number": "string"
    }
  }
}
```

<h3 id="meals-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[ApiMealReservationResponse](#schemaapimealreservationresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[ApiErrorResponseBadRequest](#schemaapierrorresponsebadrequest)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ApiErrorResponseUnauthorized](#schemaapierrorresponseunauthorized)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ApiErrorResponseNotFound](#schemaapierrorresponsenotfound)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[ApiErrorResponseInternalError](#schemaapierrorresponseinternalerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AccessToken
</aside>

## put-hotels-hotel_id-meal-reservations-meal_reservation_id

<a id="opIdput-hotels-hotel_id-meal-reservations-meal_reservation_id"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT http://localhost:3000/hotels/{hotel_id}/meal-reservations/{meal_reservation_id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'X-API-Key: API_KEY'

```

```http
PUT http://localhost:3000/hotels/{hotel_id}/meal-reservations/{meal_reservation_id} HTTP/1.1
Host: localhost:3000
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "meal_reservation": {
    "date": "2019-08-24",
    "meal_place_code": "string",
    "meal_type_code": "string",
    "meal_time_frame_code": "string",
    "meal_item_code": "string",
    "person_count": 0,
    "person_type": "ADULT",
    "unit_price": 0,
    "pricing_type": "INCLUDED",
    "start_time": "14:15:22Z",
    "end_time": "14:15:22Z",
    "valid": true,
    "note": "string"
  }
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'X-API-Key':'API_KEY'
};

fetch('http://localhost:3000/hotels/{hotel_id}/meal-reservations/{meal_reservation_id}',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'X-API-Key' => 'API_KEY'
}

result = RestClient.put 'http://localhost:3000/hotels/{hotel_id}/meal-reservations/{meal_reservation_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'X-API-Key': 'API_KEY'
}

r = requests.put('http://localhost:3000/hotels/{hotel_id}/meal-reservations/{meal_reservation_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'X-API-Key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','http://localhost:3000/hotels/{hotel_id}/meal-reservations/{meal_reservation_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://localhost:3000/hotels/{hotel_id}/meal-reservations/{meal_reservation_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "http://localhost:3000/hotels/{hotel_id}/meal-reservations/{meal_reservation_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /hotels/{hotel_id}/meal-reservations/{meal_reservation_id}`

食事予約修正

> Body parameter

```json
{
  "meal_reservation": {
    "date": "2019-08-24",
    "meal_place_code": "string",
    "meal_type_code": "string",
    "meal_time_frame_code": "string",
    "meal_item_code": "string",
    "person_count": 0,
    "person_type": "ADULT",
    "unit_price": 0,
    "pricing_type": "INCLUDED",
    "start_time": "14:15:22Z",
    "end_time": "14:15:22Z",
    "valid": true,
    "note": "string"
  }
}
```

<h3 id="put-hotels-hotel_id-meal-reservations-meal_reservation_id-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[ApiMealReservationPutRequest](#schemaapimealreservationputrequest)|false|none|
|hotel_id|path|string|true|none|
|meal_reservation_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "meal_reservation": {
    "id": "string",
    "meal_place": {
      "id": "string",
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    },
    "meal_type": {
      "id": "string",
      "meal_place_code": "string",
      "meal_time_code": "string",
      "start_time": "14:15:22Z",
      "end_time": "14:15:22Z",
      "person_count": 0,
      "table_count": 0
    },
    "meal_time_frame": {
      "id": "string",
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    },
    "use_date": "2019-08-24",
    "meal_kana_name": "string",
    "meal_name": "string",
    "meal_short_name": "string",
    "meal_item": {
      "code": "string",
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    },
    "person_count": 0,
    "person_type": "ADULT",
    "unit_price": 0,
    "pricing_type": "INCLUDED",
    "start_time": "14:15:22Z",
    "end_time": "14:15:22Z",
    "valid": true,
    "note": "string",
    "reservation_ref": {
      "reservation_id": "string",
      "room_id": "string",
      "stay_id": "string",
      "reservation_number": "string",
      "room_number": "string"
    }
  }
}
```

<h3 id="put-hotels-hotel_id-meal-reservations-meal_reservation_id-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[ApiMealReservationResponse](#schemaapimealreservationresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[ApiErrorResponseBadRequest](#schemaapierrorresponsebadrequest)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ApiErrorResponseUnauthorized](#schemaapierrorresponseunauthorized)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ApiErrorResponseNotFound](#schemaapierrorresponsenotfound)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[ApiErrorResponseInternalError](#schemaapierrorresponseinternalerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AccessToken
</aside>

<h1 id="tap-hub-api-front-api-salesentries">SalesEntries</h1>

## SalesEntries

<a id="opIdpost-hotels-hotel_id-sales-entries"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:3000/hotels/{hotel_id}/sales-entry \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'X-API-Key: API_KEY'

```

```http
POST http://localhost:3000/hotels/{hotel_id}/sales-entry HTTP/1.1
Host: localhost:3000
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "slip_date": "2019-08-24",
  "room_number": "string",
  "sales_account_list_id": "string",
  "unit_price": 0,
  "quantity": 0,
  "tax_rate": 0,
  "bill_index": 0,
  "customer_note": "string",
  "control_note": "string",
  "duty_free": true
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'X-API-Key':'API_KEY'
};

fetch('http://localhost:3000/hotels/{hotel_id}/sales-entry',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'X-API-Key' => 'API_KEY'
}

result = RestClient.post 'http://localhost:3000/hotels/{hotel_id}/sales-entry',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'X-API-Key': 'API_KEY'
}

r = requests.post('http://localhost:3000/hotels/{hotel_id}/sales-entry', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'X-API-Key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','http://localhost:3000/hotels/{hotel_id}/sales-entry', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://localhost:3000/hotels/{hotel_id}/sales-entry");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:3000/hotels/{hotel_id}/sales-entry", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /hotels/{hotel_id}/sales-entry`

Post sales entry information for a given reservation

> Body parameter

```json
{
  "slip_date": "2019-08-24",
  "room_number": "string",
  "sales_account_list_id": "string",
  "unit_price": 0,
  "quantity": 0,
  "tax_rate": 0,
  "bill_index": 0,
  "customer_note": "string",
  "control_note": "string",
  "duty_free": true
}
```

<h3 id="salesentries-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[ApiSalesEntryRequest](#schemaapisalesentryrequest)|false|none|
|hotel_id|path|string|true|facility id for the given hotel|

> Example responses

> 200 Response

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "sales_entry": {
    "slip_date": "2019-08-24",
    "sales_account_item_id": "string",
    "room_number": "string",
    "unit_price": 0,
    "quantity": 0,
    "tax_rate": 0,
    "bill_index": 0,
    "customer_note": "string",
    "control_note": "string",
    "duty_free": true
  }
}
```

<h3 id="salesentries-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[ApiSalesEntryResponse](#schemaapisalesentryresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[ApiErrorResponseBadRequest](#schemaapierrorresponsebadrequest)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ApiErrorResponseUnauthorized](#schemaapierrorresponseunauthorized)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ApiErrorResponseNotFound](#schemaapierrorresponsenotfound)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[ApiErrorResponseInternalError](#schemaapierrorresponseinternalerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AccessToken
</aside>

<h1 id="tap-hub-api-front-api-reservations">Reservations</h1>

## Reservation

<a id="opIdget-hotels-hotel_id-reservations"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:3000/hotels/{hotel_id}/reservations?to_reservation_date=2019-08-24&from_reservation_date=2019-08-24 \
  -H 'Accept: application/json' \
  -H 'X-API-Key: API_KEY'

```

```http
GET http://localhost:3000/hotels/{hotel_id}/reservations?to_reservation_date=2019-08-24&from_reservation_date=2019-08-24 HTTP/1.1
Host: localhost:3000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'API_KEY'
};

fetch('http://localhost:3000/hotels/{hotel_id}/reservations?to_reservation_date=2019-08-24&from_reservation_date=2019-08-24',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'X-API-Key' => 'API_KEY'
}

result = RestClient.get 'http://localhost:3000/hotels/{hotel_id}/reservations',
  params: {
  'to_reservation_date' => 'string(date)',
'from_reservation_date' => 'string(date)'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'API_KEY'
}

r = requests.get('http://localhost:3000/hotels/{hotel_id}/reservations', params={
  'to_reservation_date': '2019-08-24',  'from_reservation_date': '2019-08-24'
}, headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'X-API-Key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','http://localhost:3000/hotels/{hotel_id}/reservations', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://localhost:3000/hotels/{hotel_id}/reservations?to_reservation_date=2019-08-24&from_reservation_date=2019-08-24");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:3000/hotels/{hotel_id}/reservations", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /hotels/{hotel_id}/reservations`

Search for the guest reservation info

<h3 id="reservation-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|guest_name|query|string|false|guest_name|
|guest_phone_number|query|string|false|guest_phone_number|
|to_reservation_date|query|string(date)|true|to reservation date|
|reservation_number|query|string|false|reservation_number|
|room_number|query|string|false|ルーム番号|
|cursor|query|string|false|Query parameter indicating the cursor position of the list to retrieve.|
|from_reservation_date|query|string(date)|true|from reservation date|
|from_updated_date|query|string(date)|false|from_updated_date|
|to_updated_date|query|string(date)|false|to_updated_date|
|control_status|query|string|false|control_status|
|from_updated_time|query|string(time)|false|from_updated_time|
|to_updated_time|query|string(time)|false|to_updated_time|
|hotel_id|path|string|true|facility id for the given hotel|

#### Enumerated Values

|Parameter|Value|
|---|---|
|control_status|Reserve|
|control_status|Cancel|
|control_status|Stay|
|control_status|PartialStay|
|control_status|NoShow|

> Example responses

> 200 Response

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "reservations": [
    {
      "id ": "string",
      "reservation_number": "string",
      "check_in_date": "string",
      "check_out_date": "string",
      "room_sales_status": {
        "status": "Fix"
      },
      "control_status": {
        "status": "Reserve"
      },
      "person_count": [
        0
      ],
      "main_guest": {
        "person": {
          "kana_name": "string",
          "name": "string",
          "address": {
            "postal_code": "string",
            "prefecture_code": "string",
            "city": "string",
            "address_line": [
              "string"
            ]
          },
          "phone_no": "000-0000-0000",
          "phone_no_mobile": "000-0000-0000",
          "phone_no_other": "000-0000-0000",
          "gender": "Male",
          "birthday": "2019-08-24",
          "email": "example@example.com",
          "email_sub": "example@example.com",
          "external_customer_Id": "string"
        },
        "remarks": [
          {
            "system_user_company_id": "strin",
            "customer_number": "string",
            "customer_remark_id": "string",
            "importance_level_id": "PrimaryRemark",
            "facility_id": "strin",
            "date": "2019-08-24",
            "division": {
              "id": "str",
              "name": "string",
              "group_id": "str"
            },
            "type": {
              "id": "str",
              "name": "string"
            },
            "interlock_system_id": "str",
            "content": "string",
            "subject": "string",
            "output_timing": true,
            "youcom_hotel": {
              "id": "strin",
              "name": "string"
            },
            "youcom_sequence": 0,
            "create_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            },
            "change_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            }
          }
        ],
        "remak": [
          {
            "system_user_company_id": "strin",
            "customer_number": "string",
            "customer_remark_id": "string",
            "importance_level_id": "PrimaryRemark",
            "facility_id": "strin",
            "date": "2019-08-24",
            "division": {
              "id": "str",
              "name": "string",
              "group_id": "str"
            },
            "type": {
              "id": "str",
              "name": "string"
            },
            "interlock_system_id": "str",
            "content": "string",
            "subject": "string",
            "output_timing": true,
            "youcom_hotel": {
              "id": "strin",
              "name": "string"
            },
            "youcom_sequence": 0,
            "create_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            },
            "change_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            }
          }
        ],
        "id": "string",
        "customer_number": "string"
      },
      "reserved_by": {
        "person": {
          "kana_name": "string",
          "name": "string",
          "address": {
            "postal_code": "string",
            "prefecture_code": "string",
            "city": "string",
            "address_line": [
              "string"
            ]
          },
          "phone_no": "000-0000-0000",
          "phone_no_mobile": "000-0000-0000",
          "phone_no_other": "000-0000-0000",
          "gender": "Male",
          "birthday": "2019-08-24",
          "email": "example@example.com",
          "email_sub": "example@example.com",
          "external_customer_Id": "string"
        },
        "remarks": [
          {
            "system_user_company_id": "strin",
            "customer_number": "string",
            "customer_remark_id": "string",
            "importance_level_id": "PrimaryRemark",
            "facility_id": "strin",
            "date": "2019-08-24",
            "division": {
              "id": "str",
              "name": "string",
              "group_id": "str"
            },
            "type": {
              "id": "str",
              "name": "string"
            },
            "interlock_system_id": "str",
            "content": "string",
            "subject": "string",
            "output_timing": true,
            "youcom_hotel": {
              "id": "strin",
              "name": "string"
            },
            "youcom_sequence": 0,
            "create_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            },
            "change_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            }
          }
        ],
        "remak": [
          {
            "system_user_company_id": "strin",
            "customer_number": "string",
            "customer_remark_id": "string",
            "importance_level_id": "PrimaryRemark",
            "facility_id": "strin",
            "date": "2019-08-24",
            "division": {
              "id": "str",
              "name": "string",
              "group_id": "str"
            },
            "type": {
              "id": "str",
              "name": "string"
            },
            "interlock_system_id": "str",
            "content": "string",
            "subject": "string",
            "output_timing": true,
            "youcom_hotel": {
              "id": "strin",
              "name": "string"
            },
            "youcom_sequence": 0,
            "create_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            },
            "change_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            }
          }
        ],
        "id": "string",
        "customer_number": "string"
      },
      "remarks": [
        {
          "id": "string",
          "division": {
            "id": "str",
            "name": "string",
            "group_id": "str"
          },
          "remarks_type": {
            "id": "str",
            "name": "string"
          },
          "importance_level": "Primary Remark",
          "subject": "string",
          "content": "string"
        }
      ],
      "reservation_remarks": [
        {
          "id": "string",
          "division": {
            "id": "str",
            "name": "string",
            "group_id": "str"
          },
          "remarks_type": {
            "id": "str",
            "name": "string"
          },
          "importance_level": "Primary Remark",
          "subject": "string",
          "content": "string"
        }
      ],
      "room_reservations": [
        {
          "id": "string",
          "stay_registration_id ": "string",
          "room_number": "string",
          "room_status": "Vacant",
          "guests": [
            {
              "person": {
                "kana_name": "string",
                "name": "string",
                "address": {
                  "postal_code": "string",
                  "prefecture_code": "string",
                  "city": "string",
                  "address_line": [
                    "string"
                  ]
                },
                "phone_no": "000-0000-0000",
                "phone_no_mobile": "000-0000-0000",
                "phone_no_other": "000-0000-0000",
                "gender": "Male",
                "birthday": "2019-08-24",
                "email": "example@example.com",
                "email_sub": "example@example.com",
                "external_customer_Id": "string"
              },
              "remarks": [
                {
                  "system_user_company_id": "strin",
                  "customer_number": "string",
                  "customer_remark_id": "string",
                  "importance_level_id": "PrimaryRemark",
                  "facility_id": "strin",
                  "date": "2019-08-24",
                  "division": {
                    "id": "str",
                    "name": "string",
                    "group_id": "str"
                  },
                  "type": {
                    "id": "str",
                    "name": "string"
                  },
                  "interlock_system_id": "str",
                  "content": "string",
                  "subject": "string",
                  "output_timing": true,
                  "youcom_hotel": {
                    "id": "strin",
                    "name": "string"
                  },
                  "youcom_sequence": 0,
                  "create_info": {
                    "host_name": "string",
                    "time_stamp": "2019-08-24T14:15:22Z",
                    "user_account_id": "string"
                  },
                  "change_info": {
                    "host_name": "string",
                    "time_stamp": "2019-08-24T14:15:22Z",
                    "user_account_id": "string"
                  }
                }
              ],
              "remak": [
                {
                  "system_user_company_id": "strin",
                  "customer_number": "string",
                  "customer_remark_id": "string",
                  "importance_level_id": "PrimaryRemark",
                  "facility_id": "strin",
                  "date": "2019-08-24",
                  "division": {
                    "id": "str",
                    "name": "string",
                    "group_id": "str"
                  },
                  "type": {
                    "id": "str",
                    "name": "string"
                  },
                  "interlock_system_id": "str",
                  "content": "string",
                  "subject": "string",
                  "output_timing": true,
                  "youcom_hotel": {
                    "id": "strin",
                    "name": "string"
                  },
                  "youcom_sequence": 0,
                  "create_info": {
                    "host_name": "string",
                    "time_stamp": "2019-08-24T14:15:22Z",
                    "user_account_id": "string"
                  },
                  "change_info": {
                    "host_name": "string",
                    "time_stamp": "2019-08-24T14:15:22Z",
                    "user_account_id": "string"
                  }
                }
              ],
              "id": "string",
              "customer_number": "string"
            }
          ],
          "room_type": {
            "code": "string",
            "standard_persons": 0,
            "max_persons": 0,
            "name": "string",
            "short_name": "string",
            "kana_name": "string",
            "foreign_name": "string",
            "foreign_short_name": "string"
          },
          "sales_control_type": "FREE",
          "sales_control_unit": "string",
          "extra_bed_count": 0,
          "stay_period": {
            "arrival_date": "2019-08-24",
            "arrival_time": "14:15:22Z",
            "departure_date": "2019-08-24",
            "departure_time": "14:15:22Z",
            "late_out": true
          },
          "reservation_route": {
            "reservationDisplayName": "string",
            "reservationRoutes": [
              {
                "code": "string",
                "name": "string",
                "short_name": "string",
                "kana_name": "string",
                "foreign_name": "string",
                "foreign_short_name": "string"
              }
            ]
          },
          "agent_reservation_number": "string",
          "agent_course": "string",
          "person_count": [
            0
          ],
          "pricing": {
            "sales_package": {
              "code": "string",
              "name": "string",
              "short_name": "string",
              "kana_name": "string",
              "foreign_name": "string",
              "foreign_short_name": "string",
              "print_name": "string",
              "print_foreign_name": "string"
            },
            "discount_item": {
              "code": "string",
              "name": "string",
              "short_name": "string",
              "kana_name": "string",
              "foreign_name": "string",
              "foreign_short_name": "string",
              "rate": 0,
              "amount": 0
            },
            "discount_rate": 100,
            "discount_amount": 0,
            "pricing_type": "GROSS",
            "price": 0
          },
          "provision_requests": [
            {
              "id": "string",
              "provision": {
                "code": "string",
                "name": "string",
                "short_name": "string",
                "kana_name": "string",
                "foreign_name": "string",
                "foreign_short_name": "string"
              },
              "from_date": "2019-08-24",
              "to_date": "2019-08-24",
              "stock_control": true,
              "quantity": 0,
              "note": "string",
              "reservation_ref": {
                "reservation_id": "string",
                "room_id": "string",
                "stay_id": "string",
                "reservation_number": "string",
                "room_number": "string"
              }
            }
          ],
          "meal_reservations": [
            {
              "id": "string",
              "meal_place": {
                "id": "string",
                "name": "string",
                "short_name": "string",
                "kana_name": "string",
                "foreign_name": "string",
                "foreign_short_name": "string"
              },
              "meal_type": {
                "id": "string",
                "meal_place_code": "string",
                "meal_time_code": "string",
                "start_time": "14:15:22Z",
                "end_time": "14:15:22Z",
                "person_count": 0,
                "table_count": 0
              },
              "meal_time_frame": {
                "id": "string",
                "name": "string",
                "short_name": "string",
                "kana_name": "string",
                "foreign_name": "string",
                "foreign_short_name": "string"
              },
              "use_date": "2019-08-24",
              "meal_kana_name": "string",
              "meal_name": "string",
              "meal_short_name": "string",
              "meal_item": {
                "code": "string",
                "name": "string",
                "short_name": "string",
                "kana_name": "string",
                "foreign_name": "string",
                "foreign_short_name": "string"
              },
              "person_count": 0,
              "person_type": "ADULT",
              "unit_price": 0,
              "pricing_type": "INCLUDED",
              "start_time": "14:15:22Z",
              "end_time": "14:15:22Z",
              "valid": true,
              "note": "string",
              "reservation_ref": {
                "reservation_id": "string",
                "room_id": "string",
                "stay_id": "string",
                "reservation_number": "string",
                "room_number": "string"
              }
            }
          ],
          "deposits": [
            {
              "id": "string",
              "account_date": "2019-08-24",
              "payment_method": {
                "code": "string",
                "name": "string",
                "short_name": "string",
                "kana_name": "string",
                "foreign_name": "string",
                "foreign_short_name": "string",
                "use_address": true
              },
              "billing_provider": {
                "code": "string",
                "name": "string",
                "short_name": "string",
                "kana_name": "string",
                "foreign_name": "string",
                "foreign_short_name": "string"
              },
              "amount": 0,
              "bill_index": 0,
              "bill_note": "string",
              "internal_note": "string",
              "provider_reference": "string",
              "reservation_ref": {
                "reservation_id": "string",
                "room_id": "string",
                "stay_id": "string",
                "reservation_number": "string",
                "room_number": "string"
              }
            }
          ],
          "slip_items": [
            {
              "id": "string",
              "date": "2019-08-24",
              "item": {
                "code": "string",
                "name": "string",
                "short_name": "string",
                "kana_name": "string",
                "foreign_name": "string",
                "price": 0
              },
              "price_per_item": 0,
              "quantity": 0,
              "total_price": 0,
              "bill_index": 0,
              "bill_note": "string",
              "internal_note": "string",
              "tax_free": true,
              "room_type": {
                "code": "string",
                "standard_persons": 0,
                "max_persons": 0,
                "name": "string",
                "short_name": "string",
                "kana_name": "string",
                "foreign_name": "string",
                "foreign_short_name": "string"
              },
              "reservation_ref": {
                "reservation_id": "string",
                "room_id": "string",
                "stay_id": "string",
                "reservation_number": "string",
                "room_number": "string"
              }
            }
          ],
          "extra_services": [
            {
              "id": "string",
              "service_item": {
                "code": "string",
                "name": "string",
                "kana_name": "string",
                "short_name": "string",
                "foreign_name": "string",
                "foreign_short_name": "string"
              },
              "service_period": {
                "arrival_date": "2019-08-24",
                "arrival_time": "14:15:22Z",
                "departure_date": "2019-08-24",
                "departure_time": "14:15:22Z",
                "late_out": true
              },
              "person_count": 0,
              "note": "string",
              "reservation_ref": {
                "reservation_id": "string",
                "room_id": "string",
                "stay_id": "string",
                "reservation_number": "string",
                "room_number": "string"
              }
            }
          ],
          "remarks": [
            {
              "id": "string",
              "division": {
                "id": "str",
                "name": "string",
                "group_id": "str"
              },
              "remarks_type": {
                "id": "str",
                "name": "string"
              },
              "importance_level": "Primary Remark",
              "subject": "string",
              "content": "string"
            }
          ],
          "price_changes": [
            {
              "date_range_end": "2019-08-24",
              "date_range_start": "2019-08-24",
              "prices": [
                {
                  "discount_amount": 0,
                  "discount_item_id": "string",
                  "discount_item_name": "string",
                  "discount_rate": 0,
                  "person_count": [
                    0
                  ],
                  "person_count_price_calc": 0,
                  "price": 0,
                  "pricing_type": "GROSS",
                  "rate_id": "string",
                  "room_type_code": "string",
                  "sales_package_id": "string",
                  "sales_package_name": "string"
                }
              ]
            }
          ]
        }
      ],
      "is_group": true,
      "total_stay_period": {
        "arrival_date": "2019-08-24",
        "arrival_time": "14:15:22Z",
        "departure_date": "2019-08-24",
        "departure_time": "14:15:22Z",
        "late_out": true
      },
      "marketing_area": {
        "code": "string",
        "name": "string",
        "foreign_name": "string"
      },
      "last_modified": "2019-08-24T14:15:22Z",
      "created": "2019-08-24T14:15:22Z",
      "primary_remark": {
        "id": "string",
        "division": {
          "id": "str",
          "name": "string",
          "group_id": "str"
        },
        "remarks_type": {
          "id": "str",
          "name": "string"
        },
        "importance_level": "Primary Remark",
        "subject": "string",
        "content": "string"
      }
    }
  ]
}
```

<h3 id="reservation-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[ApiReservationsResponse](#schemaapireservationsresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[ApiErrorResponseBadRequest](#schemaapierrorresponsebadrequest)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ApiErrorResponseUnauthorized](#schemaapierrorresponseunauthorized)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ApiErrorResponseNotFound](#schemaapierrorresponsenotfound)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[ApiErrorResponseInternalError](#schemaapierrorresponseinternalerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AccessToken
</aside>

## Reservations

<a id="opIddelete-hotels-hotel_id-reservations-reservation_id"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id} \
  -H 'Accept: application/json' \
  -H 'X-API-Key: API_KEY'

```

```http
DELETE http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id} HTTP/1.1
Host: localhost:3000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'API_KEY'
};

fetch('http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'X-API-Key' => 'API_KEY'
}

result = RestClient.delete 'http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'API_KEY'
}

r = requests.delete('http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'X-API-Key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /hotels/{hotel_id}/reservations/{reservation_id}`

予約の削除

<h3 id="reservations-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|reservation_id|path|string|true|none|
|hotel_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "reservation": {
    "id ": "string",
    "reservation_number": "string",
    "check_in_date": "string",
    "check_out_date": "string",
    "room_sales_status": {
      "status": "Fix"
    },
    "control_status": {
      "status": "Reserve"
    },
    "person_count": [
      0
    ],
    "main_guest": {
      "person": {
        "kana_name": "string",
        "name": "string",
        "address": {
          "postal_code": "string",
          "prefecture_code": "string",
          "city": "string",
          "address_line": [
            "string"
          ]
        },
        "phone_no": "000-0000-0000",
        "phone_no_mobile": "000-0000-0000",
        "phone_no_other": "000-0000-0000",
        "gender": "Male",
        "birthday": "2019-08-24",
        "email": "example@example.com",
        "email_sub": "example@example.com",
        "external_customer_Id": "string"
      },
      "remarks": [
        {
          "system_user_company_id": "strin",
          "customer_number": "string",
          "customer_remark_id": "string",
          "importance_level_id": "PrimaryRemark",
          "facility_id": "strin",
          "date": "2019-08-24",
          "division": {
            "id": "str",
            "name": "string",
            "group_id": "str"
          },
          "type": {
            "id": "str",
            "name": "string"
          },
          "interlock_system_id": "str",
          "content": "string",
          "subject": "string",
          "output_timing": true,
          "youcom_hotel": {
            "id": "strin",
            "name": "string"
          },
          "youcom_sequence": 0,
          "create_info": {
            "host_name": "string",
            "time_stamp": "2019-08-24T14:15:22Z",
            "user_account_id": "string"
          },
          "change_info": {
            "host_name": "string",
            "time_stamp": "2019-08-24T14:15:22Z",
            "user_account_id": "string"
          }
        }
      ],
      "remak": [
        {
          "system_user_company_id": "strin",
          "customer_number": "string",
          "customer_remark_id": "string",
          "importance_level_id": "PrimaryRemark",
          "facility_id": "strin",
          "date": "2019-08-24",
          "division": {
            "id": "str",
            "name": "string",
            "group_id": "str"
          },
          "type": {
            "id": "str",
            "name": "string"
          },
          "interlock_system_id": "str",
          "content": "string",
          "subject": "string",
          "output_timing": true,
          "youcom_hotel": {
            "id": "strin",
            "name": "string"
          },
          "youcom_sequence": 0,
          "create_info": {
            "host_name": "string",
            "time_stamp": "2019-08-24T14:15:22Z",
            "user_account_id": "string"
          },
          "change_info": {
            "host_name": "string",
            "time_stamp": "2019-08-24T14:15:22Z",
            "user_account_id": "string"
          }
        }
      ],
      "id": "string",
      "customer_number": "string"
    },
    "reserved_by": {
      "person": {
        "kana_name": "string",
        "name": "string",
        "address": {
          "postal_code": "string",
          "prefecture_code": "string",
          "city": "string",
          "address_line": [
            "string"
          ]
        },
        "phone_no": "000-0000-0000",
        "phone_no_mobile": "000-0000-0000",
        "phone_no_other": "000-0000-0000",
        "gender": "Male",
        "birthday": "2019-08-24",
        "email": "example@example.com",
        "email_sub": "example@example.com",
        "external_customer_Id": "string"
      },
      "remarks": [
        {
          "system_user_company_id": "strin",
          "customer_number": "string",
          "customer_remark_id": "string",
          "importance_level_id": "PrimaryRemark",
          "facility_id": "strin",
          "date": "2019-08-24",
          "division": {
            "id": "str",
            "name": "string",
            "group_id": "str"
          },
          "type": {
            "id": "str",
            "name": "string"
          },
          "interlock_system_id": "str",
          "content": "string",
          "subject": "string",
          "output_timing": true,
          "youcom_hotel": {
            "id": "strin",
            "name": "string"
          },
          "youcom_sequence": 0,
          "create_info": {
            "host_name": "string",
            "time_stamp": "2019-08-24T14:15:22Z",
            "user_account_id": "string"
          },
          "change_info": {
            "host_name": "string",
            "time_stamp": "2019-08-24T14:15:22Z",
            "user_account_id": "string"
          }
        }
      ],
      "remak": [
        {
          "system_user_company_id": "strin",
          "customer_number": "string",
          "customer_remark_id": "string",
          "importance_level_id": "PrimaryRemark",
          "facility_id": "strin",
          "date": "2019-08-24",
          "division": {
            "id": "str",
            "name": "string",
            "group_id": "str"
          },
          "type": {
            "id": "str",
            "name": "string"
          },
          "interlock_system_id": "str",
          "content": "string",
          "subject": "string",
          "output_timing": true,
          "youcom_hotel": {
            "id": "strin",
            "name": "string"
          },
          "youcom_sequence": 0,
          "create_info": {
            "host_name": "string",
            "time_stamp": "2019-08-24T14:15:22Z",
            "user_account_id": "string"
          },
          "change_info": {
            "host_name": "string",
            "time_stamp": "2019-08-24T14:15:22Z",
            "user_account_id": "string"
          }
        }
      ],
      "id": "string",
      "customer_number": "string"
    },
    "remarks": [
      {
        "id": "string",
        "division": {
          "id": "str",
          "name": "string",
          "group_id": "str"
        },
        "remarks_type": {
          "id": "str",
          "name": "string"
        },
        "importance_level": "Primary Remark",
        "subject": "string",
        "content": "string"
      }
    ],
    "reservation_remarks": [
      {
        "id": "string",
        "division": {
          "id": "str",
          "name": "string",
          "group_id": "str"
        },
        "remarks_type": {
          "id": "str",
          "name": "string"
        },
        "importance_level": "Primary Remark",
        "subject": "string",
        "content": "string"
      }
    ],
    "room_reservations": [
      {
        "id": "string",
        "stay_registration_id ": "string",
        "room_number": "string",
        "room_status": "Vacant",
        "guests": [
          {
            "person": {
              "kana_name": "string",
              "name": "string",
              "address": {
                "postal_code": "string",
                "prefecture_code": "string",
                "city": "string",
                "address_line": [
                  "string"
                ]
              },
              "phone_no": "000-0000-0000",
              "phone_no_mobile": "000-0000-0000",
              "phone_no_other": "000-0000-0000",
              "gender": "Male",
              "birthday": "2019-08-24",
              "email": "example@example.com",
              "email_sub": "example@example.com",
              "external_customer_Id": "string"
            },
            "remarks": [
              {
                "system_user_company_id": "strin",
                "customer_number": "string",
                "customer_remark_id": "string",
                "importance_level_id": "PrimaryRemark",
                "facility_id": "strin",
                "date": "2019-08-24",
                "division": {
                  "id": "str",
                  "name": "string",
                  "group_id": "str"
                },
                "type": {
                  "id": "str",
                  "name": "string"
                },
                "interlock_system_id": "str",
                "content": "string",
                "subject": "string",
                "output_timing": true,
                "youcom_hotel": {
                  "id": "strin",
                  "name": "string"
                },
                "youcom_sequence": 0,
                "create_info": {
                  "host_name": "string",
                  "time_stamp": "2019-08-24T14:15:22Z",
                  "user_account_id": "string"
                },
                "change_info": {
                  "host_name": "string",
                  "time_stamp": "2019-08-24T14:15:22Z",
                  "user_account_id": "string"
                }
              }
            ],
            "remak": [
              {
                "system_user_company_id": "strin",
                "customer_number": "string",
                "customer_remark_id": "string",
                "importance_level_id": "PrimaryRemark",
                "facility_id": "strin",
                "date": "2019-08-24",
                "division": {
                  "id": "str",
                  "name": "string",
                  "group_id": "str"
                },
                "type": {
                  "id": "str",
                  "name": "string"
                },
                "interlock_system_id": "str",
                "content": "string",
                "subject": "string",
                "output_timing": true,
                "youcom_hotel": {
                  "id": "strin",
                  "name": "string"
                },
                "youcom_sequence": 0,
                "create_info": {
                  "host_name": "string",
                  "time_stamp": "2019-08-24T14:15:22Z",
                  "user_account_id": "string"
                },
                "change_info": {
                  "host_name": "string",
                  "time_stamp": "2019-08-24T14:15:22Z",
                  "user_account_id": "string"
                }
              }
            ],
            "id": "string",
            "customer_number": "string"
          }
        ],
        "room_type": {
          "code": "string",
          "standard_persons": 0,
          "max_persons": 0,
          "name": "string",
          "short_name": "string",
          "kana_name": "string",
          "foreign_name": "string",
          "foreign_short_name": "string"
        },
        "sales_control_type": "FREE",
        "sales_control_unit": "string",
        "extra_bed_count": 0,
        "stay_period": {
          "arrival_date": "2019-08-24",
          "arrival_time": "14:15:22Z",
          "departure_date": "2019-08-24",
          "departure_time": "14:15:22Z",
          "late_out": true
        },
        "reservation_route": {
          "reservationDisplayName": "string",
          "reservationRoutes": [
            {
              "code": "string",
              "name": "string",
              "short_name": "string",
              "kana_name": "string",
              "foreign_name": "string",
              "foreign_short_name": "string"
            }
          ]
        },
        "agent_reservation_number": "string",
        "agent_course": "string",
        "person_count": [
          0
        ],
        "pricing": {
          "sales_package": {
            "code": "string",
            "name": "string",
            "short_name": "string",
            "kana_name": "string",
            "foreign_name": "string",
            "foreign_short_name": "string",
            "print_name": "string",
            "print_foreign_name": "string"
          },
          "discount_item": {
            "code": "string",
            "name": "string",
            "short_name": "string",
            "kana_name": "string",
            "foreign_name": "string",
            "foreign_short_name": "string",
            "rate": 0,
            "amount": 0
          },
          "discount_rate": 100,
          "discount_amount": 0,
          "pricing_type": "GROSS",
          "price": 0
        },
        "provision_requests": [
          {
            "id": "string",
            "provision": {
              "code": "string",
              "name": "string",
              "short_name": "string",
              "kana_name": "string",
              "foreign_name": "string",
              "foreign_short_name": "string"
            },
            "from_date": "2019-08-24",
            "to_date": "2019-08-24",
            "stock_control": true,
            "quantity": 0,
            "note": "string",
            "reservation_ref": {
              "reservation_id": "string",
              "room_id": "string",
              "stay_id": "string",
              "reservation_number": "string",
              "room_number": "string"
            }
          }
        ],
        "meal_reservations": [
          {
            "id": "string",
            "meal_place": {
              "id": "string",
              "name": "string",
              "short_name": "string",
              "kana_name": "string",
              "foreign_name": "string",
              "foreign_short_name": "string"
            },
            "meal_type": {
              "id": "string",
              "meal_place_code": "string",
              "meal_time_code": "string",
              "start_time": "14:15:22Z",
              "end_time": "14:15:22Z",
              "person_count": 0,
              "table_count": 0
            },
            "meal_time_frame": {
              "id": "string",
              "name": "string",
              "short_name": "string",
              "kana_name": "string",
              "foreign_name": "string",
              "foreign_short_name": "string"
            },
            "use_date": "2019-08-24",
            "meal_kana_name": "string",
            "meal_name": "string",
            "meal_short_name": "string",
            "meal_item": {
              "code": "string",
              "name": "string",
              "short_name": "string",
              "kana_name": "string",
              "foreign_name": "string",
              "foreign_short_name": "string"
            },
            "person_count": 0,
            "person_type": "ADULT",
            "unit_price": 0,
            "pricing_type": "INCLUDED",
            "start_time": "14:15:22Z",
            "end_time": "14:15:22Z",
            "valid": true,
            "note": "string",
            "reservation_ref": {
              "reservation_id": "string",
              "room_id": "string",
              "stay_id": "string",
              "reservation_number": "string",
              "room_number": "string"
            }
          }
        ],
        "deposits": [
          {
            "id": "string",
            "account_date": "2019-08-24",
            "payment_method": {
              "code": "string",
              "name": "string",
              "short_name": "string",
              "kana_name": "string",
              "foreign_name": "string",
              "foreign_short_name": "string",
              "use_address": true
            },
            "billing_provider": {
              "code": "string",
              "name": "string",
              "short_name": "string",
              "kana_name": "string",
              "foreign_name": "string",
              "foreign_short_name": "string"
            },
            "amount": 0,
            "bill_index": 0,
            "bill_note": "string",
            "internal_note": "string",
            "provider_reference": "string",
            "reservation_ref": {
              "reservation_id": "string",
              "room_id": "string",
              "stay_id": "string",
              "reservation_number": "string",
              "room_number": "string"
            }
          }
        ],
        "slip_items": [
          {
            "id": "string",
            "date": "2019-08-24",
            "item": {
              "code": "string",
              "name": "string",
              "short_name": "string",
              "kana_name": "string",
              "foreign_name": "string",
              "price": 0
            },
            "price_per_item": 0,
            "quantity": 0,
            "total_price": 0,
            "bill_index": 0,
            "bill_note": "string",
            "internal_note": "string",
            "tax_free": true,
            "room_type": {
              "code": "string",
              "standard_persons": 0,
              "max_persons": 0,
              "name": "string",
              "short_name": "string",
              "kana_name": "string",
              "foreign_name": "string",
              "foreign_short_name": "string"
            },
            "reservation_ref": {
              "reservation_id": "string",
              "room_id": "string",
              "stay_id": "string",
              "reservation_number": "string",
              "room_number": "string"
            }
          }
        ],
        "extra_services": [
          {
            "id": "string",
            "service_item": {
              "code": "string",
              "name": "string",
              "kana_name": "string",
              "short_name": "string",
              "foreign_name": "string",
              "foreign_short_name": "string"
            },
            "service_period": {
              "arrival_date": "2019-08-24",
              "arrival_time": "14:15:22Z",
              "departure_date": "2019-08-24",
              "departure_time": "14:15:22Z",
              "late_out": true
            },
            "person_count": 0,
            "note": "string",
            "reservation_ref": {
              "reservation_id": "string",
              "room_id": "string",
              "stay_id": "string",
              "reservation_number": "string",
              "room_number": "string"
            }
          }
        ],
        "remarks": [
          {
            "id": "string",
            "division": {
              "id": "str",
              "name": "string",
              "group_id": "str"
            },
            "remarks_type": {
              "id": "str",
              "name": "string"
            },
            "importance_level": "Primary Remark",
            "subject": "string",
            "content": "string"
          }
        ],
        "price_changes": [
          {
            "date_range_end": "2019-08-24",
            "date_range_start": "2019-08-24",
            "prices": [
              {
                "discount_amount": 0,
                "discount_item_id": "string",
                "discount_item_name": "string",
                "discount_rate": 0,
                "person_count": [
                  0
                ],
                "person_count_price_calc": 0,
                "price": 0,
                "pricing_type": "GROSS",
                "rate_id": "string",
                "room_type_code": "string",
                "sales_package_id": "string",
                "sales_package_name": "string"
              }
            ]
          }
        ]
      }
    ],
    "is_group": true,
    "total_stay_period": {
      "arrival_date": "2019-08-24",
      "arrival_time": "14:15:22Z",
      "departure_date": "2019-08-24",
      "departure_time": "14:15:22Z",
      "late_out": true
    },
    "marketing_area": {
      "code": "string",
      "name": "string",
      "foreign_name": "string"
    },
    "last_modified": "2019-08-24T14:15:22Z",
    "created": "2019-08-24T14:15:22Z",
    "primary_remark": {
      "id": "string",
      "division": {
        "id": "str",
        "name": "string",
        "group_id": "str"
      },
      "remarks_type": {
        "id": "str",
        "name": "string"
      },
      "importance_level": "Primary Remark",
      "subject": "string",
      "content": "string"
    }
  }
}
```

<h3 id="reservations-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[ApiReservationResponse](#schemaapireservationresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[ApiErrorResponseBadRequest](#schemaapierrorresponsebadrequest)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ApiErrorResponseUnauthorized](#schemaapierrorresponseunauthorized)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ApiErrorResponseNotFound](#schemaapierrorresponsenotfound)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[ApiErrorResponseInternalError](#schemaapierrorresponseinternalerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AccessToken
</aside>

## Room-Reservation

<a id="opIddelete-hotels-hotel_id-reservations-reservation_id-rooms-room_reservation_id"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id} \
  -H 'Accept: application/json' \
  -H 'X-API-Key: API_KEY'

```

```http
DELETE http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id} HTTP/1.1
Host: localhost:3000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'API_KEY'
};

fetch('http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'X-API-Key' => 'API_KEY'
}

result = RestClient.delete 'http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'API_KEY'
}

r = requests.delete('http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'X-API-Key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}`

予約予約削除

<h3 id="room-reservation-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|hotel_id|path|string|true|none|
|reservation_id|path|string|true|none|
|room_reservation_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "room_reservation": {
    "id": "string",
    "stay_registration_id ": "string",
    "room_number": "string",
    "room_status": "Vacant",
    "guests": [
      {
        "person": {
          "kana_name": "string",
          "name": "string",
          "address": {
            "postal_code": "string",
            "prefecture_code": "string",
            "city": "string",
            "address_line": [
              "string"
            ]
          },
          "phone_no": "000-0000-0000",
          "phone_no_mobile": "000-0000-0000",
          "phone_no_other": "000-0000-0000",
          "gender": "Male",
          "birthday": "2019-08-24",
          "email": "example@example.com",
          "email_sub": "example@example.com",
          "external_customer_Id": "string"
        },
        "remarks": [
          {
            "system_user_company_id": "strin",
            "customer_number": "string",
            "customer_remark_id": "string",
            "importance_level_id": "PrimaryRemark",
            "facility_id": "strin",
            "date": "2019-08-24",
            "division": {
              "id": "str",
              "name": "string",
              "group_id": "str"
            },
            "type": {
              "id": "str",
              "name": "string"
            },
            "interlock_system_id": "str",
            "content": "string",
            "subject": "string",
            "output_timing": true,
            "youcom_hotel": {
              "id": "strin",
              "name": "string"
            },
            "youcom_sequence": 0,
            "create_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            },
            "change_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            }
          }
        ],
        "remak": [
          {
            "system_user_company_id": "strin",
            "customer_number": "string",
            "customer_remark_id": "string",
            "importance_level_id": "PrimaryRemark",
            "facility_id": "strin",
            "date": "2019-08-24",
            "division": {
              "id": "str",
              "name": "string",
              "group_id": "str"
            },
            "type": {
              "id": "str",
              "name": "string"
            },
            "interlock_system_id": "str",
            "content": "string",
            "subject": "string",
            "output_timing": true,
            "youcom_hotel": {
              "id": "strin",
              "name": "string"
            },
            "youcom_sequence": 0,
            "create_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            },
            "change_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            }
          }
        ],
        "id": "string",
        "customer_number": "string"
      }
    ],
    "room_type": {
      "code": "string",
      "standard_persons": 0,
      "max_persons": 0,
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    },
    "sales_control_type": "FREE",
    "sales_control_unit": "string",
    "extra_bed_count": 0,
    "stay_period": {
      "arrival_date": "2019-08-24",
      "arrival_time": "14:15:22Z",
      "departure_date": "2019-08-24",
      "departure_time": "14:15:22Z",
      "late_out": true
    },
    "reservation_route": {
      "reservationDisplayName": "string",
      "reservationRoutes": [
        {
          "code": "string",
          "name": "string",
          "short_name": "string",
          "kana_name": "string",
          "foreign_name": "string",
          "foreign_short_name": "string"
        }
      ]
    },
    "agent_reservation_number": "string",
    "agent_course": "string",
    "person_count": [
      0
    ],
    "pricing": {
      "sales_package": {
        "code": "string",
        "name": "string",
        "short_name": "string",
        "kana_name": "string",
        "foreign_name": "string",
        "foreign_short_name": "string",
        "print_name": "string",
        "print_foreign_name": "string"
      },
      "discount_item": {
        "code": "string",
        "name": "string",
        "short_name": "string",
        "kana_name": "string",
        "foreign_name": "string",
        "foreign_short_name": "string",
        "rate": 0,
        "amount": 0
      },
      "discount_rate": 100,
      "discount_amount": 0,
      "pricing_type": "GROSS",
      "price": 0
    },
    "provision_requests": [
      {
        "id": "string",
        "provision": {
          "code": "string",
          "name": "string",
          "short_name": "string",
          "kana_name": "string",
          "foreign_name": "string",
          "foreign_short_name": "string"
        },
        "from_date": "2019-08-24",
        "to_date": "2019-08-24",
        "stock_control": true,
        "quantity": 0,
        "note": "string",
        "reservation_ref": {
          "reservation_id": "string",
          "room_id": "string",
          "stay_id": "string",
          "reservation_number": "string",
          "room_number": "string"
        }
      }
    ],
    "meal_reservations": [
      {
        "id": "string",
        "meal_place": {
          "id": "string",
          "name": "string",
          "short_name": "string",
          "kana_name": "string",
          "foreign_name": "string",
          "foreign_short_name": "string"
        },
        "meal_type": {
          "id": "string",
          "meal_place_code": "string",
          "meal_time_code": "string",
          "start_time": "14:15:22Z",
          "end_time": "14:15:22Z",
          "person_count": 0,
          "table_count": 0
        },
        "meal_time_frame": {
          "id": "string",
          "name": "string",
          "short_name": "string",
          "kana_name": "string",
          "foreign_name": "string",
          "foreign_short_name": "string"
        },
        "use_date": "2019-08-24",
        "meal_kana_name": "string",
        "meal_name": "string",
        "meal_short_name": "string",
        "meal_item": {
          "code": "string",
          "name": "string",
          "short_name": "string",
          "kana_name": "string",
          "foreign_name": "string",
          "foreign_short_name": "string"
        },
        "person_count": 0,
        "person_type": "ADULT",
        "unit_price": 0,
        "pricing_type": "INCLUDED",
        "start_time": "14:15:22Z",
        "end_time": "14:15:22Z",
        "valid": true,
        "note": "string",
        "reservation_ref": {
          "reservation_id": "string",
          "room_id": "string",
          "stay_id": "string",
          "reservation_number": "string",
          "room_number": "string"
        }
      }
    ],
    "deposits": [
      {
        "id": "string",
        "account_date": "2019-08-24",
        "payment_method": {
          "code": "string",
          "name": "string",
          "short_name": "string",
          "kana_name": "string",
          "foreign_name": "string",
          "foreign_short_name": "string",
          "use_address": true
        },
        "billing_provider": {
          "code": "string",
          "name": "string",
          "short_name": "string",
          "kana_name": "string",
          "foreign_name": "string",
          "foreign_short_name": "string"
        },
        "amount": 0,
        "bill_index": 0,
        "bill_note": "string",
        "internal_note": "string",
        "provider_reference": "string",
        "reservation_ref": {
          "reservation_id": "string",
          "room_id": "string",
          "stay_id": "string",
          "reservation_number": "string",
          "room_number": "string"
        }
      }
    ],
    "slip_items": [
      {
        "id": "string",
        "date": "2019-08-24",
        "item": {
          "code": "string",
          "name": "string",
          "short_name": "string",
          "kana_name": "string",
          "foreign_name": "string",
          "price": 0
        },
        "price_per_item": 0,
        "quantity": 0,
        "total_price": 0,
        "bill_index": 0,
        "bill_note": "string",
        "internal_note": "string",
        "tax_free": true,
        "room_type": {
          "code": "string",
          "standard_persons": 0,
          "max_persons": 0,
          "name": "string",
          "short_name": "string",
          "kana_name": "string",
          "foreign_name": "string",
          "foreign_short_name": "string"
        },
        "reservation_ref": {
          "reservation_id": "string",
          "room_id": "string",
          "stay_id": "string",
          "reservation_number": "string",
          "room_number": "string"
        }
      }
    ],
    "extra_services": [
      {
        "id": "string",
        "service_item": {
          "code": "string",
          "name": "string",
          "kana_name": "string",
          "short_name": "string",
          "foreign_name": "string",
          "foreign_short_name": "string"
        },
        "service_period": {
          "arrival_date": "2019-08-24",
          "arrival_time": "14:15:22Z",
          "departure_date": "2019-08-24",
          "departure_time": "14:15:22Z",
          "late_out": true
        },
        "person_count": 0,
        "note": "string",
        "reservation_ref": {
          "reservation_id": "string",
          "room_id": "string",
          "stay_id": "string",
          "reservation_number": "string",
          "room_number": "string"
        }
      }
    ],
    "remarks": [
      {
        "id": "string",
        "division": {
          "id": "str",
          "name": "string",
          "group_id": "str"
        },
        "remarks_type": {
          "id": "str",
          "name": "string"
        },
        "importance_level": "Primary Remark",
        "subject": "string",
        "content": "string"
      }
    ],
    "price_changes": [
      {
        "date_range_end": "2019-08-24",
        "date_range_start": "2019-08-24",
        "prices": [
          {
            "discount_amount": 0,
            "discount_item_id": "string",
            "discount_item_name": "string",
            "discount_rate": 0,
            "person_count": [
              0
            ],
            "person_count_price_calc": 0,
            "price": 0,
            "pricing_type": "GROSS",
            "rate_id": "string",
            "room_type_code": "string",
            "sales_package_id": "string",
            "sales_package_name": "string"
          }
        ]
      }
    ]
  }
}
```

<h3 id="room-reservation-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[ApiRoomReservationResponse](#schemaapiroomreservationresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[ApiErrorResponseBadRequest](#schemaapierrorresponsebadrequest)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ApiErrorResponseUnauthorized](#schemaapierrorresponseunauthorized)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ApiErrorResponseNotFound](#schemaapierrorresponsenotfound)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[ApiErrorResponseInternalError](#schemaapierrorresponseinternalerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AccessToken
</aside>

## Room-Reservation-Remarks

<a id="opIddelete-hotels-hotel_id-reservations-reservation_id-rooms-room_reservation_id-remarks-remark_id"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/remarks/{remark_id} \
  -H 'Accept: application/json' \
  -H 'X-API-Key: API_KEY'

```

```http
DELETE http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/remarks/{remark_id} HTTP/1.1
Host: localhost:3000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'API_KEY'
};

fetch('http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/remarks/{remark_id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'X-API-Key' => 'API_KEY'
}

result = RestClient.delete 'http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/remarks/{remark_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'API_KEY'
}

r = requests.delete('http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/remarks/{remark_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'X-API-Key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/remarks/{remark_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/remarks/{remark_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/remarks/{remark_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/remarks/{remark_id}`

予約部屋備考削除

<h3 id="room-reservation-remarks-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|hotel_id|path|string|true|none|
|remark_id|path|string|true|none|
|reservation_id|path|string|true|none|
|room_reservation_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "remark": {
    "id": "string",
    "division": {
      "id": "str",
      "name": "string",
      "group_id": "str"
    },
    "remarks_type": {
      "id": "str",
      "name": "string"
    },
    "importance_level": "Primary Remark",
    "subject": "string",
    "content": "string"
  }
}
```

<h3 id="room-reservation-remarks-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[ApiRemarkResponse](#schemaapiremarkresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[ApiErrorResponseBadRequest](#schemaapierrorresponsebadrequest)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ApiErrorResponseUnauthorized](#schemaapierrorresponseunauthorized)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ApiErrorResponseNotFound](#schemaapierrorresponsenotfound)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[ApiErrorResponseInternalError](#schemaapierrorresponseinternalerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AccessToken
</aside>

## Room-Reservation-Slip-Reservation

<a id="opIddelete-hotels-hotel_id-reservations-reservation_id-rooms-room_reservation_id-slip-reservations-slip_reservation_id"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/slip-reservations/{slip_reservation_id} \
  -H 'Accept: application/json' \
  -H 'X-API-Key: API_KEY'

```

```http
DELETE http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/slip-reservations/{slip_reservation_id} HTTP/1.1
Host: localhost:3000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'API_KEY'
};

fetch('http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/slip-reservations/{slip_reservation_id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'X-API-Key' => 'API_KEY'
}

result = RestClient.delete 'http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/slip-reservations/{slip_reservation_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'API_KEY'
}

r = requests.delete('http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/slip-reservations/{slip_reservation_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'X-API-Key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/slip-reservations/{slip_reservation_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/slip-reservations/{slip_reservation_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/slip-reservations/{slip_reservation_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/slip-reservations/{slip_reservation_id}`

<h3 id="room-reservation-slip-reservation-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|hotel_id|path|string|true|none|
|reservation_id|path|string|true|none|
|room_reservation_id|path|string|true|none|
|slip_reservation_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "slip_reservation": {
    "id": "string",
    "date": "2019-08-24",
    "item": {
      "code": "string",
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "price": 0
    },
    "price_per_item": 0,
    "quantity": 0,
    "total_price": 0,
    "bill_index": 0,
    "bill_note": "string",
    "internal_note": "string",
    "tax_free": true,
    "room_type": {
      "code": "string",
      "standard_persons": 0,
      "max_persons": 0,
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    },
    "reservation_ref": {
      "reservation_id": "string",
      "room_id": "string",
      "stay_id": "string",
      "reservation_number": "string",
      "room_number": "string"
    }
  }
}
```

<h3 id="room-reservation-slip-reservation-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[ApiSlipReservationResponse](#schemaapislipreservationresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[ApiErrorResponseBadRequest](#schemaapierrorresponsebadrequest)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ApiErrorResponseUnauthorized](#schemaapierrorresponseunauthorized)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ApiErrorResponseNotFound](#schemaapierrorresponsenotfound)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[ApiErrorResponseInternalError](#schemaapierrorresponseinternalerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AccessToken
</aside>

## Room-Reservation-Deposit

<a id="opIddelete-hotels-hotel_id-reservations-reservation_id-rooms-room_reservation_id-deposits-deposit_id"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/deposits/{deposit_id} \
  -H 'Accept: application/json' \
  -H 'X-API-Key: API_KEY'

```

```http
DELETE http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/deposits/{deposit_id} HTTP/1.1
Host: localhost:3000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'API_KEY'
};

fetch('http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/deposits/{deposit_id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'X-API-Key' => 'API_KEY'
}

result = RestClient.delete 'http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/deposits/{deposit_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'API_KEY'
}

r = requests.delete('http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/deposits/{deposit_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'X-API-Key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/deposits/{deposit_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/deposits/{deposit_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/deposits/{deposit_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/deposits/{deposit_id}`

デポジットを削除

<h3 id="room-reservation-deposit-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|hotel_id|path|string|true|none|
|reservation_id|path|string|true|none|
|room_reservation_id|path|string|true|none|
|deposit_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "deposit": {
    "id": "string",
    "account_date": "2019-08-24",
    "payment_method": {
      "code": "string",
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string",
      "use_address": true
    },
    "billing_provider": {
      "code": "string",
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    },
    "amount": 0,
    "bill_index": 0,
    "bill_note": "string",
    "internal_note": "string",
    "provider_reference": "string",
    "reservation_ref": {
      "reservation_id": "string",
      "room_id": "string",
      "stay_id": "string",
      "reservation_number": "string",
      "room_number": "string"
    }
  }
}
```

<h3 id="room-reservation-deposit-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[ApiDepositResponse](#schemaapidepositresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[ApiErrorResponseBadRequest](#schemaapierrorresponsebadrequest)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ApiErrorResponseUnauthorized](#schemaapierrorresponseunauthorized)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ApiErrorResponseNotFound](#schemaapierrorresponsenotfound)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[ApiErrorResponseInternalError](#schemaapierrorresponseinternalerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AccessToken
</aside>

## Room-Reservation-Meal

<a id="opIddelete-hotels-hotel_id-reservations-reservation_id-rooms-room_reservation_id-meal-reservations-meal_reservation_id"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/meal-reservations/{meal_reservation_id} \
  -H 'Accept: application/json' \
  -H 'X-API-Key: API_KEY'

```

```http
DELETE http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/meal-reservations/{meal_reservation_id} HTTP/1.1
Host: localhost:3000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'API_KEY'
};

fetch('http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/meal-reservations/{meal_reservation_id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'X-API-Key' => 'API_KEY'
}

result = RestClient.delete 'http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/meal-reservations/{meal_reservation_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'API_KEY'
}

r = requests.delete('http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/meal-reservations/{meal_reservation_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'X-API-Key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/meal-reservations/{meal_reservation_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/meal-reservations/{meal_reservation_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/meal-reservations/{meal_reservation_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/meal-reservations/{meal_reservation_id}`

<h3 id="room-reservation-meal-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|hotel_id|path|string|true|none|
|reservation_id|path|string|true|none|
|room_reservation_id|path|string|true|none|
|meal_reservation_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "meal_reservation": {
    "id": "string",
    "meal_place": {
      "id": "string",
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    },
    "meal_type": {
      "id": "string",
      "meal_place_code": "string",
      "meal_time_code": "string",
      "start_time": "14:15:22Z",
      "end_time": "14:15:22Z",
      "person_count": 0,
      "table_count": 0
    },
    "meal_time_frame": {
      "id": "string",
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    },
    "use_date": "2019-08-24",
    "meal_kana_name": "string",
    "meal_name": "string",
    "meal_short_name": "string",
    "meal_item": {
      "code": "string",
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    },
    "person_count": 0,
    "person_type": "ADULT",
    "unit_price": 0,
    "pricing_type": "INCLUDED",
    "start_time": "14:15:22Z",
    "end_time": "14:15:22Z",
    "valid": true,
    "note": "string",
    "reservation_ref": {
      "reservation_id": "string",
      "room_id": "string",
      "stay_id": "string",
      "reservation_number": "string",
      "room_number": "string"
    }
  }
}
```

<h3 id="room-reservation-meal-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[ApiMealReservationResponse](#schemaapimealreservationresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[ApiErrorResponseBadRequest](#schemaapierrorresponsebadrequest)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ApiErrorResponseUnauthorized](#schemaapierrorresponseunauthorized)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ApiErrorResponseNotFound](#schemaapierrorresponsenotfound)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[ApiErrorResponseInternalError](#schemaapierrorresponseinternalerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AccessToken
</aside>

## Room-Reservation-Extra-Service

<a id="opIdput-hotels-hotel_id-reservations-reservation_id-rooms-room_reservation_id-extra-services-extra_service_id"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/extra-services/{extra_service_id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'X-API-Key: API_KEY'

```

```http
PUT http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/extra-services/{extra_service_id} HTTP/1.1
Host: localhost:3000
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "extra_reservation": {
    "service_item_code": "str",
    "note": "string",
    "service_period": {
      "arrival_date": "2019-08-24",
      "arrival_time": "14:15:22Z",
      "departure_date": "2019-08-24",
      "departure_time": "14:15:22Z",
      "late_out": true
    },
    "person_count": 0
  }
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'X-API-Key':'API_KEY'
};

fetch('http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/extra-services/{extra_service_id}',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'X-API-Key' => 'API_KEY'
}

result = RestClient.put 'http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/extra-services/{extra_service_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'X-API-Key': 'API_KEY'
}

r = requests.put('http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/extra-services/{extra_service_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'X-API-Key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/extra-services/{extra_service_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/extra-services/{extra_service_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/extra-services/{extra_service_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/extra-services/{extra_service_id}`

> Body parameter

```json
{
  "extra_reservation": {
    "service_item_code": "str",
    "note": "string",
    "service_period": {
      "arrival_date": "2019-08-24",
      "arrival_time": "14:15:22Z",
      "departure_date": "2019-08-24",
      "departure_time": "14:15:22Z",
      "late_out": true
    },
    "person_count": 0
  }
}
```

<h3 id="room-reservation-extra-service-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[UpdateExtraServiceReservationRequest](#schemaupdateextraservicereservationrequest)|false|none|
|hotel_id|path|string|true|none|
|reservation_id|path|string|true|none|
|room_reservation_id|path|string|true|none|
|extra_service_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "extra_reservation": {
    "id": "string",
    "service_item": {
      "code": "string",
      "name": "string",
      "kana_name": "string",
      "short_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    },
    "service_period": {
      "arrival_date": "2019-08-24",
      "arrival_time": "14:15:22Z",
      "departure_date": "2019-08-24",
      "departure_time": "14:15:22Z",
      "late_out": true
    },
    "person_count": 0,
    "note": "string",
    "reservation_ref": {
      "reservation_id": "string",
      "room_id": "string",
      "stay_id": "string",
      "reservation_number": "string",
      "room_number": "string"
    }
  }
}
```

<h3 id="room-reservation-extra-service-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[UpdateExtraServiceReservationResponse](#schemaupdateextraservicereservationresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[ApiErrorResponseBadRequest](#schemaapierrorresponsebadrequest)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ApiErrorResponseUnauthorized](#schemaapierrorresponseunauthorized)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ApiErrorResponseNotFound](#schemaapierrorresponsenotfound)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[ApiErrorResponseInternalError](#schemaapierrorresponseinternalerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AccessToken
</aside>

## delete-hotels-hotel_id-reservations-reservation_id-rooms-room_reservation_id-extra-services-extra_service_id

<a id="opIddelete-hotels-hotel_id-reservations-reservation_id-rooms-room_reservation_id-extra-services-extra_service_id"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/extra-services/{extra_service_id} \
  -H 'Accept: application/json' \
  -H 'X-API-Key: API_KEY'

```

```http
DELETE http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/extra-services/{extra_service_id} HTTP/1.1
Host: localhost:3000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'API_KEY'
};

fetch('http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/extra-services/{extra_service_id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'X-API-Key' => 'API_KEY'
}

result = RestClient.delete 'http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/extra-services/{extra_service_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'API_KEY'
}

r = requests.delete('http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/extra-services/{extra_service_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'X-API-Key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/extra-services/{extra_service_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/extra-services/{extra_service_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/extra-services/{extra_service_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/extra-services/{extra_service_id}`

Room-Reservation-Extra-Service

<h3 id="delete-hotels-hotel_id-reservations-reservation_id-rooms-room_reservation_id-extra-services-extra_service_id-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|hotel_id|path|string|true|none|
|reservation_id|path|string|true|none|
|room_reservation_id|path|string|true|none|
|extra_service_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "extra_reservation": {
    "id": "string",
    "service_item": {
      "code": "string",
      "name": "string",
      "kana_name": "string",
      "short_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    },
    "service_period": {
      "arrival_date": "2019-08-24",
      "arrival_time": "14:15:22Z",
      "departure_date": "2019-08-24",
      "departure_time": "14:15:22Z",
      "late_out": true
    },
    "person_count": 0,
    "note": "string",
    "reservation_ref": {
      "reservation_id": "string",
      "room_id": "string",
      "stay_id": "string",
      "reservation_number": "string",
      "room_number": "string"
    }
  }
}
```

<h3 id="delete-hotels-hotel_id-reservations-reservation_id-rooms-room_reservation_id-extra-services-extra_service_id-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[DeleteExtraServiceReservationResponse](#schemadeleteextraservicereservationresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[ApiErrorResponseBadRequest](#schemaapierrorresponsebadrequest)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ApiErrorResponseUnauthorized](#schemaapierrorresponseunauthorized)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ApiErrorResponseNotFound](#schemaapierrorresponsenotfound)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[ApiErrorResponseInternalError](#schemaapierrorresponseinternalerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AccessToken
</aside>

## Room-Reservation-Provisions

<a id="opIddelete-hotels-hotel_id-reservations-reservation_id-rooms-room_reservation_id-provisions-provision_id"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/provisions/{provision_id} \
  -H 'Accept: application/json' \
  -H 'X-API-Key: API_KEY'

```

```http
DELETE http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/provisions/{provision_id} HTTP/1.1
Host: localhost:3000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'API_KEY'
};

fetch('http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/provisions/{provision_id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'X-API-Key' => 'API_KEY'
}

result = RestClient.delete 'http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/provisions/{provision_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'API_KEY'
}

r = requests.delete('http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/provisions/{provision_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'X-API-Key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/provisions/{provision_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/provisions/{provision_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/provisions/{provision_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/provisions/{provision_id}`

<h3 id="room-reservation-provisions-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|hotel_id|path|string|true|none|
|reservation_id|path|string|true|none|
|room_reservation_id|path|string|true|none|
|provision_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "provision_requests": {
    "id": "string",
    "provision": {
      "code": "string",
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    },
    "from_date": "2019-08-24",
    "to_date": "2019-08-24",
    "stock_control": true,
    "quantity": 0,
    "note": "string",
    "reservation_ref": {
      "reservation_id": "string",
      "room_id": "string",
      "stay_id": "string",
      "reservation_number": "string",
      "room_number": "string"
    }
  }
}
```

<h3 id="room-reservation-provisions-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[ApiProvisionRequestResponse](#schemaapiprovisionrequestresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[ApiErrorResponseBadRequest](#schemaapierrorresponsebadrequest)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ApiErrorResponseUnauthorized](#schemaapierrorresponseunauthorized)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ApiErrorResponseNotFound](#schemaapierrorresponsenotfound)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[ApiErrorResponseInternalError](#schemaapierrorresponseinternalerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AccessToken
</aside>

## Reservation-Revenue

<a id="opIdget-hotels-hotel_id-reservations-reservation_id-revenue"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/revenue \
  -H 'Accept: application/json' \
  -H 'X-API-Key: API_KEY'

```

```http
GET http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/revenue HTTP/1.1
Host: localhost:3000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'API_KEY'
};

fetch('http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/revenue',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'X-API-Key' => 'API_KEY'
}

result = RestClient.get 'http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/revenue',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'API_KEY'
}

r = requests.get('http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/revenue', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'X-API-Key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/revenue', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/revenue");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/revenue", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /hotels/{hotel_id}/reservations/{reservation_id}/revenue`

室料明細を取得

<h3 id="reservation-revenue-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|bill_index|query|integer|false|bill_index|
|hotel_id|path|string|true|none|
|reservation_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "revenue_info": [
    {
      "date": "2019-08-24",
      "no": "string",
      "bill_index": "string",
      "pricing_type": "string",
      "name": "string",
      "standard_rate": "string",
      "sale_rate": "string",
      "package_rate_type": "string",
      "discount_rate": 0,
      "discount_amount": 0,
      "rate_per_person": 0,
      "rate_per_room": 0,
      "person_count": [
        0
      ],
      "number_of_use": 0,
      "number_of_room": 0,
      "sales_amount": 0,
      "service_charge": 0,
      "hotel_tax": 0,
      "bath_tax": 0,
      "meal_amount": 0,
      "tax_include": 0,
      "deposit": 0,
      "total": 0
    }
  ],
  "total_revenue": 0,
  "deposit_total": 0,
  "total": 0
}
```

<h3 id="reservation-revenue-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[ApiRevenueResponse](#schemaapirevenueresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[ApiErrorResponseBadRequest](#schemaapierrorresponsebadrequest)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ApiErrorResponseUnauthorized](#schemaapierrorresponseunauthorized)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ApiErrorResponseNotFound](#schemaapierrorresponsenotfound)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[ApiErrorResponseInternalError](#schemaapierrorresponseinternalerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AccessToken
</aside>

## Room-Reservation-Revenue

<a id="opIdget-hotels-hotel_id-reservations-reservation_id-rooms-room_reservation_id-revenue"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/revenue \
  -H 'Accept: application/json' \
  -H 'X-API-Key: API_KEY'

```

```http
GET http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/revenue HTTP/1.1
Host: localhost:3000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'API_KEY'
};

fetch('http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/revenue',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'X-API-Key' => 'API_KEY'
}

result = RestClient.get 'http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/revenue',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'API_KEY'
}

r = requests.get('http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/revenue', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'X-API-Key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/revenue', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/revenue");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/revenue", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/revenue`

室料明細を取得

<h3 id="room-reservation-revenue-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|bill_index|query|integer|false|bill_index|
|hotel_id|path|string|true|none|
|reservation_id|path|string|true|none|
|room_reservation_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "revenue_info": [
    {
      "date": "2019-08-24",
      "no": "string",
      "bill_index": "string",
      "pricing_type": "string",
      "name": "string",
      "standard_rate": "string",
      "sale_rate": "string",
      "package_rate_type": "string",
      "discount_rate": 0,
      "discount_amount": 0,
      "rate_per_person": 0,
      "rate_per_room": 0,
      "person_count": [
        0
      ],
      "number_of_use": 0,
      "number_of_room": 0,
      "sales_amount": 0,
      "service_charge": 0,
      "hotel_tax": 0,
      "bath_tax": 0,
      "meal_amount": 0,
      "tax_include": 0,
      "deposit": 0,
      "total": 0
    }
  ],
  "total_revenue": 0,
  "deposit_total": 0,
  "total": 0
}
```

<h3 id="room-reservation-revenue-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[ApiRevenueResponse](#schemaapirevenueresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[ApiErrorResponseBadRequest](#schemaapierrorresponsebadrequest)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ApiErrorResponseUnauthorized](#schemaapierrorresponseunauthorized)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ApiErrorResponseNotFound](#schemaapierrorresponsenotfound)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[ApiErrorResponseInternalError](#schemaapierrorresponseinternalerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AccessToken
</aside>

## Reservation-Remarks

<a id="opIddelete-hotels-hotel_id-reservations-reservation_id-remarks-remark_id"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/remarks/{remark_id} \
  -H 'Accept: application/json' \
  -H 'X-API-Key: API_KEY'

```

```http
DELETE http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/remarks/{remark_id} HTTP/1.1
Host: localhost:3000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'API_KEY'
};

fetch('http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/remarks/{remark_id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'X-API-Key' => 'API_KEY'
}

result = RestClient.delete 'http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/remarks/{remark_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'API_KEY'
}

r = requests.delete('http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/remarks/{remark_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'X-API-Key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/remarks/{remark_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/remarks/{remark_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/remarks/{remark_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /hotels/{hotel_id}/reservations/{reservation_id}/remarks/{remark_id}`

予約備考削除

<h3 id="reservation-remarks-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|hotel_id|path|string|true|none|
|remark_id|path|string|true|none|
|reservation_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "remark": {
    "id": "string",
    "division": {
      "id": "str",
      "name": "string",
      "group_id": "str"
    },
    "remarks_type": {
      "id": "str",
      "name": "string"
    },
    "importance_level": "Primary Remark",
    "subject": "string",
    "content": "string"
  }
}
```

<h3 id="reservation-remarks-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[ApiRemarkResponse](#schemaapiremarkresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[ApiErrorResponseBadRequest](#schemaapierrorresponsebadrequest)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ApiErrorResponseUnauthorized](#schemaapierrorresponseunauthorized)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ApiErrorResponseNotFound](#schemaapierrorresponsenotfound)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[ApiErrorResponseInternalError](#schemaapierrorresponseinternalerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AccessToken
</aside>

## Reservation-Deposit

<a id="opIddelete-hotels-hotel_id-reservations-reservation_id-deposits-deposit_id"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/deposits/{deposit_id} \
  -H 'Accept: application/json' \
  -H 'X-API-Key: API_KEY'

```

```http
DELETE http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/deposits/{deposit_id} HTTP/1.1
Host: localhost:3000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'API_KEY'
};

fetch('http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/deposits/{deposit_id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'X-API-Key' => 'API_KEY'
}

result = RestClient.delete 'http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/deposits/{deposit_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'API_KEY'
}

r = requests.delete('http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/deposits/{deposit_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'X-API-Key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/deposits/{deposit_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/deposits/{deposit_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/deposits/{deposit_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /hotels/{hotel_id}/reservations/{reservation_id}/deposits/{deposit_id}`

<h3 id="reservation-deposit-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|hotel_id|path|string|true|none|
|reservation_id|path|string|true|none|
|deposit_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "deposit": {
    "id": "string",
    "account_date": "2019-08-24",
    "payment_method": {
      "code": "string",
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string",
      "use_address": true
    },
    "billing_provider": {
      "code": "string",
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    },
    "amount": 0,
    "bill_index": 0,
    "bill_note": "string",
    "internal_note": "string",
    "provider_reference": "string",
    "reservation_ref": {
      "reservation_id": "string",
      "room_id": "string",
      "stay_id": "string",
      "reservation_number": "string",
      "room_number": "string"
    }
  }
}
```

<h3 id="reservation-deposit-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[ApiDepositResponse](#schemaapidepositresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[ApiErrorResponseBadRequest](#schemaapierrorresponsebadrequest)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ApiErrorResponseUnauthorized](#schemaapierrorresponseunauthorized)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ApiErrorResponseNotFound](#schemaapierrorresponsenotfound)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[ApiErrorResponseInternalError](#schemaapierrorresponseinternalerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AccessToken
</aside>

## Reservation-Slip-Reservation

<a id="opIddelete-hotels-hotel_id-reservations-reservation_id-slip-reservations-slip_reservation_id"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/slip-reservations/{slip_reservation_id} \
  -H 'Accept: application/json' \
  -H 'X-API-Key: API_KEY'

```

```http
DELETE http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/slip-reservations/{slip_reservation_id} HTTP/1.1
Host: localhost:3000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'API_KEY'
};

fetch('http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/slip-reservations/{slip_reservation_id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'X-API-Key' => 'API_KEY'
}

result = RestClient.delete 'http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/slip-reservations/{slip_reservation_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'API_KEY'
}

r = requests.delete('http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/slip-reservations/{slip_reservation_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'X-API-Key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/slip-reservations/{slip_reservation_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/slip-reservations/{slip_reservation_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/slip-reservations/{slip_reservation_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /hotels/{hotel_id}/reservations/{reservation_id}/slip-reservations/{slip_reservation_id}`

<h3 id="reservation-slip-reservation-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|hotel_id|path|string|true|none|
|reservation_id|path|string|true|none|
|slip_reservation_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "slip_reservation": {
    "id": "string",
    "date": "2019-08-24",
    "item": {
      "code": "string",
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "price": 0
    },
    "price_per_item": 0,
    "quantity": 0,
    "total_price": 0,
    "bill_index": 0,
    "bill_note": "string",
    "internal_note": "string",
    "tax_free": true,
    "room_type": {
      "code": "string",
      "standard_persons": 0,
      "max_persons": 0,
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    },
    "reservation_ref": {
      "reservation_id": "string",
      "room_id": "string",
      "stay_id": "string",
      "reservation_number": "string",
      "room_number": "string"
    }
  }
}
```

<h3 id="reservation-slip-reservation-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[ApiSlipReservationResponse](#schemaapislipreservationresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[ApiErrorResponseBadRequest](#schemaapierrorresponsebadrequest)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ApiErrorResponseUnauthorized](#schemaapierrorresponseunauthorized)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ApiErrorResponseNotFound](#schemaapierrorresponsenotfound)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[ApiErrorResponseInternalError](#schemaapierrorresponseinternalerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AccessToken
</aside>

## Reservation-Extra-Service

<a id="opIddelete-hotels-hotel_id-reservations-reservation_id-extra-services-extra_service_id"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/extra-services/{extra_service_id} \
  -H 'Accept: application/json' \
  -H 'X-API-Key: API_KEY'

```

```http
DELETE http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/extra-services/{extra_service_id} HTTP/1.1
Host: localhost:3000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'API_KEY'
};

fetch('http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/extra-services/{extra_service_id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'X-API-Key' => 'API_KEY'
}

result = RestClient.delete 'http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/extra-services/{extra_service_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'API_KEY'
}

r = requests.delete('http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/extra-services/{extra_service_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'X-API-Key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/extra-services/{extra_service_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/extra-services/{extra_service_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/extra-services/{extra_service_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /hotels/{hotel_id}/reservations/{reservation_id}/extra-services/{extra_service_id}`

<h3 id="reservation-extra-service-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|hotel_id|path|string|true|none|
|reservation_id|path|string|true|none|
|extra_service_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "extra_reservation": {
    "id": "string",
    "service_item": {
      "code": "string",
      "name": "string",
      "kana_name": "string",
      "short_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    },
    "service_period": {
      "arrival_date": "2019-08-24",
      "arrival_time": "14:15:22Z",
      "departure_date": "2019-08-24",
      "departure_time": "14:15:22Z",
      "late_out": true
    },
    "person_count": 0,
    "note": "string",
    "reservation_ref": {
      "reservation_id": "string",
      "room_id": "string",
      "stay_id": "string",
      "reservation_number": "string",
      "room_number": "string"
    }
  }
}
```

<h3 id="reservation-extra-service-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[DeleteExtraServiceReservationResponse](#schemadeleteextraservicereservationresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[ApiErrorResponseBadRequest](#schemaapierrorresponsebadrequest)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ApiErrorResponseUnauthorized](#schemaapierrorresponseunauthorized)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ApiErrorResponseNotFound](#schemaapierrorresponsenotfound)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[ApiErrorResponseInternalError](#schemaapierrorresponseinternalerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AccessToken
</aside>

## Reservation-Meal

<a id="opIddelete-hotels-hotel_id-reservations-reservation_id-meal-reservations-meal_reservation_id"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/meal-reservations/{meal_reservation_id} \
  -H 'Accept: application/json' \
  -H 'X-API-Key: API_KEY'

```

```http
DELETE http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/meal-reservations/{meal_reservation_id} HTTP/1.1
Host: localhost:3000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'API_KEY'
};

fetch('http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/meal-reservations/{meal_reservation_id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'X-API-Key' => 'API_KEY'
}

result = RestClient.delete 'http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/meal-reservations/{meal_reservation_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'API_KEY'
}

r = requests.delete('http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/meal-reservations/{meal_reservation_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'X-API-Key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/meal-reservations/{meal_reservation_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/meal-reservations/{meal_reservation_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/meal-reservations/{meal_reservation_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /hotels/{hotel_id}/reservations/{reservation_id}/meal-reservations/{meal_reservation_id}`

<h3 id="reservation-meal-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|hotel_id|path|string|true|none|
|reservation_id|path|string|true|none|
|meal_reservation_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "meal_reservation": {
    "id": "string",
    "meal_place": {
      "id": "string",
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    },
    "meal_type": {
      "id": "string",
      "meal_place_code": "string",
      "meal_time_code": "string",
      "start_time": "14:15:22Z",
      "end_time": "14:15:22Z",
      "person_count": 0,
      "table_count": 0
    },
    "meal_time_frame": {
      "id": "string",
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    },
    "use_date": "2019-08-24",
    "meal_kana_name": "string",
    "meal_name": "string",
    "meal_short_name": "string",
    "meal_item": {
      "code": "string",
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    },
    "person_count": 0,
    "person_type": "ADULT",
    "unit_price": 0,
    "pricing_type": "INCLUDED",
    "start_time": "14:15:22Z",
    "end_time": "14:15:22Z",
    "valid": true,
    "note": "string",
    "reservation_ref": {
      "reservation_id": "string",
      "room_id": "string",
      "stay_id": "string",
      "reservation_number": "string",
      "room_number": "string"
    }
  }
}
```

<h3 id="reservation-meal-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[ApiMealReservationResponse](#schemaapimealreservationresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[ApiErrorResponseBadRequest](#schemaapierrorresponsebadrequest)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ApiErrorResponseUnauthorized](#schemaapierrorresponseunauthorized)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ApiErrorResponseNotFound](#schemaapierrorresponsenotfound)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[ApiErrorResponseInternalError](#schemaapierrorresponseinternalerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AccessToken
</aside>

## Reservation-Provisions

<a id="opIddelete-hotels-hotel_id-reservations-reservation_id-provisions-provision_id"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/provisions/{provision_id} \
  -H 'Accept: application/json' \
  -H 'X-API-Key: API_KEY'

```

```http
DELETE http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/provisions/{provision_id} HTTP/1.1
Host: localhost:3000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'API_KEY'
};

fetch('http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/provisions/{provision_id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'X-API-Key' => 'API_KEY'
}

result = RestClient.delete 'http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/provisions/{provision_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'API_KEY'
}

r = requests.delete('http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/provisions/{provision_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'X-API-Key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/provisions/{provision_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/provisions/{provision_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/provisions/{provision_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /hotels/{hotel_id}/reservations/{reservation_id}/provisions/{provision_id}`

<h3 id="reservation-provisions-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|hotel_id|path|string|true|none|
|reservation_id|path|string|true|none|
|provision_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "provision_requests": {
    "id": "string",
    "provision": {
      "code": "string",
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    },
    "from_date": "2019-08-24",
    "to_date": "2019-08-24",
    "stock_control": true,
    "quantity": 0,
    "note": "string",
    "reservation_ref": {
      "reservation_id": "string",
      "room_id": "string",
      "stay_id": "string",
      "reservation_number": "string",
      "room_number": "string"
    }
  }
}
```

<h3 id="reservation-provisions-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[ApiProvisionRequestResponse](#schemaapiprovisionrequestresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[ApiErrorResponseBadRequest](#schemaapierrorresponsebadrequest)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ApiErrorResponseUnauthorized](#schemaapierrorresponseunauthorized)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ApiErrorResponseNotFound](#schemaapierrorresponsenotfound)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[ApiErrorResponseInternalError](#schemaapierrorresponseinternalerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AccessToken
</aside>

## Reservation-BillingRequest

<a id="opIdDeleteReservationBilling"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/billing-requests/{bill_index} \
  -H 'Accept: application/json' \
  -H 'X-API-Key: API_KEY'

```

```http
DELETE http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/billing-requests/{bill_index} HTTP/1.1
Host: localhost:3000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'API_KEY'
};

fetch('http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/billing-requests/{bill_index}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'X-API-Key' => 'API_KEY'
}

result = RestClient.delete 'http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/billing-requests/{bill_index}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'API_KEY'
}

r = requests.delete('http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/billing-requests/{bill_index}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'X-API-Key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/billing-requests/{bill_index}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/billing-requests/{bill_index}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/billing-requests/{bill_index}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /hotels/{hotel_id}/reservations/{reservation_id}/billing-requests/{bill_index}`

<h3 id="reservation-billingrequest-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|hotel_id|path|string|true|none|
|reservation_id|path|string|true|none|
|bill_index|path|integer|true|none|

> Example responses

> 200 Response

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "billing_request": {
    "bill_address_id": "string",
    "bill_address_name": "string",
    "bill_index": 0,
    "bill_to_name": "string",
    "bill_to_option_id": "Guest",
    "payment_method_id": "string",
    "payment_method_name": "string",
    "conditions": [
      {
        "item_id": "string",
        "item_name": "string"
      }
    ]
  }
}
```

<h3 id="reservation-billingrequest-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[DeleteReservationBillingResponse](#schemadeletereservationbillingresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[ApiErrorResponseBadRequest](#schemaapierrorresponsebadrequest)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ApiErrorResponseUnauthorized](#schemaapierrorresponseunauthorized)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ApiErrorResponseNotFound](#schemaapierrorresponsenotfound)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[ApiErrorResponseInternalError](#schemaapierrorresponseinternalerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AccessToken
</aside>

## RoomReservation-BillingRequest

<a id="opIdDeleteRoomReservationBilling"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/billing-requests/{bill_index} \
  -H 'Accept: application/json' \
  -H 'X-API-Key: API_KEY'

```

```http
DELETE http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/billing-requests/{bill_index} HTTP/1.1
Host: localhost:3000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'API_KEY'
};

fetch('http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/billing-requests/{bill_index}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'X-API-Key' => 'API_KEY'
}

result = RestClient.delete 'http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/billing-requests/{bill_index}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'API_KEY'
}

r = requests.delete('http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/billing-requests/{bill_index}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'X-API-Key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/billing-requests/{bill_index}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/billing-requests/{bill_index}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "http://localhost:3000/hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/billing-requests/{bill_index}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /hotels/{hotel_id}/reservations/{reservation_id}/rooms/{room_reservation_id}/billing-requests/{bill_index}`

<h3 id="roomreservation-billingrequest-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|hotel_id|path|string|true|none|
|reservation_id|path|string|true|none|
|room_reservation_id|path|string|true|none|
|bill_index|path|integer|true|none|

> Example responses

> 200 Response

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "billing_request": {
    "bill_address_id": "string",
    "bill_address_name": "string",
    "bill_index": 0,
    "bill_to_name": "string",
    "bill_to_option_id": "Guest",
    "payment_method_id": "string",
    "payment_method_name": "string",
    "conditions": [
      {
        "item_id": "string",
        "item_name": "string"
      }
    ]
  }
}
```

<h3 id="roomreservation-billingrequest-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[DeleteRoomReservationBillingResponse](#schemadeleteroomreservationbillingresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[ApiErrorResponseBadRequest](#schemaapierrorresponsebadrequest)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ApiErrorResponseUnauthorized](#schemaapierrorresponseunauthorized)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ApiErrorResponseNotFound](#schemaapierrorresponsenotfound)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[ApiErrorResponseInternalError](#schemaapierrorresponseinternalerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AccessToken
</aside>

<h1 id="tap-hub-api-front-api-rooms">Rooms</h1>

## RoomTypeGroups

<a id="opIdget-hotels-hotel_d-room-type-groups"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:3000/hotels/{hotel_id}/room-type-groups \
  -H 'Accept: application/json' \
  -H 'X-API-Key: API_KEY'

```

```http
GET http://localhost:3000/hotels/{hotel_id}/room-type-groups HTTP/1.1
Host: localhost:3000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'API_KEY'
};

fetch('http://localhost:3000/hotels/{hotel_id}/room-type-groups',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'X-API-Key' => 'API_KEY'
}

result = RestClient.get 'http://localhost:3000/hotels/{hotel_id}/room-type-groups',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'API_KEY'
}

r = requests.get('http://localhost:3000/hotels/{hotel_id}/room-type-groups', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'X-API-Key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','http://localhost:3000/hotels/{hotel_id}/room-type-groups', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://localhost:3000/hotels/{hotel_id}/room-type-groups");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:3000/hotels/{hotel_id}/room-type-groups", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /hotels/{hotel_id}/room-type-groups`

ルームタイプグループ　一覧取得

<h3 id="roomtypegroups-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|hotel_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "room_type_groups": [
    {
      "id": "string",
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foereign_name": "string",
      "foreign_short_name": "string"
    }
  ]
}
```

<h3 id="roomtypegroups-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[ApiRoomTypeGroupsResponse](#schemaapiroomtypegroupsresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[ApiErrorResponseBadRequest](#schemaapierrorresponsebadrequest)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ApiErrorResponseUnauthorized](#schemaapierrorresponseunauthorized)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ApiErrorResponseNotFound](#schemaapierrorresponsenotfound)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[ApiErrorResponseInternalError](#schemaapierrorresponseinternalerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AccessToken
</aside>

## RoomTypes

<a id="opIdget-hotel-hotel_id-room-types"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:3000/hotels/{hotel_id}/room-types \
  -H 'Accept: application/json' \
  -H 'X-API-Key: API_KEY'

```

```http
GET http://localhost:3000/hotels/{hotel_id}/room-types HTTP/1.1
Host: localhost:3000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'API_KEY'
};

fetch('http://localhost:3000/hotels/{hotel_id}/room-types',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'X-API-Key' => 'API_KEY'
}

result = RestClient.get 'http://localhost:3000/hotels/{hotel_id}/room-types',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'API_KEY'
}

r = requests.get('http://localhost:3000/hotels/{hotel_id}/room-types', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'X-API-Key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','http://localhost:3000/hotels/{hotel_id}/room-types', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://localhost:3000/hotels/{hotel_id}/room-types");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:3000/hotels/{hotel_id}/room-types", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /hotels/{hotel_id}/room-types`

ルームタイプ　一覧取得

<h3 id="roomtypes-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|hotel_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "room_types": [
    {
      "code": "string",
      "standard_persons": 0,
      "max_persons": 0,
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    }
  ]
}
```

<h3 id="roomtypes-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[ApiRoomTypesResponse](#schemaapiroomtypesresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[ApiErrorResponseBadRequest](#schemaapierrorresponsebadrequest)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ApiErrorResponseUnauthorized](#schemaapierrorresponseunauthorized)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ApiErrorResponseNotFound](#schemaapierrorresponsenotfound)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[ApiErrorResponseInternalError](#schemaapierrorresponseinternalerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AccessToken
</aside>

## Rooms

<a id="opIdget-hotels-hotel_id-rooms"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:3000/hotels/{hotel_id}/rooms \
  -H 'Accept: application/json' \
  -H 'X-API-Key: API_KEY'

```

```http
GET http://localhost:3000/hotels/{hotel_id}/rooms HTTP/1.1
Host: localhost:3000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'API_KEY'
};

fetch('http://localhost:3000/hotels/{hotel_id}/rooms',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'X-API-Key' => 'API_KEY'
}

result = RestClient.get 'http://localhost:3000/hotels/{hotel_id}/rooms',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'API_KEY'
}

r = requests.get('http://localhost:3000/hotels/{hotel_id}/rooms', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'X-API-Key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','http://localhost:3000/hotels/{hotel_id}/rooms', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://localhost:3000/hotels/{hotel_id}/rooms");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:3000/hotels/{hotel_id}/rooms", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /hotels/{hotel_id}/rooms`

ルームNO.　一覧取得

<h3 id="rooms-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|hotel_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "rooms": [
    {
      "room_number": "string",
      "floor_id": "string",
      "room_type": {
        "code": "string",
        "standard_persons": 0,
        "max_persons": 0,
        "name": "string",
        "short_name": "string",
        "kana_name": "string",
        "foreign_name": "string",
        "foreign_short_name": "string"
      },
      "vacant_days": 0,
      "stay_count": 0
    }
  ]
}
```

<h3 id="rooms-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[ApiRoomsResponse](#schemaapiroomsresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[ApiErrorResponseBadRequest](#schemaapierrorresponsebadrequest)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ApiErrorResponseUnauthorized](#schemaapierrorresponseunauthorized)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ApiErrorResponseNotFound](#schemaapierrorresponsenotfound)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[ApiErrorResponseInternalError](#schemaapierrorresponseinternalerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AccessToken
</aside>

<h1 id="tap-hub-api-front-api-salesaccountitems">SalesAccountItems</h1>

## SalesAccountItem

<a id="opIdget-hotels-hotel_id-sales-account-items"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:3000/hotels/{hotel_id}/sales-account-items \
  -H 'Accept: application/json' \
  -H 'X-API-Key: API_KEY'

```

```http
GET http://localhost:3000/hotels/{hotel_id}/sales-account-items HTTP/1.1
Host: localhost:3000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'API_KEY'
};

fetch('http://localhost:3000/hotels/{hotel_id}/sales-account-items',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'X-API-Key' => 'API_KEY'
}

result = RestClient.get 'http://localhost:3000/hotels/{hotel_id}/sales-account-items',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'API_KEY'
}

r = requests.get('http://localhost:3000/hotels/{hotel_id}/sales-account-items', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'X-API-Key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','http://localhost:3000/hotels/{hotel_id}/sales-account-items', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://localhost:3000/hotels/{hotel_id}/sales-account-items");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:3000/hotels/{hotel_id}/sales-account-items", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /hotels/{hotel_id}/sales-account-items`

Get available sales items for a given restaurant.

<h3 id="salesaccountitem-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|item_name|query|string|false|item name|
|cursor|query|string|false|Query parameter indicating the cursor position of the list to retrieve.|
|hotel_id|path|string|true|facility id for the given hotel|

> Example responses

> 200 Response

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "sales_account_items": [
    {
      "id": "string",
      "mid_group_id": "string",
      "kana_nane": "string",
      "name": "string",
      "short_name": "string",
      "use": true,
      "consumption_tax_calc_type_id": "st",
      "consumption_tax_charge": true,
      "sequence": 0,
      "base_unit_price": 0,
      "unit_price_exclude_tax": 0,
      "tax_rate": 0
    }
  ]
}
```

<h3 id="salesaccountitem-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[ApiSalesAccountItemResponse](#schemaapisalesaccountitemresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[ApiErrorResponseBadRequest](#schemaapierrorresponsebadrequest)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ApiErrorResponseUnauthorized](#schemaapierrorresponseunauthorized)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ApiErrorResponseNotFound](#schemaapierrorresponsenotfound)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[ApiErrorResponseInternalError](#schemaapierrorresponseinternalerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AccessToken
</aside>

<h1 id="tap-hub-api-front-api-slip-reservations">Slip Reservations</h1>

## SlipReservationItems

<a id="opIdget-hotels-hotel_id-slip_reservation_items"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:3000/hotels/{hotel_id}/slip-reservation-items \
  -H 'Accept: application/json' \
  -H 'X-API-Key: API_KEY'

```

```http
GET http://localhost:3000/hotels/{hotel_id}/slip-reservation-items HTTP/1.1
Host: localhost:3000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'API_KEY'
};

fetch('http://localhost:3000/hotels/{hotel_id}/slip-reservation-items',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'X-API-Key' => 'API_KEY'
}

result = RestClient.get 'http://localhost:3000/hotels/{hotel_id}/slip-reservation-items',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'API_KEY'
}

r = requests.get('http://localhost:3000/hotels/{hotel_id}/slip-reservation-items', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'X-API-Key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','http://localhost:3000/hotels/{hotel_id}/slip-reservation-items', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://localhost:3000/hotels/{hotel_id}/slip-reservation-items");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:3000/hotels/{hotel_id}/slip-reservation-items", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /hotels/{hotel_id}/slip-reservation-items`

伝票予約一覧取得

<h3 id="slipreservationitems-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|hotel_id|path|string|true|none|

> Example responses

> 400 Response

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "errors": [
    {
      "parameter": "start_date",
      "detail": "invalid date",
      "code": "INVALID_PARAMETER",
      "value": "2021-13-32",
      "message": "Expected valid date, but got '2021-13-32' for start_date"
    }
  ]
}
```

<h3 id="slipreservationitems-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[ApiSlipReservationItemsResponse](#schemaapislipreservationitemsresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[ApiErrorResponseBadRequest](#schemaapierrorresponsebadrequest)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ApiErrorResponseUnauthorized](#schemaapierrorresponseunauthorized)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ApiErrorResponseNotFound](#schemaapierrorresponsenotfound)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|User Not Found|[ApiErrorResponseInternalError](#schemaapierrorresponseinternalerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AccessToken
</aside>

## SlipReservations

<a id="opIdget-hotels-hotel_id-slip_reservations-slip_reservation_id"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:3000/hotels/{hotel_id}/slip-reservation/{slip_reservation_id} \
  -H 'Accept: application/json' \
  -H 'X-API-Key: API_KEY'

```

```http
GET http://localhost:3000/hotels/{hotel_id}/slip-reservation/{slip_reservation_id} HTTP/1.1
Host: localhost:3000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'API_KEY'
};

fetch('http://localhost:3000/hotels/{hotel_id}/slip-reservation/{slip_reservation_id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'X-API-Key' => 'API_KEY'
}

result = RestClient.get 'http://localhost:3000/hotels/{hotel_id}/slip-reservation/{slip_reservation_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'API_KEY'
}

r = requests.get('http://localhost:3000/hotels/{hotel_id}/slip-reservation/{slip_reservation_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'X-API-Key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','http://localhost:3000/hotels/{hotel_id}/slip-reservation/{slip_reservation_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://localhost:3000/hotels/{hotel_id}/slip-reservation/{slip_reservation_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:3000/hotels/{hotel_id}/slip-reservation/{slip_reservation_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /hotels/{hotel_id}/slip-reservation/{slip_reservation_id}`

伝票予約取得

<h3 id="slipreservations-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|hotel_id|path|string|true|none|
|slip_reservation_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "slip_reservation": {
    "id": "string",
    "date": "2019-08-24",
    "item": {
      "code": "string",
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "price": 0
    },
    "price_per_item": 0,
    "quantity": 0,
    "total_price": 0,
    "bill_index": 0,
    "bill_note": "string",
    "internal_note": "string",
    "tax_free": true,
    "room_type": {
      "code": "string",
      "standard_persons": 0,
      "max_persons": 0,
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    },
    "reservation_ref": {
      "reservation_id": "string",
      "room_id": "string",
      "stay_id": "string",
      "reservation_number": "string",
      "room_number": "string"
    }
  }
}
```

<h3 id="slipreservations-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[ApiSlipReservationResponse](#schemaapislipreservationresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[ApiErrorResponseBadRequest](#schemaapierrorresponsebadrequest)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ApiErrorResponseUnauthorized](#schemaapierrorresponseunauthorized)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ApiErrorResponseNotFound](#schemaapierrorresponsenotfound)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[ApiErrorResponseInternalError](#schemaapierrorresponseinternalerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AccessToken
</aside>

## put-hotels-hotel_id-slip-reservations-slip_reservation_id

<a id="opIdput-hotels-hotel_id-slip-reservations-slip_reservation_id"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT http://localhost:3000/hotels/{hotel_id}/slip-reservation/{slip_reservation_id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'X-API-Key: API_KEY'

```

```http
PUT http://localhost:3000/hotels/{hotel_id}/slip-reservation/{slip_reservation_id} HTTP/1.1
Host: localhost:3000
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "slip_reservation": {
    "date": "2019-08-24",
    "item_code": "string",
    "price_per_item": 0,
    "quantity": 0,
    "total_price": 0,
    "bill_index": 0,
    "bill_note": "string",
    "internal_note": "string",
    "tax_free": true,
    "room_type_code": "string"
  }
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'X-API-Key':'API_KEY'
};

fetch('http://localhost:3000/hotels/{hotel_id}/slip-reservation/{slip_reservation_id}',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'X-API-Key' => 'API_KEY'
}

result = RestClient.put 'http://localhost:3000/hotels/{hotel_id}/slip-reservation/{slip_reservation_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'X-API-Key': 'API_KEY'
}

r = requests.put('http://localhost:3000/hotels/{hotel_id}/slip-reservation/{slip_reservation_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'X-API-Key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','http://localhost:3000/hotels/{hotel_id}/slip-reservation/{slip_reservation_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://localhost:3000/hotels/{hotel_id}/slip-reservation/{slip_reservation_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "http://localhost:3000/hotels/{hotel_id}/slip-reservation/{slip_reservation_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /hotels/{hotel_id}/slip-reservation/{slip_reservation_id}`

伝票予約修正

> Body parameter

```json
{
  "slip_reservation": {
    "date": "2019-08-24",
    "item_code": "string",
    "price_per_item": 0,
    "quantity": 0,
    "total_price": 0,
    "bill_index": 0,
    "bill_note": "string",
    "internal_note": "string",
    "tax_free": true,
    "room_type_code": "string"
  }
}
```

<h3 id="put-hotels-hotel_id-slip-reservations-slip_reservation_id-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[ApiSlipReservationPutRequest](#schemaapislipreservationputrequest)|false|none|
|hotel_id|path|string|true|none|
|slip_reservation_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "slip_reservation": {
    "id": "string",
    "date": "2019-08-24",
    "item": {
      "code": "string",
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "price": 0
    },
    "price_per_item": 0,
    "quantity": 0,
    "total_price": 0,
    "bill_index": 0,
    "bill_note": "string",
    "internal_note": "string",
    "tax_free": true,
    "room_type": {
      "code": "string",
      "standard_persons": 0,
      "max_persons": 0,
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    },
    "reservation_ref": {
      "reservation_id": "string",
      "room_id": "string",
      "stay_id": "string",
      "reservation_number": "string",
      "room_number": "string"
    }
  }
}
```

<h3 id="put-hotels-hotel_id-slip-reservations-slip_reservation_id-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[ApiSlipReservationResponse](#schemaapislipreservationresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[ApiErrorResponseBadRequest](#schemaapierrorresponsebadrequest)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ApiErrorResponseUnauthorized](#schemaapierrorresponseunauthorized)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ApiErrorResponseNotFound](#schemaapierrorresponsenotfound)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[ApiErrorResponseInternalError](#schemaapierrorresponseinternalerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AccessToken
</aside>

## delete-hotels-hotel_id-slip_reservations-slip_reservation_id

<a id="opIddelete-hotels-hotel_id-slip_reservations-slip_reservation_id"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE http://localhost:3000/hotels/{hotel_id}/slip-reservation/{slip_reservation_id} \
  -H 'Accept: application/json' \
  -H 'X-API-Key: API_KEY'

```

```http
DELETE http://localhost:3000/hotels/{hotel_id}/slip-reservation/{slip_reservation_id} HTTP/1.1
Host: localhost:3000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'API_KEY'
};

fetch('http://localhost:3000/hotels/{hotel_id}/slip-reservation/{slip_reservation_id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'X-API-Key' => 'API_KEY'
}

result = RestClient.delete 'http://localhost:3000/hotels/{hotel_id}/slip-reservation/{slip_reservation_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'API_KEY'
}

r = requests.delete('http://localhost:3000/hotels/{hotel_id}/slip-reservation/{slip_reservation_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'X-API-Key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','http://localhost:3000/hotels/{hotel_id}/slip-reservation/{slip_reservation_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://localhost:3000/hotels/{hotel_id}/slip-reservation/{slip_reservation_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "http://localhost:3000/hotels/{hotel_id}/slip-reservation/{slip_reservation_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /hotels/{hotel_id}/slip-reservation/{slip_reservation_id}`

伝票予約削除

<h3 id="delete-hotels-hotel_id-slip_reservations-slip_reservation_id-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|hotel_id|path|string|true|none|
|slip_reservation_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "slip_reservation": {
    "id": "string",
    "date": "2019-08-24",
    "item": {
      "code": "string",
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "price": 0
    },
    "price_per_item": 0,
    "quantity": 0,
    "total_price": 0,
    "bill_index": 0,
    "bill_note": "string",
    "internal_note": "string",
    "tax_free": true,
    "room_type": {
      "code": "string",
      "standard_persons": 0,
      "max_persons": 0,
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    },
    "reservation_ref": {
      "reservation_id": "string",
      "room_id": "string",
      "stay_id": "string",
      "reservation_number": "string",
      "room_number": "string"
    }
  }
}
```

<h3 id="delete-hotels-hotel_id-slip_reservations-slip_reservation_id-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[ApiSlipReservationResponse](#schemaapislipreservationresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[ApiErrorResponseBadRequest](#schemaapierrorresponsebadrequest)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ApiErrorResponseUnauthorized](#schemaapierrorresponseunauthorized)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ApiErrorResponseNotFound](#schemaapierrorresponsenotfound)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[ApiErrorResponseInternalError](#schemaapierrorresponseinternalerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AccessToken
</aside>

## Deposits

<a id="opIdget-hotels-hotel_id-deposits"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:3000/hotels/{hotel_id}/deposits \
  -H 'Accept: application/json' \
  -H 'X-API-Key: API_KEY'

```

```http
GET http://localhost:3000/hotels/{hotel_id}/deposits HTTP/1.1
Host: localhost:3000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'API_KEY'
};

fetch('http://localhost:3000/hotels/{hotel_id}/deposits',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'X-API-Key' => 'API_KEY'
}

result = RestClient.get 'http://localhost:3000/hotels/{hotel_id}/deposits',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'API_KEY'
}

r = requests.get('http://localhost:3000/hotels/{hotel_id}/deposits', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'X-API-Key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','http://localhost:3000/hotels/{hotel_id}/deposits', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://localhost:3000/hotels/{hotel_id}/deposits");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:3000/hotels/{hotel_id}/deposits", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /hotels/{hotel_id}/deposits`

前受金予約一覧取得

<h3 id="deposits-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|account_date|query|string(date)|false|account date|
|payment_method|query|string|false|Payment Method|
|billing_provider|query|string|false|Billing Provider|
|note|query|string|false|Note|
|provider_reference|query|string|false|Provider Reference|
|hotel_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "deposits": [
    {
      "id": "string",
      "account_date": "2019-08-24",
      "payment_method": {
        "code": "string",
        "name": "string",
        "short_name": "string",
        "kana_name": "string",
        "foreign_name": "string",
        "foreign_short_name": "string",
        "use_address": true
      },
      "billing_provider": {
        "code": "string",
        "name": "string",
        "short_name": "string",
        "kana_name": "string",
        "foreign_name": "string",
        "foreign_short_name": "string"
      },
      "amount": 0,
      "bill_index": 0,
      "bill_note": "string",
      "internal_note": "string",
      "provider_reference": "string",
      "reservation_ref": {
        "reservation_id": "string",
        "room_id": "string",
        "stay_id": "string",
        "reservation_number": "string",
        "room_number": "string"
      }
    }
  ]
}
```

<h3 id="deposits-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[ApiDepositsResponse](#schemaapidepositsresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[ApiErrorResponseBadRequest](#schemaapierrorresponsebadrequest)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ApiErrorResponseUnauthorized](#schemaapierrorresponseunauthorized)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ApiErrorResponseNotFound](#schemaapierrorresponsenotfound)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[ApiErrorResponseInternalError](#schemaapierrorresponseinternalerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AccessToken
</aside>

## DepositSlipReservations

<a id="opIdget-hotels-hotel_id-deposits-deposit_id"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:3000/hotels/{hotel_id}/deposits/{deposit_id} \
  -H 'Accept: application/json' \
  -H 'X-API-Key: API_KEY'

```

```http
GET http://localhost:3000/hotels/{hotel_id}/deposits/{deposit_id} HTTP/1.1
Host: localhost:3000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'API_KEY'
};

fetch('http://localhost:3000/hotels/{hotel_id}/deposits/{deposit_id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'X-API-Key' => 'API_KEY'
}

result = RestClient.get 'http://localhost:3000/hotels/{hotel_id}/deposits/{deposit_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'API_KEY'
}

r = requests.get('http://localhost:3000/hotels/{hotel_id}/deposits/{deposit_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'X-API-Key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','http://localhost:3000/hotels/{hotel_id}/deposits/{deposit_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://localhost:3000/hotels/{hotel_id}/deposits/{deposit_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:3000/hotels/{hotel_id}/deposits/{deposit_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /hotels/{hotel_id}/deposits/{deposit_id}`

前受金予約取得

<h3 id="depositslipreservations-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|hotel_id|path|string|true|none|
|deposit_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "deposit": {
    "id": "string",
    "account_date": "2019-08-24",
    "payment_method": {
      "code": "string",
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string",
      "use_address": true
    },
    "billing_provider": {
      "code": "string",
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    },
    "amount": 0,
    "bill_index": 0,
    "bill_note": "string",
    "internal_note": "string",
    "provider_reference": "string",
    "reservation_ref": {
      "reservation_id": "string",
      "room_id": "string",
      "stay_id": "string",
      "reservation_number": "string",
      "room_number": "string"
    }
  }
}
```

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<ApiDepositResponse>
  <request>
    <version>string</version>
    <body>string</body>
    <url>string</url>
  </request>
  <request_id>594600f4-7eec-47ca-8012-02e7b89859ce</request_id>
  <next_cursor>c-3yvu1pzhd3i7</next_cursor>
  <deposit>
    <id>string</id>
    <account_date>2019-08-24</account_date>
    <payment_method>
      <code>string</code>
      <name>string</name>
      <short_name>string</short_name>
      <kana_name>string</kana_name>
      <foreign_name>string</foreign_name>
      <foreign_short_name>string</foreign_short_name>
      <use_address>true</use_address>
    </payment_method>
    <billing_provider>
      <code>string</code>
      <name>string</name>
      <short_name>string</short_name>
      <kana_name>string</kana_name>
      <foreign_name>string</foreign_name>
      <foreign_short_name>string</foreign_short_name>
    </billing_provider>
    <amount>0</amount>
    <bill_index>0</bill_index>
    <bill_note>string</bill_note>
    <internal_note>string</internal_note>
    <provider_reference>string</provider_reference>
    <reservation_ref>
      <reservation_id>string</reservation_id>
      <room_id>string</room_id>
      <stay_id>string</stay_id>
      <reservation_number>string</reservation_number>
      <room_number>string</room_number>
    </reservation_ref>
  </deposit>
</ApiDepositResponse>
```

<h3 id="depositslipreservations-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[ApiDepositResponse](#schemaapidepositresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[ApiErrorResponseBadRequest](#schemaapierrorresponsebadrequest)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ApiErrorResponseUnauthorized](#schemaapierrorresponseunauthorized)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ApiErrorResponseNotFound](#schemaapierrorresponsenotfound)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[ApiErrorResponseInternalError](#schemaapierrorresponseinternalerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AccessToken
</aside>

## put-hotels-hotel_id-deposits-deposit_id

<a id="opIdput-hotels-hotel_id-deposits-deposit_id"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT http://localhost:3000/hotels/{hotel_id}/deposits/{deposit_id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'X-API-Key: API_KEY'

```

```http
PUT http://localhost:3000/hotels/{hotel_id}/deposits/{deposit_id} HTTP/1.1
Host: localhost:3000
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "deposit": {
    "account_date": "2019-08-24",
    "payment_method_code": "string",
    "billing_provider_code": "string",
    "amount": 0,
    "bill_index": 0,
    "bill_note": "string",
    "internal_note": "string",
    "provider_reference": "string"
  }
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'X-API-Key':'API_KEY'
};

fetch('http://localhost:3000/hotels/{hotel_id}/deposits/{deposit_id}',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'X-API-Key' => 'API_KEY'
}

result = RestClient.put 'http://localhost:3000/hotels/{hotel_id}/deposits/{deposit_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'X-API-Key': 'API_KEY'
}

r = requests.put('http://localhost:3000/hotels/{hotel_id}/deposits/{deposit_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'X-API-Key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','http://localhost:3000/hotels/{hotel_id}/deposits/{deposit_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://localhost:3000/hotels/{hotel_id}/deposits/{deposit_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "http://localhost:3000/hotels/{hotel_id}/deposits/{deposit_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /hotels/{hotel_id}/deposits/{deposit_id}`

前受金予約修正

> Body parameter

```json
{
  "deposit": {
    "account_date": "2019-08-24",
    "payment_method_code": "string",
    "billing_provider_code": "string",
    "amount": 0,
    "bill_index": 0,
    "bill_note": "string",
    "internal_note": "string",
    "provider_reference": "string"
  }
}
```

<h3 id="put-hotels-hotel_id-deposits-deposit_id-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[ApiDepositPutRequest](#schemaapidepositputrequest)|false|none|
|hotel_id|path|string|true|none|
|deposit_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "deposit": {
    "id": "string",
    "account_date": "2019-08-24",
    "payment_method": {
      "code": "string",
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string",
      "use_address": true
    },
    "billing_provider": {
      "code": "string",
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    },
    "amount": 0,
    "bill_index": 0,
    "bill_note": "string",
    "internal_note": "string",
    "provider_reference": "string",
    "reservation_ref": {
      "reservation_id": "string",
      "room_id": "string",
      "stay_id": "string",
      "reservation_number": "string",
      "room_number": "string"
    }
  }
}
```

<h3 id="put-hotels-hotel_id-deposits-deposit_id-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[ApiDepositResponse](#schemaapidepositresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[ApiErrorResponseBadRequest](#schemaapierrorresponsebadrequest)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ApiErrorResponseUnauthorized](#schemaapierrorresponseunauthorized)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ApiErrorResponseNotFound](#schemaapierrorresponsenotfound)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[ApiErrorResponseInternalError](#schemaapierrorresponseinternalerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AccessToken
</aside>

## delete-hotels-hotel_id-deposits-deposit_id

<a id="opIddelete-hotels-hotel_id-deposits-deposit_id"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE http://localhost:3000/hotels/{hotel_id}/deposits/{deposit_id} \
  -H 'Accept: application/json' \
  -H 'X-API-Key: API_KEY'

```

```http
DELETE http://localhost:3000/hotels/{hotel_id}/deposits/{deposit_id} HTTP/1.1
Host: localhost:3000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'API_KEY'
};

fetch('http://localhost:3000/hotels/{hotel_id}/deposits/{deposit_id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'X-API-Key' => 'API_KEY'
}

result = RestClient.delete 'http://localhost:3000/hotels/{hotel_id}/deposits/{deposit_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'API_KEY'
}

r = requests.delete('http://localhost:3000/hotels/{hotel_id}/deposits/{deposit_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'X-API-Key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','http://localhost:3000/hotels/{hotel_id}/deposits/{deposit_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://localhost:3000/hotels/{hotel_id}/deposits/{deposit_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "http://localhost:3000/hotels/{hotel_id}/deposits/{deposit_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /hotels/{hotel_id}/deposits/{deposit_id}`

前受金予約削除

<h3 id="delete-hotels-hotel_id-deposits-deposit_id-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|hotel_id|path|string|true|none|
|deposit_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "deposit": {
    "id": "string",
    "account_date": "2019-08-24",
    "payment_method": {
      "code": "string",
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string",
      "use_address": true
    },
    "billing_provider": {
      "code": "string",
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    },
    "amount": 0,
    "bill_index": 0,
    "bill_note": "string",
    "internal_note": "string",
    "provider_reference": "string",
    "reservation_ref": {
      "reservation_id": "string",
      "room_id": "string",
      "stay_id": "string",
      "reservation_number": "string",
      "room_number": "string"
    }
  }
}
```

<h3 id="delete-hotels-hotel_id-deposits-deposit_id-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[ApiDepositResponse](#schemaapidepositresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[ApiErrorResponseBadRequest](#schemaapierrorresponsebadrequest)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ApiErrorResponseUnauthorized](#schemaapierrorresponseunauthorized)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ApiErrorResponseNotFound](#schemaapierrorresponsenotfound)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[ApiErrorResponseInternalError](#schemaapierrorresponseinternalerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AccessToken
</aside>

<h1 id="tap-hub-api-front-api-stays">Stays</h1>

## Stay

<a id="opIdget-hotels-hotel_id-stays"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:3000/hotels/{hotel_id}/stays?to_reservation_date=2019-08-24&from_reservation_date=2019-08-24 \
  -H 'Accept: application/json' \
  -H 'X-API-Key: API_KEY'

```

```http
GET http://localhost:3000/hotels/{hotel_id}/stays?to_reservation_date=2019-08-24&from_reservation_date=2019-08-24 HTTP/1.1
Host: localhost:3000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'API_KEY'
};

fetch('http://localhost:3000/hotels/{hotel_id}/stays?to_reservation_date=2019-08-24&from_reservation_date=2019-08-24',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'X-API-Key' => 'API_KEY'
}

result = RestClient.get 'http://localhost:3000/hotels/{hotel_id}/stays',
  params: {
  'to_reservation_date' => 'string(date)',
'from_reservation_date' => 'string(date)'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'API_KEY'
}

r = requests.get('http://localhost:3000/hotels/{hotel_id}/stays', params={
  'to_reservation_date': '2019-08-24',  'from_reservation_date': '2019-08-24'
}, headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'X-API-Key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','http://localhost:3000/hotels/{hotel_id}/stays', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://localhost:3000/hotels/{hotel_id}/stays?to_reservation_date=2019-08-24&from_reservation_date=2019-08-24");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:3000/hotels/{hotel_id}/stays", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /hotels/{hotel_id}/stays`

Retrives reservation for guest that have already checked-in

<h3 id="stay-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|guest_name|query|string|false|guest_name|
|guest_phone_number|query|string|false|guest_phone_number|
|to_reservation_date|query|string(date)|true|to reservation date|
|reservation_number|query|string|false|reservation_number|
|room_number|query|string|false|ルーム番号|
|cursor|query|string|false|Query parameter indicating the cursor position of the list to retrieve.|
|from_reservation_date|query|string(date)|true|from reservation date|
|hotel_id|path|string|true|facility id for the given hotel|

> Example responses

> 200 Response

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "stays": [
    {
      "id ": "string",
      "reservation_number": "string",
      "check_in_date": "string",
      "check_out_date": "string",
      "room_sales_status": {
        "status": "Fix"
      },
      "control_status": {
        "status": "Reserve"
      },
      "person_count": [
        3,
        3,
        3,
        3,
        3,
        3
      ],
      "main_guest": {
        "person": {
          "kana_name": "string",
          "name": "string",
          "address": {
            "postal_code": "string",
            "prefecture_code": "string",
            "city": "string",
            "address_line": [
              "string"
            ]
          },
          "phone_no": "000-0000-0000",
          "phone_no_mobile": "000-0000-0000",
          "phone_no_other": "000-0000-0000",
          "gender": "Male",
          "birthday": "2019-08-24",
          "email": "example@example.com",
          "email_sub": "example@example.com",
          "external_customer_Id": "string"
        },
        "remarks": [
          {
            "system_user_company_id": "strin",
            "customer_number": "string",
            "customer_remark_id": "string",
            "importance_level_id": "PrimaryRemark",
            "facility_id": "strin",
            "date": "2019-08-24",
            "division": {
              "id": "str",
              "name": "string",
              "group_id": "str"
            },
            "type": {
              "id": "str",
              "name": "string"
            },
            "interlock_system_id": "str",
            "content": "string",
            "subject": "string",
            "output_timing": true,
            "youcom_hotel": {
              "id": "strin",
              "name": "string"
            },
            "youcom_sequence": 0,
            "create_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            },
            "change_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            }
          }
        ],
        "remak": [
          {
            "system_user_company_id": "strin",
            "customer_number": "string",
            "customer_remark_id": "string",
            "importance_level_id": "PrimaryRemark",
            "facility_id": "strin",
            "date": "2019-08-24",
            "division": {
              "id": "str",
              "name": "string",
              "group_id": "str"
            },
            "type": {
              "id": "str",
              "name": "string"
            },
            "interlock_system_id": "str",
            "content": "string",
            "subject": "string",
            "output_timing": true,
            "youcom_hotel": {
              "id": "strin",
              "name": "string"
            },
            "youcom_sequence": 0,
            "create_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            },
            "change_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            }
          }
        ],
        "id": "string",
        "customer_number": "string"
      },
      "reserved_by": {
        "person": {
          "kana_name": "string",
          "name": "string",
          "address": {
            "postal_code": "string",
            "prefecture_code": "string",
            "city": "string",
            "address_line": [
              "string"
            ]
          },
          "phone_no": "000-0000-0000",
          "phone_no_mobile": "000-0000-0000",
          "phone_no_other": "000-0000-0000",
          "gender": "Male",
          "birthday": "2019-08-24",
          "email": "example@example.com",
          "email_sub": "example@example.com",
          "external_customer_Id": "string"
        },
        "remarks": [
          {
            "system_user_company_id": "strin",
            "customer_number": "string",
            "customer_remark_id": "string",
            "importance_level_id": "PrimaryRemark",
            "facility_id": "strin",
            "date": "2019-08-24",
            "division": {
              "id": "str",
              "name": "string",
              "group_id": "str"
            },
            "type": {
              "id": "str",
              "name": "string"
            },
            "interlock_system_id": "str",
            "content": "string",
            "subject": "string",
            "output_timing": true,
            "youcom_hotel": {
              "id": "strin",
              "name": "string"
            },
            "youcom_sequence": 0,
            "create_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            },
            "change_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            }
          }
        ],
        "remak": [
          {
            "system_user_company_id": "strin",
            "customer_number": "string",
            "customer_remark_id": "string",
            "importance_level_id": "PrimaryRemark",
            "facility_id": "strin",
            "date": "2019-08-24",
            "division": {
              "id": "str",
              "name": "string",
              "group_id": "str"
            },
            "type": {
              "id": "str",
              "name": "string"
            },
            "interlock_system_id": "str",
            "content": "string",
            "subject": "string",
            "output_timing": true,
            "youcom_hotel": {
              "id": "strin",
              "name": "string"
            },
            "youcom_sequence": 0,
            "create_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            },
            "change_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            }
          }
        ],
        "id": "string",
        "customer_number": "string"
      },
      "remarks": [
        {
          "id": "string",
          "division": {
            "id": "str",
            "name": "string",
            "group_id": "str"
          },
          "remarks_type": {
            "id": "str",
            "name": "string"
          },
          "importance_level": "Primary Remark",
          "subject": "string",
          "content": "string"
        }
      ],
      "reservation_remarks": [
        {
          "id": "string",
          "division": {
            "id": "str",
            "name": "string",
            "group_id": "str"
          },
          "remarks_type": {
            "id": "str",
            "name": "string"
          },
          "importance_level": "Primary Remark",
          "subject": "string",
          "content": "string"
        }
      ],
      "room_reservation": {
        "id": "string",
        "stay_registration_id ": "string",
        "room_number": "string",
        "room_status": "Vacant",
        "guests": [
          {
            "person": {
              "kana_name": "string",
              "name": "string",
              "address": {
                "postal_code": "string",
                "prefecture_code": "string",
                "city": "string",
                "address_line": [
                  "string"
                ]
              },
              "phone_no": "000-0000-0000",
              "phone_no_mobile": "000-0000-0000",
              "phone_no_other": "000-0000-0000",
              "gender": "Male",
              "birthday": "2019-08-24",
              "email": "example@example.com",
              "email_sub": "example@example.com",
              "external_customer_Id": "string"
            },
            "remarks": [
              {
                "system_user_company_id": "strin",
                "customer_number": "string",
                "customer_remark_id": "string",
                "importance_level_id": "PrimaryRemark",
                "facility_id": "strin",
                "date": "2019-08-24",
                "division": {
                  "id": "str",
                  "name": "string",
                  "group_id": "str"
                },
                "type": {
                  "id": "str",
                  "name": "string"
                },
                "interlock_system_id": "str",
                "content": "string",
                "subject": "string",
                "output_timing": true,
                "youcom_hotel": {
                  "id": "strin",
                  "name": "string"
                },
                "youcom_sequence": 0,
                "create_info": {
                  "host_name": "string",
                  "time_stamp": "2019-08-24T14:15:22Z",
                  "user_account_id": "string"
                },
                "change_info": {
                  "host_name": "string",
                  "time_stamp": "2019-08-24T14:15:22Z",
                  "user_account_id": "string"
                }
              }
            ],
            "remak": [
              {
                "system_user_company_id": "strin",
                "customer_number": "string",
                "customer_remark_id": "string",
                "importance_level_id": "PrimaryRemark",
                "facility_id": "strin",
                "date": "2019-08-24",
                "division": {
                  "id": "str",
                  "name": "string",
                  "group_id": "str"
                },
                "type": {
                  "id": "str",
                  "name": "string"
                },
                "interlock_system_id": "str",
                "content": "string",
                "subject": "string",
                "output_timing": true,
                "youcom_hotel": {
                  "id": "strin",
                  "name": "string"
                },
                "youcom_sequence": 0,
                "create_info": {
                  "host_name": "string",
                  "time_stamp": "2019-08-24T14:15:22Z",
                  "user_account_id": "string"
                },
                "change_info": {
                  "host_name": "string",
                  "time_stamp": "2019-08-24T14:15:22Z",
                  "user_account_id": "string"
                }
              }
            ],
            "id": "string",
            "customer_number": "string"
          }
        ],
        "room_type": {
          "code": "string",
          "standard_persons": 0,
          "max_persons": 0,
          "name": "string",
          "short_name": "string",
          "kana_name": "string",
          "foreign_name": "string",
          "foreign_short_name": "string"
        },
        "sales_control_type": "FREE",
        "sales_control_unit": "string",
        "extra_bed_count": 0,
        "stay_period": {
          "arrival_date": "2019-08-24",
          "arrival_time": "14:15:22Z",
          "departure_date": "2019-08-24",
          "departure_time": "14:15:22Z",
          "late_out": true
        },
        "reservation_route": {
          "reservationDisplayName": "string",
          "reservationRoutes": [
            {
              "code": "string",
              "name": "string",
              "short_name": "string",
              "kana_name": "string",
              "foreign_name": "string",
              "foreign_short_name": "string"
            }
          ]
        },
        "agent_reservation_number": "string",
        "agent_course": "string",
        "person_count": [
          0
        ],
        "pricing": {
          "sales_package": {
            "code": "string",
            "name": "string",
            "short_name": "string",
            "kana_name": "string",
            "foreign_name": "string",
            "foreign_short_name": "string",
            "print_name": "string",
            "print_foreign_name": "string"
          },
          "discount_item": {
            "code": "string",
            "name": "string",
            "short_name": "string",
            "kana_name": "string",
            "foreign_name": "string",
            "foreign_short_name": "string",
            "rate": 0,
            "amount": 0
          },
          "discount_rate": 100,
          "discount_amount": 0,
          "pricing_type": "GROSS",
          "price": 0
        },
        "provision_requests": [
          {
            "id": "string",
            "provision": {
              "code": "string",
              "name": "string",
              "short_name": "string",
              "kana_name": "string",
              "foreign_name": "string",
              "foreign_short_name": "string"
            },
            "from_date": "2019-08-24",
            "to_date": "2019-08-24",
            "stock_control": true,
            "quantity": 0,
            "note": "string",
            "reservation_ref": {
              "reservation_id": "string",
              "room_id": "string",
              "stay_id": "string",
              "reservation_number": "string",
              "room_number": "string"
            }
          }
        ],
        "meal_reservations": [
          {
            "id": "string",
            "meal_place": {
              "id": "string",
              "name": "string",
              "short_name": "string",
              "kana_name": "string",
              "foreign_name": "string",
              "foreign_short_name": "string"
            },
            "meal_type": {
              "id": "string",
              "meal_place_code": "string",
              "meal_time_code": "string",
              "start_time": "14:15:22Z",
              "end_time": "14:15:22Z",
              "person_count": 0,
              "table_count": 0
            },
            "meal_time_frame": {
              "id": "string",
              "name": "string",
              "short_name": "string",
              "kana_name": "string",
              "foreign_name": "string",
              "foreign_short_name": "string"
            },
            "use_date": "2019-08-24",
            "meal_kana_name": "string",
            "meal_name": "string",
            "meal_short_name": "string",
            "meal_item": {
              "code": "string",
              "name": "string",
              "short_name": "string",
              "kana_name": "string",
              "foreign_name": "string",
              "foreign_short_name": "string"
            },
            "person_count": 0,
            "person_type": "ADULT",
            "unit_price": 0,
            "pricing_type": "INCLUDED",
            "start_time": "14:15:22Z",
            "end_time": "14:15:22Z",
            "valid": true,
            "note": "string",
            "reservation_ref": {
              "reservation_id": "string",
              "room_id": "string",
              "stay_id": "string",
              "reservation_number": "string",
              "room_number": "string"
            }
          }
        ],
        "deposits": [
          {
            "id": "string",
            "account_date": "2019-08-24",
            "payment_method": {
              "code": "string",
              "name": "string",
              "short_name": "string",
              "kana_name": "string",
              "foreign_name": "string",
              "foreign_short_name": "string",
              "use_address": true
            },
            "billing_provider": {
              "code": "string",
              "name": "string",
              "short_name": "string",
              "kana_name": "string",
              "foreign_name": "string",
              "foreign_short_name": "string"
            },
            "amount": 0,
            "bill_index": 0,
            "bill_note": "string",
            "internal_note": "string",
            "provider_reference": "string",
            "reservation_ref": {
              "reservation_id": "string",
              "room_id": "string",
              "stay_id": "string",
              "reservation_number": "string",
              "room_number": "string"
            }
          }
        ],
        "slip_items": [
          {
            "id": "string",
            "date": "2019-08-24",
            "item": {
              "code": "string",
              "name": "string",
              "short_name": "string",
              "kana_name": "string",
              "foreign_name": "string",
              "price": 0
            },
            "price_per_item": 0,
            "quantity": 0,
            "total_price": 0,
            "bill_index": 0,
            "bill_note": "string",
            "internal_note": "string",
            "tax_free": true,
            "room_type": {
              "code": "string",
              "standard_persons": 0,
              "max_persons": 0,
              "name": "string",
              "short_name": "string",
              "kana_name": "string",
              "foreign_name": "string",
              "foreign_short_name": "string"
            },
            "reservation_ref": {
              "reservation_id": "string",
              "room_id": "string",
              "stay_id": "string",
              "reservation_number": "string",
              "room_number": "string"
            }
          }
        ],
        "extra_services": [
          {
            "id": "string",
            "service_item": {
              "code": "string",
              "name": "string",
              "kana_name": "string",
              "short_name": "string",
              "foreign_name": "string",
              "foreign_short_name": "string"
            },
            "service_period": {
              "arrival_date": "2019-08-24",
              "arrival_time": "14:15:22Z",
              "departure_date": "2019-08-24",
              "departure_time": "14:15:22Z",
              "late_out": true
            },
            "person_count": 0,
            "note": "string",
            "reservation_ref": {
              "reservation_id": "string",
              "room_id": "string",
              "stay_id": "string",
              "reservation_number": "string",
              "room_number": "string"
            }
          }
        ],
        "remarks": [
          {
            "id": "string",
            "division": {
              "id": "str",
              "name": "string",
              "group_id": "str"
            },
            "remarks_type": {
              "id": "str",
              "name": "string"
            },
            "importance_level": "Primary Remark",
            "subject": "string",
            "content": "string"
          }
        ],
        "price_changes": [
          {
            "date_range_end": "2019-08-24",
            "date_range_start": "2019-08-24",
            "prices": [
              {
                "discount_amount": 0,
                "discount_item_id": "string",
                "discount_item_name": "string",
                "discount_rate": 0,
                "person_count": [
                  0
                ],
                "person_count_price_calc": 0,
                "price": 0,
                "pricing_type": "GROSS",
                "rate_id": "string",
                "room_type_code": "string",
                "sales_package_id": "string",
                "sales_package_name": "string"
              }
            ]
          }
        ]
      }
    }
  ]
}
```

<h3 id="stay-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[ApiStaysResponse](#schemaapistaysresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[ApiErrorResponseBadRequest](#schemaapierrorresponsebadrequest)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ApiErrorResponseUnauthorized](#schemaapierrorresponseunauthorized)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ApiErrorResponseNotFound](#schemaapierrorresponsenotfound)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[ApiErrorResponseInternalError](#schemaapierrorresponseinternalerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AccessToken
</aside>

<h1 id="tap-hub-api-front-api-vacancy">Vacancy</h1>

## Vacancy

<a id="opIdget-hotels-hotel_id-vacancy"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:3000/hotels/{hotel_id}/vacancy?to_reservation_date=2019-08-24&from_reservation_date=2019-08-24 \
  -H 'Accept: application/json'

```

```http
GET http://localhost:3000/hotels/{hotel_id}/vacancy?to_reservation_date=2019-08-24&from_reservation_date=2019-08-24 HTTP/1.1
Host: localhost:3000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('http://localhost:3000/hotels/{hotel_id}/vacancy?to_reservation_date=2019-08-24&from_reservation_date=2019-08-24',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get 'http://localhost:3000/hotels/{hotel_id}/vacancy',
  params: {
  'to_reservation_date' => 'string(date)',
'from_reservation_date' => 'string(date)'
}, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://localhost:3000/hotels/{hotel_id}/vacancy', params={
  'to_reservation_date': '2019-08-24',  'from_reservation_date': '2019-08-24'
}, headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','http://localhost:3000/hotels/{hotel_id}/vacancy', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://localhost:3000/hotels/{hotel_id}/vacancy?to_reservation_date=2019-08-24&from_reservation_date=2019-08-24");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:3000/hotels/{hotel_id}/vacancy", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /hotels/{hotel_id}/vacancy`

Retrives vacancy information for given hotel and parameters

<h3 id="vacancy-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|to_reservation_date|query|string(date)|true|to reservation date|
|from_reservation_date|query|string(date)|true|from reservation date|
|room_type_code|query|array[string]|false|ルームタイプコード|
|hotel_id|path|string|true|facility id for the given hotel|

> Example responses

> 200 Response

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "vacant_rooms": [
    {
      "room_type_code": "string",
      "room_quantity": 0,
      "room_stock": 0,
      "date": "2019-08-24",
      "is_sale_stop": "true",
      "sale_quantity": 0,
      "closing_state": "true"
    }
  ]
}
```

<h3 id="vacancy-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[ApiVacancyResponse](#schemaapivacancyresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[ApiErrorResponseBadRequest](#schemaapierrorresponsebadrequest)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ApiErrorResponseUnauthorized](#schemaapierrorresponseunauthorized)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ApiErrorResponseNotFound](#schemaapierrorresponsenotfound)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[ApiErrorResponseInternalError](#schemaapierrorresponseinternalerror)|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="tap-hub-api-front-api-outoforders">OutOfOrders</h1>

## 故障部屋情報取得

<a id="opIdListOutOfOrders"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:3000/hotels/{hotel_id}/out-of-orders \
  -H 'Accept: application/json' \
  -H 'X-API-Key: API_KEY'

```

```http
GET http://localhost:3000/hotels/{hotel_id}/out-of-orders HTTP/1.1
Host: localhost:3000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'API_KEY'
};

fetch('http://localhost:3000/hotels/{hotel_id}/out-of-orders',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'X-API-Key' => 'API_KEY'
}

result = RestClient.get 'http://localhost:3000/hotels/{hotel_id}/out-of-orders',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'API_KEY'
}

r = requests.get('http://localhost:3000/hotels/{hotel_id}/out-of-orders', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'X-API-Key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','http://localhost:3000/hotels/{hotel_id}/out-of-orders', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://localhost:3000/hotels/{hotel_id}/out-of-orders");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://localhost:3000/hotels/{hotel_id}/out-of-orders", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /hotels/{hotel_id}/out-of-orders`

故障部屋情報を取得する

<h3 id="故障部屋情報取得-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|date|query|string(date)|false|date|
|cursor|query|string|false|Query parameter indicating the cursor position of the list to retrieve.|
|hotel_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "total_pages": 0,
  "total_records": 0,
  "out_of_orders": [
    {
      "room_number": "string",
      "out_of_order_id": "string",
      "reason_name": "string",
      "room_floor_id": "string",
      "date_range_start": "2019-08-24",
      "date_range_end": "2019-08-24"
    }
  ]
}
```

<h3 id="故障部屋情報取得-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[ListOutOfOrdersResponse](#schemalistoutofordersresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[ApiErrorResponseBadRequest](#schemaapierrorresponsebadrequest)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ApiErrorResponseUnauthorized](#schemaapierrorresponseunauthorized)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ApiErrorResponseNotFound](#schemaapierrorresponsenotfound)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[ApiErrorResponseInternalError](#schemaapierrorresponseinternalerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AccessToken
</aside>

## 故障部屋情報作成

<a id="opIdCreateOutOfOrder"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:3000/hotels/{hotel_id}/out-of-orders \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'X-API-Key: API_KEY'

```

```http
POST http://localhost:3000/hotels/{hotel_id}/out-of-orders HTTP/1.1
Host: localhost:3000
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "out_of_order": {
    "room_number": "string",
    "reason_name": "string",
    "date_range_start": "2019-08-24",
    "date_range_end": "2019-08-24"
  }
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'X-API-Key':'API_KEY'
};

fetch('http://localhost:3000/hotels/{hotel_id}/out-of-orders',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'X-API-Key' => 'API_KEY'
}

result = RestClient.post 'http://localhost:3000/hotels/{hotel_id}/out-of-orders',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'X-API-Key': 'API_KEY'
}

r = requests.post('http://localhost:3000/hotels/{hotel_id}/out-of-orders', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'X-API-Key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','http://localhost:3000/hotels/{hotel_id}/out-of-orders', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://localhost:3000/hotels/{hotel_id}/out-of-orders");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://localhost:3000/hotels/{hotel_id}/out-of-orders", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /hotels/{hotel_id}/out-of-orders`

故障部屋情報を作成する

> Body parameter

```json
{
  "out_of_order": {
    "room_number": "string",
    "reason_name": "string",
    "date_range_start": "2019-08-24",
    "date_range_end": "2019-08-24"
  }
}
```

<h3 id="故障部屋情報作成-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[CreateOutOfOrderRequest](#schemacreateoutoforderrequest)|false|none|
|hotel_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "out_of_order": {
    "room_number": "string",
    "out_of_order_id": "string",
    "reason_name": "string",
    "room_floor_id": "string",
    "date_range_start": "2019-08-24",
    "date_range_end": "2019-08-24"
  }
}
```

<h3 id="故障部屋情報作成-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[CreateOutOfOrderResponse](#schemacreateoutoforderresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[ApiErrorResponseBadRequest](#schemaapierrorresponsebadrequest)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ApiErrorResponseUnauthorized](#schemaapierrorresponseunauthorized)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[ApiErrorResponseInternalError](#schemaapierrorresponseinternalerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AccessToken
</aside>

## 故障部屋情報更新

<a id="opIdUpdateOutOfOrder"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT http://localhost:3000/hotels/{hotel_id}/out-of-orders/{out_of_order_id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'X-API-Key: API_KEY'

```

```http
PUT http://localhost:3000/hotels/{hotel_id}/out-of-orders/{out_of_order_id} HTTP/1.1
Host: localhost:3000
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "out_of_order": {
    "reason_name": "string",
    "date_range_start": "2019-08-24",
    "date_range_end": "2019-08-24"
  }
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'X-API-Key':'API_KEY'
};

fetch('http://localhost:3000/hotels/{hotel_id}/out-of-orders/{out_of_order_id}',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'X-API-Key' => 'API_KEY'
}

result = RestClient.put 'http://localhost:3000/hotels/{hotel_id}/out-of-orders/{out_of_order_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'X-API-Key': 'API_KEY'
}

r = requests.put('http://localhost:3000/hotels/{hotel_id}/out-of-orders/{out_of_order_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'X-API-Key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','http://localhost:3000/hotels/{hotel_id}/out-of-orders/{out_of_order_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://localhost:3000/hotels/{hotel_id}/out-of-orders/{out_of_order_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "http://localhost:3000/hotels/{hotel_id}/out-of-orders/{out_of_order_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /hotels/{hotel_id}/out-of-orders/{out_of_order_id}`

故障部屋情報を更新する

> Body parameter

```json
{
  "out_of_order": {
    "reason_name": "string",
    "date_range_start": "2019-08-24",
    "date_range_end": "2019-08-24"
  }
}
```

<h3 id="故障部屋情報更新-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[UpdateOutOfOrderRequest](#schemaupdateoutoforderrequest)|false|none|
|hotel_id|path|string|true|none|
|out_of_order_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "out_of_order": {
    "room_number": "string",
    "out_of_order_id": "string",
    "reason_name": "string",
    "room_floor_id": "string",
    "date_range_start": "2019-08-24",
    "date_range_end": "2019-08-24"
  }
}
```

<h3 id="故障部屋情報更新-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[UpdateOutOfOrderResponse](#schemaupdateoutoforderresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[ApiErrorResponseBadRequest](#schemaapierrorresponsebadrequest)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ApiErrorResponseUnauthorized](#schemaapierrorresponseunauthorized)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ApiErrorResponseNotFound](#schemaapierrorresponsenotfound)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[ApiErrorResponseInternalError](#schemaapierrorresponseinternalerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AccessToken
</aside>

## 故障部屋削除

<a id="opIdDeleteOutOfOrder"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE http://localhost:3000/hotels/{hotel_id}/out-of-orders/{out_of_order_id} \
  -H 'Accept: application/json' \
  -H 'X-API-Key: API_KEY'

```

```http
DELETE http://localhost:3000/hotels/{hotel_id}/out-of-orders/{out_of_order_id} HTTP/1.1
Host: localhost:3000
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'X-API-Key':'API_KEY'
};

fetch('http://localhost:3000/hotels/{hotel_id}/out-of-orders/{out_of_order_id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'X-API-Key' => 'API_KEY'
}

result = RestClient.delete 'http://localhost:3000/hotels/{hotel_id}/out-of-orders/{out_of_order_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'X-API-Key': 'API_KEY'
}

r = requests.delete('http://localhost:3000/hotels/{hotel_id}/out-of-orders/{out_of_order_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'X-API-Key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','http://localhost:3000/hotels/{hotel_id}/out-of-orders/{out_of_order_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://localhost:3000/hotels/{hotel_id}/out-of-orders/{out_of_order_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "X-API-Key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "http://localhost:3000/hotels/{hotel_id}/out-of-orders/{out_of_order_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /hotels/{hotel_id}/out-of-orders/{out_of_order_id}`

故障部屋情報を削除する

<h3 id="故障部屋削除-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|hotel_id|path|string|true|none|
|out_of_order_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "out_of_order": {
    "room_number": "string",
    "out_of_order_id": "string",
    "reason_name": "string",
    "room_floor_id": "string",
    "date_range_start": "2019-08-24",
    "date_range_end": "2019-08-24"
  }
}
```

<h3 id="故障部屋削除-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[DeleteOutOfOrderResponse](#schemadeleteoutoforderresponse)|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No Content|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[ApiErrorResponseBadRequest](#schemaapierrorresponsebadrequest)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ApiErrorResponseUnauthorized](#schemaapierrorresponseunauthorized)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|[ApiErrorResponseNotFound](#schemaapierrorresponsenotfound)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[ApiErrorResponseInternalError](#schemaapierrorresponseinternalerror)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AccessToken
</aside>

# Schemas

<h2 id="tocS_ApiFacilityResponse">ApiFacilityResponse</h2>
<!-- backwards compatibility -->
<a id="schemaapifacilityresponse"></a>
<a id="schema_ApiFacilityResponse"></a>
<a id="tocSapifacilityresponse"></a>
<a id="tocsapifacilityresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "facility": {
    "status": 0,
    "error_code": 0,
    "error_message": "string",
    "language": "string",
    "data": [
      {
        "access_info": "string",
        "address": "string",
        "hotel-id": "string",
        "hotel_name": "string",
        "image_url": "string",
        "search_hotel_name": "string"
      }
    ]
  }
}

```

ApiFacilityResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|request|[ApiCommonResponseRequest](#schemaapicommonresponserequest)|false|none|Request|
|request_id|[ApiCommonResponseRequestId](#schemaapicommonresponserequestid)|false|none|RequestId|
|next_cursor|[ApiCommonResponseNextCursor](#schemaapicommonresponsenextcursor)|false|none|Indicates the position of the next entity. If an entity less than a limit is returned by the current page of the result set, then Cursor value is null.|
|facility|[Facility](#schemafacility)|false|none|Model of a facility|

<h2 id="tocS_ApiErrorResponseBadRequest">ApiErrorResponseBadRequest</h2>
<!-- backwards compatibility -->
<a id="schemaapierrorresponsebadrequest"></a>
<a id="schema_ApiErrorResponseBadRequest"></a>
<a id="tocSapierrorresponsebadrequest"></a>
<a id="tocsapierrorresponsebadrequest"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "errors": [
    {
      "parameter": "start_date",
      "detail": "invalid date",
      "code": "INVALID_PARAMETER",
      "value": "2021-13-32",
      "message": "Expected valid date, but got '2021-13-32' for start_date"
    }
  ]
}

```

ApiErrorResponseBadRequest

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|request|[ApiCommonResponseRequest](#schemaapicommonresponserequest)|false|none|Request|
|request_id|[ApiCommonResponseRequestId](#schemaapicommonresponserequestid)|false|none|RequestId|
|errors|[[InvalidParameter](#schemainvalidparameter)]|false|none|[InvalidParameter]|

<h2 id="tocS_InvalidParameter">InvalidParameter</h2>
<!-- backwards compatibility -->
<a id="schemainvalidparameter"></a>
<a id="schema_InvalidParameter"></a>
<a id="tocSinvalidparameter"></a>
<a id="tocsinvalidparameter"></a>

```json
{
  "parameter": "start_date",
  "detail": "invalid date",
  "code": "INVALID_PARAMETER",
  "value": "2021-13-32",
  "message": "Expected valid date, but got '2021-13-32' for start_date"
}

```

InvalidParameter

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|parameter|string|false|none|parameter name|
|detail|string|false|none|error detail|
|code|string|false|none|error code|
|value|string|false|none|parameter value|
|message|string|false|none|error message|

<h2 id="tocS_ApiErrorResponseUnauthorized">ApiErrorResponseUnauthorized</h2>
<!-- backwards compatibility -->
<a id="schemaapierrorresponseunauthorized"></a>
<a id="schema_ApiErrorResponseUnauthorized"></a>
<a id="tocSapierrorresponseunauthorized"></a>
<a id="tocsapierrorresponseunauthorized"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "errors": {
    "code": "string",
    "message": "string"
  }
}

```

ApiErrorResponseUnauthorized

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|request|[ApiCommonResponseRequest](#schemaapicommonresponserequest)|false|none|Request|
|request_id|[ApiCommonResponseRequestId](#schemaapicommonresponserequestid)|false|none|RequestId|
|errors|[ApiError](#schemaapierror)|false|none|none|

<h2 id="tocS_ApiError">ApiError</h2>
<!-- backwards compatibility -->
<a id="schemaapierror"></a>
<a id="schema_ApiError"></a>
<a id="tocSapierror"></a>
<a id="tocsapierror"></a>

```json
{
  "code": "string",
  "message": "string"
}

```

ApiError

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|string|false|none|none|
|message|string|false|none|none|

<h2 id="tocS_ApiErrorResponseNotFound">ApiErrorResponseNotFound</h2>
<!-- backwards compatibility -->
<a id="schemaapierrorresponsenotfound"></a>
<a id="schema_ApiErrorResponseNotFound"></a>
<a id="tocSapierrorresponsenotfound"></a>
<a id="tocsapierrorresponsenotfound"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "errors": {
    "code": "string",
    "message": "string"
  }
}

```

ApiErrorResponseNotFound

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|request|[ApiCommonResponseRequest](#schemaapicommonresponserequest)|false|none|Request|
|request_id|[ApiCommonResponseRequestId](#schemaapicommonresponserequestid)|false|none|RequestId|
|errors|[ApiError](#schemaapierror)|false|none|none|

<h2 id="tocS_ApiErrorResponseInternalError">ApiErrorResponseInternalError</h2>
<!-- backwards compatibility -->
<a id="schemaapierrorresponseinternalerror"></a>
<a id="schema_ApiErrorResponseInternalError"></a>
<a id="tocSapierrorresponseinternalerror"></a>
<a id="tocsapierrorresponseinternalerror"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "errors": {
    "code": "string",
    "message": "string"
  }
}

```

ApiErrorResponseInternalError

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|request|[ApiCommonResponseRequest](#schemaapicommonresponserequest)|false|none|Request|
|request_id|[ApiCommonResponseRequestId](#schemaapicommonresponserequestid)|false|none|RequestId|
|errors|[ApiError](#schemaapierror)|false|none|none|

<h2 id="tocS_ApiProvisionsResponse">ApiProvisionsResponse</h2>
<!-- backwards compatibility -->
<a id="schemaapiprovisionsresponse"></a>
<a id="schema_ApiProvisionsResponse"></a>
<a id="tocSapiprovisionsresponse"></a>
<a id="tocsapiprovisionsresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "provisions": [
    {
      "code": "string",
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    }
  ]
}

```

ApiProvisionsResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|request|[ApiCommonResponseRequest](#schemaapicommonresponserequest)|false|none|Request|
|request_id|[ApiCommonResponseRequestId](#schemaapicommonresponserequestid)|false|none|RequestId|
|next_cursor|[ApiCommonResponseNextCursor](#schemaapicommonresponsenextcursor)|false|none|Indicates the position of the next entity. If an entity less than a limit is returned by the current page of the result set, then Cursor value is null.|
|provisions|[[ProvisionItem](#schemaprovisionitem)]|false|none|none|

<h2 id="tocS_ApiProvisionRequestsResponse">ApiProvisionRequestsResponse</h2>
<!-- backwards compatibility -->
<a id="schemaapiprovisionrequestsresponse"></a>
<a id="schema_ApiProvisionRequestsResponse"></a>
<a id="tocSapiprovisionrequestsresponse"></a>
<a id="tocsapiprovisionrequestsresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "provision_requests": [
    {
      "id": "string",
      "provision": {
        "code": "string",
        "name": "string",
        "short_name": "string",
        "kana_name": "string",
        "foreign_name": "string",
        "foreign_short_name": "string"
      },
      "from_date": "2019-08-24",
      "to_date": "2019-08-24",
      "stock_control": true,
      "quantity": 0,
      "note": "string",
      "reservation_ref": {
        "reservation_id": "string",
        "room_id": "string",
        "stay_id": "string",
        "reservation_number": "string",
        "room_number": "string"
      }
    }
  ]
}

```

ApiProvisionRequestsResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|request|[ApiCommonResponseRequest](#schemaapicommonresponserequest)|false|none|Request|
|request_id|[ApiCommonResponseRequestId](#schemaapicommonresponserequestid)|false|none|RequestId|
|next_cursor|[ApiCommonResponseNextCursor](#schemaapicommonresponsenextcursor)|false|none|Indicates the position of the next entity. If an entity less than a limit is returned by the current page of the result set, then Cursor value is null.|
|provision_requests|[[Provision](#schemaprovision)]|false|none|[Model for a provision request]|

<h2 id="tocS_ApiProvisionRequestResponse">ApiProvisionRequestResponse</h2>
<!-- backwards compatibility -->
<a id="schemaapiprovisionrequestresponse"></a>
<a id="schema_ApiProvisionRequestResponse"></a>
<a id="tocSapiprovisionrequestresponse"></a>
<a id="tocsapiprovisionrequestresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "provision_requests": {
    "id": "string",
    "provision": {
      "code": "string",
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    },
    "from_date": "2019-08-24",
    "to_date": "2019-08-24",
    "stock_control": true,
    "quantity": 0,
    "note": "string",
    "reservation_ref": {
      "reservation_id": "string",
      "room_id": "string",
      "stay_id": "string",
      "reservation_number": "string",
      "room_number": "string"
    }
  }
}

```

ApiProvisionRequestResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|request|[ApiCommonResponseRequest](#schemaapicommonresponserequest)|false|none|Request|
|request_id|[ApiCommonResponseRequestId](#schemaapicommonresponserequestid)|false|none|RequestId|
|next_cursor|[ApiCommonResponseNextCursor](#schemaapicommonresponsenextcursor)|false|none|Indicates the position of the next entity. If an entity less than a limit is returned by the current page of the result set, then Cursor value is null.|
|provision_requests|[Provision](#schemaprovision)|false|none|Model for a provision request|

<h2 id="tocS_ApiProvisionRequestPutRequest">ApiProvisionRequestPutRequest</h2>
<!-- backwards compatibility -->
<a id="schemaapiprovisionrequestputrequest"></a>
<a id="schema_ApiProvisionRequestPutRequest"></a>
<a id="tocSapiprovisionrequestputrequest"></a>
<a id="tocsapiprovisionrequestputrequest"></a>

```json
{
  "provision_request": {
    "provision_code": "string",
    "from_date": "2019-08-24",
    "to_date": "2019-08-24",
    "stock_control": true,
    "quantity": 0,
    "note": "string"
  }
}

```

ApiProvisionRequestPutRequest

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|provision_request|[ProvisionRequest](#schemaprovisionrequest)|false|none|Model for a provision request|

<h2 id="tocS_ProvisionRequest">ProvisionRequest</h2>
<!-- backwards compatibility -->
<a id="schemaprovisionrequest"></a>
<a id="schema_ProvisionRequest"></a>
<a id="tocSprovisionrequest"></a>
<a id="tocsprovisionrequest"></a>

```json
{
  "provision_code": "string",
  "from_date": "2019-08-24",
  "to_date": "2019-08-24",
  "stock_control": true,
  "quantity": 0,
  "note": "string"
}

```

ProvisionRequest

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|provision_code|string|true|none|none|
|from_date|[Date](#schemadate)|true|none|日付(Date)|
|to_date|[Date](#schemadate)|true|none|日付(Date)|
|stock_control|boolean|true|none|none|
|quantity|integer|true|none|none|
|note|string|false|none|none|

<h2 id="tocS_ListExtraServicesResponse">ListExtraServicesResponse</h2>
<!-- backwards compatibility -->
<a id="schemalistextraservicesresponse"></a>
<a id="schema_ListExtraServicesResponse"></a>
<a id="tocSlistextraservicesresponse"></a>
<a id="tocslistextraservicesresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "total_pages": 0,
  "total_records": 0,
  "extra_services": [
    {
      "code": "string",
      "name": "string",
      "kana_name": "string",
      "short_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    }
  ]
}

```

ListExtraServicesResponse

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[ApiListResponse](#schemaapilistresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» extra_services|[[ExtraService](#schemaextraservice)]|false|none|none|

<h2 id="tocS_ListExtraServiceReservationsResponse">ListExtraServiceReservationsResponse</h2>
<!-- backwards compatibility -->
<a id="schemalistextraservicereservationsresponse"></a>
<a id="schema_ListExtraServiceReservationsResponse"></a>
<a id="tocSlistextraservicereservationsresponse"></a>
<a id="tocslistextraservicereservationsresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "total_pages": 0,
  "total_records": 0,
  "extra_reservations": [
    {
      "id": "string",
      "service_item": {
        "code": "string",
        "name": "string",
        "kana_name": "string",
        "short_name": "string",
        "foreign_name": "string",
        "foreign_short_name": "string"
      },
      "service_period": {
        "arrival_date": "2019-08-24",
        "arrival_time": "14:15:22Z",
        "departure_date": "2019-08-24",
        "departure_time": "14:15:22Z",
        "late_out": true
      },
      "person_count": 0,
      "note": "string",
      "reservation_ref": {
        "reservation_id": "string",
        "room_id": "string",
        "stay_id": "string",
        "reservation_number": "string",
        "room_number": "string"
      }
    }
  ]
}

```

ListExtraServiceReservationsResponse

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[ApiListResponse](#schemaapilistresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» extra_reservations|[[ExtraServiceReservation](#schemaextraservicereservation)]|false|none|[Describe details for an extra service]|

<h2 id="tocS_GetExtraServiceReservationResponse">GetExtraServiceReservationResponse</h2>
<!-- backwards compatibility -->
<a id="schemagetextraservicereservationresponse"></a>
<a id="schema_GetExtraServiceReservationResponse"></a>
<a id="tocSgetextraservicereservationresponse"></a>
<a id="tocsgetextraservicereservationresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "extra_reservation": {
    "id": "string",
    "service_item": {
      "code": "string",
      "name": "string",
      "kana_name": "string",
      "short_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    },
    "service_period": {
      "arrival_date": "2019-08-24",
      "arrival_time": "14:15:22Z",
      "departure_date": "2019-08-24",
      "departure_time": "14:15:22Z",
      "late_out": true
    },
    "person_count": 0,
    "note": "string",
    "reservation_ref": {
      "reservation_id": "string",
      "room_id": "string",
      "stay_id": "string",
      "reservation_number": "string",
      "room_number": "string"
    }
  }
}

```

GetExtraServiceReservationResponse

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[ApiGetResponse](#schemaapigetresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» extra_reservation|[ExtraServiceReservation](#schemaextraservicereservation)|false|none|Describe details for an extra service|

<h2 id="tocS_UpdateExtraServiceReservationResponse">UpdateExtraServiceReservationResponse</h2>
<!-- backwards compatibility -->
<a id="schemaupdateextraservicereservationresponse"></a>
<a id="schema_UpdateExtraServiceReservationResponse"></a>
<a id="tocSupdateextraservicereservationresponse"></a>
<a id="tocsupdateextraservicereservationresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "extra_reservation": {
    "id": "string",
    "service_item": {
      "code": "string",
      "name": "string",
      "kana_name": "string",
      "short_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    },
    "service_period": {
      "arrival_date": "2019-08-24",
      "arrival_time": "14:15:22Z",
      "departure_date": "2019-08-24",
      "departure_time": "14:15:22Z",
      "late_out": true
    },
    "person_count": 0,
    "note": "string",
    "reservation_ref": {
      "reservation_id": "string",
      "room_id": "string",
      "stay_id": "string",
      "reservation_number": "string",
      "room_number": "string"
    }
  }
}

```

UpdateExtraServiceReservationResponse

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[ApiUpdateResponse](#schemaapiupdateresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» extra_reservation|[ExtraServiceReservation](#schemaextraservicereservation)|false|none|Describe details for an extra service|

<h2 id="tocS_UpdateExtraServiceReservationRequest">UpdateExtraServiceReservationRequest</h2>
<!-- backwards compatibility -->
<a id="schemaupdateextraservicereservationrequest"></a>
<a id="schema_UpdateExtraServiceReservationRequest"></a>
<a id="tocSupdateextraservicereservationrequest"></a>
<a id="tocsupdateextraservicereservationrequest"></a>

```json
{
  "extra_reservation": {
    "service_item_code": "str",
    "note": "string",
    "service_period": {
      "arrival_date": "2019-08-24",
      "arrival_time": "14:15:22Z",
      "departure_date": "2019-08-24",
      "departure_time": "14:15:22Z",
      "late_out": true
    },
    "person_count": 0
  }
}

```

UpdateExtraServiceReservationRequest

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[ApiUpdateRequest](#schemaapiupdaterequest)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» extra_reservation|[ExtraServiceReservationRequest](#schemaextraservicereservationrequest)|false|none|Describe details for an extra service|

<h2 id="tocS_DeleteExtraServiceReservationResponse">DeleteExtraServiceReservationResponse</h2>
<!-- backwards compatibility -->
<a id="schemadeleteextraservicereservationresponse"></a>
<a id="schema_DeleteExtraServiceReservationResponse"></a>
<a id="tocSdeleteextraservicereservationresponse"></a>
<a id="tocsdeleteextraservicereservationresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "extra_reservation": {
    "id": "string",
    "service_item": {
      "code": "string",
      "name": "string",
      "kana_name": "string",
      "short_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    },
    "service_period": {
      "arrival_date": "2019-08-24",
      "arrival_time": "14:15:22Z",
      "departure_date": "2019-08-24",
      "departure_time": "14:15:22Z",
      "late_out": true
    },
    "person_count": 0,
    "note": "string",
    "reservation_ref": {
      "reservation_id": "string",
      "room_id": "string",
      "stay_id": "string",
      "reservation_number": "string",
      "room_number": "string"
    }
  }
}

```

DeleteExtraServiceReservationResponse

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[ApiDeleteResponse](#schemaapideleteresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» extra_reservation|[ExtraServiceReservation](#schemaextraservicereservation)|false|none|Describe details for an extra service|

<h2 id="tocS_ApiMealPlacesResponse">ApiMealPlacesResponse</h2>
<!-- backwards compatibility -->
<a id="schemaapimealplacesresponse"></a>
<a id="schema_ApiMealPlacesResponse"></a>
<a id="tocSapimealplacesresponse"></a>
<a id="tocsapimealplacesresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "meal_place": [
    {
      "id": "string",
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    }
  ]
}

```

ApiMealPlacesResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|request|[ApiCommonResponseRequest](#schemaapicommonresponserequest)|false|none|Request|
|request_id|[ApiCommonResponseRequestId](#schemaapicommonresponserequestid)|false|none|RequestId|
|next_cursor|[ApiCommonResponseNextCursor](#schemaapicommonresponsenextcursor)|false|none|Indicates the position of the next entity. If an entity less than a limit is returned by the current page of the result set, then Cursor value is null.|
|meal_place|[[MealPlace](#schemamealplace)]|false|none|[Model for meal place]|

<h2 id="tocS_ApiMealTimesResponse">ApiMealTimesResponse</h2>
<!-- backwards compatibility -->
<a id="schemaapimealtimesresponse"></a>
<a id="schema_ApiMealTimesResponse"></a>
<a id="tocSapimealtimesresponse"></a>
<a id="tocsapimealtimesresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "meal_time": [
    {
      "id": "string",
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    }
  ]
}

```

ApiMealTimesResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|request|[ApiCommonResponseRequest](#schemaapicommonresponserequest)|false|none|Request|
|request_id|[ApiCommonResponseRequestId](#schemaapicommonresponserequestid)|false|none|RequestId|
|next_cursor|[ApiCommonResponseNextCursor](#schemaapicommonresponsenextcursor)|false|none|Indicates the position of the next entity. If an entity less than a limit is returned by the current page of the result set, then Cursor value is null.|
|meal_time|[[MealTimeFrame](#schemamealtimeframe)]|false|none|[Model for meal timeframe]|

<h2 id="tocS_ApiMealTypesResponse">ApiMealTypesResponse</h2>
<!-- backwards compatibility -->
<a id="schemaapimealtypesresponse"></a>
<a id="schema_ApiMealTypesResponse"></a>
<a id="tocSapimealtypesresponse"></a>
<a id="tocsapimealtypesresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "meal_type": [
    {
      "id": "string",
      "meal_place_code": "string",
      "meal_time_code": "string",
      "start_time": "14:15:22Z",
      "end_time": "14:15:22Z",
      "person_count": 0,
      "table_count": 0
    }
  ]
}

```

ApiMealTimesResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|request|[ApiCommonResponseRequest](#schemaapicommonresponserequest)|false|none|Request|
|request_id|[ApiCommonResponseRequestId](#schemaapicommonresponserequestid)|false|none|RequestId|
|next_cursor|[ApiCommonResponseNextCursor](#schemaapicommonresponsenextcursor)|false|none|Indicates the position of the next entity. If an entity less than a limit is returned by the current page of the result set, then Cursor value is null.|
|meal_type|[[MealType](#schemamealtype)]|false|none|[Model for meal type]|

<h2 id="tocS_ApiMealItemsResponse">ApiMealItemsResponse</h2>
<!-- backwards compatibility -->
<a id="schemaapimealitemsresponse"></a>
<a id="schema_ApiMealItemsResponse"></a>
<a id="tocSapimealitemsresponse"></a>
<a id="tocsapimealitemsresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "meal_item": [
    {
      "code": "string",
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    }
  ]
}

```

ApiMealItemsResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|request|[ApiCommonResponseRequest](#schemaapicommonresponserequest)|false|none|Request|
|request_id|[ApiCommonResponseRequestId](#schemaapicommonresponserequestid)|false|none|RequestId|
|next_cursor|[ApiCommonResponseNextCursor](#schemaapicommonresponsenextcursor)|false|none|Indicates the position of the next entity. If an entity less than a limit is returned by the current page of the result set, then Cursor value is null.|
|meal_item|[[MealItem](#schemamealitem)]|false|none|[Model for meal sales item]|

<h2 id="tocS_ApiMealReservationsResponse">ApiMealReservationsResponse</h2>
<!-- backwards compatibility -->
<a id="schemaapimealreservationsresponse"></a>
<a id="schema_ApiMealReservationsResponse"></a>
<a id="tocSapimealreservationsresponse"></a>
<a id="tocsapimealreservationsresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "meal_reservation": [
    {
      "id": "string",
      "meal_place": {
        "id": "string",
        "name": "string",
        "short_name": "string",
        "kana_name": "string",
        "foreign_name": "string",
        "foreign_short_name": "string"
      },
      "meal_type": {
        "id": "string",
        "meal_place_code": "string",
        "meal_time_code": "string",
        "start_time": "14:15:22Z",
        "end_time": "14:15:22Z",
        "person_count": 0,
        "table_count": 0
      },
      "meal_time_frame": {
        "id": "string",
        "name": "string",
        "short_name": "string",
        "kana_name": "string",
        "foreign_name": "string",
        "foreign_short_name": "string"
      },
      "use_date": "2019-08-24",
      "meal_kana_name": "string",
      "meal_name": "string",
      "meal_short_name": "string",
      "meal_item": {
        "code": "string",
        "name": "string",
        "short_name": "string",
        "kana_name": "string",
        "foreign_name": "string",
        "foreign_short_name": "string"
      },
      "person_count": 0,
      "person_type": "ADULT",
      "unit_price": 0,
      "pricing_type": "INCLUDED",
      "start_time": "14:15:22Z",
      "end_time": "14:15:22Z",
      "valid": true,
      "note": "string",
      "reservation_ref": {
        "reservation_id": "string",
        "room_id": "string",
        "stay_id": "string",
        "reservation_number": "string",
        "room_number": "string"
      }
    }
  ]
}

```

ApiMealReservationsResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|request|[ApiCommonResponseRequest](#schemaapicommonresponserequest)|false|none|Request|
|request_id|[ApiCommonResponseRequestId](#schemaapicommonresponserequestid)|false|none|RequestId|
|next_cursor|[ApiCommonResponseNextCursor](#schemaapicommonresponsenextcursor)|false|none|Indicates the position of the next entity. If an entity less than a limit is returned by the current page of the result set, then Cursor value is null.|
|meal_reservation|[[MealReservation](#schemamealreservation)]|false|none|[Describes detailed meal information for a given guest.]|

<h2 id="tocS_ApiMealReservationResponse">ApiMealReservationResponse</h2>
<!-- backwards compatibility -->
<a id="schemaapimealreservationresponse"></a>
<a id="schema_ApiMealReservationResponse"></a>
<a id="tocSapimealreservationresponse"></a>
<a id="tocsapimealreservationresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "meal_reservation": {
    "id": "string",
    "meal_place": {
      "id": "string",
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    },
    "meal_type": {
      "id": "string",
      "meal_place_code": "string",
      "meal_time_code": "string",
      "start_time": "14:15:22Z",
      "end_time": "14:15:22Z",
      "person_count": 0,
      "table_count": 0
    },
    "meal_time_frame": {
      "id": "string",
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    },
    "use_date": "2019-08-24",
    "meal_kana_name": "string",
    "meal_name": "string",
    "meal_short_name": "string",
    "meal_item": {
      "code": "string",
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    },
    "person_count": 0,
    "person_type": "ADULT",
    "unit_price": 0,
    "pricing_type": "INCLUDED",
    "start_time": "14:15:22Z",
    "end_time": "14:15:22Z",
    "valid": true,
    "note": "string",
    "reservation_ref": {
      "reservation_id": "string",
      "room_id": "string",
      "stay_id": "string",
      "reservation_number": "string",
      "room_number": "string"
    }
  }
}

```

ApiMealReservationResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|request|[ApiCommonResponseRequest](#schemaapicommonresponserequest)|false|none|Request|
|request_id|[ApiCommonResponseRequestId](#schemaapicommonresponserequestid)|false|none|RequestId|
|next_cursor|[ApiCommonResponseNextCursor](#schemaapicommonresponsenextcursor)|false|none|Indicates the position of the next entity. If an entity less than a limit is returned by the current page of the result set, then Cursor value is null.|
|meal_reservation|[MealReservation](#schemamealreservation)|false|none|Describes detailed meal information for a given guest.|

<h2 id="tocS_ApiMealReservationPutRequest">ApiMealReservationPutRequest</h2>
<!-- backwards compatibility -->
<a id="schemaapimealreservationputrequest"></a>
<a id="schema_ApiMealReservationPutRequest"></a>
<a id="tocSapimealreservationputrequest"></a>
<a id="tocsapimealreservationputrequest"></a>

```json
{
  "meal_reservation": {
    "date": "2019-08-24",
    "meal_place_code": "string",
    "meal_type_code": "string",
    "meal_time_frame_code": "string",
    "meal_item_code": "string",
    "person_count": 0,
    "person_type": "ADULT",
    "unit_price": 0,
    "pricing_type": "INCLUDED",
    "start_time": "14:15:22Z",
    "end_time": "14:15:22Z",
    "valid": true,
    "note": "string"
  }
}

```

ApiMealReservationPutRequest

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|meal_reservation|[MealReservationRequest](#schemamealreservationrequest)|false|none|Describes detailed meal information for a given guest.|

<h2 id="tocS_MealReservationRequest">MealReservationRequest</h2>
<!-- backwards compatibility -->
<a id="schemamealreservationrequest"></a>
<a id="schema_MealReservationRequest"></a>
<a id="tocSmealreservationrequest"></a>
<a id="tocsmealreservationrequest"></a>

```json
{
  "date": "2019-08-24",
  "meal_place_code": "string",
  "meal_type_code": "string",
  "meal_time_frame_code": "string",
  "meal_item_code": "string",
  "person_count": 0,
  "person_type": "ADULT",
  "unit_price": 0,
  "pricing_type": "INCLUDED",
  "start_time": "14:15:22Z",
  "end_time": "14:15:22Z",
  "valid": true,
  "note": "string"
}

```

MealReservationRequest

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|date|[Date](#schemadate)|false|none|日付(Date)|
|meal_place_code|string|true|none|none|
|meal_type_code|string|true|none|none|
|meal_time_frame_code|string|true|none|none|
|meal_item_code|string|true|none|none|
|person_count|integer|true|none|none|
|person_type|string|true|none|none|
|unit_price|number(double)|true|none|none|
|pricing_type|string|true|none|none|
|start_time|string(time)|false|none|none|
|end_time|string(time)|false|none|none|
|valid|boolean|false|none|none|
|note|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|person_type|ADULT|
|person_type|CHILD_A|
|person_type|CHILD_B|
|person_type|CHILD_C|
|person_type|CHILD_D|
|person_type|ROOM|
|pricing_type|INCLUDED|
|pricing_type|ADDED|
|pricing_type|SEPARATE|

<h2 id="tocS_ApiSalesEntryResponse">ApiSalesEntryResponse</h2>
<!-- backwards compatibility -->
<a id="schemaapisalesentryresponse"></a>
<a id="schema_ApiSalesEntryResponse"></a>
<a id="tocSapisalesentryresponse"></a>
<a id="tocsapisalesentryresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "sales_entry": {
    "slip_date": "2019-08-24",
    "sales_account_item_id": "string",
    "room_number": "string",
    "unit_price": 0,
    "quantity": 0,
    "tax_rate": 0,
    "bill_index": 0,
    "customer_note": "string",
    "control_note": "string",
    "duty_free": true
  }
}

```

ApiSalesEntryResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|request|[ApiCommonResponseRequest](#schemaapicommonresponserequest)|false|none|Request|
|request_id|[ApiCommonResponseRequestId](#schemaapicommonresponserequestid)|false|none|RequestId|
|sales_entry|[SalesEntry](#schemasalesentry)|false|none|Sales entry model|

<h2 id="tocS_ApiSalesEntryRequest">ApiSalesEntryRequest</h2>
<!-- backwards compatibility -->
<a id="schemaapisalesentryrequest"></a>
<a id="schema_ApiSalesEntryRequest"></a>
<a id="tocSapisalesentryrequest"></a>
<a id="tocsapisalesentryrequest"></a>

```json
{
  "slip_date": "2019-08-24",
  "room_number": "string",
  "sales_account_list_id": "string",
  "unit_price": 0,
  "quantity": 0,
  "tax_rate": 0,
  "bill_index": 0,
  "customer_note": "string",
  "control_note": "string",
  "duty_free": true
}

```

ApiSalesEntryRequest

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|slip_date|[Date](#schemadate)|true|none|日付(Date)|
|room_number|string|true|none|none|
|sales_account_list_id|string|true|none|none|
|unit_price|number(double)|true|none|none|
|quantity|number(double)|true|none|none|
|tax_rate|number(double)|false|none|none|
|bill_index|integer|false|none|none|
|customer_note|string|false|none|none|
|control_note|string|false|none|none|
|duty_free|boolean|false|none|none|

<h2 id="tocS_ApiReservationsResponse">ApiReservationsResponse</h2>
<!-- backwards compatibility -->
<a id="schemaapireservationsresponse"></a>
<a id="schema_ApiReservationsResponse"></a>
<a id="tocSapireservationsresponse"></a>
<a id="tocsapireservationsresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "reservations": [
    {
      "id ": "string",
      "reservation_number": "string",
      "check_in_date": "string",
      "check_out_date": "string",
      "room_sales_status": {
        "status": "Fix"
      },
      "control_status": {
        "status": "Reserve"
      },
      "person_count": [
        0
      ],
      "main_guest": {
        "person": {
          "kana_name": "string",
          "name": "string",
          "address": {
            "postal_code": "string",
            "prefecture_code": "string",
            "city": "string",
            "address_line": [
              "string"
            ]
          },
          "phone_no": "000-0000-0000",
          "phone_no_mobile": "000-0000-0000",
          "phone_no_other": "000-0000-0000",
          "gender": "Male",
          "birthday": "2019-08-24",
          "email": "example@example.com",
          "email_sub": "example@example.com",
          "external_customer_Id": "string"
        },
        "remarks": [
          {
            "system_user_company_id": "strin",
            "customer_number": "string",
            "customer_remark_id": "string",
            "importance_level_id": "PrimaryRemark",
            "facility_id": "strin",
            "date": "2019-08-24",
            "division": {
              "id": "str",
              "name": "string",
              "group_id": "str"
            },
            "type": {
              "id": "str",
              "name": "string"
            },
            "interlock_system_id": "str",
            "content": "string",
            "subject": "string",
            "output_timing": true,
            "youcom_hotel": {
              "id": "strin",
              "name": "string"
            },
            "youcom_sequence": 0,
            "create_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            },
            "change_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            }
          }
        ],
        "remak": [
          {
            "system_user_company_id": "strin",
            "customer_number": "string",
            "customer_remark_id": "string",
            "importance_level_id": "PrimaryRemark",
            "facility_id": "strin",
            "date": "2019-08-24",
            "division": {
              "id": "str",
              "name": "string",
              "group_id": "str"
            },
            "type": {
              "id": "str",
              "name": "string"
            },
            "interlock_system_id": "str",
            "content": "string",
            "subject": "string",
            "output_timing": true,
            "youcom_hotel": {
              "id": "strin",
              "name": "string"
            },
            "youcom_sequence": 0,
            "create_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            },
            "change_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            }
          }
        ],
        "id": "string",
        "customer_number": "string"
      },
      "reserved_by": {
        "person": {
          "kana_name": "string",
          "name": "string",
          "address": {
            "postal_code": "string",
            "prefecture_code": "string",
            "city": "string",
            "address_line": [
              "string"
            ]
          },
          "phone_no": "000-0000-0000",
          "phone_no_mobile": "000-0000-0000",
          "phone_no_other": "000-0000-0000",
          "gender": "Male",
          "birthday": "2019-08-24",
          "email": "example@example.com",
          "email_sub": "example@example.com",
          "external_customer_Id": "string"
        },
        "remarks": [
          {
            "system_user_company_id": "strin",
            "customer_number": "string",
            "customer_remark_id": "string",
            "importance_level_id": "PrimaryRemark",
            "facility_id": "strin",
            "date": "2019-08-24",
            "division": {
              "id": "str",
              "name": "string",
              "group_id": "str"
            },
            "type": {
              "id": "str",
              "name": "string"
            },
            "interlock_system_id": "str",
            "content": "string",
            "subject": "string",
            "output_timing": true,
            "youcom_hotel": {
              "id": "strin",
              "name": "string"
            },
            "youcom_sequence": 0,
            "create_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            },
            "change_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            }
          }
        ],
        "remak": [
          {
            "system_user_company_id": "strin",
            "customer_number": "string",
            "customer_remark_id": "string",
            "importance_level_id": "PrimaryRemark",
            "facility_id": "strin",
            "date": "2019-08-24",
            "division": {
              "id": "str",
              "name": "string",
              "group_id": "str"
            },
            "type": {
              "id": "str",
              "name": "string"
            },
            "interlock_system_id": "str",
            "content": "string",
            "subject": "string",
            "output_timing": true,
            "youcom_hotel": {
              "id": "strin",
              "name": "string"
            },
            "youcom_sequence": 0,
            "create_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            },
            "change_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            }
          }
        ],
        "id": "string",
        "customer_number": "string"
      },
      "remarks": [
        {
          "id": "string",
          "division": {
            "id": "str",
            "name": "string",
            "group_id": "str"
          },
          "remarks_type": {
            "id": "str",
            "name": "string"
          },
          "importance_level": "Primary Remark",
          "subject": "string",
          "content": "string"
        }
      ],
      "reservation_remarks": [
        {
          "id": "string",
          "division": {
            "id": "str",
            "name": "string",
            "group_id": "str"
          },
          "remarks_type": {
            "id": "str",
            "name": "string"
          },
          "importance_level": "Primary Remark",
          "subject": "string",
          "content": "string"
        }
      ],
      "room_reservations": [
        {
          "id": "string",
          "stay_registration_id ": "string",
          "room_number": "string",
          "room_status": "Vacant",
          "guests": [
            {
              "person": {
                "kana_name": "string",
                "name": "string",
                "address": {
                  "postal_code": "string",
                  "prefecture_code": "string",
                  "city": "string",
                  "address_line": [
                    "string"
                  ]
                },
                "phone_no": "000-0000-0000",
                "phone_no_mobile": "000-0000-0000",
                "phone_no_other": "000-0000-0000",
                "gender": "Male",
                "birthday": "2019-08-24",
                "email": "example@example.com",
                "email_sub": "example@example.com",
                "external_customer_Id": "string"
              },
              "remarks": [
                {
                  "system_user_company_id": "strin",
                  "customer_number": "string",
                  "customer_remark_id": "string",
                  "importance_level_id": "PrimaryRemark",
                  "facility_id": "strin",
                  "date": "2019-08-24",
                  "division": {
                    "id": "str",
                    "name": "string",
                    "group_id": "str"
                  },
                  "type": {
                    "id": "str",
                    "name": "string"
                  },
                  "interlock_system_id": "str",
                  "content": "string",
                  "subject": "string",
                  "output_timing": true,
                  "youcom_hotel": {
                    "id": "strin",
                    "name": "string"
                  },
                  "youcom_sequence": 0,
                  "create_info": {
                    "host_name": "string",
                    "time_stamp": "2019-08-24T14:15:22Z",
                    "user_account_id": "string"
                  },
                  "change_info": {
                    "host_name": "string",
                    "time_stamp": "2019-08-24T14:15:22Z",
                    "user_account_id": "string"
                  }
                }
              ],
              "remak": [
                {
                  "system_user_company_id": "strin",
                  "customer_number": "string",
                  "customer_remark_id": "string",
                  "importance_level_id": "PrimaryRemark",
                  "facility_id": "strin",
                  "date": "2019-08-24",
                  "division": {
                    "id": "str",
                    "name": "string",
                    "group_id": "str"
                  },
                  "type": {
                    "id": "str",
                    "name": "string"
                  },
                  "interlock_system_id": "str",
                  "content": "string",
                  "subject": "string",
                  "output_timing": true,
                  "youcom_hotel": {
                    "id": "strin",
                    "name": "string"
                  },
                  "youcom_sequence": 0,
                  "create_info": {
                    "host_name": "string",
                    "time_stamp": "2019-08-24T14:15:22Z",
                    "user_account_id": "string"
                  },
                  "change_info": {
                    "host_name": "string",
                    "time_stamp": "2019-08-24T14:15:22Z",
                    "user_account_id": "string"
                  }
                }
              ],
              "id": "string",
              "customer_number": "string"
            }
          ],
          "room_type": {
            "code": "string",
            "standard_persons": 0,
            "max_persons": 0,
            "name": "string",
            "short_name": "string",
            "kana_name": "string",
            "foreign_name": "string",
            "foreign_short_name": "string"
          },
          "sales_control_type": "FREE",
          "sales_control_unit": "string",
          "extra_bed_count": 0,
          "stay_period": {
            "arrival_date": "2019-08-24",
            "arrival_time": "14:15:22Z",
            "departure_date": "2019-08-24",
            "departure_time": "14:15:22Z",
            "late_out": true
          },
          "reservation_route": {
            "reservationDisplayName": "string",
            "reservationRoutes": [
              {
                "code": "string",
                "name": "string",
                "short_name": "string",
                "kana_name": "string",
                "foreign_name": "string",
                "foreign_short_name": "string"
              }
            ]
          },
          "agent_reservation_number": "string",
          "agent_course": "string",
          "person_count": [
            0
          ],
          "pricing": {
            "sales_package": {
              "code": "string",
              "name": "string",
              "short_name": "string",
              "kana_name": "string",
              "foreign_name": "string",
              "foreign_short_name": "string",
              "print_name": "string",
              "print_foreign_name": "string"
            },
            "discount_item": {
              "code": "string",
              "name": "string",
              "short_name": "string",
              "kana_name": "string",
              "foreign_name": "string",
              "foreign_short_name": "string",
              "rate": 0,
              "amount": 0
            },
            "discount_rate": 100,
            "discount_amount": 0,
            "pricing_type": "GROSS",
            "price": 0
          },
          "provision_requests": [
            {
              "id": "string",
              "provision": {
                "code": "string",
                "name": "string",
                "short_name": "string",
                "kana_name": "string",
                "foreign_name": "string",
                "foreign_short_name": "string"
              },
              "from_date": "2019-08-24",
              "to_date": "2019-08-24",
              "stock_control": true,
              "quantity": 0,
              "note": "string",
              "reservation_ref": {
                "reservation_id": "string",
                "room_id": "string",
                "stay_id": "string",
                "reservation_number": "string",
                "room_number": "string"
              }
            }
          ],
          "meal_reservations": [
            {
              "id": "string",
              "meal_place": {
                "id": "string",
                "name": "string",
                "short_name": "string",
                "kana_name": "string",
                "foreign_name": "string",
                "foreign_short_name": "string"
              },
              "meal_type": {
                "id": "string",
                "meal_place_code": "string",
                "meal_time_code": "string",
                "start_time": "14:15:22Z",
                "end_time": "14:15:22Z",
                "person_count": 0,
                "table_count": 0
              },
              "meal_time_frame": {
                "id": "string",
                "name": "string",
                "short_name": "string",
                "kana_name": "string",
                "foreign_name": "string",
                "foreign_short_name": "string"
              },
              "use_date": "2019-08-24",
              "meal_kana_name": "string",
              "meal_name": "string",
              "meal_short_name": "string",
              "meal_item": {
                "code": "string",
                "name": "string",
                "short_name": "string",
                "kana_name": "string",
                "foreign_name": "string",
                "foreign_short_name": "string"
              },
              "person_count": 0,
              "person_type": "ADULT",
              "unit_price": 0,
              "pricing_type": "INCLUDED",
              "start_time": "14:15:22Z",
              "end_time": "14:15:22Z",
              "valid": true,
              "note": "string",
              "reservation_ref": {
                "reservation_id": "string",
                "room_id": "string",
                "stay_id": "string",
                "reservation_number": "string",
                "room_number": "string"
              }
            }
          ],
          "deposits": [
            {
              "id": "string",
              "account_date": "2019-08-24",
              "payment_method": {
                "code": "string",
                "name": "string",
                "short_name": "string",
                "kana_name": "string",
                "foreign_name": "string",
                "foreign_short_name": "string",
                "use_address": true
              },
              "billing_provider": {
                "code": "string",
                "name": "string",
                "short_name": "string",
                "kana_name": "string",
                "foreign_name": "string",
                "foreign_short_name": "string"
              },
              "amount": 0,
              "bill_index": 0,
              "bill_note": "string",
              "internal_note": "string",
              "provider_reference": "string",
              "reservation_ref": {
                "reservation_id": "string",
                "room_id": "string",
                "stay_id": "string",
                "reservation_number": "string",
                "room_number": "string"
              }
            }
          ],
          "slip_items": [
            {
              "id": "string",
              "date": "2019-08-24",
              "item": {
                "code": "string",
                "name": "string",
                "short_name": "string",
                "kana_name": "string",
                "foreign_name": "string",
                "price": 0
              },
              "price_per_item": 0,
              "quantity": 0,
              "total_price": 0,
              "bill_index": 0,
              "bill_note": "string",
              "internal_note": "string",
              "tax_free": true,
              "room_type": {
                "code": "string",
                "standard_persons": 0,
                "max_persons": 0,
                "name": "string",
                "short_name": "string",
                "kana_name": "string",
                "foreign_name": "string",
                "foreign_short_name": "string"
              },
              "reservation_ref": {
                "reservation_id": "string",
                "room_id": "string",
                "stay_id": "string",
                "reservation_number": "string",
                "room_number": "string"
              }
            }
          ],
          "extra_services": [
            {
              "id": "string",
              "service_item": {
                "code": "string",
                "name": "string",
                "kana_name": "string",
                "short_name": "string",
                "foreign_name": "string",
                "foreign_short_name": "string"
              },
              "service_period": {
                "arrival_date": "2019-08-24",
                "arrival_time": "14:15:22Z",
                "departure_date": "2019-08-24",
                "departure_time": "14:15:22Z",
                "late_out": true
              },
              "person_count": 0,
              "note": "string",
              "reservation_ref": {
                "reservation_id": "string",
                "room_id": "string",
                "stay_id": "string",
                "reservation_number": "string",
                "room_number": "string"
              }
            }
          ],
          "remarks": [
            {
              "id": "string",
              "division": {
                "id": "str",
                "name": "string",
                "group_id": "str"
              },
              "remarks_type": {
                "id": "str",
                "name": "string"
              },
              "importance_level": "Primary Remark",
              "subject": "string",
              "content": "string"
            }
          ],
          "price_changes": [
            {
              "date_range_end": "2019-08-24",
              "date_range_start": "2019-08-24",
              "prices": [
                {
                  "discount_amount": 0,
                  "discount_item_id": "string",
                  "discount_item_name": "string",
                  "discount_rate": 0,
                  "person_count": [
                    0
                  ],
                  "person_count_price_calc": 0,
                  "price": 0,
                  "pricing_type": "GROSS",
                  "rate_id": "string",
                  "room_type_code": "string",
                  "sales_package_id": "string",
                  "sales_package_name": "string"
                }
              ]
            }
          ]
        }
      ],
      "is_group": true,
      "total_stay_period": {
        "arrival_date": "2019-08-24",
        "arrival_time": "14:15:22Z",
        "departure_date": "2019-08-24",
        "departure_time": "14:15:22Z",
        "late_out": true
      },
      "marketing_area": {
        "code": "string",
        "name": "string",
        "foreign_name": "string"
      },
      "last_modified": "2019-08-24T14:15:22Z",
      "created": "2019-08-24T14:15:22Z",
      "primary_remark": {
        "id": "string",
        "division": {
          "id": "str",
          "name": "string",
          "group_id": "str"
        },
        "remarks_type": {
          "id": "str",
          "name": "string"
        },
        "importance_level": "Primary Remark",
        "subject": "string",
        "content": "string"
      }
    }
  ]
}

```

ApiReservationsResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|request|[ApiCommonResponseRequest](#schemaapicommonresponserequest)|false|none|Request|
|request_id|[ApiCommonResponseRequestId](#schemaapicommonresponserequestid)|false|none|RequestId|
|next_cursor|[ApiCommonResponseNextCursor](#schemaapicommonresponsenextcursor)|false|none|Indicates the position of the next entity. If an entity less than a limit is returned by the current page of the result set, then Cursor value is null.|
|reservations|[[Reservation](#schemareservation)]|false|none|[Describes reservation details for a guest]|

<h2 id="tocS_ApiReservationResponse">ApiReservationResponse</h2>
<!-- backwards compatibility -->
<a id="schemaapireservationresponse"></a>
<a id="schema_ApiReservationResponse"></a>
<a id="tocSapireservationresponse"></a>
<a id="tocsapireservationresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "reservation": {
    "id ": "string",
    "reservation_number": "string",
    "check_in_date": "string",
    "check_out_date": "string",
    "room_sales_status": {
      "status": "Fix"
    },
    "control_status": {
      "status": "Reserve"
    },
    "person_count": [
      0
    ],
    "main_guest": {
      "person": {
        "kana_name": "string",
        "name": "string",
        "address": {
          "postal_code": "string",
          "prefecture_code": "string",
          "city": "string",
          "address_line": [
            "string"
          ]
        },
        "phone_no": "000-0000-0000",
        "phone_no_mobile": "000-0000-0000",
        "phone_no_other": "000-0000-0000",
        "gender": "Male",
        "birthday": "2019-08-24",
        "email": "example@example.com",
        "email_sub": "example@example.com",
        "external_customer_Id": "string"
      },
      "remarks": [
        {
          "system_user_company_id": "strin",
          "customer_number": "string",
          "customer_remark_id": "string",
          "importance_level_id": "PrimaryRemark",
          "facility_id": "strin",
          "date": "2019-08-24",
          "division": {
            "id": "str",
            "name": "string",
            "group_id": "str"
          },
          "type": {
            "id": "str",
            "name": "string"
          },
          "interlock_system_id": "str",
          "content": "string",
          "subject": "string",
          "output_timing": true,
          "youcom_hotel": {
            "id": "strin",
            "name": "string"
          },
          "youcom_sequence": 0,
          "create_info": {
            "host_name": "string",
            "time_stamp": "2019-08-24T14:15:22Z",
            "user_account_id": "string"
          },
          "change_info": {
            "host_name": "string",
            "time_stamp": "2019-08-24T14:15:22Z",
            "user_account_id": "string"
          }
        }
      ],
      "remak": [
        {
          "system_user_company_id": "strin",
          "customer_number": "string",
          "customer_remark_id": "string",
          "importance_level_id": "PrimaryRemark",
          "facility_id": "strin",
          "date": "2019-08-24",
          "division": {
            "id": "str",
            "name": "string",
            "group_id": "str"
          },
          "type": {
            "id": "str",
            "name": "string"
          },
          "interlock_system_id": "str",
          "content": "string",
          "subject": "string",
          "output_timing": true,
          "youcom_hotel": {
            "id": "strin",
            "name": "string"
          },
          "youcom_sequence": 0,
          "create_info": {
            "host_name": "string",
            "time_stamp": "2019-08-24T14:15:22Z",
            "user_account_id": "string"
          },
          "change_info": {
            "host_name": "string",
            "time_stamp": "2019-08-24T14:15:22Z",
            "user_account_id": "string"
          }
        }
      ],
      "id": "string",
      "customer_number": "string"
    },
    "reserved_by": {
      "person": {
        "kana_name": "string",
        "name": "string",
        "address": {
          "postal_code": "string",
          "prefecture_code": "string",
          "city": "string",
          "address_line": [
            "string"
          ]
        },
        "phone_no": "000-0000-0000",
        "phone_no_mobile": "000-0000-0000",
        "phone_no_other": "000-0000-0000",
        "gender": "Male",
        "birthday": "2019-08-24",
        "email": "example@example.com",
        "email_sub": "example@example.com",
        "external_customer_Id": "string"
      },
      "remarks": [
        {
          "system_user_company_id": "strin",
          "customer_number": "string",
          "customer_remark_id": "string",
          "importance_level_id": "PrimaryRemark",
          "facility_id": "strin",
          "date": "2019-08-24",
          "division": {
            "id": "str",
            "name": "string",
            "group_id": "str"
          },
          "type": {
            "id": "str",
            "name": "string"
          },
          "interlock_system_id": "str",
          "content": "string",
          "subject": "string",
          "output_timing": true,
          "youcom_hotel": {
            "id": "strin",
            "name": "string"
          },
          "youcom_sequence": 0,
          "create_info": {
            "host_name": "string",
            "time_stamp": "2019-08-24T14:15:22Z",
            "user_account_id": "string"
          },
          "change_info": {
            "host_name": "string",
            "time_stamp": "2019-08-24T14:15:22Z",
            "user_account_id": "string"
          }
        }
      ],
      "remak": [
        {
          "system_user_company_id": "strin",
          "customer_number": "string",
          "customer_remark_id": "string",
          "importance_level_id": "PrimaryRemark",
          "facility_id": "strin",
          "date": "2019-08-24",
          "division": {
            "id": "str",
            "name": "string",
            "group_id": "str"
          },
          "type": {
            "id": "str",
            "name": "string"
          },
          "interlock_system_id": "str",
          "content": "string",
          "subject": "string",
          "output_timing": true,
          "youcom_hotel": {
            "id": "strin",
            "name": "string"
          },
          "youcom_sequence": 0,
          "create_info": {
            "host_name": "string",
            "time_stamp": "2019-08-24T14:15:22Z",
            "user_account_id": "string"
          },
          "change_info": {
            "host_name": "string",
            "time_stamp": "2019-08-24T14:15:22Z",
            "user_account_id": "string"
          }
        }
      ],
      "id": "string",
      "customer_number": "string"
    },
    "remarks": [
      {
        "id": "string",
        "division": {
          "id": "str",
          "name": "string",
          "group_id": "str"
        },
        "remarks_type": {
          "id": "str",
          "name": "string"
        },
        "importance_level": "Primary Remark",
        "subject": "string",
        "content": "string"
      }
    ],
    "reservation_remarks": [
      {
        "id": "string",
        "division": {
          "id": "str",
          "name": "string",
          "group_id": "str"
        },
        "remarks_type": {
          "id": "str",
          "name": "string"
        },
        "importance_level": "Primary Remark",
        "subject": "string",
        "content": "string"
      }
    ],
    "room_reservations": [
      {
        "id": "string",
        "stay_registration_id ": "string",
        "room_number": "string",
        "room_status": "Vacant",
        "guests": [
          {
            "person": {
              "kana_name": "string",
              "name": "string",
              "address": {
                "postal_code": "string",
                "prefecture_code": "string",
                "city": "string",
                "address_line": [
                  "string"
                ]
              },
              "phone_no": "000-0000-0000",
              "phone_no_mobile": "000-0000-0000",
              "phone_no_other": "000-0000-0000",
              "gender": "Male",
              "birthday": "2019-08-24",
              "email": "example@example.com",
              "email_sub": "example@example.com",
              "external_customer_Id": "string"
            },
            "remarks": [
              {
                "system_user_company_id": "strin",
                "customer_number": "string",
                "customer_remark_id": "string",
                "importance_level_id": "PrimaryRemark",
                "facility_id": "strin",
                "date": "2019-08-24",
                "division": {
                  "id": "str",
                  "name": "string",
                  "group_id": "str"
                },
                "type": {
                  "id": "str",
                  "name": "string"
                },
                "interlock_system_id": "str",
                "content": "string",
                "subject": "string",
                "output_timing": true,
                "youcom_hotel": {
                  "id": "strin",
                  "name": "string"
                },
                "youcom_sequence": 0,
                "create_info": {
                  "host_name": "string",
                  "time_stamp": "2019-08-24T14:15:22Z",
                  "user_account_id": "string"
                },
                "change_info": {
                  "host_name": "string",
                  "time_stamp": "2019-08-24T14:15:22Z",
                  "user_account_id": "string"
                }
              }
            ],
            "remak": [
              {
                "system_user_company_id": "strin",
                "customer_number": "string",
                "customer_remark_id": "string",
                "importance_level_id": "PrimaryRemark",
                "facility_id": "strin",
                "date": "2019-08-24",
                "division": {
                  "id": "str",
                  "name": "string",
                  "group_id": "str"
                },
                "type": {
                  "id": "str",
                  "name": "string"
                },
                "interlock_system_id": "str",
                "content": "string",
                "subject": "string",
                "output_timing": true,
                "youcom_hotel": {
                  "id": "strin",
                  "name": "string"
                },
                "youcom_sequence": 0,
                "create_info": {
                  "host_name": "string",
                  "time_stamp": "2019-08-24T14:15:22Z",
                  "user_account_id": "string"
                },
                "change_info": {
                  "host_name": "string",
                  "time_stamp": "2019-08-24T14:15:22Z",
                  "user_account_id": "string"
                }
              }
            ],
            "id": "string",
            "customer_number": "string"
          }
        ],
        "room_type": {
          "code": "string",
          "standard_persons": 0,
          "max_persons": 0,
          "name": "string",
          "short_name": "string",
          "kana_name": "string",
          "foreign_name": "string",
          "foreign_short_name": "string"
        },
        "sales_control_type": "FREE",
        "sales_control_unit": "string",
        "extra_bed_count": 0,
        "stay_period": {
          "arrival_date": "2019-08-24",
          "arrival_time": "14:15:22Z",
          "departure_date": "2019-08-24",
          "departure_time": "14:15:22Z",
          "late_out": true
        },
        "reservation_route": {
          "reservationDisplayName": "string",
          "reservationRoutes": [
            {
              "code": "string",
              "name": "string",
              "short_name": "string",
              "kana_name": "string",
              "foreign_name": "string",
              "foreign_short_name": "string"
            }
          ]
        },
        "agent_reservation_number": "string",
        "agent_course": "string",
        "person_count": [
          0
        ],
        "pricing": {
          "sales_package": {
            "code": "string",
            "name": "string",
            "short_name": "string",
            "kana_name": "string",
            "foreign_name": "string",
            "foreign_short_name": "string",
            "print_name": "string",
            "print_foreign_name": "string"
          },
          "discount_item": {
            "code": "string",
            "name": "string",
            "short_name": "string",
            "kana_name": "string",
            "foreign_name": "string",
            "foreign_short_name": "string",
            "rate": 0,
            "amount": 0
          },
          "discount_rate": 100,
          "discount_amount": 0,
          "pricing_type": "GROSS",
          "price": 0
        },
        "provision_requests": [
          {
            "id": "string",
            "provision": {
              "code": "string",
              "name": "string",
              "short_name": "string",
              "kana_name": "string",
              "foreign_name": "string",
              "foreign_short_name": "string"
            },
            "from_date": "2019-08-24",
            "to_date": "2019-08-24",
            "stock_control": true,
            "quantity": 0,
            "note": "string",
            "reservation_ref": {
              "reservation_id": "string",
              "room_id": "string",
              "stay_id": "string",
              "reservation_number": "string",
              "room_number": "string"
            }
          }
        ],
        "meal_reservations": [
          {
            "id": "string",
            "meal_place": {
              "id": "string",
              "name": "string",
              "short_name": "string",
              "kana_name": "string",
              "foreign_name": "string",
              "foreign_short_name": "string"
            },
            "meal_type": {
              "id": "string",
              "meal_place_code": "string",
              "meal_time_code": "string",
              "start_time": "14:15:22Z",
              "end_time": "14:15:22Z",
              "person_count": 0,
              "table_count": 0
            },
            "meal_time_frame": {
              "id": "string",
              "name": "string",
              "short_name": "string",
              "kana_name": "string",
              "foreign_name": "string",
              "foreign_short_name": "string"
            },
            "use_date": "2019-08-24",
            "meal_kana_name": "string",
            "meal_name": "string",
            "meal_short_name": "string",
            "meal_item": {
              "code": "string",
              "name": "string",
              "short_name": "string",
              "kana_name": "string",
              "foreign_name": "string",
              "foreign_short_name": "string"
            },
            "person_count": 0,
            "person_type": "ADULT",
            "unit_price": 0,
            "pricing_type": "INCLUDED",
            "start_time": "14:15:22Z",
            "end_time": "14:15:22Z",
            "valid": true,
            "note": "string",
            "reservation_ref": {
              "reservation_id": "string",
              "room_id": "string",
              "stay_id": "string",
              "reservation_number": "string",
              "room_number": "string"
            }
          }
        ],
        "deposits": [
          {
            "id": "string",
            "account_date": "2019-08-24",
            "payment_method": {
              "code": "string",
              "name": "string",
              "short_name": "string",
              "kana_name": "string",
              "foreign_name": "string",
              "foreign_short_name": "string",
              "use_address": true
            },
            "billing_provider": {
              "code": "string",
              "name": "string",
              "short_name": "string",
              "kana_name": "string",
              "foreign_name": "string",
              "foreign_short_name": "string"
            },
            "amount": 0,
            "bill_index": 0,
            "bill_note": "string",
            "internal_note": "string",
            "provider_reference": "string",
            "reservation_ref": {
              "reservation_id": "string",
              "room_id": "string",
              "stay_id": "string",
              "reservation_number": "string",
              "room_number": "string"
            }
          }
        ],
        "slip_items": [
          {
            "id": "string",
            "date": "2019-08-24",
            "item": {
              "code": "string",
              "name": "string",
              "short_name": "string",
              "kana_name": "string",
              "foreign_name": "string",
              "price": 0
            },
            "price_per_item": 0,
            "quantity": 0,
            "total_price": 0,
            "bill_index": 0,
            "bill_note": "string",
            "internal_note": "string",
            "tax_free": true,
            "room_type": {
              "code": "string",
              "standard_persons": 0,
              "max_persons": 0,
              "name": "string",
              "short_name": "string",
              "kana_name": "string",
              "foreign_name": "string",
              "foreign_short_name": "string"
            },
            "reservation_ref": {
              "reservation_id": "string",
              "room_id": "string",
              "stay_id": "string",
              "reservation_number": "string",
              "room_number": "string"
            }
          }
        ],
        "extra_services": [
          {
            "id": "string",
            "service_item": {
              "code": "string",
              "name": "string",
              "kana_name": "string",
              "short_name": "string",
              "foreign_name": "string",
              "foreign_short_name": "string"
            },
            "service_period": {
              "arrival_date": "2019-08-24",
              "arrival_time": "14:15:22Z",
              "departure_date": "2019-08-24",
              "departure_time": "14:15:22Z",
              "late_out": true
            },
            "person_count": 0,
            "note": "string",
            "reservation_ref": {
              "reservation_id": "string",
              "room_id": "string",
              "stay_id": "string",
              "reservation_number": "string",
              "room_number": "string"
            }
          }
        ],
        "remarks": [
          {
            "id": "string",
            "division": {
              "id": "str",
              "name": "string",
              "group_id": "str"
            },
            "remarks_type": {
              "id": "str",
              "name": "string"
            },
            "importance_level": "Primary Remark",
            "subject": "string",
            "content": "string"
          }
        ],
        "price_changes": [
          {
            "date_range_end": "2019-08-24",
            "date_range_start": "2019-08-24",
            "prices": [
              {
                "discount_amount": 0,
                "discount_item_id": "string",
                "discount_item_name": "string",
                "discount_rate": 0,
                "person_count": [
                  0
                ],
                "person_count_price_calc": 0,
                "price": 0,
                "pricing_type": "GROSS",
                "rate_id": "string",
                "room_type_code": "string",
                "sales_package_id": "string",
                "sales_package_name": "string"
              }
            ]
          }
        ]
      }
    ],
    "is_group": true,
    "total_stay_period": {
      "arrival_date": "2019-08-24",
      "arrival_time": "14:15:22Z",
      "departure_date": "2019-08-24",
      "departure_time": "14:15:22Z",
      "late_out": true
    },
    "marketing_area": {
      "code": "string",
      "name": "string",
      "foreign_name": "string"
    },
    "last_modified": "2019-08-24T14:15:22Z",
    "created": "2019-08-24T14:15:22Z",
    "primary_remark": {
      "id": "string",
      "division": {
        "id": "str",
        "name": "string",
        "group_id": "str"
      },
      "remarks_type": {
        "id": "str",
        "name": "string"
      },
      "importance_level": "Primary Remark",
      "subject": "string",
      "content": "string"
    }
  }
}

```

ApiReservationResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|request|[ApiCommonResponseRequest](#schemaapicommonresponserequest)|false|none|Request|
|request_id|[ApiCommonResponseRequestId](#schemaapicommonresponserequestid)|false|none|RequestId|
|reservation|[Reservation](#schemareservation)|false|none|Describes reservation details for a guest|

<h2 id="tocS_ApiReservationPostRequest">ApiReservationPostRequest</h2>
<!-- backwards compatibility -->
<a id="schemaapireservationpostrequest"></a>
<a id="schema_ApiReservationPostRequest"></a>
<a id="tocSapireservationpostrequest"></a>
<a id="tocsapireservationpostrequest"></a>

```json
{
  "reservation": {
    "main_guest": {
      "kana_name": "string",
      "name": "string",
      "address": {
        "postal_code": "string",
        "prefecture_code": "string",
        "city": "string",
        "address_line": [
          "string"
        ]
      },
      "phone_no": "000-0000-0000",
      "phone_no_mobile": "000-0000-0000",
      "phone_no_other": "000-0000-0000",
      "gender": "Male",
      "birthday": "2019-08-24",
      "email": "example@example.com",
      "email_sub": "example@example.com",
      "external_customer_Id": "string"
    },
    "reserved_by": {
      "kana_name": "string",
      "name": "string",
      "address": {
        "postal_code": "string",
        "prefecture_code": "string",
        "city": "string",
        "address_line": [
          "string"
        ]
      },
      "phone_no": "000-0000-0000",
      "phone_no_mobile": "000-0000-0000",
      "phone_no_other": "000-0000-0000",
      "gender": "Male",
      "birthday": "2019-08-24",
      "email": "example@example.com",
      "email_sub": "example@example.com",
      "external_customer_Id": "string"
    },
    "room_reservations": [
      {
        "room_number": "string",
        "guests": [
          {
            "person": {
              "kana_name": "string",
              "name": "string",
              "address": {
                "postal_code": "string",
                "prefecture_code": "string",
                "city": "string",
                "address_line": [
                  "string"
                ]
              },
              "phone_no": "000-0000-0000",
              "phone_no_mobile": "000-0000-0000",
              "phone_no_other": "000-0000-0000",
              "gender": "Male",
              "birthday": "2019-08-24",
              "email": "example@example.com",
              "email_sub": "example@example.com",
              "external_customer_Id": "string"
            },
            "remarks": [
              {
                "system_user_company_id": "strin",
                "customer_number": "string",
                "customer_remark_id": "string",
                "importance_level_id": "PrimaryRemark",
                "facility_id": "strin",
                "date": "2019-08-24",
                "division": {
                  "id": "str",
                  "name": "string",
                  "group_id": "str"
                },
                "type": {
                  "id": "str",
                  "name": "string"
                },
                "interlock_system_id": "str",
                "content": "string",
                "subject": "string",
                "output_timing": true,
                "youcom_hotel": {
                  "id": "strin",
                  "name": "string"
                },
                "youcom_sequence": 0,
                "create_info": {
                  "host_name": "string",
                  "time_stamp": "2019-08-24T14:15:22Z",
                  "user_account_id": "string"
                },
                "change_info": {
                  "host_name": "string",
                  "time_stamp": "2019-08-24T14:15:22Z",
                  "user_account_id": "string"
                }
              }
            ],
            "remak": [
              {
                "system_user_company_id": "strin",
                "customer_number": "string",
                "customer_remark_id": "string",
                "importance_level_id": "PrimaryRemark",
                "facility_id": "strin",
                "date": "2019-08-24",
                "division": {
                  "id": "str",
                  "name": "string",
                  "group_id": "str"
                },
                "type": {
                  "id": "str",
                  "name": "string"
                },
                "interlock_system_id": "str",
                "content": "string",
                "subject": "string",
                "output_timing": true,
                "youcom_hotel": {
                  "id": "strin",
                  "name": "string"
                },
                "youcom_sequence": 0,
                "create_info": {
                  "host_name": "string",
                  "time_stamp": "2019-08-24T14:15:22Z",
                  "user_account_id": "string"
                },
                "change_info": {
                  "host_name": "string",
                  "time_stamp": "2019-08-24T14:15:22Z",
                  "user_account_id": "string"
                }
              }
            ],
            "id": "string",
            "customer_number": "string"
          }
        ],
        "room_type_id": "string",
        "sales_control_type": "FREE",
        "sales_control_unit": "string",
        "extra_bed_count": 0,
        "stay_period": {
          "arrival_date": "2019-08-24",
          "arrival_time": "14:15:22Z",
          "departure_date": "2019-08-24",
          "departure_time": "14:15:22Z",
          "late_out": true
        },
        "reservation_routes": [
          "string"
        ],
        "agent_course": "string",
        "person_count": [
          0
        ],
        "external_agent": {
          "external_agent_type": "TLL",
          "external_agent_code": "string",
          "external_agent_course_name": "string",
          "external_meal_type": "string",
          "external_room_type_id": "string",
          "external_facility_code": "string"
        },
        "agent_reservation_number": "string",
        "price_changes": [
          {
            "date_range_end": "2019-08-24",
            "date_range_start": "2019-08-24",
            "prices": [
              {
                "discount_amount": 0,
                "discount_item_id": "string",
                "discount_item_name": "string",
                "discount_rate": 0,
                "person_count": [
                  0
                ],
                "person_count_price_calc": 0,
                "price": 0,
                "pricing_type": "GROSS",
                "rate_id": "string",
                "room_type_code": "string",
                "sales_package_id": "string",
                "sales_package_name": "string"
              }
            ]
          }
        ]
      }
    ],
    "is_group": true,
    "marketing_area_code": "string"
  }
}

```

ApiReservationPostRequest

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|reservation|[ReservationCreateRequest](#schemareservationcreaterequest)|false|none|Describes a new reservation to be created|

<h2 id="tocS_ReservationCreateRequest">ReservationCreateRequest</h2>
<!-- backwards compatibility -->
<a id="schemareservationcreaterequest"></a>
<a id="schema_ReservationCreateRequest"></a>
<a id="tocSreservationcreaterequest"></a>
<a id="tocsreservationcreaterequest"></a>

```json
{
  "main_guest": {
    "kana_name": "string",
    "name": "string",
    "address": {
      "postal_code": "string",
      "prefecture_code": "string",
      "city": "string",
      "address_line": [
        "string"
      ]
    },
    "phone_no": "000-0000-0000",
    "phone_no_mobile": "000-0000-0000",
    "phone_no_other": "000-0000-0000",
    "gender": "Male",
    "birthday": "2019-08-24",
    "email": "example@example.com",
    "email_sub": "example@example.com",
    "external_customer_Id": "string"
  },
  "reserved_by": {
    "kana_name": "string",
    "name": "string",
    "address": {
      "postal_code": "string",
      "prefecture_code": "string",
      "city": "string",
      "address_line": [
        "string"
      ]
    },
    "phone_no": "000-0000-0000",
    "phone_no_mobile": "000-0000-0000",
    "phone_no_other": "000-0000-0000",
    "gender": "Male",
    "birthday": "2019-08-24",
    "email": "example@example.com",
    "email_sub": "example@example.com",
    "external_customer_Id": "string"
  },
  "room_reservations": [
    {
      "room_number": "string",
      "guests": [
        {
          "person": {
            "kana_name": "string",
            "name": "string",
            "address": {
              "postal_code": "string",
              "prefecture_code": "string",
              "city": "string",
              "address_line": [
                "string"
              ]
            },
            "phone_no": "000-0000-0000",
            "phone_no_mobile": "000-0000-0000",
            "phone_no_other": "000-0000-0000",
            "gender": "Male",
            "birthday": "2019-08-24",
            "email": "example@example.com",
            "email_sub": "example@example.com",
            "external_customer_Id": "string"
          },
          "remarks": [
            {
              "system_user_company_id": "strin",
              "customer_number": "string",
              "customer_remark_id": "string",
              "importance_level_id": "PrimaryRemark",
              "facility_id": "strin",
              "date": "2019-08-24",
              "division": {
                "id": "str",
                "name": "string",
                "group_id": "str"
              },
              "type": {
                "id": "str",
                "name": "string"
              },
              "interlock_system_id": "str",
              "content": "string",
              "subject": "string",
              "output_timing": true,
              "youcom_hotel": {
                "id": "strin",
                "name": "string"
              },
              "youcom_sequence": 0,
              "create_info": {
                "host_name": "string",
                "time_stamp": "2019-08-24T14:15:22Z",
                "user_account_id": "string"
              },
              "change_info": {
                "host_name": "string",
                "time_stamp": "2019-08-24T14:15:22Z",
                "user_account_id": "string"
              }
            }
          ],
          "remak": [
            {
              "system_user_company_id": "strin",
              "customer_number": "string",
              "customer_remark_id": "string",
              "importance_level_id": "PrimaryRemark",
              "facility_id": "strin",
              "date": "2019-08-24",
              "division": {
                "id": "str",
                "name": "string",
                "group_id": "str"
              },
              "type": {
                "id": "str",
                "name": "string"
              },
              "interlock_system_id": "str",
              "content": "string",
              "subject": "string",
              "output_timing": true,
              "youcom_hotel": {
                "id": "strin",
                "name": "string"
              },
              "youcom_sequence": 0,
              "create_info": {
                "host_name": "string",
                "time_stamp": "2019-08-24T14:15:22Z",
                "user_account_id": "string"
              },
              "change_info": {
                "host_name": "string",
                "time_stamp": "2019-08-24T14:15:22Z",
                "user_account_id": "string"
              }
            }
          ],
          "id": "string",
          "customer_number": "string"
        }
      ],
      "room_type_id": "string",
      "sales_control_type": "FREE",
      "sales_control_unit": "string",
      "extra_bed_count": 0,
      "stay_period": {
        "arrival_date": "2019-08-24",
        "arrival_time": "14:15:22Z",
        "departure_date": "2019-08-24",
        "departure_time": "14:15:22Z",
        "late_out": true
      },
      "reservation_routes": [
        "string"
      ],
      "agent_course": "string",
      "person_count": [
        0
      ],
      "external_agent": {
        "external_agent_type": "TLL",
        "external_agent_code": "string",
        "external_agent_course_name": "string",
        "external_meal_type": "string",
        "external_room_type_id": "string",
        "external_facility_code": "string"
      },
      "agent_reservation_number": "string",
      "price_changes": [
        {
          "date_range_end": "2019-08-24",
          "date_range_start": "2019-08-24",
          "prices": [
            {
              "discount_amount": 0,
              "discount_item_id": "string",
              "discount_item_name": "string",
              "discount_rate": 0,
              "person_count": [
                0
              ],
              "person_count_price_calc": 0,
              "price": 0,
              "pricing_type": "GROSS",
              "rate_id": "string",
              "room_type_code": "string",
              "sales_package_id": "string",
              "sales_package_name": "string"
            }
          ]
        }
      ]
    }
  ],
  "is_group": true,
  "marketing_area_code": "string"
}

```

ReservationCreateRequest

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|main_guest|[Person](#schemaperson)|true|none|個人情報。phone_noはメイン番号、phone_no_mobileは携帯番号、phone_no_otherはその他の電話番号。emailはメインメールアドレス、email_subは予備のメールアドレス(Personal information.Phone_no is the main number,phone_no_mobile is the mobile number,phone_no_other is the other phone number.email is the main email address,email_sub is the spare email address.)|
|reserved_by|[Person](#schemaperson)|false|none|個人情報。phone_noはメイン番号、phone_no_mobileは携帯番号、phone_no_otherはその他の電話番号。emailはメインメールアドレス、email_subは予備のメールアドレス(Personal information.Phone_no is the main number,phone_no_mobile is the mobile number,phone_no_other is the other phone number.email is the main email address,email_sub is the spare email address.)|
|room_reservations|[[RoomReservationCreateRequest](#schemaroomreservationcreaterequest)]|true|none|[Model for a room reservation.If there is no email, use the phone number to look up the customernumber]|
|is_group|boolean|true|none|none|
|marketing_area_code|string|true|none|none|

<h2 id="tocS_RoomReservationCreateRequest">RoomReservationCreateRequest</h2>
<!-- backwards compatibility -->
<a id="schemaroomreservationcreaterequest"></a>
<a id="schema_RoomReservationCreateRequest"></a>
<a id="tocSroomreservationcreaterequest"></a>
<a id="tocsroomreservationcreaterequest"></a>

```json
{
  "room_number": "string",
  "guests": [
    {
      "person": {
        "kana_name": "string",
        "name": "string",
        "address": {
          "postal_code": "string",
          "prefecture_code": "string",
          "city": "string",
          "address_line": [
            "string"
          ]
        },
        "phone_no": "000-0000-0000",
        "phone_no_mobile": "000-0000-0000",
        "phone_no_other": "000-0000-0000",
        "gender": "Male",
        "birthday": "2019-08-24",
        "email": "example@example.com",
        "email_sub": "example@example.com",
        "external_customer_Id": "string"
      },
      "remarks": [
        {
          "system_user_company_id": "strin",
          "customer_number": "string",
          "customer_remark_id": "string",
          "importance_level_id": "PrimaryRemark",
          "facility_id": "strin",
          "date": "2019-08-24",
          "division": {
            "id": "str",
            "name": "string",
            "group_id": "str"
          },
          "type": {
            "id": "str",
            "name": "string"
          },
          "interlock_system_id": "str",
          "content": "string",
          "subject": "string",
          "output_timing": true,
          "youcom_hotel": {
            "id": "strin",
            "name": "string"
          },
          "youcom_sequence": 0,
          "create_info": {
            "host_name": "string",
            "time_stamp": "2019-08-24T14:15:22Z",
            "user_account_id": "string"
          },
          "change_info": {
            "host_name": "string",
            "time_stamp": "2019-08-24T14:15:22Z",
            "user_account_id": "string"
          }
        }
      ],
      "remak": [
        {
          "system_user_company_id": "strin",
          "customer_number": "string",
          "customer_remark_id": "string",
          "importance_level_id": "PrimaryRemark",
          "facility_id": "strin",
          "date": "2019-08-24",
          "division": {
            "id": "str",
            "name": "string",
            "group_id": "str"
          },
          "type": {
            "id": "str",
            "name": "string"
          },
          "interlock_system_id": "str",
          "content": "string",
          "subject": "string",
          "output_timing": true,
          "youcom_hotel": {
            "id": "strin",
            "name": "string"
          },
          "youcom_sequence": 0,
          "create_info": {
            "host_name": "string",
            "time_stamp": "2019-08-24T14:15:22Z",
            "user_account_id": "string"
          },
          "change_info": {
            "host_name": "string",
            "time_stamp": "2019-08-24T14:15:22Z",
            "user_account_id": "string"
          }
        }
      ],
      "id": "string",
      "customer_number": "string"
    }
  ],
  "room_type_id": "string",
  "sales_control_type": "FREE",
  "sales_control_unit": "string",
  "extra_bed_count": 0,
  "stay_period": {
    "arrival_date": "2019-08-24",
    "arrival_time": "14:15:22Z",
    "departure_date": "2019-08-24",
    "departure_time": "14:15:22Z",
    "late_out": true
  },
  "reservation_routes": [
    "string"
  ],
  "agent_course": "string",
  "person_count": [
    0
  ],
  "external_agent": {
    "external_agent_type": "TLL",
    "external_agent_code": "string",
    "external_agent_course_name": "string",
    "external_meal_type": "string",
    "external_room_type_id": "string",
    "external_facility_code": "string"
  },
  "agent_reservation_number": "string",
  "price_changes": [
    {
      "date_range_end": "2019-08-24",
      "date_range_start": "2019-08-24",
      "prices": [
        {
          "discount_amount": 0,
          "discount_item_id": "string",
          "discount_item_name": "string",
          "discount_rate": 0,
          "person_count": [
            0
          ],
          "person_count_price_calc": 0,
          "price": 0,
          "pricing_type": "GROSS",
          "rate_id": "string",
          "room_type_code": "string",
          "sales_package_id": "string",
          "sales_package_name": "string"
        }
      ]
    }
  ]
}

```

New Room Reservation

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|room_number|string|false|none|none|
|guests|[[Guest](#schemaguest)]|true|none|[Model for a guest]|
|room_type_id|string|true|none|none|
|sales_control_type|string|true|none|none|
|sales_control_unit|string|true|none|none|
|extra_bed_count|integer|false|none|none|
|stay_period|[StayPeriod](#schemastayperiod)|true|none|none|
|reservation_routes|[string]|true|none|none|
|agent_course|string|false|none|none|
|person_count|[PersonCount](#schemapersoncount)|true|none|none|
|external_agent|[ExternalAgent](#schemaexternalagent)|false|none|Returns an error package if it cannot be converted|
|agent_reservation_number|string|false|none|none|
|price_changes|[[PriceChangeReservation](#schemapricechangereservation)]|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|sales_control_type|FREE|
|sales_control_type|AGENT|
|sales_control_type|BLOCK|
|sales_control_type|WAITING|
|sales_control_type|OOO|
|sales_control_type|TENTATIVE|

<h2 id="tocS_ApiReservationPutRequest">ApiReservationPutRequest</h2>
<!-- backwards compatibility -->
<a id="schemaapireservationputrequest"></a>
<a id="schema_ApiReservationPutRequest"></a>
<a id="tocSapireservationputrequest"></a>
<a id="tocsapireservationputrequest"></a>

```json
{
  "reservation": {
    "main_guest": {
      "person": {
        "kana_name": "string",
        "name": "string",
        "address": {
          "postal_code": "string",
          "prefecture_code": "string",
          "city": "string",
          "address_line": [
            "string"
          ]
        },
        "phone_no": "000-0000-0000",
        "phone_no_mobile": "000-0000-0000",
        "phone_no_other": "000-0000-0000",
        "gender": "Male",
        "birthday": "2019-08-24",
        "email": "example@example.com",
        "email_sub": "example@example.com",
        "external_customer_Id": "string"
      },
      "remarks": [
        {
          "system_user_company_id": "strin",
          "customer_number": "string",
          "customer_remark_id": "string",
          "importance_level_id": "PrimaryRemark",
          "facility_id": "strin",
          "date": "2019-08-24",
          "division": {
            "id": "str",
            "name": "string",
            "group_id": "str"
          },
          "type": {
            "id": "str",
            "name": "string"
          },
          "interlock_system_id": "str",
          "content": "string",
          "subject": "string",
          "output_timing": true,
          "youcom_hotel": {
            "id": "strin",
            "name": "string"
          },
          "youcom_sequence": 0,
          "create_info": {
            "host_name": "string",
            "time_stamp": "2019-08-24T14:15:22Z",
            "user_account_id": "string"
          },
          "change_info": {
            "host_name": "string",
            "time_stamp": "2019-08-24T14:15:22Z",
            "user_account_id": "string"
          }
        }
      ],
      "remak": [
        {
          "system_user_company_id": "strin",
          "customer_number": "string",
          "customer_remark_id": "string",
          "importance_level_id": "PrimaryRemark",
          "facility_id": "strin",
          "date": "2019-08-24",
          "division": {
            "id": "str",
            "name": "string",
            "group_id": "str"
          },
          "type": {
            "id": "str",
            "name": "string"
          },
          "interlock_system_id": "str",
          "content": "string",
          "subject": "string",
          "output_timing": true,
          "youcom_hotel": {
            "id": "strin",
            "name": "string"
          },
          "youcom_sequence": 0,
          "create_info": {
            "host_name": "string",
            "time_stamp": "2019-08-24T14:15:22Z",
            "user_account_id": "string"
          },
          "change_info": {
            "host_name": "string",
            "time_stamp": "2019-08-24T14:15:22Z",
            "user_account_id": "string"
          }
        }
      ],
      "id": "string",
      "customer_number": "string"
    },
    "reserved_by": {
      "person": {
        "kana_name": "string",
        "name": "string",
        "address": {
          "postal_code": "string",
          "prefecture_code": "string",
          "city": "string",
          "address_line": [
            "string"
          ]
        },
        "phone_no": "000-0000-0000",
        "phone_no_mobile": "000-0000-0000",
        "phone_no_other": "000-0000-0000",
        "gender": "Male",
        "birthday": "2019-08-24",
        "email": "example@example.com",
        "email_sub": "example@example.com",
        "external_customer_Id": "string"
      },
      "remarks": [
        {
          "system_user_company_id": "strin",
          "customer_number": "string",
          "customer_remark_id": "string",
          "importance_level_id": "PrimaryRemark",
          "facility_id": "strin",
          "date": "2019-08-24",
          "division": {
            "id": "str",
            "name": "string",
            "group_id": "str"
          },
          "type": {
            "id": "str",
            "name": "string"
          },
          "interlock_system_id": "str",
          "content": "string",
          "subject": "string",
          "output_timing": true,
          "youcom_hotel": {
            "id": "strin",
            "name": "string"
          },
          "youcom_sequence": 0,
          "create_info": {
            "host_name": "string",
            "time_stamp": "2019-08-24T14:15:22Z",
            "user_account_id": "string"
          },
          "change_info": {
            "host_name": "string",
            "time_stamp": "2019-08-24T14:15:22Z",
            "user_account_id": "string"
          }
        }
      ],
      "remak": [
        {
          "system_user_company_id": "strin",
          "customer_number": "string",
          "customer_remark_id": "string",
          "importance_level_id": "PrimaryRemark",
          "facility_id": "strin",
          "date": "2019-08-24",
          "division": {
            "id": "str",
            "name": "string",
            "group_id": "str"
          },
          "type": {
            "id": "str",
            "name": "string"
          },
          "interlock_system_id": "str",
          "content": "string",
          "subject": "string",
          "output_timing": true,
          "youcom_hotel": {
            "id": "strin",
            "name": "string"
          },
          "youcom_sequence": 0,
          "create_info": {
            "host_name": "string",
            "time_stamp": "2019-08-24T14:15:22Z",
            "user_account_id": "string"
          },
          "change_info": {
            "host_name": "string",
            "time_stamp": "2019-08-24T14:15:22Z",
            "user_account_id": "string"
          }
        }
      ],
      "id": "string",
      "customer_number": "string"
    },
    "is_group": true,
    "marketing_area_code": "string"
  }
}

```

ApiReservationPutRequest

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|reservation|[ReservationUpdateRequest](#schemareservationupdaterequest)|false|none|Describes reservation details for a guest|

<h2 id="tocS_ReservationUpdateRequest">ReservationUpdateRequest</h2>
<!-- backwards compatibility -->
<a id="schemareservationupdaterequest"></a>
<a id="schema_ReservationUpdateRequest"></a>
<a id="tocSreservationupdaterequest"></a>
<a id="tocsreservationupdaterequest"></a>

```json
{
  "main_guest": {
    "person": {
      "kana_name": "string",
      "name": "string",
      "address": {
        "postal_code": "string",
        "prefecture_code": "string",
        "city": "string",
        "address_line": [
          "string"
        ]
      },
      "phone_no": "000-0000-0000",
      "phone_no_mobile": "000-0000-0000",
      "phone_no_other": "000-0000-0000",
      "gender": "Male",
      "birthday": "2019-08-24",
      "email": "example@example.com",
      "email_sub": "example@example.com",
      "external_customer_Id": "string"
    },
    "remarks": [
      {
        "system_user_company_id": "strin",
        "customer_number": "string",
        "customer_remark_id": "string",
        "importance_level_id": "PrimaryRemark",
        "facility_id": "strin",
        "date": "2019-08-24",
        "division": {
          "id": "str",
          "name": "string",
          "group_id": "str"
        },
        "type": {
          "id": "str",
          "name": "string"
        },
        "interlock_system_id": "str",
        "content": "string",
        "subject": "string",
        "output_timing": true,
        "youcom_hotel": {
          "id": "strin",
          "name": "string"
        },
        "youcom_sequence": 0,
        "create_info": {
          "host_name": "string",
          "time_stamp": "2019-08-24T14:15:22Z",
          "user_account_id": "string"
        },
        "change_info": {
          "host_name": "string",
          "time_stamp": "2019-08-24T14:15:22Z",
          "user_account_id": "string"
        }
      }
    ],
    "remak": [
      {
        "system_user_company_id": "strin",
        "customer_number": "string",
        "customer_remark_id": "string",
        "importance_level_id": "PrimaryRemark",
        "facility_id": "strin",
        "date": "2019-08-24",
        "division": {
          "id": "str",
          "name": "string",
          "group_id": "str"
        },
        "type": {
          "id": "str",
          "name": "string"
        },
        "interlock_system_id": "str",
        "content": "string",
        "subject": "string",
        "output_timing": true,
        "youcom_hotel": {
          "id": "strin",
          "name": "string"
        },
        "youcom_sequence": 0,
        "create_info": {
          "host_name": "string",
          "time_stamp": "2019-08-24T14:15:22Z",
          "user_account_id": "string"
        },
        "change_info": {
          "host_name": "string",
          "time_stamp": "2019-08-24T14:15:22Z",
          "user_account_id": "string"
        }
      }
    ],
    "id": "string",
    "customer_number": "string"
  },
  "reserved_by": {
    "person": {
      "kana_name": "string",
      "name": "string",
      "address": {
        "postal_code": "string",
        "prefecture_code": "string",
        "city": "string",
        "address_line": [
          "string"
        ]
      },
      "phone_no": "000-0000-0000",
      "phone_no_mobile": "000-0000-0000",
      "phone_no_other": "000-0000-0000",
      "gender": "Male",
      "birthday": "2019-08-24",
      "email": "example@example.com",
      "email_sub": "example@example.com",
      "external_customer_Id": "string"
    },
    "remarks": [
      {
        "system_user_company_id": "strin",
        "customer_number": "string",
        "customer_remark_id": "string",
        "importance_level_id": "PrimaryRemark",
        "facility_id": "strin",
        "date": "2019-08-24",
        "division": {
          "id": "str",
          "name": "string",
          "group_id": "str"
        },
        "type": {
          "id": "str",
          "name": "string"
        },
        "interlock_system_id": "str",
        "content": "string",
        "subject": "string",
        "output_timing": true,
        "youcom_hotel": {
          "id": "strin",
          "name": "string"
        },
        "youcom_sequence": 0,
        "create_info": {
          "host_name": "string",
          "time_stamp": "2019-08-24T14:15:22Z",
          "user_account_id": "string"
        },
        "change_info": {
          "host_name": "string",
          "time_stamp": "2019-08-24T14:15:22Z",
          "user_account_id": "string"
        }
      }
    ],
    "remak": [
      {
        "system_user_company_id": "strin",
        "customer_number": "string",
        "customer_remark_id": "string",
        "importance_level_id": "PrimaryRemark",
        "facility_id": "strin",
        "date": "2019-08-24",
        "division": {
          "id": "str",
          "name": "string",
          "group_id": "str"
        },
        "type": {
          "id": "str",
          "name": "string"
        },
        "interlock_system_id": "str",
        "content": "string",
        "subject": "string",
        "output_timing": true,
        "youcom_hotel": {
          "id": "strin",
          "name": "string"
        },
        "youcom_sequence": 0,
        "create_info": {
          "host_name": "string",
          "time_stamp": "2019-08-24T14:15:22Z",
          "user_account_id": "string"
        },
        "change_info": {
          "host_name": "string",
          "time_stamp": "2019-08-24T14:15:22Z",
          "user_account_id": "string"
        }
      }
    ],
    "id": "string",
    "customer_number": "string"
  },
  "is_group": true,
  "marketing_area_code": "string"
}

```

ReservationUpdateRequest

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|main_guest|[Guest](#schemaguest)|false|none|Model for a guest|
|reserved_by|[Guest](#schemaguest)|false|none|Model for a guest|
|is_group|boolean|true|none|none|
|marketing_area_code|string|true|none|none|

<h2 id="tocS_ApiRoomReservationsResponse">ApiRoomReservationsResponse</h2>
<!-- backwards compatibility -->
<a id="schemaapiroomreservationsresponse"></a>
<a id="schema_ApiRoomReservationsResponse"></a>
<a id="tocSapiroomreservationsresponse"></a>
<a id="tocsapiroomreservationsresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "room_reservation": [
    {
      "id": "string",
      "stay_registration_id ": "string",
      "room_number": "string",
      "room_status": "Vacant",
      "guests": [
        {
          "person": {
            "kana_name": "string",
            "name": "string",
            "address": {
              "postal_code": "string",
              "prefecture_code": "string",
              "city": "string",
              "address_line": [
                "string"
              ]
            },
            "phone_no": "000-0000-0000",
            "phone_no_mobile": "000-0000-0000",
            "phone_no_other": "000-0000-0000",
            "gender": "Male",
            "birthday": "2019-08-24",
            "email": "example@example.com",
            "email_sub": "example@example.com",
            "external_customer_Id": "string"
          },
          "remarks": [
            {
              "system_user_company_id": "strin",
              "customer_number": "string",
              "customer_remark_id": "string",
              "importance_level_id": "PrimaryRemark",
              "facility_id": "strin",
              "date": "2019-08-24",
              "division": {
                "id": "str",
                "name": "string",
                "group_id": "str"
              },
              "type": {
                "id": "str",
                "name": "string"
              },
              "interlock_system_id": "str",
              "content": "string",
              "subject": "string",
              "output_timing": true,
              "youcom_hotel": {
                "id": "strin",
                "name": "string"
              },
              "youcom_sequence": 0,
              "create_info": {
                "host_name": "string",
                "time_stamp": "2019-08-24T14:15:22Z",
                "user_account_id": "string"
              },
              "change_info": {
                "host_name": "string",
                "time_stamp": "2019-08-24T14:15:22Z",
                "user_account_id": "string"
              }
            }
          ],
          "remak": [
            {
              "system_user_company_id": "strin",
              "customer_number": "string",
              "customer_remark_id": "string",
              "importance_level_id": "PrimaryRemark",
              "facility_id": "strin",
              "date": "2019-08-24",
              "division": {
                "id": "str",
                "name": "string",
                "group_id": "str"
              },
              "type": {
                "id": "str",
                "name": "string"
              },
              "interlock_system_id": "str",
              "content": "string",
              "subject": "string",
              "output_timing": true,
              "youcom_hotel": {
                "id": "strin",
                "name": "string"
              },
              "youcom_sequence": 0,
              "create_info": {
                "host_name": "string",
                "time_stamp": "2019-08-24T14:15:22Z",
                "user_account_id": "string"
              },
              "change_info": {
                "host_name": "string",
                "time_stamp": "2019-08-24T14:15:22Z",
                "user_account_id": "string"
              }
            }
          ],
          "id": "string",
          "customer_number": "string"
        }
      ],
      "room_type": {
        "code": "string",
        "standard_persons": 0,
        "max_persons": 0,
        "name": "string",
        "short_name": "string",
        "kana_name": "string",
        "foreign_name": "string",
        "foreign_short_name": "string"
      },
      "sales_control_type": "FREE",
      "sales_control_unit": "string",
      "extra_bed_count": 0,
      "stay_period": {
        "arrival_date": "2019-08-24",
        "arrival_time": "14:15:22Z",
        "departure_date": "2019-08-24",
        "departure_time": "14:15:22Z",
        "late_out": true
      },
      "reservation_route": {
        "reservationDisplayName": "string",
        "reservationRoutes": [
          {
            "code": "string",
            "name": "string",
            "short_name": "string",
            "kana_name": "string",
            "foreign_name": "string",
            "foreign_short_name": "string"
          }
        ]
      },
      "agent_reservation_number": "string",
      "agent_course": "string",
      "person_count": [
        0
      ],
      "pricing": {
        "sales_package": {
          "code": "string",
          "name": "string",
          "short_name": "string",
          "kana_name": "string",
          "foreign_name": "string",
          "foreign_short_name": "string",
          "print_name": "string",
          "print_foreign_name": "string"
        },
        "discount_item": {
          "code": "string",
          "name": "string",
          "short_name": "string",
          "kana_name": "string",
          "foreign_name": "string",
          "foreign_short_name": "string",
          "rate": 0,
          "amount": 0
        },
        "discount_rate": 100,
        "discount_amount": 0,
        "pricing_type": "GROSS",
        "price": 0
      },
      "provision_requests": [
        {
          "id": "string",
          "provision": {
            "code": "string",
            "name": "string",
            "short_name": "string",
            "kana_name": "string",
            "foreign_name": "string",
            "foreign_short_name": "string"
          },
          "from_date": "2019-08-24",
          "to_date": "2019-08-24",
          "stock_control": true,
          "quantity": 0,
          "note": "string",
          "reservation_ref": {
            "reservation_id": "string",
            "room_id": "string",
            "stay_id": "string",
            "reservation_number": "string",
            "room_number": "string"
          }
        }
      ],
      "meal_reservations": [
        {
          "id": "string",
          "meal_place": {
            "id": "string",
            "name": "string",
            "short_name": "string",
            "kana_name": "string",
            "foreign_name": "string",
            "foreign_short_name": "string"
          },
          "meal_type": {
            "id": "string",
            "meal_place_code": "string",
            "meal_time_code": "string",
            "start_time": "14:15:22Z",
            "end_time": "14:15:22Z",
            "person_count": 0,
            "table_count": 0
          },
          "meal_time_frame": {
            "id": "string",
            "name": "string",
            "short_name": "string",
            "kana_name": "string",
            "foreign_name": "string",
            "foreign_short_name": "string"
          },
          "use_date": "2019-08-24",
          "meal_kana_name": "string",
          "meal_name": "string",
          "meal_short_name": "string",
          "meal_item": {
            "code": "string",
            "name": "string",
            "short_name": "string",
            "kana_name": "string",
            "foreign_name": "string",
            "foreign_short_name": "string"
          },
          "person_count": 0,
          "person_type": "ADULT",
          "unit_price": 0,
          "pricing_type": "INCLUDED",
          "start_time": "14:15:22Z",
          "end_time": "14:15:22Z",
          "valid": true,
          "note": "string",
          "reservation_ref": {
            "reservation_id": "string",
            "room_id": "string",
            "stay_id": "string",
            "reservation_number": "string",
            "room_number": "string"
          }
        }
      ],
      "deposits": [
        {
          "id": "string",
          "account_date": "2019-08-24",
          "payment_method": {
            "code": "string",
            "name": "string",
            "short_name": "string",
            "kana_name": "string",
            "foreign_name": "string",
            "foreign_short_name": "string",
            "use_address": true
          },
          "billing_provider": {
            "code": "string",
            "name": "string",
            "short_name": "string",
            "kana_name": "string",
            "foreign_name": "string",
            "foreign_short_name": "string"
          },
          "amount": 0,
          "bill_index": 0,
          "bill_note": "string",
          "internal_note": "string",
          "provider_reference": "string",
          "reservation_ref": {
            "reservation_id": "string",
            "room_id": "string",
            "stay_id": "string",
            "reservation_number": "string",
            "room_number": "string"
          }
        }
      ],
      "slip_items": [
        {
          "id": "string",
          "date": "2019-08-24",
          "item": {
            "code": "string",
            "name": "string",
            "short_name": "string",
            "kana_name": "string",
            "foreign_name": "string",
            "price": 0
          },
          "price_per_item": 0,
          "quantity": 0,
          "total_price": 0,
          "bill_index": 0,
          "bill_note": "string",
          "internal_note": "string",
          "tax_free": true,
          "room_type": {
            "code": "string",
            "standard_persons": 0,
            "max_persons": 0,
            "name": "string",
            "short_name": "string",
            "kana_name": "string",
            "foreign_name": "string",
            "foreign_short_name": "string"
          },
          "reservation_ref": {
            "reservation_id": "string",
            "room_id": "string",
            "stay_id": "string",
            "reservation_number": "string",
            "room_number": "string"
          }
        }
      ],
      "extra_services": [
        {
          "id": "string",
          "service_item": {
            "code": "string",
            "name": "string",
            "kana_name": "string",
            "short_name": "string",
            "foreign_name": "string",
            "foreign_short_name": "string"
          },
          "service_period": {
            "arrival_date": "2019-08-24",
            "arrival_time": "14:15:22Z",
            "departure_date": "2019-08-24",
            "departure_time": "14:15:22Z",
            "late_out": true
          },
          "person_count": 0,
          "note": "string",
          "reservation_ref": {
            "reservation_id": "string",
            "room_id": "string",
            "stay_id": "string",
            "reservation_number": "string",
            "room_number": "string"
          }
        }
      ],
      "remarks": [
        {
          "id": "string",
          "division": {
            "id": "str",
            "name": "string",
            "group_id": "str"
          },
          "remarks_type": {
            "id": "str",
            "name": "string"
          },
          "importance_level": "Primary Remark",
          "subject": "string",
          "content": "string"
        }
      ],
      "price_changes": [
        {
          "date_range_end": "2019-08-24",
          "date_range_start": "2019-08-24",
          "prices": [
            {
              "discount_amount": 0,
              "discount_item_id": "string",
              "discount_item_name": "string",
              "discount_rate": 0,
              "person_count": [
                0
              ],
              "person_count_price_calc": 0,
              "price": 0,
              "pricing_type": "GROSS",
              "rate_id": "string",
              "room_type_code": "string",
              "sales_package_id": "string",
              "sales_package_name": "string"
            }
          ]
        }
      ]
    }
  ]
}

```

ApiRoomReservationsResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|request|[ApiCommonResponseRequest](#schemaapicommonresponserequest)|false|none|Request|
|request_id|[ApiCommonResponseRequestId](#schemaapicommonresponserequestid)|false|none|RequestId|
|next_cursor|[ApiCommonResponseNextCursor](#schemaapicommonresponsenextcursor)|false|none|Indicates the position of the next entity. If an entity less than a limit is returned by the current page of the result set, then Cursor value is null.|
|room_reservation|[[RoomReservation](#schemaroomreservation)]|false|none|[Model for a room reservation]|

<h2 id="tocS_ApiRoomReservationResponse">ApiRoomReservationResponse</h2>
<!-- backwards compatibility -->
<a id="schemaapiroomreservationresponse"></a>
<a id="schema_ApiRoomReservationResponse"></a>
<a id="tocSapiroomreservationresponse"></a>
<a id="tocsapiroomreservationresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "room_reservation": {
    "id": "string",
    "stay_registration_id ": "string",
    "room_number": "string",
    "room_status": "Vacant",
    "guests": [
      {
        "person": {
          "kana_name": "string",
          "name": "string",
          "address": {
            "postal_code": "string",
            "prefecture_code": "string",
            "city": "string",
            "address_line": [
              "string"
            ]
          },
          "phone_no": "000-0000-0000",
          "phone_no_mobile": "000-0000-0000",
          "phone_no_other": "000-0000-0000",
          "gender": "Male",
          "birthday": "2019-08-24",
          "email": "example@example.com",
          "email_sub": "example@example.com",
          "external_customer_Id": "string"
        },
        "remarks": [
          {
            "system_user_company_id": "strin",
            "customer_number": "string",
            "customer_remark_id": "string",
            "importance_level_id": "PrimaryRemark",
            "facility_id": "strin",
            "date": "2019-08-24",
            "division": {
              "id": "str",
              "name": "string",
              "group_id": "str"
            },
            "type": {
              "id": "str",
              "name": "string"
            },
            "interlock_system_id": "str",
            "content": "string",
            "subject": "string",
            "output_timing": true,
            "youcom_hotel": {
              "id": "strin",
              "name": "string"
            },
            "youcom_sequence": 0,
            "create_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            },
            "change_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            }
          }
        ],
        "remak": [
          {
            "system_user_company_id": "strin",
            "customer_number": "string",
            "customer_remark_id": "string",
            "importance_level_id": "PrimaryRemark",
            "facility_id": "strin",
            "date": "2019-08-24",
            "division": {
              "id": "str",
              "name": "string",
              "group_id": "str"
            },
            "type": {
              "id": "str",
              "name": "string"
            },
            "interlock_system_id": "str",
            "content": "string",
            "subject": "string",
            "output_timing": true,
            "youcom_hotel": {
              "id": "strin",
              "name": "string"
            },
            "youcom_sequence": 0,
            "create_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            },
            "change_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            }
          }
        ],
        "id": "string",
        "customer_number": "string"
      }
    ],
    "room_type": {
      "code": "string",
      "standard_persons": 0,
      "max_persons": 0,
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    },
    "sales_control_type": "FREE",
    "sales_control_unit": "string",
    "extra_bed_count": 0,
    "stay_period": {
      "arrival_date": "2019-08-24",
      "arrival_time": "14:15:22Z",
      "departure_date": "2019-08-24",
      "departure_time": "14:15:22Z",
      "late_out": true
    },
    "reservation_route": {
      "reservationDisplayName": "string",
      "reservationRoutes": [
        {
          "code": "string",
          "name": "string",
          "short_name": "string",
          "kana_name": "string",
          "foreign_name": "string",
          "foreign_short_name": "string"
        }
      ]
    },
    "agent_reservation_number": "string",
    "agent_course": "string",
    "person_count": [
      0
    ],
    "pricing": {
      "sales_package": {
        "code": "string",
        "name": "string",
        "short_name": "string",
        "kana_name": "string",
        "foreign_name": "string",
        "foreign_short_name": "string",
        "print_name": "string",
        "print_foreign_name": "string"
      },
      "discount_item": {
        "code": "string",
        "name": "string",
        "short_name": "string",
        "kana_name": "string",
        "foreign_name": "string",
        "foreign_short_name": "string",
        "rate": 0,
        "amount": 0
      },
      "discount_rate": 100,
      "discount_amount": 0,
      "pricing_type": "GROSS",
      "price": 0
    },
    "provision_requests": [
      {
        "id": "string",
        "provision": {
          "code": "string",
          "name": "string",
          "short_name": "string",
          "kana_name": "string",
          "foreign_name": "string",
          "foreign_short_name": "string"
        },
        "from_date": "2019-08-24",
        "to_date": "2019-08-24",
        "stock_control": true,
        "quantity": 0,
        "note": "string",
        "reservation_ref": {
          "reservation_id": "string",
          "room_id": "string",
          "stay_id": "string",
          "reservation_number": "string",
          "room_number": "string"
        }
      }
    ],
    "meal_reservations": [
      {
        "id": "string",
        "meal_place": {
          "id": "string",
          "name": "string",
          "short_name": "string",
          "kana_name": "string",
          "foreign_name": "string",
          "foreign_short_name": "string"
        },
        "meal_type": {
          "id": "string",
          "meal_place_code": "string",
          "meal_time_code": "string",
          "start_time": "14:15:22Z",
          "end_time": "14:15:22Z",
          "person_count": 0,
          "table_count": 0
        },
        "meal_time_frame": {
          "id": "string",
          "name": "string",
          "short_name": "string",
          "kana_name": "string",
          "foreign_name": "string",
          "foreign_short_name": "string"
        },
        "use_date": "2019-08-24",
        "meal_kana_name": "string",
        "meal_name": "string",
        "meal_short_name": "string",
        "meal_item": {
          "code": "string",
          "name": "string",
          "short_name": "string",
          "kana_name": "string",
          "foreign_name": "string",
          "foreign_short_name": "string"
        },
        "person_count": 0,
        "person_type": "ADULT",
        "unit_price": 0,
        "pricing_type": "INCLUDED",
        "start_time": "14:15:22Z",
        "end_time": "14:15:22Z",
        "valid": true,
        "note": "string",
        "reservation_ref": {
          "reservation_id": "string",
          "room_id": "string",
          "stay_id": "string",
          "reservation_number": "string",
          "room_number": "string"
        }
      }
    ],
    "deposits": [
      {
        "id": "string",
        "account_date": "2019-08-24",
        "payment_method": {
          "code": "string",
          "name": "string",
          "short_name": "string",
          "kana_name": "string",
          "foreign_name": "string",
          "foreign_short_name": "string",
          "use_address": true
        },
        "billing_provider": {
          "code": "string",
          "name": "string",
          "short_name": "string",
          "kana_name": "string",
          "foreign_name": "string",
          "foreign_short_name": "string"
        },
        "amount": 0,
        "bill_index": 0,
        "bill_note": "string",
        "internal_note": "string",
        "provider_reference": "string",
        "reservation_ref": {
          "reservation_id": "string",
          "room_id": "string",
          "stay_id": "string",
          "reservation_number": "string",
          "room_number": "string"
        }
      }
    ],
    "slip_items": [
      {
        "id": "string",
        "date": "2019-08-24",
        "item": {
          "code": "string",
          "name": "string",
          "short_name": "string",
          "kana_name": "string",
          "foreign_name": "string",
          "price": 0
        },
        "price_per_item": 0,
        "quantity": 0,
        "total_price": 0,
        "bill_index": 0,
        "bill_note": "string",
        "internal_note": "string",
        "tax_free": true,
        "room_type": {
          "code": "string",
          "standard_persons": 0,
          "max_persons": 0,
          "name": "string",
          "short_name": "string",
          "kana_name": "string",
          "foreign_name": "string",
          "foreign_short_name": "string"
        },
        "reservation_ref": {
          "reservation_id": "string",
          "room_id": "string",
          "stay_id": "string",
          "reservation_number": "string",
          "room_number": "string"
        }
      }
    ],
    "extra_services": [
      {
        "id": "string",
        "service_item": {
          "code": "string",
          "name": "string",
          "kana_name": "string",
          "short_name": "string",
          "foreign_name": "string",
          "foreign_short_name": "string"
        },
        "service_period": {
          "arrival_date": "2019-08-24",
          "arrival_time": "14:15:22Z",
          "departure_date": "2019-08-24",
          "departure_time": "14:15:22Z",
          "late_out": true
        },
        "person_count": 0,
        "note": "string",
        "reservation_ref": {
          "reservation_id": "string",
          "room_id": "string",
          "stay_id": "string",
          "reservation_number": "string",
          "room_number": "string"
        }
      }
    ],
    "remarks": [
      {
        "id": "string",
        "division": {
          "id": "str",
          "name": "string",
          "group_id": "str"
        },
        "remarks_type": {
          "id": "str",
          "name": "string"
        },
        "importance_level": "Primary Remark",
        "subject": "string",
        "content": "string"
      }
    ],
    "price_changes": [
      {
        "date_range_end": "2019-08-24",
        "date_range_start": "2019-08-24",
        "prices": [
          {
            "discount_amount": 0,
            "discount_item_id": "string",
            "discount_item_name": "string",
            "discount_rate": 0,
            "person_count": [
              0
            ],
            "person_count_price_calc": 0,
            "price": 0,
            "pricing_type": "GROSS",
            "rate_id": "string",
            "room_type_code": "string",
            "sales_package_id": "string",
            "sales_package_name": "string"
          }
        ]
      }
    ]
  }
}

```

ApiRoomReservationResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|request|[ApiCommonResponseRequest](#schemaapicommonresponserequest)|false|none|Request|
|request_id|[ApiCommonResponseRequestId](#schemaapicommonresponserequestid)|false|none|RequestId|
|room_reservation|[RoomReservation](#schemaroomreservation)|false|none|Model for a room reservation|

<h2 id="tocS_ApiRoomReservationPostRequest">ApiRoomReservationPostRequest</h2>
<!-- backwards compatibility -->
<a id="schemaapiroomreservationpostrequest"></a>
<a id="schema_ApiRoomReservationPostRequest"></a>
<a id="tocSapiroomreservationpostrequest"></a>
<a id="tocsapiroomreservationpostrequest"></a>

```json
{
  "room_reservation": {
    "room_number": "string",
    "guests": [
      {
        "person": {
          "kana_name": "string",
          "name": "string",
          "address": {
            "postal_code": "string",
            "prefecture_code": "string",
            "city": "string",
            "address_line": [
              "string"
            ]
          },
          "phone_no": "000-0000-0000",
          "phone_no_mobile": "000-0000-0000",
          "phone_no_other": "000-0000-0000",
          "gender": "Male",
          "birthday": "2019-08-24",
          "email": "example@example.com",
          "email_sub": "example@example.com",
          "external_customer_Id": "string"
        },
        "remarks": [
          {
            "system_user_company_id": "strin",
            "customer_number": "string",
            "customer_remark_id": "string",
            "importance_level_id": "PrimaryRemark",
            "facility_id": "strin",
            "date": "2019-08-24",
            "division": {
              "id": "str",
              "name": "string",
              "group_id": "str"
            },
            "type": {
              "id": "str",
              "name": "string"
            },
            "interlock_system_id": "str",
            "content": "string",
            "subject": "string",
            "output_timing": true,
            "youcom_hotel": {
              "id": "strin",
              "name": "string"
            },
            "youcom_sequence": 0,
            "create_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            },
            "change_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            }
          }
        ],
        "remak": [
          {
            "system_user_company_id": "strin",
            "customer_number": "string",
            "customer_remark_id": "string",
            "importance_level_id": "PrimaryRemark",
            "facility_id": "strin",
            "date": "2019-08-24",
            "division": {
              "id": "str",
              "name": "string",
              "group_id": "str"
            },
            "type": {
              "id": "str",
              "name": "string"
            },
            "interlock_system_id": "str",
            "content": "string",
            "subject": "string",
            "output_timing": true,
            "youcom_hotel": {
              "id": "strin",
              "name": "string"
            },
            "youcom_sequence": 0,
            "create_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            },
            "change_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            }
          }
        ],
        "id": "string",
        "customer_number": "string"
      }
    ],
    "room_type_id": "string",
    "sales_control_type": "FREE",
    "sales_control_unit": "string",
    "extra_bed_count": 0,
    "stay_period": {
      "arrival_date": "2019-08-24",
      "arrival_time": "14:15:22Z",
      "departure_date": "2019-08-24",
      "departure_time": "14:15:22Z",
      "late_out": true
    },
    "reservation_routes": [
      "string"
    ],
    "agent_course": "string",
    "person_count": [
      0
    ],
    "external_agent": {
      "external_agent_type": "TLL",
      "external_agent_code": "string",
      "external_agent_course_name": "string",
      "external_meal_type": "string",
      "external_room_type_id": "string",
      "external_facility_code": "string"
    },
    "agent_reservation_number": "string",
    "price_changes": [
      {
        "date_range_end": "2019-08-24",
        "date_range_start": "2019-08-24",
        "prices": [
          {
            "discount_amount": 0,
            "discount_item_id": "string",
            "discount_item_name": "string",
            "discount_rate": 0,
            "person_count": [
              0
            ],
            "person_count_price_calc": 0,
            "price": 0,
            "pricing_type": "GROSS",
            "rate_id": "string",
            "room_type_code": "string",
            "sales_package_id": "string",
            "sales_package_name": "string"
          }
        ]
      }
    ]
  }
}

```

ApiRoomReservationPostRequest

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|room_reservation|[RoomReservationCreateRequest](#schemaroomreservationcreaterequest)|false|none|Model for a room reservation.If there is no email, use the phone number to look up the customernumber|

<h2 id="tocS_ApiRoomReservationPutRequest">ApiRoomReservationPutRequest</h2>
<!-- backwards compatibility -->
<a id="schemaapiroomreservationputrequest"></a>
<a id="schema_ApiRoomReservationPutRequest"></a>
<a id="tocSapiroomreservationputrequest"></a>
<a id="tocsapiroomreservationputrequest"></a>

```json
{
  "room_reservation": {
    "room_number": "string",
    "guests": [
      {
        "person": {
          "kana_name": "string",
          "name": "string",
          "address": {
            "postal_code": "string",
            "prefecture_code": "string",
            "city": "string",
            "address_line": [
              "string"
            ]
          },
          "phone_no": "000-0000-0000",
          "phone_no_mobile": "000-0000-0000",
          "phone_no_other": "000-0000-0000",
          "gender": "Male",
          "birthday": "2019-08-24",
          "email": "example@example.com",
          "email_sub": "example@example.com",
          "external_customer_Id": "string"
        },
        "remarks": [
          {
            "system_user_company_id": "strin",
            "customer_number": "string",
            "customer_remark_id": "string",
            "importance_level_id": "PrimaryRemark",
            "facility_id": "strin",
            "date": "2019-08-24",
            "division": {
              "id": "str",
              "name": "string",
              "group_id": "str"
            },
            "type": {
              "id": "str",
              "name": "string"
            },
            "interlock_system_id": "str",
            "content": "string",
            "subject": "string",
            "output_timing": true,
            "youcom_hotel": {
              "id": "strin",
              "name": "string"
            },
            "youcom_sequence": 0,
            "create_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            },
            "change_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            }
          }
        ],
        "remak": [
          {
            "system_user_company_id": "strin",
            "customer_number": "string",
            "customer_remark_id": "string",
            "importance_level_id": "PrimaryRemark",
            "facility_id": "strin",
            "date": "2019-08-24",
            "division": {
              "id": "str",
              "name": "string",
              "group_id": "str"
            },
            "type": {
              "id": "str",
              "name": "string"
            },
            "interlock_system_id": "str",
            "content": "string",
            "subject": "string",
            "output_timing": true,
            "youcom_hotel": {
              "id": "strin",
              "name": "string"
            },
            "youcom_sequence": 0,
            "create_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            },
            "change_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            }
          }
        ],
        "id": "string",
        "customer_number": "string"
      }
    ],
    "extra_bed_count": 0,
    "room_type_code": "string",
    "sales_control_type": "FREE",
    "sales_control_unit": "string",
    "stay_period": {
      "arrival_date": "2019-08-24",
      "arrival_time": "14:15:22Z",
      "departure_date": "2019-08-24",
      "departure_time": "14:15:22Z",
      "late_out": true
    },
    "reservation_routes": [
      "string"
    ],
    "agent_course": "string",
    "person_count": [
      0
    ],
    "external_agent": {
      "external_agent_type": "TLL",
      "external_agent_code": "string",
      "external_agent_course_name": "string",
      "external_meal_type": "string",
      "external_room_type_id": "string",
      "external_facility_code": "string"
    },
    "agent_reservation_number": "string",
    "price_changes": [
      {
        "date_range_end": "2019-08-24",
        "date_range_start": "2019-08-24",
        "prices": [
          {
            "discount_amount": 0,
            "discount_item_id": "string",
            "discount_item_name": "string",
            "discount_rate": 0,
            "person_count": [
              0
            ],
            "person_count_price_calc": 0,
            "price": 0,
            "pricing_type": "GROSS",
            "rate_id": "string",
            "room_type_code": "string",
            "sales_package_id": "string",
            "sales_package_name": "string"
          }
        ]
      }
    ]
  }
}

```

ApiRoomReservationPutRequest

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|room_reservation|[RoomReservationUpdateRequest](#schemaroomreservationupdaterequest)|false|none|Model for a room reservation.If there is no email, use the phone number to look up the customernumber|

<h2 id="tocS_RoomReservationUpdateRequest">RoomReservationUpdateRequest</h2>
<!-- backwards compatibility -->
<a id="schemaroomreservationupdaterequest"></a>
<a id="schema_RoomReservationUpdateRequest"></a>
<a id="tocSroomreservationupdaterequest"></a>
<a id="tocsroomreservationupdaterequest"></a>

```json
{
  "room_number": "string",
  "guests": [
    {
      "person": {
        "kana_name": "string",
        "name": "string",
        "address": {
          "postal_code": "string",
          "prefecture_code": "string",
          "city": "string",
          "address_line": [
            "string"
          ]
        },
        "phone_no": "000-0000-0000",
        "phone_no_mobile": "000-0000-0000",
        "phone_no_other": "000-0000-0000",
        "gender": "Male",
        "birthday": "2019-08-24",
        "email": "example@example.com",
        "email_sub": "example@example.com",
        "external_customer_Id": "string"
      },
      "remarks": [
        {
          "system_user_company_id": "strin",
          "customer_number": "string",
          "customer_remark_id": "string",
          "importance_level_id": "PrimaryRemark",
          "facility_id": "strin",
          "date": "2019-08-24",
          "division": {
            "id": "str",
            "name": "string",
            "group_id": "str"
          },
          "type": {
            "id": "str",
            "name": "string"
          },
          "interlock_system_id": "str",
          "content": "string",
          "subject": "string",
          "output_timing": true,
          "youcom_hotel": {
            "id": "strin",
            "name": "string"
          },
          "youcom_sequence": 0,
          "create_info": {
            "host_name": "string",
            "time_stamp": "2019-08-24T14:15:22Z",
            "user_account_id": "string"
          },
          "change_info": {
            "host_name": "string",
            "time_stamp": "2019-08-24T14:15:22Z",
            "user_account_id": "string"
          }
        }
      ],
      "remak": [
        {
          "system_user_company_id": "strin",
          "customer_number": "string",
          "customer_remark_id": "string",
          "importance_level_id": "PrimaryRemark",
          "facility_id": "strin",
          "date": "2019-08-24",
          "division": {
            "id": "str",
            "name": "string",
            "group_id": "str"
          },
          "type": {
            "id": "str",
            "name": "string"
          },
          "interlock_system_id": "str",
          "content": "string",
          "subject": "string",
          "output_timing": true,
          "youcom_hotel": {
            "id": "strin",
            "name": "string"
          },
          "youcom_sequence": 0,
          "create_info": {
            "host_name": "string",
            "time_stamp": "2019-08-24T14:15:22Z",
            "user_account_id": "string"
          },
          "change_info": {
            "host_name": "string",
            "time_stamp": "2019-08-24T14:15:22Z",
            "user_account_id": "string"
          }
        }
      ],
      "id": "string",
      "customer_number": "string"
    }
  ],
  "extra_bed_count": 0,
  "room_type_code": "string",
  "sales_control_type": "FREE",
  "sales_control_unit": "string",
  "stay_period": {
    "arrival_date": "2019-08-24",
    "arrival_time": "14:15:22Z",
    "departure_date": "2019-08-24",
    "departure_time": "14:15:22Z",
    "late_out": true
  },
  "reservation_routes": [
    "string"
  ],
  "agent_course": "string",
  "person_count": [
    0
  ],
  "external_agent": {
    "external_agent_type": "TLL",
    "external_agent_code": "string",
    "external_agent_course_name": "string",
    "external_meal_type": "string",
    "external_room_type_id": "string",
    "external_facility_code": "string"
  },
  "agent_reservation_number": "string",
  "price_changes": [
    {
      "date_range_end": "2019-08-24",
      "date_range_start": "2019-08-24",
      "prices": [
        {
          "discount_amount": 0,
          "discount_item_id": "string",
          "discount_item_name": "string",
          "discount_rate": 0,
          "person_count": [
            0
          ],
          "person_count_price_calc": 0,
          "price": 0,
          "pricing_type": "GROSS",
          "rate_id": "string",
          "room_type_code": "string",
          "sales_package_id": "string",
          "sales_package_name": "string"
        }
      ]
    }
  ]
}

```

RoomReservationUpdateRequest

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|room_number|string|false|none|none|
|guests|[[Guest](#schemaguest)]|false|none|[Model for a guest]|
|extra_bed_count|integer|false|none|none|
|room_type_code|string|true|none|none|
|sales_control_type|string|true|none|none|
|sales_control_unit|string|true|none|none|
|stay_period|[StayPeriod](#schemastayperiod)|true|none|none|
|reservation_routes|[string]|true|none|none|
|agent_course|string|false|none|none|
|person_count|[PersonCount](#schemapersoncount)|true|none|none|
|external_agent|[ExternalAgent](#schemaexternalagent)|false|none|Returns an error package if it cannot be converted|
|agent_reservation_number|string|false|none|none|
|price_changes|[[PriceChangeReservation](#schemapricechangereservation)]|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|sales_control_type|FREE|
|sales_control_type|AGENT|
|sales_control_type|BLOCK|
|sales_control_type|WAITING|
|sales_control_type|OOO|
|sales_control_type|TENTATIVE|

<h2 id="tocS_ApiRemarksResponse">ApiRemarksResponse</h2>
<!-- backwards compatibility -->
<a id="schemaapiremarksresponse"></a>
<a id="schema_ApiRemarksResponse"></a>
<a id="tocSapiremarksresponse"></a>
<a id="tocsapiremarksresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "remark": [
    {
      "id": "string",
      "division": {
        "id": "str",
        "name": "string",
        "group_id": "str"
      },
      "remarks_type": {
        "id": "str",
        "name": "string"
      },
      "importance_level": "Primary Remark",
      "subject": "string",
      "content": "string"
    }
  ]
}

```

ApiRemarksResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|request|[ApiCommonResponseRequest](#schemaapicommonresponserequest)|false|none|Request|
|request_id|[ApiCommonResponseRequestId](#schemaapicommonresponserequestid)|false|none|RequestId|
|next_cursor|[ApiCommonResponseNextCursor](#schemaapicommonresponsenextcursor)|false|none|Indicates the position of the next entity. If an entity less than a limit is returned by the current page of the result set, then Cursor value is null.|
|remark|[[Remark](#schemaremark)]|false|none|[List of remarks]|

<h2 id="tocS_ApiRemarkResponse">ApiRemarkResponse</h2>
<!-- backwards compatibility -->
<a id="schemaapiremarkresponse"></a>
<a id="schema_ApiRemarkResponse"></a>
<a id="tocSapiremarkresponse"></a>
<a id="tocsapiremarkresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "remark": {
    "id": "string",
    "division": {
      "id": "str",
      "name": "string",
      "group_id": "str"
    },
    "remarks_type": {
      "id": "str",
      "name": "string"
    },
    "importance_level": "Primary Remark",
    "subject": "string",
    "content": "string"
  }
}

```

ApiRemarkResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|request|[ApiCommonResponseRequest](#schemaapicommonresponserequest)|false|none|Request|
|request_id|[ApiCommonResponseRequestId](#schemaapicommonresponserequestid)|false|none|RequestId|
|remark|[Remark](#schemaremark)|false|none|List of remarks|

<h2 id="tocS_ApiRemarkRequest">ApiRemarkRequest</h2>
<!-- backwards compatibility -->
<a id="schemaapiremarkrequest"></a>
<a id="schema_ApiRemarkRequest"></a>
<a id="tocSapiremarkrequest"></a>
<a id="tocsapiremarkrequest"></a>

```json
{
  "remark": {
    "importance_level": "Primary Remark",
    "subject": "string",
    "content": "string"
  }
}

```

ApiRemarkRequest

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|remark|[RemarkRequest](#schemaremarkrequest)|false|none|Set Remark|

<h2 id="tocS_RemarkRequest">RemarkRequest</h2>
<!-- backwards compatibility -->
<a id="schemaremarkrequest"></a>
<a id="schema_RemarkRequest"></a>
<a id="tocSremarkrequest"></a>
<a id="tocsremarkrequest"></a>

```json
{
  "importance_level": "Primary Remark",
  "subject": "string",
  "content": "string"
}

```

RemarkRequest

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|importance_level|string|true|none|none|
|subject|string|true|none|none|
|content|string|true|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|importance_level|Primary Remark|
|importance_level|High|
|importance_level|Standard|
|importance_level|Low|

<h2 id="tocS_ApiSlipReservationsResponse">ApiSlipReservationsResponse</h2>
<!-- backwards compatibility -->
<a id="schemaapislipreservationsresponse"></a>
<a id="schema_ApiSlipReservationsResponse"></a>
<a id="tocSapislipreservationsresponse"></a>
<a id="tocsapislipreservationsresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "slip_reservations": [
    {
      "id": "string",
      "date": "2019-08-24",
      "item": {
        "code": "string",
        "name": "string",
        "short_name": "string",
        "kana_name": "string",
        "foreign_name": "string",
        "price": 0
      },
      "price_per_item": 0,
      "quantity": 0,
      "total_price": 0,
      "bill_index": 0,
      "bill_note": "string",
      "internal_note": "string",
      "tax_free": true,
      "room_type": {
        "code": "string",
        "standard_persons": 0,
        "max_persons": 0,
        "name": "string",
        "short_name": "string",
        "kana_name": "string",
        "foreign_name": "string",
        "foreign_short_name": "string"
      },
      "reservation_ref": {
        "reservation_id": "string",
        "room_id": "string",
        "stay_id": "string",
        "reservation_number": "string",
        "room_number": "string"
      }
    }
  ]
}

```

ApiSlipReservationsResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|request|[ApiCommonResponseRequest](#schemaapicommonresponserequest)|false|none|Request|
|request_id|[ApiCommonResponseRequestId](#schemaapicommonresponserequestid)|false|none|RequestId|
|next_cursor|[ApiCommonResponseNextCursor](#schemaapicommonresponsenextcursor)|false|none|Indicates the position of the next entity. If an entity less than a limit is returned by the current page of the result set, then Cursor value is null.|
|slip_reservations|[[SlipReservation](#schemaslipreservation)]|false|none|none|

<h2 id="tocS_ApiSlipReservationPostRequest">ApiSlipReservationPostRequest</h2>
<!-- backwards compatibility -->
<a id="schemaapislipreservationpostrequest"></a>
<a id="schema_ApiSlipReservationPostRequest"></a>
<a id="tocSapislipreservationpostrequest"></a>
<a id="tocsapislipreservationpostrequest"></a>

```json
{
  "slip_reservation": {
    "date": "2019-08-24",
    "item_code": "string",
    "price_per_item": 0,
    "quantity": 0,
    "total_price": 0,
    "bill_index": 0,
    "bill_note": "string",
    "internal_note": "string",
    "tax_free": true,
    "room_type_code": "string"
  }
}

```

ApiSlipReservationPostRequest

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|slip_reservation|[SlipReservationRequest](#schemaslipreservationrequest)|false|none|none|

<h2 id="tocS_SlipReservationRequest">SlipReservationRequest</h2>
<!-- backwards compatibility -->
<a id="schemaslipreservationrequest"></a>
<a id="schema_SlipReservationRequest"></a>
<a id="tocSslipreservationrequest"></a>
<a id="tocsslipreservationrequest"></a>

```json
{
  "date": "2019-08-24",
  "item_code": "string",
  "price_per_item": 0,
  "quantity": 0,
  "total_price": 0,
  "bill_index": 0,
  "bill_note": "string",
  "internal_note": "string",
  "tax_free": true,
  "room_type_code": "string"
}

```

SlipReservationRequest

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|date|[Date](#schemadate)|true|none|日付(Date)|
|item_code|string|true|none|none|
|price_per_item|number|true|none|none|
|quantity|integer|true|none|none|
|total_price|number|true|none|none|
|bill_index|integer|false|none|none|
|bill_note|string|false|none|none|
|internal_note|string|false|none|none|
|tax_free|boolean|false|none|none|
|room_type_code|string|false|none|none|

<h2 id="tocS_ApiSlipReservationResponse">ApiSlipReservationResponse</h2>
<!-- backwards compatibility -->
<a id="schemaapislipreservationresponse"></a>
<a id="schema_ApiSlipReservationResponse"></a>
<a id="tocSapislipreservationresponse"></a>
<a id="tocsapislipreservationresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "slip_reservation": {
    "id": "string",
    "date": "2019-08-24",
    "item": {
      "code": "string",
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "price": 0
    },
    "price_per_item": 0,
    "quantity": 0,
    "total_price": 0,
    "bill_index": 0,
    "bill_note": "string",
    "internal_note": "string",
    "tax_free": true,
    "room_type": {
      "code": "string",
      "standard_persons": 0,
      "max_persons": 0,
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    },
    "reservation_ref": {
      "reservation_id": "string",
      "room_id": "string",
      "stay_id": "string",
      "reservation_number": "string",
      "room_number": "string"
    }
  }
}

```

ApiSlipReservationResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|request|[ApiCommonResponseRequest](#schemaapicommonresponserequest)|false|none|Request|
|request_id|[ApiCommonResponseRequestId](#schemaapicommonresponserequestid)|false|none|RequestId|
|next_cursor|[ApiCommonResponseNextCursor](#schemaapicommonresponsenextcursor)|false|none|Indicates the position of the next entity. If an entity less than a limit is returned by the current page of the result set, then Cursor value is null.|
|slip_reservation|[SlipReservation](#schemaslipreservation)|false|none|none|

<h2 id="tocS_ApiSlipReservationPutRequest">ApiSlipReservationPutRequest</h2>
<!-- backwards compatibility -->
<a id="schemaapislipreservationputrequest"></a>
<a id="schema_ApiSlipReservationPutRequest"></a>
<a id="tocSapislipreservationputrequest"></a>
<a id="tocsapislipreservationputrequest"></a>

```json
{
  "slip_reservation": {
    "date": "2019-08-24",
    "item_code": "string",
    "price_per_item": 0,
    "quantity": 0,
    "total_price": 0,
    "bill_index": 0,
    "bill_note": "string",
    "internal_note": "string",
    "tax_free": true,
    "room_type_code": "string"
  }
}

```

ApiSlipReservationPutRequest

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|slip_reservation|[SlipReservationRequest](#schemaslipreservationrequest)|false|none|none|

<h2 id="tocS_ApiDepositsResponse">ApiDepositsResponse</h2>
<!-- backwards compatibility -->
<a id="schemaapidepositsresponse"></a>
<a id="schema_ApiDepositsResponse"></a>
<a id="tocSapidepositsresponse"></a>
<a id="tocsapidepositsresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "deposits": [
    {
      "id": "string",
      "account_date": "2019-08-24",
      "payment_method": {
        "code": "string",
        "name": "string",
        "short_name": "string",
        "kana_name": "string",
        "foreign_name": "string",
        "foreign_short_name": "string",
        "use_address": true
      },
      "billing_provider": {
        "code": "string",
        "name": "string",
        "short_name": "string",
        "kana_name": "string",
        "foreign_name": "string",
        "foreign_short_name": "string"
      },
      "amount": 0,
      "bill_index": 0,
      "bill_note": "string",
      "internal_note": "string",
      "provider_reference": "string",
      "reservation_ref": {
        "reservation_id": "string",
        "room_id": "string",
        "stay_id": "string",
        "reservation_number": "string",
        "room_number": "string"
      }
    }
  ]
}

```

ApiDepositSlipReservationsResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|request|[ApiCommonResponseRequest](#schemaapicommonresponserequest)|false|none|Request|
|request_id|[ApiCommonResponseRequestId](#schemaapicommonresponserequestid)|false|none|RequestId|
|next_cursor|[ApiCommonResponseNextCursor](#schemaapicommonresponsenextcursor)|false|none|Indicates the position of the next entity. If an entity less than a limit is returned by the current page of the result set, then Cursor value is null.|
|deposits|[[Deposit](#schemadeposit)]|false|none|none|

<h2 id="tocS_ApiDepositPostRequest">ApiDepositPostRequest</h2>
<!-- backwards compatibility -->
<a id="schemaapidepositpostrequest"></a>
<a id="schema_ApiDepositPostRequest"></a>
<a id="tocSapidepositpostrequest"></a>
<a id="tocsapidepositpostrequest"></a>

```json
{
  "deposit": {
    "account_date": "2019-08-24",
    "payment_method_code": "string",
    "billing_provider_code": "string",
    "amount": 0,
    "bill_index": 0,
    "bill_note": "string",
    "internal_note": "string",
    "provider_reference": "string"
  }
}

```

ApiDepositPostRequest

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|deposit|[DepositRequest](#schemadepositrequest)|false|none|none|

<h2 id="tocS_DepositRequest">DepositRequest</h2>
<!-- backwards compatibility -->
<a id="schemadepositrequest"></a>
<a id="schema_DepositRequest"></a>
<a id="tocSdepositrequest"></a>
<a id="tocsdepositrequest"></a>

```json
{
  "account_date": "2019-08-24",
  "payment_method_code": "string",
  "billing_provider_code": "string",
  "amount": 0,
  "bill_index": 0,
  "bill_note": "string",
  "internal_note": "string",
  "provider_reference": "string"
}

```

DepositRequest

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|account_date|[Date](#schemadate)|true|none|日付(Date)|
|payment_method_code|string|true|none|none|
|billing_provider_code|string|false|none|none|
|amount|number|true|none|none|
|bill_index|integer|false|none|none|
|bill_note|string|false|none|none|
|internal_note|string|false|none|none|
|provider_reference|string|false|none|none|

<h2 id="tocS_ApiDepositResponse">ApiDepositResponse</h2>
<!-- backwards compatibility -->
<a id="schemaapidepositresponse"></a>
<a id="schema_ApiDepositResponse"></a>
<a id="tocSapidepositresponse"></a>
<a id="tocsapidepositresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "deposit": {
    "id": "string",
    "account_date": "2019-08-24",
    "payment_method": {
      "code": "string",
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string",
      "use_address": true
    },
    "billing_provider": {
      "code": "string",
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    },
    "amount": 0,
    "bill_index": 0,
    "bill_note": "string",
    "internal_note": "string",
    "provider_reference": "string",
    "reservation_ref": {
      "reservation_id": "string",
      "room_id": "string",
      "stay_id": "string",
      "reservation_number": "string",
      "room_number": "string"
    }
  }
}

```

ApiDepositSlipReservation

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|request|[ApiCommonResponseRequest](#schemaapicommonresponserequest)|false|none|Request|
|request_id|[ApiCommonResponseRequestId](#schemaapicommonresponserequestid)|false|none|RequestId|
|next_cursor|[ApiCommonResponseNextCursor](#schemaapicommonresponsenextcursor)|false|none|Indicates the position of the next entity. If an entity less than a limit is returned by the current page of the result set, then Cursor value is null.|
|deposit|[Deposit](#schemadeposit)|false|none|none|

<h2 id="tocS_ApiDepositPutRequest">ApiDepositPutRequest</h2>
<!-- backwards compatibility -->
<a id="schemaapidepositputrequest"></a>
<a id="schema_ApiDepositPutRequest"></a>
<a id="tocSapidepositputrequest"></a>
<a id="tocsapidepositputrequest"></a>

```json
{
  "deposit": {
    "account_date": "2019-08-24",
    "payment_method_code": "string",
    "billing_provider_code": "string",
    "amount": 0,
    "bill_index": 0,
    "bill_note": "string",
    "internal_note": "string",
    "provider_reference": "string"
  }
}

```

ApiDepositPutRequest

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|deposit|[DepositRequest](#schemadepositrequest)|false|none|none|

<h2 id="tocS_ApiMealReservationPostRequest">ApiMealReservationPostRequest</h2>
<!-- backwards compatibility -->
<a id="schemaapimealreservationpostrequest"></a>
<a id="schema_ApiMealReservationPostRequest"></a>
<a id="tocSapimealreservationpostrequest"></a>
<a id="tocsapimealreservationpostrequest"></a>

```json
{
  "meal_reservation": {
    "date": "2019-08-24",
    "meal_place_code": "string",
    "meal_type_code": "string",
    "meal_time_frame_code": "string",
    "meal_item_code": "string",
    "person_count": 0,
    "person_type": "ADULT",
    "unit_price": 0,
    "pricing_type": "INCLUDED",
    "start_time": "14:15:22Z",
    "end_time": "14:15:22Z",
    "valid": true,
    "note": "string"
  }
}

```

ApiMealReservationPostRequest

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|meal_reservation|[MealReservationRequest](#schemamealreservationrequest)|false|none|Describes detailed meal information for a given guest.|

<h2 id="tocS_CreateExtraServiceReservationRequest">CreateExtraServiceReservationRequest</h2>
<!-- backwards compatibility -->
<a id="schemacreateextraservicereservationrequest"></a>
<a id="schema_CreateExtraServiceReservationRequest"></a>
<a id="tocScreateextraservicereservationrequest"></a>
<a id="tocscreateextraservicereservationrequest"></a>

```json
{
  "extra_reservation": {
    "service_item_code": "str",
    "note": "string",
    "service_period": {
      "arrival_date": "2019-08-24",
      "arrival_time": "14:15:22Z",
      "departure_date": "2019-08-24",
      "departure_time": "14:15:22Z",
      "late_out": true
    },
    "person_count": 0
  }
}

```

CreateExtraServiceReservationRequest

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[ApiCreateRequest](#schemaapicreaterequest)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» extra_reservation|[ExtraServiceReservationRequest](#schemaextraservicereservationrequest)|false|none|Describe details for an extra service|

<h2 id="tocS_CreateExtraServiceReservationResponse">CreateExtraServiceReservationResponse</h2>
<!-- backwards compatibility -->
<a id="schemacreateextraservicereservationresponse"></a>
<a id="schema_CreateExtraServiceReservationResponse"></a>
<a id="tocScreateextraservicereservationresponse"></a>
<a id="tocscreateextraservicereservationresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "extra_reservation": {
    "id": "string",
    "service_item": {
      "code": "string",
      "name": "string",
      "kana_name": "string",
      "short_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    },
    "service_period": {
      "arrival_date": "2019-08-24",
      "arrival_time": "14:15:22Z",
      "departure_date": "2019-08-24",
      "departure_time": "14:15:22Z",
      "late_out": true
    },
    "person_count": 0,
    "note": "string",
    "reservation_ref": {
      "reservation_id": "string",
      "room_id": "string",
      "stay_id": "string",
      "reservation_number": "string",
      "room_number": "string"
    }
  }
}

```

CreateExtraServiceReservationResponse

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[ApiCreateResponse](#schemaapicreateresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» extra_reservation|[ExtraServiceReservation](#schemaextraservicereservation)|false|none|Describe details for an extra service|

<h2 id="tocS_ApiProvisionRequestPostRequest">ApiProvisionRequestPostRequest</h2>
<!-- backwards compatibility -->
<a id="schemaapiprovisionrequestpostrequest"></a>
<a id="schema_ApiProvisionRequestPostRequest"></a>
<a id="tocSapiprovisionrequestpostrequest"></a>
<a id="tocsapiprovisionrequestpostrequest"></a>

```json
{
  "provision_request": {
    "provision_code": "string",
    "from_date": "2019-08-24",
    "to_date": "2019-08-24",
    "stock_control": true,
    "quantity": 0,
    "note": "string"
  }
}

```

ApiProvisionRequestPostRequest

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|provision_request|[ProvisionRequest](#schemaprovisionrequest)|false|none|Model for a provision request|

<h2 id="tocS_ApiRoomTypeGroupsResponse">ApiRoomTypeGroupsResponse</h2>
<!-- backwards compatibility -->
<a id="schemaapiroomtypegroupsresponse"></a>
<a id="schema_ApiRoomTypeGroupsResponse"></a>
<a id="tocSapiroomtypegroupsresponse"></a>
<a id="tocsapiroomtypegroupsresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "room_type_groups": [
    {
      "id": "string",
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foereign_name": "string",
      "foreign_short_name": "string"
    }
  ]
}

```

ApiRoomTypeGroups

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|request|[ApiCommonResponseRequest](#schemaapicommonresponserequest)|false|none|Request|
|request_id|[ApiCommonResponseRequestId](#schemaapicommonresponserequestid)|false|none|RequestId|
|next_cursor|[ApiCommonResponseNextCursor](#schemaapicommonresponsenextcursor)|false|none|Indicates the position of the next entity. If an entity less than a limit is returned by the current page of the result set, then Cursor value is null.|
|room_type_groups|[[RoomTypeGroup](#schemaroomtypegroup)]|false|none|[Model for room type group]|

<h2 id="tocS_ApiRoomTypesResponse">ApiRoomTypesResponse</h2>
<!-- backwards compatibility -->
<a id="schemaapiroomtypesresponse"></a>
<a id="schema_ApiRoomTypesResponse"></a>
<a id="tocSapiroomtypesresponse"></a>
<a id="tocsapiroomtypesresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "room_types": [
    {
      "code": "string",
      "standard_persons": 0,
      "max_persons": 0,
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    }
  ]
}

```

ApiRoomTypesResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|request|[ApiCommonResponseRequest](#schemaapicommonresponserequest)|false|none|Request|
|request_id|[ApiCommonResponseRequestId](#schemaapicommonresponserequestid)|false|none|RequestId|
|next_cursor|[ApiCommonResponseNextCursor](#schemaapicommonresponsenextcursor)|false|none|Indicates the position of the next entity. If an entity less than a limit is returned by the current page of the result set, then Cursor value is null.|
|room_types|[[RoomType](#schemaroomtype)]|false|none|[Model for a room type]|

<h2 id="tocS_ApiRoomsResponse">ApiRoomsResponse</h2>
<!-- backwards compatibility -->
<a id="schemaapiroomsresponse"></a>
<a id="schema_ApiRoomsResponse"></a>
<a id="tocSapiroomsresponse"></a>
<a id="tocsapiroomsresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "rooms": [
    {
      "room_number": "string",
      "floor_id": "string",
      "room_type": {
        "code": "string",
        "standard_persons": 0,
        "max_persons": 0,
        "name": "string",
        "short_name": "string",
        "kana_name": "string",
        "foreign_name": "string",
        "foreign_short_name": "string"
      },
      "vacant_days": 0,
      "stay_count": 0
    }
  ]
}

```

ApiRoomNumbersResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|request|[ApiCommonResponseRequest](#schemaapicommonresponserequest)|false|none|Request|
|request_id|[ApiCommonResponseRequestId](#schemaapicommonresponserequestid)|false|none|RequestId|
|next_cursor|[ApiCommonResponseNextCursor](#schemaapicommonresponsenextcursor)|false|none|Indicates the position of the next entity. If an entity less than a limit is returned by the current page of the result set, then Cursor value is null.|
|rooms|[[RoomNumber](#schemaroomnumber)]|false|none|[Model for room number]|

<h2 id="tocS_ApiSalesAccountItemResponse">ApiSalesAccountItemResponse</h2>
<!-- backwards compatibility -->
<a id="schemaapisalesaccountitemresponse"></a>
<a id="schema_ApiSalesAccountItemResponse"></a>
<a id="tocSapisalesaccountitemresponse"></a>
<a id="tocsapisalesaccountitemresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "sales_account_items": [
    {
      "id": "string",
      "mid_group_id": "string",
      "kana_nane": "string",
      "name": "string",
      "short_name": "string",
      "use": true,
      "consumption_tax_calc_type_id": "st",
      "consumption_tax_charge": true,
      "sequence": 0,
      "base_unit_price": 0,
      "unit_price_exclude_tax": 0,
      "tax_rate": 0
    }
  ]
}

```

SalesAccountItemResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|request|[ApiCommonResponseRequest](#schemaapicommonresponserequest)|false|none|Request|
|request_id|[ApiCommonResponseRequestId](#schemaapicommonresponserequestid)|false|none|RequestId|
|next_cursor|[ApiCommonResponseNextCursor](#schemaapicommonresponsenextcursor)|false|none|Indicates the position of the next entity. If an entity less than a limit is returned by the current page of the result set, then Cursor value is null.|
|sales_account_items|[[SalesAccountItem](#schemasalesaccountitem)]|false|none|[Model describing the account list item<br>]|

<h2 id="tocS_ApiSlipReservationItemsResponse">ApiSlipReservationItemsResponse</h2>
<!-- backwards compatibility -->
<a id="schemaapislipreservationitemsresponse"></a>
<a id="schema_ApiSlipReservationItemsResponse"></a>
<a id="tocSapislipreservationitemsresponse"></a>
<a id="tocsapislipreservationitemsresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "slip_items": [
    {
      "code": "string",
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "price": 0
    }
  ]
}

```

ApiSlipReservationItemsResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|request|[ApiCommonResponseRequest](#schemaapicommonresponserequest)|false|none|Request|
|request_id|[ApiCommonResponseRequestId](#schemaapicommonresponserequestid)|false|none|RequestId|
|next_cursor|[ApiCommonResponseNextCursor](#schemaapicommonresponsenextcursor)|false|none|Indicates the position of the next entity. If an entity less than a limit is returned by the current page of the result set, then Cursor value is null.|
|slip_items|[[SlipReservationItem](#schemaslipreservationitem)]|false|none|none|

<h2 id="tocS_ApiStaysResponse">ApiStaysResponse</h2>
<!-- backwards compatibility -->
<a id="schemaapistaysresponse"></a>
<a id="schema_ApiStaysResponse"></a>
<a id="tocSapistaysresponse"></a>
<a id="tocsapistaysresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "stays": [
    {
      "id ": "string",
      "reservation_number": "string",
      "check_in_date": "string",
      "check_out_date": "string",
      "room_sales_status": {
        "status": "Fix"
      },
      "control_status": {
        "status": "Reserve"
      },
      "person_count": [
        3,
        3,
        3,
        3,
        3,
        3
      ],
      "main_guest": {
        "person": {
          "kana_name": "string",
          "name": "string",
          "address": {
            "postal_code": "string",
            "prefecture_code": "string",
            "city": "string",
            "address_line": [
              "string"
            ]
          },
          "phone_no": "000-0000-0000",
          "phone_no_mobile": "000-0000-0000",
          "phone_no_other": "000-0000-0000",
          "gender": "Male",
          "birthday": "2019-08-24",
          "email": "example@example.com",
          "email_sub": "example@example.com",
          "external_customer_Id": "string"
        },
        "remarks": [
          {
            "system_user_company_id": "strin",
            "customer_number": "string",
            "customer_remark_id": "string",
            "importance_level_id": "PrimaryRemark",
            "facility_id": "strin",
            "date": "2019-08-24",
            "division": {
              "id": "str",
              "name": "string",
              "group_id": "str"
            },
            "type": {
              "id": "str",
              "name": "string"
            },
            "interlock_system_id": "str",
            "content": "string",
            "subject": "string",
            "output_timing": true,
            "youcom_hotel": {
              "id": "strin",
              "name": "string"
            },
            "youcom_sequence": 0,
            "create_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            },
            "change_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            }
          }
        ],
        "remak": [
          {
            "system_user_company_id": "strin",
            "customer_number": "string",
            "customer_remark_id": "string",
            "importance_level_id": "PrimaryRemark",
            "facility_id": "strin",
            "date": "2019-08-24",
            "division": {
              "id": "str",
              "name": "string",
              "group_id": "str"
            },
            "type": {
              "id": "str",
              "name": "string"
            },
            "interlock_system_id": "str",
            "content": "string",
            "subject": "string",
            "output_timing": true,
            "youcom_hotel": {
              "id": "strin",
              "name": "string"
            },
            "youcom_sequence": 0,
            "create_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            },
            "change_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            }
          }
        ],
        "id": "string",
        "customer_number": "string"
      },
      "reserved_by": {
        "person": {
          "kana_name": "string",
          "name": "string",
          "address": {
            "postal_code": "string",
            "prefecture_code": "string",
            "city": "string",
            "address_line": [
              "string"
            ]
          },
          "phone_no": "000-0000-0000",
          "phone_no_mobile": "000-0000-0000",
          "phone_no_other": "000-0000-0000",
          "gender": "Male",
          "birthday": "2019-08-24",
          "email": "example@example.com",
          "email_sub": "example@example.com",
          "external_customer_Id": "string"
        },
        "remarks": [
          {
            "system_user_company_id": "strin",
            "customer_number": "string",
            "customer_remark_id": "string",
            "importance_level_id": "PrimaryRemark",
            "facility_id": "strin",
            "date": "2019-08-24",
            "division": {
              "id": "str",
              "name": "string",
              "group_id": "str"
            },
            "type": {
              "id": "str",
              "name": "string"
            },
            "interlock_system_id": "str",
            "content": "string",
            "subject": "string",
            "output_timing": true,
            "youcom_hotel": {
              "id": "strin",
              "name": "string"
            },
            "youcom_sequence": 0,
            "create_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            },
            "change_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            }
          }
        ],
        "remak": [
          {
            "system_user_company_id": "strin",
            "customer_number": "string",
            "customer_remark_id": "string",
            "importance_level_id": "PrimaryRemark",
            "facility_id": "strin",
            "date": "2019-08-24",
            "division": {
              "id": "str",
              "name": "string",
              "group_id": "str"
            },
            "type": {
              "id": "str",
              "name": "string"
            },
            "interlock_system_id": "str",
            "content": "string",
            "subject": "string",
            "output_timing": true,
            "youcom_hotel": {
              "id": "strin",
              "name": "string"
            },
            "youcom_sequence": 0,
            "create_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            },
            "change_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            }
          }
        ],
        "id": "string",
        "customer_number": "string"
      },
      "remarks": [
        {
          "id": "string",
          "division": {
            "id": "str",
            "name": "string",
            "group_id": "str"
          },
          "remarks_type": {
            "id": "str",
            "name": "string"
          },
          "importance_level": "Primary Remark",
          "subject": "string",
          "content": "string"
        }
      ],
      "reservation_remarks": [
        {
          "id": "string",
          "division": {
            "id": "str",
            "name": "string",
            "group_id": "str"
          },
          "remarks_type": {
            "id": "str",
            "name": "string"
          },
          "importance_level": "Primary Remark",
          "subject": "string",
          "content": "string"
        }
      ],
      "room_reservation": {
        "id": "string",
        "stay_registration_id ": "string",
        "room_number": "string",
        "room_status": "Vacant",
        "guests": [
          {
            "person": {
              "kana_name": "string",
              "name": "string",
              "address": {
                "postal_code": "string",
                "prefecture_code": "string",
                "city": "string",
                "address_line": [
                  "string"
                ]
              },
              "phone_no": "000-0000-0000",
              "phone_no_mobile": "000-0000-0000",
              "phone_no_other": "000-0000-0000",
              "gender": "Male",
              "birthday": "2019-08-24",
              "email": "example@example.com",
              "email_sub": "example@example.com",
              "external_customer_Id": "string"
            },
            "remarks": [
              {
                "system_user_company_id": "strin",
                "customer_number": "string",
                "customer_remark_id": "string",
                "importance_level_id": "PrimaryRemark",
                "facility_id": "strin",
                "date": "2019-08-24",
                "division": {
                  "id": "str",
                  "name": "string",
                  "group_id": "str"
                },
                "type": {
                  "id": "str",
                  "name": "string"
                },
                "interlock_system_id": "str",
                "content": "string",
                "subject": "string",
                "output_timing": true,
                "youcom_hotel": {
                  "id": "strin",
                  "name": "string"
                },
                "youcom_sequence": 0,
                "create_info": {
                  "host_name": "string",
                  "time_stamp": "2019-08-24T14:15:22Z",
                  "user_account_id": "string"
                },
                "change_info": {
                  "host_name": "string",
                  "time_stamp": "2019-08-24T14:15:22Z",
                  "user_account_id": "string"
                }
              }
            ],
            "remak": [
              {
                "system_user_company_id": "strin",
                "customer_number": "string",
                "customer_remark_id": "string",
                "importance_level_id": "PrimaryRemark",
                "facility_id": "strin",
                "date": "2019-08-24",
                "division": {
                  "id": "str",
                  "name": "string",
                  "group_id": "str"
                },
                "type": {
                  "id": "str",
                  "name": "string"
                },
                "interlock_system_id": "str",
                "content": "string",
                "subject": "string",
                "output_timing": true,
                "youcom_hotel": {
                  "id": "strin",
                  "name": "string"
                },
                "youcom_sequence": 0,
                "create_info": {
                  "host_name": "string",
                  "time_stamp": "2019-08-24T14:15:22Z",
                  "user_account_id": "string"
                },
                "change_info": {
                  "host_name": "string",
                  "time_stamp": "2019-08-24T14:15:22Z",
                  "user_account_id": "string"
                }
              }
            ],
            "id": "string",
            "customer_number": "string"
          }
        ],
        "room_type": {
          "code": "string",
          "standard_persons": 0,
          "max_persons": 0,
          "name": "string",
          "short_name": "string",
          "kana_name": "string",
          "foreign_name": "string",
          "foreign_short_name": "string"
        },
        "sales_control_type": "FREE",
        "sales_control_unit": "string",
        "extra_bed_count": 0,
        "stay_period": {
          "arrival_date": "2019-08-24",
          "arrival_time": "14:15:22Z",
          "departure_date": "2019-08-24",
          "departure_time": "14:15:22Z",
          "late_out": true
        },
        "reservation_route": {
          "reservationDisplayName": "string",
          "reservationRoutes": [
            {
              "code": "string",
              "name": "string",
              "short_name": "string",
              "kana_name": "string",
              "foreign_name": "string",
              "foreign_short_name": "string"
            }
          ]
        },
        "agent_reservation_number": "string",
        "agent_course": "string",
        "person_count": [
          0
        ],
        "pricing": {
          "sales_package": {
            "code": "string",
            "name": "string",
            "short_name": "string",
            "kana_name": "string",
            "foreign_name": "string",
            "foreign_short_name": "string",
            "print_name": "string",
            "print_foreign_name": "string"
          },
          "discount_item": {
            "code": "string",
            "name": "string",
            "short_name": "string",
            "kana_name": "string",
            "foreign_name": "string",
            "foreign_short_name": "string",
            "rate": 0,
            "amount": 0
          },
          "discount_rate": 100,
          "discount_amount": 0,
          "pricing_type": "GROSS",
          "price": 0
        },
        "provision_requests": [
          {
            "id": "string",
            "provision": {
              "code": "string",
              "name": "string",
              "short_name": "string",
              "kana_name": "string",
              "foreign_name": "string",
              "foreign_short_name": "string"
            },
            "from_date": "2019-08-24",
            "to_date": "2019-08-24",
            "stock_control": true,
            "quantity": 0,
            "note": "string",
            "reservation_ref": {
              "reservation_id": "string",
              "room_id": "string",
              "stay_id": "string",
              "reservation_number": "string",
              "room_number": "string"
            }
          }
        ],
        "meal_reservations": [
          {
            "id": "string",
            "meal_place": {
              "id": "string",
              "name": "string",
              "short_name": "string",
              "kana_name": "string",
              "foreign_name": "string",
              "foreign_short_name": "string"
            },
            "meal_type": {
              "id": "string",
              "meal_place_code": "string",
              "meal_time_code": "string",
              "start_time": "14:15:22Z",
              "end_time": "14:15:22Z",
              "person_count": 0,
              "table_count": 0
            },
            "meal_time_frame": {
              "id": "string",
              "name": "string",
              "short_name": "string",
              "kana_name": "string",
              "foreign_name": "string",
              "foreign_short_name": "string"
            },
            "use_date": "2019-08-24",
            "meal_kana_name": "string",
            "meal_name": "string",
            "meal_short_name": "string",
            "meal_item": {
              "code": "string",
              "name": "string",
              "short_name": "string",
              "kana_name": "string",
              "foreign_name": "string",
              "foreign_short_name": "string"
            },
            "person_count": 0,
            "person_type": "ADULT",
            "unit_price": 0,
            "pricing_type": "INCLUDED",
            "start_time": "14:15:22Z",
            "end_time": "14:15:22Z",
            "valid": true,
            "note": "string",
            "reservation_ref": {
              "reservation_id": "string",
              "room_id": "string",
              "stay_id": "string",
              "reservation_number": "string",
              "room_number": "string"
            }
          }
        ],
        "deposits": [
          {
            "id": "string",
            "account_date": "2019-08-24",
            "payment_method": {
              "code": "string",
              "name": "string",
              "short_name": "string",
              "kana_name": "string",
              "foreign_name": "string",
              "foreign_short_name": "string",
              "use_address": true
            },
            "billing_provider": {
              "code": "string",
              "name": "string",
              "short_name": "string",
              "kana_name": "string",
              "foreign_name": "string",
              "foreign_short_name": "string"
            },
            "amount": 0,
            "bill_index": 0,
            "bill_note": "string",
            "internal_note": "string",
            "provider_reference": "string",
            "reservation_ref": {
              "reservation_id": "string",
              "room_id": "string",
              "stay_id": "string",
              "reservation_number": "string",
              "room_number": "string"
            }
          }
        ],
        "slip_items": [
          {
            "id": "string",
            "date": "2019-08-24",
            "item": {
              "code": "string",
              "name": "string",
              "short_name": "string",
              "kana_name": "string",
              "foreign_name": "string",
              "price": 0
            },
            "price_per_item": 0,
            "quantity": 0,
            "total_price": 0,
            "bill_index": 0,
            "bill_note": "string",
            "internal_note": "string",
            "tax_free": true,
            "room_type": {
              "code": "string",
              "standard_persons": 0,
              "max_persons": 0,
              "name": "string",
              "short_name": "string",
              "kana_name": "string",
              "foreign_name": "string",
              "foreign_short_name": "string"
            },
            "reservation_ref": {
              "reservation_id": "string",
              "room_id": "string",
              "stay_id": "string",
              "reservation_number": "string",
              "room_number": "string"
            }
          }
        ],
        "extra_services": [
          {
            "id": "string",
            "service_item": {
              "code": "string",
              "name": "string",
              "kana_name": "string",
              "short_name": "string",
              "foreign_name": "string",
              "foreign_short_name": "string"
            },
            "service_period": {
              "arrival_date": "2019-08-24",
              "arrival_time": "14:15:22Z",
              "departure_date": "2019-08-24",
              "departure_time": "14:15:22Z",
              "late_out": true
            },
            "person_count": 0,
            "note": "string",
            "reservation_ref": {
              "reservation_id": "string",
              "room_id": "string",
              "stay_id": "string",
              "reservation_number": "string",
              "room_number": "string"
            }
          }
        ],
        "remarks": [
          {
            "id": "string",
            "division": {
              "id": "str",
              "name": "string",
              "group_id": "str"
            },
            "remarks_type": {
              "id": "str",
              "name": "string"
            },
            "importance_level": "Primary Remark",
            "subject": "string",
            "content": "string"
          }
        ],
        "price_changes": [
          {
            "date_range_end": "2019-08-24",
            "date_range_start": "2019-08-24",
            "prices": [
              {
                "discount_amount": 0,
                "discount_item_id": "string",
                "discount_item_name": "string",
                "discount_rate": 0,
                "person_count": [
                  0
                ],
                "person_count_price_calc": 0,
                "price": 0,
                "pricing_type": "GROSS",
                "rate_id": "string",
                "room_type_code": "string",
                "sales_package_id": "string",
                "sales_package_name": "string"
              }
            ]
          }
        ]
      }
    }
  ]
}

```

Tap booking API - Stays Api Schemas

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|request|[ApiCommonResponseRequest](#schemaapicommonresponserequest)|false|none|Request|
|request_id|[ApiCommonResponseRequestId](#schemaapicommonresponserequestid)|false|none|RequestId|
|next_cursor|[ApiCommonResponseNextCursor](#schemaapicommonresponsenextcursor)|false|none|Indicates the position of the next entity. If an entity less than a limit is returned by the current page of the result set, then Cursor value is null.|
|stays|[[Stay](#schemastay)]|false|none|[Describes reservation details for a guest]|

<h2 id="tocS_ApiRevenueResponse">ApiRevenueResponse</h2>
<!-- backwards compatibility -->
<a id="schemaapirevenueresponse"></a>
<a id="schema_ApiRevenueResponse"></a>
<a id="tocSapirevenueresponse"></a>
<a id="tocsapirevenueresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "revenue_info": [
    {
      "date": "2019-08-24",
      "no": "string",
      "bill_index": "string",
      "pricing_type": "string",
      "name": "string",
      "standard_rate": "string",
      "sale_rate": "string",
      "package_rate_type": "string",
      "discount_rate": 0,
      "discount_amount": 0,
      "rate_per_person": 0,
      "rate_per_room": 0,
      "person_count": [
        0
      ],
      "number_of_use": 0,
      "number_of_room": 0,
      "sales_amount": 0,
      "service_charge": 0,
      "hotel_tax": 0,
      "bath_tax": 0,
      "meal_amount": 0,
      "tax_include": 0,
      "deposit": 0,
      "total": 0
    }
  ],
  "total_revenue": 0,
  "deposit_total": 0,
  "total": 0
}

```

ApiRevenueResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|request|[ApiCommonResponseRequest](#schemaapicommonresponserequest)|false|none|Request|
|request_id|[ApiCommonResponseRequestId](#schemaapicommonresponserequestid)|false|none|RequestId|
|revenue_info|[[Revenue](#schemarevenue)]|false|none|none|
|total_revenue|number(double)|false|none|none|
|deposit_total|number(double)|false|none|none|
|total|number(double)|false|none|none|

<h2 id="tocS_ApiVacancyResponse">ApiVacancyResponse</h2>
<!-- backwards compatibility -->
<a id="schemaapivacancyresponse"></a>
<a id="schema_ApiVacancyResponse"></a>
<a id="tocSapivacancyresponse"></a>
<a id="tocsapivacancyresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "vacant_rooms": [
    {
      "room_type_code": "string",
      "room_quantity": 0,
      "room_stock": 0,
      "date": "2019-08-24",
      "is_sale_stop": "true",
      "sale_quantity": 0,
      "closing_state": "true"
    }
  ]
}

```

Tap booking API - Stays Api Schemas

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|request|[ApiCommonResponseRequest](#schemaapicommonresponserequest)|false|none|Request|
|request_id|[ApiCommonResponseRequestId](#schemaapicommonresponserequestid)|false|none|RequestId|
|next_cursor|[ApiCommonResponseNextCursor](#schemaapicommonresponsenextcursor)|false|none|Indicates the position of the next entity. If an entity less than a limit is returned by the current page of the result set, then Cursor value is null.|
|vacant_rooms|[[RoomTypeVacancy](#schemaroomtypevacancy)]|false|none|none|

<h2 id="tocS_RoomTypeVacancy">RoomTypeVacancy</h2>
<!-- backwards compatibility -->
<a id="schemaroomtypevacancy"></a>
<a id="schema_RoomTypeVacancy"></a>
<a id="tocSroomtypevacancy"></a>
<a id="tocsroomtypevacancy"></a>

```json
{
  "room_type_code": "string",
  "room_quantity": 0,
  "room_stock": 0,
  "date": "2019-08-24",
  "is_sale_stop": "true",
  "sale_quantity": 0,
  "closing_state": "true"
}

```

RoomTypeVacancy

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|room_type_code|string|false|none|none|
|room_quantity|integer|false|none|none|
|room_stock|integer|false|none|none|
|date|[Date](#schemadate)|false|none|日付(Date)|
|is_sale_stop|string|false|none|none|
|sale_quantity|integer|false|none|none|
|closing_state|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|is_sale_stop|true|
|is_sale_stop|false|
|closing_state|true|
|closing_state|false|

<h2 id="tocS_ListOutOfOrdersResponse">ListOutOfOrdersResponse</h2>
<!-- backwards compatibility -->
<a id="schemalistoutofordersresponse"></a>
<a id="schema_ListOutOfOrdersResponse"></a>
<a id="tocSlistoutofordersresponse"></a>
<a id="tocslistoutofordersresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "total_pages": 0,
  "total_records": 0,
  "out_of_orders": [
    {
      "room_number": "string",
      "out_of_order_id": "string",
      "reason_name": "string",
      "room_floor_id": "string",
      "date_range_start": "2019-08-24",
      "date_range_end": "2019-08-24"
    }
  ]
}

```

ListOutOfOrdersResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|ListOutOfOrdersResponse|any|false|none|none|

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[ApiListResponse](#schemaapilistresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» out_of_orders|[[OutOfOrder](#schemaoutoforder)]|false|none|[Out Of Order]|

<h2 id="tocS_CreateOutOfOrderResponse">CreateOutOfOrderResponse</h2>
<!-- backwards compatibility -->
<a id="schemacreateoutoforderresponse"></a>
<a id="schema_CreateOutOfOrderResponse"></a>
<a id="tocScreateoutoforderresponse"></a>
<a id="tocscreateoutoforderresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "out_of_order": {
    "room_number": "string",
    "out_of_order_id": "string",
    "reason_name": "string",
    "room_floor_id": "string",
    "date_range_start": "2019-08-24",
    "date_range_end": "2019-08-24"
  }
}

```

CreateOutOfOrderResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|CreateOutOfOrderResponse|any|false|none|none|

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[ApiCreateResponse](#schemaapicreateresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» out_of_order|[OutOfOrder](#schemaoutoforder)|false|none|Out Of Order|

<h2 id="tocS_CreateOutOfOrderRequest">CreateOutOfOrderRequest</h2>
<!-- backwards compatibility -->
<a id="schemacreateoutoforderrequest"></a>
<a id="schema_CreateOutOfOrderRequest"></a>
<a id="tocScreateoutoforderrequest"></a>
<a id="tocscreateoutoforderrequest"></a>

```json
{
  "out_of_order": {
    "room_number": "string",
    "out_of_order_id": "string",
    "reason_name": "string",
    "room_floor_id": "string",
    "date_range_start": "2019-08-24",
    "date_range_end": "2019-08-24"
  }
}

```

CreateOutOfOrderRequest

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|CreateOutOfOrderRequest|any|false|none|none|

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[ApiCreateRequest](#schemaapicreaterequest)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» out_of_order|[OutOfOrder](#schemaoutoforder)|false|none|Out Of Order|

<h2 id="tocS_UpdateOutOfOrderResponse">UpdateOutOfOrderResponse</h2>
<!-- backwards compatibility -->
<a id="schemaupdateoutoforderresponse"></a>
<a id="schema_UpdateOutOfOrderResponse"></a>
<a id="tocSupdateoutoforderresponse"></a>
<a id="tocsupdateoutoforderresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "out_of_order": {
    "room_number": "string",
    "out_of_order_id": "string",
    "reason_name": "string",
    "room_floor_id": "string",
    "date_range_start": "2019-08-24",
    "date_range_end": "2019-08-24"
  }
}

```

UpdateOutOfOrderResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|UpdateOutOfOrderResponse|any|false|none|none|

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[ApiUpdateResponse](#schemaapiupdateresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» out_of_order|[OutOfOrder](#schemaoutoforder)|false|none|Out Of Order|

<h2 id="tocS_UpdateOutOfOrderRequest">UpdateOutOfOrderRequest</h2>
<!-- backwards compatibility -->
<a id="schemaupdateoutoforderrequest"></a>
<a id="schema_UpdateOutOfOrderRequest"></a>
<a id="tocSupdateoutoforderrequest"></a>
<a id="tocsupdateoutoforderrequest"></a>

```json
{
  "out_of_order": {
    "out_of_order_id": "string",
    "reason_name": "string",
    "room_floor_id": "string",
    "date_range_start": "2019-08-24",
    "date_range_end": "2019-08-24"
  }
}

```

UpdateOutOfOrderRequest

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|UpdateOutOfOrderRequest|any|false|none|none|

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[ApiUpdateRequest](#schemaapiupdaterequest)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» out_of_order|[OutOfOrderDynamic](#schemaoutoforderdynamic)|false|none|none|

<h2 id="tocS_DeleteOutOfOrderResponse">DeleteOutOfOrderResponse</h2>
<!-- backwards compatibility -->
<a id="schemadeleteoutoforderresponse"></a>
<a id="schema_DeleteOutOfOrderResponse"></a>
<a id="tocSdeleteoutoforderresponse"></a>
<a id="tocsdeleteoutoforderresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "out_of_order": {
    "room_number": "string",
    "out_of_order_id": "string",
    "reason_name": "string",
    "room_floor_id": "string",
    "date_range_start": "2019-08-24",
    "date_range_end": "2019-08-24"
  }
}

```

DeleteOutOfOrderResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|DeleteOutOfOrderResponse|any|false|none|none|

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[ApiDeleteResponse](#schemaapideleteresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» out_of_order|[OutOfOrder](#schemaoutoforder)|false|none|Out Of Order|

<h2 id="tocS_ListReservationBillingsResponse">ListReservationBillingsResponse</h2>
<!-- backwards compatibility -->
<a id="schemalistreservationbillingsresponse"></a>
<a id="schema_ListReservationBillingsResponse"></a>
<a id="tocSlistreservationbillingsresponse"></a>
<a id="tocslistreservationbillingsresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "total_pages": 0,
  "total_records": 0,
  "billing_requests": [
    {
      "bill_address_id": "string",
      "bill_address_name": "string",
      "bill_index": 0,
      "bill_to_name": "string",
      "bill_to_option_id": "Guest",
      "payment_method_id": "string",
      "payment_method_name": "string",
      "conditions": [
        {
          "item_id": "string",
          "item_name": "string"
        }
      ]
    }
  ]
}

```

ListReservationBillingsResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|ListReservationBillingsResponse|any|false|none|none|

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[ApiListResponse](#schemaapilistresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|returns a list of customer|
|» billing_requests|[[BillingRequest](#schemabillingrequest)]|false|none|none|

<h2 id="tocS_CreateReservationBillingResponse">CreateReservationBillingResponse</h2>
<!-- backwards compatibility -->
<a id="schemacreatereservationbillingresponse"></a>
<a id="schema_CreateReservationBillingResponse"></a>
<a id="tocScreatereservationbillingresponse"></a>
<a id="tocscreatereservationbillingresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "billing_request": {
    "bill_address_id": "string",
    "bill_address_name": "string",
    "bill_index": 0,
    "bill_to_name": "string",
    "bill_to_option_id": "Guest",
    "payment_method_id": "string",
    "payment_method_name": "string",
    "conditions": [
      {
        "item_id": "string",
        "item_name": "string"
      }
    ]
  }
}

```

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[ApiCreateResponse](#schemaapicreateresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» billing_request|[BillingRequest](#schemabillingrequest)|false|none|none|

<h2 id="tocS_CreateReservationBillingRequest">CreateReservationBillingRequest</h2>
<!-- backwards compatibility -->
<a id="schemacreatereservationbillingrequest"></a>
<a id="schema_CreateReservationBillingRequest"></a>
<a id="tocScreatereservationbillingrequest"></a>
<a id="tocscreatereservationbillingrequest"></a>

```json
{
  "billing_request": {
    "bill_address_id": "string",
    "bill_address_name": "string",
    "bill_index": 0,
    "bill_to_name": "string",
    "bill_to_option_id": "Guest",
    "payment_method_id": "string",
    "payment_method_name": "string",
    "conditions": [
      {
        "item_id": "string",
        "item_name": "string"
      }
    ]
  }
}

```

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[ApiCreateRequest](#schemaapicreaterequest)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» billing_request|[BillingRequest](#schemabillingrequest)|false|none|none|

<h2 id="tocS_UpdateReservationBillingResponse">UpdateReservationBillingResponse</h2>
<!-- backwards compatibility -->
<a id="schemaupdatereservationbillingresponse"></a>
<a id="schema_UpdateReservationBillingResponse"></a>
<a id="tocSupdatereservationbillingresponse"></a>
<a id="tocsupdatereservationbillingresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "billing_request": {
    "bill_address_id": "string",
    "bill_address_name": "string",
    "bill_index": 0,
    "bill_to_name": "string",
    "bill_to_option_id": "Guest",
    "payment_method_id": "string",
    "payment_method_name": "string",
    "conditions": [
      {
        "item_id": "string",
        "item_name": "string"
      }
    ]
  }
}

```

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[ApiUpdateResponse](#schemaapiupdateresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» billing_request|[BillingRequest](#schemabillingrequest)|false|none|none|

<h2 id="tocS_UpdateReservationBillingRequest">UpdateReservationBillingRequest</h2>
<!-- backwards compatibility -->
<a id="schemaupdatereservationbillingrequest"></a>
<a id="schema_UpdateReservationBillingRequest"></a>
<a id="tocSupdatereservationbillingrequest"></a>
<a id="tocsupdatereservationbillingrequest"></a>

```json
{
  "billing_request": {
    "bill_address_id": "string",
    "bill_address_name": "string",
    "bill_index": 0,
    "bill_to_name": "string",
    "bill_to_option_id": "Guest",
    "payment_method_id": "string",
    "payment_method_name": "string",
    "conditions": [
      {
        "item_id": "string",
        "item_name": "string"
      }
    ]
  }
}

```

UpdatePolicyRequest

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[ApiUpdateRequest](#schemaapiupdaterequest)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» billing_request|[BillingRequest](#schemabillingrequest)|false|none|none|

<h2 id="tocS_DeleteReservationBillingResponse">DeleteReservationBillingResponse</h2>
<!-- backwards compatibility -->
<a id="schemadeletereservationbillingresponse"></a>
<a id="schema_DeleteReservationBillingResponse"></a>
<a id="tocSdeletereservationbillingresponse"></a>
<a id="tocsdeletereservationbillingresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "billing_request": {
    "bill_address_id": "string",
    "bill_address_name": "string",
    "bill_index": 0,
    "bill_to_name": "string",
    "bill_to_option_id": "Guest",
    "payment_method_id": "string",
    "payment_method_name": "string",
    "conditions": [
      {
        "item_id": "string",
        "item_name": "string"
      }
    ]
  }
}

```

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[ApiDeleteResponse](#schemaapideleteresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» billing_request|[BillingRequest](#schemabillingrequest)|false|none|none|

<h2 id="tocS_CreateRoomReservationBillingResponse">CreateRoomReservationBillingResponse</h2>
<!-- backwards compatibility -->
<a id="schemacreateroomreservationbillingresponse"></a>
<a id="schema_CreateRoomReservationBillingResponse"></a>
<a id="tocScreateroomreservationbillingresponse"></a>
<a id="tocscreateroomreservationbillingresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "billing_request": {
    "bill_address_id": "string",
    "bill_address_name": "string",
    "bill_index": 0,
    "bill_to_name": "string",
    "bill_to_option_id": "Guest",
    "payment_method_id": "string",
    "payment_method_name": "string",
    "conditions": [
      {
        "item_id": "string",
        "item_name": "string"
      }
    ]
  }
}

```

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[ApiCreateResponse](#schemaapicreateresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» billing_request|[BillingRequest](#schemabillingrequest)|false|none|none|

<h2 id="tocS_CreateRoomReservationBillingRequest">CreateRoomReservationBillingRequest</h2>
<!-- backwards compatibility -->
<a id="schemacreateroomreservationbillingrequest"></a>
<a id="schema_CreateRoomReservationBillingRequest"></a>
<a id="tocScreateroomreservationbillingrequest"></a>
<a id="tocscreateroomreservationbillingrequest"></a>

```json
{
  "billing_request": {
    "bill_address_id": "string",
    "bill_address_name": "string",
    "bill_index": 0,
    "bill_to_name": "string",
    "bill_to_option_id": "Guest",
    "payment_method_id": "string",
    "payment_method_name": "string",
    "conditions": [
      {
        "item_id": "string",
        "item_name": "string"
      }
    ]
  }
}

```

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[ApiCreateRequest](#schemaapicreaterequest)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» billing_request|[BillingRequest](#schemabillingrequest)|false|none|none|

<h2 id="tocS_UpdateRoomReservationBillingResponse">UpdateRoomReservationBillingResponse</h2>
<!-- backwards compatibility -->
<a id="schemaupdateroomreservationbillingresponse"></a>
<a id="schema_UpdateRoomReservationBillingResponse"></a>
<a id="tocSupdateroomreservationbillingresponse"></a>
<a id="tocsupdateroomreservationbillingresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "billing_request": {
    "bill_address_id": "string",
    "bill_address_name": "string",
    "bill_index": 0,
    "bill_to_name": "string",
    "bill_to_option_id": "Guest",
    "payment_method_id": "string",
    "payment_method_name": "string",
    "conditions": [
      {
        "item_id": "string",
        "item_name": "string"
      }
    ]
  }
}

```

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[ApiUpdateResponse](#schemaapiupdateresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» billing_request|[BillingRequest](#schemabillingrequest)|false|none|none|

<h2 id="tocS_UpdateRoomReservationBillingRequest">UpdateRoomReservationBillingRequest</h2>
<!-- backwards compatibility -->
<a id="schemaupdateroomreservationbillingrequest"></a>
<a id="schema_UpdateRoomReservationBillingRequest"></a>
<a id="tocSupdateroomreservationbillingrequest"></a>
<a id="tocsupdateroomreservationbillingrequest"></a>

```json
{
  "billing_request": {
    "bill_address_id": "string",
    "bill_address_name": "string",
    "bill_index": 0,
    "bill_to_name": "string",
    "bill_to_option_id": "Guest",
    "payment_method_id": "string",
    "payment_method_name": "string",
    "conditions": [
      {
        "item_id": "string",
        "item_name": "string"
      }
    ]
  }
}

```

UpdatePolicyRequest

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[ApiUpdateRequest](#schemaapiupdaterequest)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» billing_request|[BillingRequest](#schemabillingrequest)|false|none|none|

<h2 id="tocS_DeleteRoomReservationBillingResponse">DeleteRoomReservationBillingResponse</h2>
<!-- backwards compatibility -->
<a id="schemadeleteroomreservationbillingresponse"></a>
<a id="schema_DeleteRoomReservationBillingResponse"></a>
<a id="tocSdeleteroomreservationbillingresponse"></a>
<a id="tocsdeleteroomreservationbillingresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "billing_request": {
    "bill_address_id": "string",
    "bill_address_name": "string",
    "bill_index": 0,
    "bill_to_name": "string",
    "bill_to_option_id": "Guest",
    "payment_method_id": "string",
    "payment_method_name": "string",
    "conditions": [
      {
        "item_id": "string",
        "item_name": "string"
      }
    ]
  }
}

```

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[ApiDeleteResponse](#schemaapideleteresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» billing_request|[BillingRequest](#schemabillingrequest)|false|none|none|

<h2 id="tocS_ApiCommonResponseRequest">ApiCommonResponseRequest</h2>
<!-- backwards compatibility -->
<a id="schemaapicommonresponserequest"></a>
<a id="schema_ApiCommonResponseRequest"></a>
<a id="tocSapicommonresponserequest"></a>
<a id="tocsapicommonresponserequest"></a>

```json
{
  "version": "string",
  "body": "string",
  "url": "string"
}

```

ApiCommonResponseRequest

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|version|string|false|none|none|
|body|string|false|none|none|
|url|string|false|none|none|

<h2 id="tocS_ApiCommonResponseRequestId">ApiCommonResponseRequestId</h2>
<!-- backwards compatibility -->
<a id="schemaapicommonresponserequestid"></a>
<a id="schema_ApiCommonResponseRequestId"></a>
<a id="tocSapicommonresponserequestid"></a>
<a id="tocsapicommonresponserequestid"></a>

```json
"594600f4-7eec-47ca-8012-02e7b89859ce"

```

ApiCommonResponseRequestId

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|ApiCommonResponseRequestId|string|false|none|RequestId|

<h2 id="tocS_ApiCommonResponseNextCursor">ApiCommonResponseNextCursor</h2>
<!-- backwards compatibility -->
<a id="schemaapicommonresponsenextcursor"></a>
<a id="schema_ApiCommonResponseNextCursor"></a>
<a id="tocSapicommonresponsenextcursor"></a>
<a id="tocsapicommonresponsenextcursor"></a>

```json
"c-3yvu1pzhd3i7"

```

ApiCommonResponseNextCursor

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|ApiCommonResponseNextCursor|string|false|none|Indicates the position of the next entity. If an entity less than a limit is returned by the current page of the result set, then Cursor value is null.|

<h2 id="tocS_Facility">Facility</h2>
<!-- backwards compatibility -->
<a id="schemafacility"></a>
<a id="schema_Facility"></a>
<a id="tocSfacility"></a>
<a id="tocsfacility"></a>

```json
{
  "status": 0,
  "error_code": 0,
  "error_message": "string",
  "language": "string",
  "data": [
    {
      "access_info": "string",
      "address": "string",
      "hotel-id": "string",
      "hotel_name": "string",
      "image_url": "string",
      "search_hotel_name": "string"
    }
  ]
}

```

Facility

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|status|integer|false|none|none|
|error_code|integer|false|none|none|
|error_message|string|false|none|none|
|language|string|false|none|none|
|data|[[Data](#schemadata)]|false|none|[Model of a data for facility]|

<h2 id="tocS_Data">Data</h2>
<!-- backwards compatibility -->
<a id="schemadata"></a>
<a id="schema_Data"></a>
<a id="tocSdata"></a>
<a id="tocsdata"></a>

```json
{
  "access_info": "string",
  "address": "string",
  "hotel-id": "string",
  "hotel_name": "string",
  "image_url": "string",
  "search_hotel_name": "string"
}

```

Data

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|access_info|string|false|none|none|
|address|string|false|none|none|
|hotel-id|string|false|none|none|
|hotel_name|string|false|none|none|
|image_url|string|false|none|none|
|search_hotel_name|string|false|none|none|

<h2 id="tocS_ProvisionItem">ProvisionItem</h2>
<!-- backwards compatibility -->
<a id="schemaprovisionitem"></a>
<a id="schema_ProvisionItem"></a>
<a id="tocSprovisionitem"></a>
<a id="tocsprovisionitem"></a>

```json
{
  "code": "string",
  "name": "string",
  "short_name": "string",
  "kana_name": "string",
  "foreign_name": "string",
  "foreign_short_name": "string"
}

```

ProvisionItem

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|string|false|none|none|
|name|string|false|none|none|
|short_name|string|false|none|none|
|kana_name|string|false|none|none|
|foreign_name|string|false|none|none|
|foreign_short_name|string|false|none|none|

<h2 id="tocS_Provision">Provision</h2>
<!-- backwards compatibility -->
<a id="schemaprovision"></a>
<a id="schema_Provision"></a>
<a id="tocSprovision"></a>
<a id="tocsprovision"></a>

```json
{
  "id": "string",
  "provision": {
    "code": "string",
    "name": "string",
    "short_name": "string",
    "kana_name": "string",
    "foreign_name": "string",
    "foreign_short_name": "string"
  },
  "from_date": "2019-08-24",
  "to_date": "2019-08-24",
  "stock_control": true,
  "quantity": 0,
  "note": "string",
  "reservation_ref": {
    "reservation_id": "string",
    "room_id": "string",
    "stay_id": "string",
    "reservation_number": "string",
    "room_number": "string"
  }
}

```

Provision

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|false|none|none|
|provision|[ProvisionItem](#schemaprovisionitem)|false|none|none|
|from_date|[Date](#schemadate)|false|none|日付(Date)|
|to_date|[Date](#schemadate)|false|none|日付(Date)|
|stock_control|boolean|false|none|none|
|quantity|integer|false|none|none|
|note|string|false|none|none|
|reservation_ref|[ReservationReference](#schemareservationreference)|false|none|none|

<h2 id="tocS_ReservationReference">ReservationReference</h2>
<!-- backwards compatibility -->
<a id="schemareservationreference"></a>
<a id="schema_ReservationReference"></a>
<a id="tocSreservationreference"></a>
<a id="tocsreservationreference"></a>

```json
{
  "reservation_id": "string",
  "room_id": "string",
  "stay_id": "string",
  "reservation_number": "string",
  "room_number": "string"
}

```

ReservationReference

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|reservation_id|string|false|none|none|
|room_id|string|false|none|none|
|stay_id|string|false|none|none|
|reservation_number|string|false|none|none|
|room_number|string|false|none|none|

<h2 id="tocS_Date">Date</h2>
<!-- backwards compatibility -->
<a id="schemadate"></a>
<a id="schema_Date"></a>
<a id="tocSdate"></a>
<a id="tocsdate"></a>

```json
"2019-08-24"

```

Year, Month, Day

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|Year, Month, Day|string(date)|false|none|日付(Date)|

<h2 id="tocS_ApiListResponse">ApiListResponse</h2>
<!-- backwards compatibility -->
<a id="schemaapilistresponse"></a>
<a id="schema_ApiListResponse"></a>
<a id="tocSapilistresponse"></a>
<a id="tocsapilistresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce",
  "next_cursor": "c-3yvu1pzhd3i7",
  "total_pages": 0,
  "total_records": 0
}

```

ApiListResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|ApiListResponse|any|false|none|none|

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[ApiResponse](#schemaapiresponse)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» next_cursor|[ApiCommonResponseNextCursor](#schemaapicommonresponsenextcursor)|false|none|Indicates the position of the next entity. If an entity less than a limit is returned by the current page of the result set, then Cursor value is null.|
|» total_pages|integer|false|none|none|
|» total_records|integer|false|none|none|

<h2 id="tocS_ApiResponse">ApiResponse</h2>
<!-- backwards compatibility -->
<a id="schemaapiresponse"></a>
<a id="schema_ApiResponse"></a>
<a id="tocSapiresponse"></a>
<a id="tocsapiresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce"
}

```

ApiResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|request|[ApiCommonResponseRequest](#schemaapicommonresponserequest)|false|none|Request|
|request_id|[ApiCommonResponseRequestId](#schemaapicommonresponserequestid)|false|none|RequestId|

<h2 id="tocS_ExtraService">ExtraService</h2>
<!-- backwards compatibility -->
<a id="schemaextraservice"></a>
<a id="schema_ExtraService"></a>
<a id="tocSextraservice"></a>
<a id="tocsextraservice"></a>

```json
{
  "code": "string",
  "name": "string",
  "kana_name": "string",
  "short_name": "string",
  "foreign_name": "string",
  "foreign_short_name": "string"
}

```

ExtraService

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|string|false|none|none|
|name|string|false|none|none|
|kana_name|string|false|none|none|
|short_name|string|false|none|none|
|foreign_name|string|false|none|none|
|foreign_short_name|string|false|none|none|

<h2 id="tocS_ExtraServiceReservation">ExtraServiceReservation</h2>
<!-- backwards compatibility -->
<a id="schemaextraservicereservation"></a>
<a id="schema_ExtraServiceReservation"></a>
<a id="tocSextraservicereservation"></a>
<a id="tocsextraservicereservation"></a>

```json
{
  "id": "string",
  "service_item": {
    "code": "string",
    "name": "string",
    "kana_name": "string",
    "short_name": "string",
    "foreign_name": "string",
    "foreign_short_name": "string"
  },
  "service_period": {
    "arrival_date": "2019-08-24",
    "arrival_time": "14:15:22Z",
    "departure_date": "2019-08-24",
    "departure_time": "14:15:22Z",
    "late_out": true
  },
  "person_count": 0,
  "note": "string",
  "reservation_ref": {
    "reservation_id": "string",
    "room_id": "string",
    "stay_id": "string",
    "reservation_number": "string",
    "room_number": "string"
  }
}

```

ExtraServiceReservation

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|false|none|none|
|service_item|[ExtraService](#schemaextraservice)|false|none|none|
|service_period|[StayPeriod](#schemastayperiod)|false|none|none|
|person_count|integer|false|none|none|
|note|string|false|none|none|
|reservation_ref|[ReservationReference](#schemareservationreference)|false|none|none|

<h2 id="tocS_StayPeriod">StayPeriod</h2>
<!-- backwards compatibility -->
<a id="schemastayperiod"></a>
<a id="schema_StayPeriod"></a>
<a id="tocSstayperiod"></a>
<a id="tocsstayperiod"></a>

```json
{
  "arrival_date": "2019-08-24",
  "arrival_time": "14:15:22Z",
  "departure_date": "2019-08-24",
  "departure_time": "14:15:22Z",
  "late_out": true
}

```

StayPeriod

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|arrival_date|[Date](#schemadate)|false|none|日付(Date)|
|arrival_time|[Time](#schematime)|false|none|時間(Time)|
|departure_date|[Date](#schemadate)|false|none|日付(Date)|
|departure_time|[Time](#schematime)|false|none|時間(Time)|
|late_out|boolean|false|none|none|

<h2 id="tocS_ApiGetResponse">ApiGetResponse</h2>
<!-- backwards compatibility -->
<a id="schemaapigetresponse"></a>
<a id="schema_ApiGetResponse"></a>
<a id="tocSapigetresponse"></a>
<a id="tocsapigetresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce"
}

```

ApiGetResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|ApiGetResponse|[ApiResponse](#schemaapiresponse)|false|none|none|

<h2 id="tocS_ApiUpdateResponse">ApiUpdateResponse</h2>
<!-- backwards compatibility -->
<a id="schemaapiupdateresponse"></a>
<a id="schema_ApiUpdateResponse"></a>
<a id="tocSapiupdateresponse"></a>
<a id="tocsapiupdateresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce"
}

```

ApiUpdateResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|ApiUpdateResponse|[ApiResponse](#schemaapiresponse)|false|none|none|

<h2 id="tocS_ApiUpdateRequest">ApiUpdateRequest</h2>
<!-- backwards compatibility -->
<a id="schemaapiupdaterequest"></a>
<a id="schema_ApiUpdateRequest"></a>
<a id="tocSapiupdaterequest"></a>
<a id="tocsapiupdaterequest"></a>

```json
{}

```

ApiUpdateRequest

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|ApiUpdateRequest|[ApiRequest](#schemaapirequest)|false|none|none|

<h2 id="tocS_ApiRequest">ApiRequest</h2>
<!-- backwards compatibility -->
<a id="schemaapirequest"></a>
<a id="schema_ApiRequest"></a>
<a id="tocSapirequest"></a>
<a id="tocsapirequest"></a>

```json
{}

```

ApiRequest

### Properties

*None*

<h2 id="tocS_ExtraServiceReservationRequest">ExtraServiceReservationRequest</h2>
<!-- backwards compatibility -->
<a id="schemaextraservicereservationrequest"></a>
<a id="schema_ExtraServiceReservationRequest"></a>
<a id="tocSextraservicereservationrequest"></a>
<a id="tocsextraservicereservationrequest"></a>

```json
{
  "service_item_code": "str",
  "note": "string",
  "service_period": {
    "arrival_date": "2019-08-24",
    "arrival_time": "14:15:22Z",
    "departure_date": "2019-08-24",
    "departure_time": "14:15:22Z",
    "late_out": true
  },
  "person_count": 0
}

```

ExtraServiceReservationRequest

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|service_item_code|string|true|none|付帯サービスコード<br>ExtraServiceCode|
|note|string|false|none|none|
|service_period|[StayPeriod](#schemastayperiod)|true|none|none|
|person_count|integer|true|none|人数1<br>Person count|

<h2 id="tocS_ApiDeleteResponse">ApiDeleteResponse</h2>
<!-- backwards compatibility -->
<a id="schemaapideleteresponse"></a>
<a id="schema_ApiDeleteResponse"></a>
<a id="tocSapideleteresponse"></a>
<a id="tocsapideleteresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce"
}

```

ApiGetResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|ApiGetResponse|[ApiResponse](#schemaapiresponse)|false|none|none|

<h2 id="tocS_MealPlace">MealPlace</h2>
<!-- backwards compatibility -->
<a id="schemamealplace"></a>
<a id="schema_MealPlace"></a>
<a id="tocSmealplace"></a>
<a id="tocsmealplace"></a>

```json
{
  "id": "string",
  "name": "string",
  "short_name": "string",
  "kana_name": "string",
  "foreign_name": "string",
  "foreign_short_name": "string"
}

```

MealPlace

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|false|none|version 0.1 support|
|name|string|false|none|none|
|short_name|string|false|none|none|
|kana_name|string|false|none|none|
|foreign_name|string|false|none|none|
|foreign_short_name|string|false|none|none|

<h2 id="tocS_MealTimeFrame">MealTimeFrame</h2>
<!-- backwards compatibility -->
<a id="schemamealtimeframe"></a>
<a id="schema_MealTimeFrame"></a>
<a id="tocSmealtimeframe"></a>
<a id="tocsmealtimeframe"></a>

```json
{
  "id": "string",
  "name": "string",
  "short_name": "string",
  "kana_name": "string",
  "foreign_name": "string",
  "foreign_short_name": "string"
}

```

MealTimeframe

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|false|none|version 0.1 support|
|name|string|false|none|none|
|short_name|string|false|none|none|
|kana_name|string|false|none|none|
|foreign_name|string|false|none|none|
|foreign_short_name|string|false|none|none|

<h2 id="tocS_MealType">MealType</h2>
<!-- backwards compatibility -->
<a id="schemamealtype"></a>
<a id="schema_MealType"></a>
<a id="tocSmealtype"></a>
<a id="tocsmealtype"></a>

```json
{
  "id": "string",
  "meal_place_code": "string",
  "meal_time_code": "string",
  "start_time": "14:15:22Z",
  "end_time": "14:15:22Z",
  "person_count": 0,
  "table_count": 0
}

```

MealType

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|false|none|version 0.1 support|
|meal_place_code|string|false|none|none|
|meal_time_code|string|false|none|none|
|start_time|[Time](#schematime)|false|none|時間(Time)|
|end_time|[Time](#schematime)|false|none|時間(Time)|
|person_count|integer|false|none|none|
|table_count|integer|false|none|none|

<h2 id="tocS_MealItem">MealItem</h2>
<!-- backwards compatibility -->
<a id="schemamealitem"></a>
<a id="schema_MealItem"></a>
<a id="tocSmealitem"></a>
<a id="tocsmealitem"></a>

```json
{
  "code": "string",
  "name": "string",
  "short_name": "string",
  "kana_name": "string",
  "foreign_name": "string",
  "foreign_short_name": "string"
}

```

MealItem

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|string|false|none|none|
|name|string|false|none|none|
|short_name|string|false|none|none|
|kana_name|string|false|none|none|
|foreign_name|string|false|none|none|
|foreign_short_name|string|false|none|none|

<h2 id="tocS_MealReservation">MealReservation</h2>
<!-- backwards compatibility -->
<a id="schemamealreservation"></a>
<a id="schema_MealReservation"></a>
<a id="tocSmealreservation"></a>
<a id="tocsmealreservation"></a>

```json
{
  "id": "string",
  "meal_place": {
    "id": "string",
    "name": "string",
    "short_name": "string",
    "kana_name": "string",
    "foreign_name": "string",
    "foreign_short_name": "string"
  },
  "meal_type": {
    "id": "string",
    "meal_place_code": "string",
    "meal_time_code": "string",
    "start_time": "14:15:22Z",
    "end_time": "14:15:22Z",
    "person_count": 0,
    "table_count": 0
  },
  "meal_time_frame": {
    "id": "string",
    "name": "string",
    "short_name": "string",
    "kana_name": "string",
    "foreign_name": "string",
    "foreign_short_name": "string"
  },
  "use_date": "2019-08-24",
  "meal_kana_name": "string",
  "meal_name": "string",
  "meal_short_name": "string",
  "meal_item": {
    "code": "string",
    "name": "string",
    "short_name": "string",
    "kana_name": "string",
    "foreign_name": "string",
    "foreign_short_name": "string"
  },
  "person_count": 0,
  "person_type": "ADULT",
  "unit_price": 0,
  "pricing_type": "INCLUDED",
  "start_time": "14:15:22Z",
  "end_time": "14:15:22Z",
  "valid": true,
  "note": "string",
  "reservation_ref": {
    "reservation_id": "string",
    "room_id": "string",
    "stay_id": "string",
    "reservation_number": "string",
    "room_number": "string"
  }
}

```

MealReservation

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|false|none|none|
|meal_place|[MealPlace](#schemamealplace)|false|none|Model for meal place|
|meal_type|[MealType](#schemamealtype)|false|none|Model for meal type|
|meal_time_frame|[MealTimeFrame](#schemamealtimeframe)|false|none|Model for meal timeframe|
|use_date|[Date](#schemadate)|false|none|日付(Date)|
|meal_kana_name|string|false|none|version 0.1 support|
|meal_name|string|false|none|version 0.1 support|
|meal_short_name|string|false|none|version 0.1 support|
|meal_item|[MealItem](#schemamealitem)|false|none|Model for meal sales item|
|person_count|integer|false|none|none|
|person_type|string|false|none|none|
|unit_price|number(double)|false|none|none|
|pricing_type|string|false|none|none|
|start_time|string(time)|false|none|none|
|end_time|string(time)|false|none|none|
|valid|boolean|false|none|none|
|note|string|false|none|none|
|reservation_ref|[ReservationReference](#schemareservationreference)|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|person_type|ADULT|
|person_type|CHILD_A|
|person_type|CHILD_B|
|person_type|CHILD_C|
|person_type|CHILD_D|
|person_type|ROOM|
|pricing_type|INCLUDED|
|pricing_type|ADDED|
|pricing_type|SEPARATE|

<h2 id="tocS_SalesEntry">SalesEntry</h2>
<!-- backwards compatibility -->
<a id="schemasalesentry"></a>
<a id="schema_SalesEntry"></a>
<a id="tocSsalesentry"></a>
<a id="tocssalesentry"></a>

```json
{
  "slip_date": "2019-08-24",
  "sales_account_item_id": "string",
  "room_number": "string",
  "unit_price": 0,
  "quantity": 0,
  "tax_rate": 0,
  "bill_index": 0,
  "customer_note": "string",
  "control_note": "string",
  "duty_free": true
}

```

SalesEntry

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|slip_date|[Date](#schemadate)|true|none|日付(Date)|
|sales_account_item_id|string|true|none|none|
|room_number|string|true|none|none|
|unit_price|number(double)|true|none|none|
|quantity|number(double)|true|none|none|
|tax_rate|number(double)|true|none|none|
|bill_index|integer(double)|false|none|none|
|customer_note|string|false|none|none|
|control_note|string|false|none|none|
|duty_free|boolean|false|none|none|

<h2 id="tocS_Reservation">Reservation</h2>
<!-- backwards compatibility -->
<a id="schemareservation"></a>
<a id="schema_Reservation"></a>
<a id="tocSreservation"></a>
<a id="tocsreservation"></a>

```json
{
  "id ": "string",
  "reservation_number": "string",
  "check_in_date": "string",
  "check_out_date": "string",
  "room_sales_status": {
    "status": "Fix"
  },
  "control_status": {
    "status": "Reserve"
  },
  "person_count": [
    0
  ],
  "main_guest": {
    "person": {
      "kana_name": "string",
      "name": "string",
      "address": {
        "postal_code": "string",
        "prefecture_code": "string",
        "city": "string",
        "address_line": [
          "string"
        ]
      },
      "phone_no": "000-0000-0000",
      "phone_no_mobile": "000-0000-0000",
      "phone_no_other": "000-0000-0000",
      "gender": "Male",
      "birthday": "2019-08-24",
      "email": "example@example.com",
      "email_sub": "example@example.com",
      "external_customer_Id": "string"
    },
    "remarks": [
      {
        "system_user_company_id": "strin",
        "customer_number": "string",
        "customer_remark_id": "string",
        "importance_level_id": "PrimaryRemark",
        "facility_id": "strin",
        "date": "2019-08-24",
        "division": {
          "id": "str",
          "name": "string",
          "group_id": "str"
        },
        "type": {
          "id": "str",
          "name": "string"
        },
        "interlock_system_id": "str",
        "content": "string",
        "subject": "string",
        "output_timing": true,
        "youcom_hotel": {
          "id": "strin",
          "name": "string"
        },
        "youcom_sequence": 0,
        "create_info": {
          "host_name": "string",
          "time_stamp": "2019-08-24T14:15:22Z",
          "user_account_id": "string"
        },
        "change_info": {
          "host_name": "string",
          "time_stamp": "2019-08-24T14:15:22Z",
          "user_account_id": "string"
        }
      }
    ],
    "remak": [
      {
        "system_user_company_id": "strin",
        "customer_number": "string",
        "customer_remark_id": "string",
        "importance_level_id": "PrimaryRemark",
        "facility_id": "strin",
        "date": "2019-08-24",
        "division": {
          "id": "str",
          "name": "string",
          "group_id": "str"
        },
        "type": {
          "id": "str",
          "name": "string"
        },
        "interlock_system_id": "str",
        "content": "string",
        "subject": "string",
        "output_timing": true,
        "youcom_hotel": {
          "id": "strin",
          "name": "string"
        },
        "youcom_sequence": 0,
        "create_info": {
          "host_name": "string",
          "time_stamp": "2019-08-24T14:15:22Z",
          "user_account_id": "string"
        },
        "change_info": {
          "host_name": "string",
          "time_stamp": "2019-08-24T14:15:22Z",
          "user_account_id": "string"
        }
      }
    ],
    "id": "string",
    "customer_number": "string"
  },
  "reserved_by": {
    "person": {
      "kana_name": "string",
      "name": "string",
      "address": {
        "postal_code": "string",
        "prefecture_code": "string",
        "city": "string",
        "address_line": [
          "string"
        ]
      },
      "phone_no": "000-0000-0000",
      "phone_no_mobile": "000-0000-0000",
      "phone_no_other": "000-0000-0000",
      "gender": "Male",
      "birthday": "2019-08-24",
      "email": "example@example.com",
      "email_sub": "example@example.com",
      "external_customer_Id": "string"
    },
    "remarks": [
      {
        "system_user_company_id": "strin",
        "customer_number": "string",
        "customer_remark_id": "string",
        "importance_level_id": "PrimaryRemark",
        "facility_id": "strin",
        "date": "2019-08-24",
        "division": {
          "id": "str",
          "name": "string",
          "group_id": "str"
        },
        "type": {
          "id": "str",
          "name": "string"
        },
        "interlock_system_id": "str",
        "content": "string",
        "subject": "string",
        "output_timing": true,
        "youcom_hotel": {
          "id": "strin",
          "name": "string"
        },
        "youcom_sequence": 0,
        "create_info": {
          "host_name": "string",
          "time_stamp": "2019-08-24T14:15:22Z",
          "user_account_id": "string"
        },
        "change_info": {
          "host_name": "string",
          "time_stamp": "2019-08-24T14:15:22Z",
          "user_account_id": "string"
        }
      }
    ],
    "remak": [
      {
        "system_user_company_id": "strin",
        "customer_number": "string",
        "customer_remark_id": "string",
        "importance_level_id": "PrimaryRemark",
        "facility_id": "strin",
        "date": "2019-08-24",
        "division": {
          "id": "str",
          "name": "string",
          "group_id": "str"
        },
        "type": {
          "id": "str",
          "name": "string"
        },
        "interlock_system_id": "str",
        "content": "string",
        "subject": "string",
        "output_timing": true,
        "youcom_hotel": {
          "id": "strin",
          "name": "string"
        },
        "youcom_sequence": 0,
        "create_info": {
          "host_name": "string",
          "time_stamp": "2019-08-24T14:15:22Z",
          "user_account_id": "string"
        },
        "change_info": {
          "host_name": "string",
          "time_stamp": "2019-08-24T14:15:22Z",
          "user_account_id": "string"
        }
      }
    ],
    "id": "string",
    "customer_number": "string"
  },
  "remarks": [
    {
      "id": "string",
      "division": {
        "id": "str",
        "name": "string",
        "group_id": "str"
      },
      "remarks_type": {
        "id": "str",
        "name": "string"
      },
      "importance_level": "Primary Remark",
      "subject": "string",
      "content": "string"
    }
  ],
  "reservation_remarks": [
    {
      "id": "string",
      "division": {
        "id": "str",
        "name": "string",
        "group_id": "str"
      },
      "remarks_type": {
        "id": "str",
        "name": "string"
      },
      "importance_level": "Primary Remark",
      "subject": "string",
      "content": "string"
    }
  ],
  "room_reservations": [
    {
      "id": "string",
      "stay_registration_id ": "string",
      "room_number": "string",
      "room_status": "Vacant",
      "guests": [
        {
          "person": {
            "kana_name": "string",
            "name": "string",
            "address": {
              "postal_code": "string",
              "prefecture_code": "string",
              "city": "string",
              "address_line": [
                "string"
              ]
            },
            "phone_no": "000-0000-0000",
            "phone_no_mobile": "000-0000-0000",
            "phone_no_other": "000-0000-0000",
            "gender": "Male",
            "birthday": "2019-08-24",
            "email": "example@example.com",
            "email_sub": "example@example.com",
            "external_customer_Id": "string"
          },
          "remarks": [
            {
              "system_user_company_id": "strin",
              "customer_number": "string",
              "customer_remark_id": "string",
              "importance_level_id": "PrimaryRemark",
              "facility_id": "strin",
              "date": "2019-08-24",
              "division": {
                "id": "str",
                "name": "string",
                "group_id": "str"
              },
              "type": {
                "id": "str",
                "name": "string"
              },
              "interlock_system_id": "str",
              "content": "string",
              "subject": "string",
              "output_timing": true,
              "youcom_hotel": {
                "id": "strin",
                "name": "string"
              },
              "youcom_sequence": 0,
              "create_info": {
                "host_name": "string",
                "time_stamp": "2019-08-24T14:15:22Z",
                "user_account_id": "string"
              },
              "change_info": {
                "host_name": "string",
                "time_stamp": "2019-08-24T14:15:22Z",
                "user_account_id": "string"
              }
            }
          ],
          "remak": [
            {
              "system_user_company_id": "strin",
              "customer_number": "string",
              "customer_remark_id": "string",
              "importance_level_id": "PrimaryRemark",
              "facility_id": "strin",
              "date": "2019-08-24",
              "division": {
                "id": "str",
                "name": "string",
                "group_id": "str"
              },
              "type": {
                "id": "str",
                "name": "string"
              },
              "interlock_system_id": "str",
              "content": "string",
              "subject": "string",
              "output_timing": true,
              "youcom_hotel": {
                "id": "strin",
                "name": "string"
              },
              "youcom_sequence": 0,
              "create_info": {
                "host_name": "string",
                "time_stamp": "2019-08-24T14:15:22Z",
                "user_account_id": "string"
              },
              "change_info": {
                "host_name": "string",
                "time_stamp": "2019-08-24T14:15:22Z",
                "user_account_id": "string"
              }
            }
          ],
          "id": "string",
          "customer_number": "string"
        }
      ],
      "room_type": {
        "code": "string",
        "standard_persons": 0,
        "max_persons": 0,
        "name": "string",
        "short_name": "string",
        "kana_name": "string",
        "foreign_name": "string",
        "foreign_short_name": "string"
      },
      "sales_control_type": "FREE",
      "sales_control_unit": "string",
      "extra_bed_count": 0,
      "stay_period": {
        "arrival_date": "2019-08-24",
        "arrival_time": "14:15:22Z",
        "departure_date": "2019-08-24",
        "departure_time": "14:15:22Z",
        "late_out": true
      },
      "reservation_route": {
        "reservationDisplayName": "string",
        "reservationRoutes": [
          {
            "code": "string",
            "name": "string",
            "short_name": "string",
            "kana_name": "string",
            "foreign_name": "string",
            "foreign_short_name": "string"
          }
        ]
      },
      "agent_reservation_number": "string",
      "agent_course": "string",
      "person_count": [
        0
      ],
      "pricing": {
        "sales_package": {
          "code": "string",
          "name": "string",
          "short_name": "string",
          "kana_name": "string",
          "foreign_name": "string",
          "foreign_short_name": "string",
          "print_name": "string",
          "print_foreign_name": "string"
        },
        "discount_item": {
          "code": "string",
          "name": "string",
          "short_name": "string",
          "kana_name": "string",
          "foreign_name": "string",
          "foreign_short_name": "string",
          "rate": 0,
          "amount": 0
        },
        "discount_rate": 100,
        "discount_amount": 0,
        "pricing_type": "GROSS",
        "price": 0
      },
      "provision_requests": [
        {
          "id": "string",
          "provision": {
            "code": "string",
            "name": "string",
            "short_name": "string",
            "kana_name": "string",
            "foreign_name": "string",
            "foreign_short_name": "string"
          },
          "from_date": "2019-08-24",
          "to_date": "2019-08-24",
          "stock_control": true,
          "quantity": 0,
          "note": "string",
          "reservation_ref": {
            "reservation_id": "string",
            "room_id": "string",
            "stay_id": "string",
            "reservation_number": "string",
            "room_number": "string"
          }
        }
      ],
      "meal_reservations": [
        {
          "id": "string",
          "meal_place": {
            "id": "string",
            "name": "string",
            "short_name": "string",
            "kana_name": "string",
            "foreign_name": "string",
            "foreign_short_name": "string"
          },
          "meal_type": {
            "id": "string",
            "meal_place_code": "string",
            "meal_time_code": "string",
            "start_time": "14:15:22Z",
            "end_time": "14:15:22Z",
            "person_count": 0,
            "table_count": 0
          },
          "meal_time_frame": {
            "id": "string",
            "name": "string",
            "short_name": "string",
            "kana_name": "string",
            "foreign_name": "string",
            "foreign_short_name": "string"
          },
          "use_date": "2019-08-24",
          "meal_kana_name": "string",
          "meal_name": "string",
          "meal_short_name": "string",
          "meal_item": {
            "code": "string",
            "name": "string",
            "short_name": "string",
            "kana_name": "string",
            "foreign_name": "string",
            "foreign_short_name": "string"
          },
          "person_count": 0,
          "person_type": "ADULT",
          "unit_price": 0,
          "pricing_type": "INCLUDED",
          "start_time": "14:15:22Z",
          "end_time": "14:15:22Z",
          "valid": true,
          "note": "string",
          "reservation_ref": {
            "reservation_id": "string",
            "room_id": "string",
            "stay_id": "string",
            "reservation_number": "string",
            "room_number": "string"
          }
        }
      ],
      "deposits": [
        {
          "id": "string",
          "account_date": "2019-08-24",
          "payment_method": {
            "code": "string",
            "name": "string",
            "short_name": "string",
            "kana_name": "string",
            "foreign_name": "string",
            "foreign_short_name": "string",
            "use_address": true
          },
          "billing_provider": {
            "code": "string",
            "name": "string",
            "short_name": "string",
            "kana_name": "string",
            "foreign_name": "string",
            "foreign_short_name": "string"
          },
          "amount": 0,
          "bill_index": 0,
          "bill_note": "string",
          "internal_note": "string",
          "provider_reference": "string",
          "reservation_ref": {
            "reservation_id": "string",
            "room_id": "string",
            "stay_id": "string",
            "reservation_number": "string",
            "room_number": "string"
          }
        }
      ],
      "slip_items": [
        {
          "id": "string",
          "date": "2019-08-24",
          "item": {
            "code": "string",
            "name": "string",
            "short_name": "string",
            "kana_name": "string",
            "foreign_name": "string",
            "price": 0
          },
          "price_per_item": 0,
          "quantity": 0,
          "total_price": 0,
          "bill_index": 0,
          "bill_note": "string",
          "internal_note": "string",
          "tax_free": true,
          "room_type": {
            "code": "string",
            "standard_persons": 0,
            "max_persons": 0,
            "name": "string",
            "short_name": "string",
            "kana_name": "string",
            "foreign_name": "string",
            "foreign_short_name": "string"
          },
          "reservation_ref": {
            "reservation_id": "string",
            "room_id": "string",
            "stay_id": "string",
            "reservation_number": "string",
            "room_number": "string"
          }
        }
      ],
      "extra_services": [
        {
          "id": "string",
          "service_item": {
            "code": "string",
            "name": "string",
            "kana_name": "string",
            "short_name": "string",
            "foreign_name": "string",
            "foreign_short_name": "string"
          },
          "service_period": {
            "arrival_date": "2019-08-24",
            "arrival_time": "14:15:22Z",
            "departure_date": "2019-08-24",
            "departure_time": "14:15:22Z",
            "late_out": true
          },
          "person_count": 0,
          "note": "string",
          "reservation_ref": {
            "reservation_id": "string",
            "room_id": "string",
            "stay_id": "string",
            "reservation_number": "string",
            "room_number": "string"
          }
        }
      ],
      "remarks": [
        {
          "id": "string",
          "division": {
            "id": "str",
            "name": "string",
            "group_id": "str"
          },
          "remarks_type": {
            "id": "str",
            "name": "string"
          },
          "importance_level": "Primary Remark",
          "subject": "string",
          "content": "string"
        }
      ],
      "price_changes": [
        {
          "date_range_end": "2019-08-24",
          "date_range_start": "2019-08-24",
          "prices": [
            {
              "discount_amount": 0,
              "discount_item_id": "string",
              "discount_item_name": "string",
              "discount_rate": 0,
              "person_count": [
                0
              ],
              "person_count_price_calc": 0,
              "price": 0,
              "pricing_type": "GROSS",
              "rate_id": "string",
              "room_type_code": "string",
              "sales_package_id": "string",
              "sales_package_name": "string"
            }
          ]
        }
      ]
    }
  ],
  "is_group": true,
  "total_stay_period": {
    "arrival_date": "2019-08-24",
    "arrival_time": "14:15:22Z",
    "departure_date": "2019-08-24",
    "departure_time": "14:15:22Z",
    "late_out": true
  },
  "marketing_area": {
    "code": "string",
    "name": "string",
    "foreign_name": "string"
  },
  "last_modified": "2019-08-24T14:15:22Z",
  "created": "2019-08-24T14:15:22Z",
  "primary_remark": {
    "id": "string",
    "division": {
      "id": "str",
      "name": "string",
      "group_id": "str"
    },
    "remarks_type": {
      "id": "str",
      "name": "string"
    },
    "importance_level": "Primary Remark",
    "subject": "string",
    "content": "string"
  }
}

```

Reservation

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|false|none|none|
|reservation_number|string|false|none|none|
|check_in_date|[DateWithTime](#schemadatewithtime)|false|none|none|
|check_out_date|[DateWithTime](#schemadatewithtime)|false|none|none|
|room_sales_status|[RoomSalesStatus](#schemaroomsalesstatus)|false|none|none|
|control_status|[ReservationControlStatus](#schemareservationcontrolstatus)|false|none|none|
|person_count|[PersonCount](#schemapersoncount)|false|none|none|
|main_guest|[Guest](#schemaguest)|false|none|Model for a guest|
|reserved_by|[Guest](#schemaguest)|false|none|Model for a guest|
|remarks|[[Remark](#schemaremark)]|false|none|[List of remarks]|
|reservation_remarks|[[Remark](#schemaremark)]|false|none|version 0.1 support|
|room_reservations|[[RoomReservation](#schemaroomreservation)]|false|none|[Model for a room reservation]|
|is_group|boolean|false|none|none|
|total_stay_period|[StayPeriod](#schemastayperiod)|false|none|none|
|marketing_area|[MarketingArea](#schemamarketingarea)|false|none|none|
|last_modified|[Timestamp](#schematimestamp)|false|none|none|
|created|[Timestamp](#schematimestamp)|false|none|none|
|primary_remark|[Remark](#schemaremark)|false|none|List of remarks|

<h2 id="tocS_RoomSalesStatus">RoomSalesStatus</h2>
<!-- backwards compatibility -->
<a id="schemaroomsalesstatus"></a>
<a id="schema_RoomSalesStatus"></a>
<a id="tocSroomsalesstatus"></a>
<a id="tocsroomsalesstatus"></a>

```json
{
  "status": "Fix"
}

```

RoomSalesStatus

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|status|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|status|Fix|
|status|Waiting|
|status|Tentative|

<h2 id="tocS_ReservationControlStatus">ReservationControlStatus</h2>
<!-- backwards compatibility -->
<a id="schemareservationcontrolstatus"></a>
<a id="schema_ReservationControlStatus"></a>
<a id="tocSreservationcontrolstatus"></a>
<a id="tocsreservationcontrolstatus"></a>

```json
{
  "status": "Reserve"
}

```

ReservationControlStatus

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|status|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|status|Reserve|
|status|Cancel|
|status|Stay|
|status|PartialStay|
|status|NoShow|

<h2 id="tocS_PersonCount">PersonCount</h2>
<!-- backwards compatibility -->
<a id="schemapersoncount"></a>
<a id="schema_PersonCount"></a>
<a id="tocSpersoncount"></a>
<a id="tocspersoncount"></a>

```json
[
  0
]

```

PersonCount

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|PersonCount|[integer]|false|none|none|

<h2 id="tocS_Guest">Guest</h2>
<!-- backwards compatibility -->
<a id="schemaguest"></a>
<a id="schema_Guest"></a>
<a id="tocSguest"></a>
<a id="tocsguest"></a>

```json
{
  "person": {
    "kana_name": "string",
    "name": "string",
    "address": {
      "postal_code": "string",
      "prefecture_code": "string",
      "city": "string",
      "address_line": [
        "string"
      ]
    },
    "phone_no": "000-0000-0000",
    "phone_no_mobile": "000-0000-0000",
    "phone_no_other": "000-0000-0000",
    "gender": "Male",
    "birthday": "2019-08-24",
    "email": "example@example.com",
    "email_sub": "example@example.com",
    "external_customer_Id": "string"
  },
  "remarks": [
    {
      "system_user_company_id": "strin",
      "customer_number": "string",
      "customer_remark_id": "string",
      "importance_level_id": "PrimaryRemark",
      "facility_id": "strin",
      "date": "2019-08-24",
      "division": {
        "id": "str",
        "name": "string",
        "group_id": "str"
      },
      "type": {
        "id": "str",
        "name": "string"
      },
      "interlock_system_id": "str",
      "content": "string",
      "subject": "string",
      "output_timing": true,
      "youcom_hotel": {
        "id": "strin",
        "name": "string"
      },
      "youcom_sequence": 0,
      "create_info": {
        "host_name": "string",
        "time_stamp": "2019-08-24T14:15:22Z",
        "user_account_id": "string"
      },
      "change_info": {
        "host_name": "string",
        "time_stamp": "2019-08-24T14:15:22Z",
        "user_account_id": "string"
      }
    }
  ],
  "remak": [
    {
      "system_user_company_id": "strin",
      "customer_number": "string",
      "customer_remark_id": "string",
      "importance_level_id": "PrimaryRemark",
      "facility_id": "strin",
      "date": "2019-08-24",
      "division": {
        "id": "str",
        "name": "string",
        "group_id": "str"
      },
      "type": {
        "id": "str",
        "name": "string"
      },
      "interlock_system_id": "str",
      "content": "string",
      "subject": "string",
      "output_timing": true,
      "youcom_hotel": {
        "id": "strin",
        "name": "string"
      },
      "youcom_sequence": 0,
      "create_info": {
        "host_name": "string",
        "time_stamp": "2019-08-24T14:15:22Z",
        "user_account_id": "string"
      },
      "change_info": {
        "host_name": "string",
        "time_stamp": "2019-08-24T14:15:22Z",
        "user_account_id": "string"
      }
    }
  ],
  "id": "string",
  "customer_number": "string"
}

```

Guest

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|person|[Person](#schemaperson)|false|none|個人情報。phone_noはメイン番号、phone_no_mobileは携帯番号、phone_no_otherはその他の電話番号。emailはメインメールアドレス、email_subは予備のメールアドレス(Personal information.Phone_no is the main number,phone_no_mobile is the mobile number,phone_no_other is the other phone number.email is the main email address,email_sub is the spare email address.)|
|remarks|[[CustomerRemark](#schemacustomerremark)]|false|none|[CustomerNote]|
|remak|[[CustomerRemark](#schemacustomerremark)]|false|none|version 0.1 support|
|id|string|false|none|none|
|customer_number|string|false|none|none|

<h2 id="tocS_CustomerRemark">CustomerRemark</h2>
<!-- backwards compatibility -->
<a id="schemacustomerremark"></a>
<a id="schema_CustomerRemark"></a>
<a id="tocScustomerremark"></a>
<a id="tocscustomerremark"></a>

```json
{
  "system_user_company_id": "strin",
  "customer_number": "string",
  "customer_remark_id": "string",
  "importance_level_id": "PrimaryRemark",
  "facility_id": "strin",
  "date": "2019-08-24",
  "division": {
    "id": "str",
    "name": "string",
    "group_id": "str"
  },
  "type": {
    "id": "str",
    "name": "string"
  },
  "interlock_system_id": "str",
  "content": "string",
  "subject": "string",
  "output_timing": true,
  "youcom_hotel": {
    "id": "strin",
    "name": "string"
  },
  "youcom_sequence": 0,
  "create_info": {
    "host_name": "string",
    "time_stamp": "2019-08-24T14:15:22Z",
    "user_account_id": "string"
  },
  "change_info": {
    "host_name": "string",
    "time_stamp": "2019-08-24T14:15:22Z",
    "user_account_id": "string"
  }
}

```

CustomerRemark

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|system_user_company_id|string|false|none|SystemUserCompanyId|
|customer_number|string|false|none|CustomerNumber|
|customer_remark_id|string|false|none|CustomerNoteId|
|importance_level_id|[ImportanceLevel](#schemaimportancelevel)|false|none|ImportanceLevel|
|facility_id|string|false|none|FacilityId|
|date|[Date](#schemadate)|false|none|日付(Date)|
|division|[Division](#schemadivision)|false|none|none|
|type|[CustomerNoteType](#schemacustomernotetype)|false|none|none|
|interlock_system_id|string|false|none|InterlockSystemId|
|content|string|false|none|Contents|
|subject|string|false|none|ContentsHead|
|output_timing|boolean|false|none|OutputTiming|
|youcom_hotel|[Facility_1](#schemafacility_1)|false|none|none|
|youcom_sequence|integer|false|none|YoucomSequence|
|create_info|[EditInfo](#schemaeditinfo)|false|none|none|
|change_info|[EditInfo](#schemaeditinfo)|false|none|none|

<h2 id="tocS_Remark">Remark</h2>
<!-- backwards compatibility -->
<a id="schemaremark"></a>
<a id="schema_Remark"></a>
<a id="tocSremark"></a>
<a id="tocsremark"></a>

```json
{
  "id": "string",
  "division": {
    "id": "str",
    "name": "string",
    "group_id": "str"
  },
  "remarks_type": {
    "id": "str",
    "name": "string"
  },
  "importance_level": "Primary Remark",
  "subject": "string",
  "content": "string"
}

```

Remark

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|false|none|none|
|division|[Division](#schemadivision)|false|none|none|
|remarks_type|[RemarkType](#schemaremarktype)|false|none|none|
|importance_level|string|false|none|none|
|subject|string|false|none|none|
|content|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|importance_level|Primary Remark|
|importance_level|High|
|importance_level|Standard|
|importance_level|Low|

<h2 id="tocS_RoomReservation">RoomReservation</h2>
<!-- backwards compatibility -->
<a id="schemaroomreservation"></a>
<a id="schema_RoomReservation"></a>
<a id="tocSroomreservation"></a>
<a id="tocsroomreservation"></a>

```json
{
  "id": "string",
  "stay_registration_id ": "string",
  "room_number": "string",
  "room_status": "Vacant",
  "guests": [
    {
      "person": {
        "kana_name": "string",
        "name": "string",
        "address": {
          "postal_code": "string",
          "prefecture_code": "string",
          "city": "string",
          "address_line": [
            "string"
          ]
        },
        "phone_no": "000-0000-0000",
        "phone_no_mobile": "000-0000-0000",
        "phone_no_other": "000-0000-0000",
        "gender": "Male",
        "birthday": "2019-08-24",
        "email": "example@example.com",
        "email_sub": "example@example.com",
        "external_customer_Id": "string"
      },
      "remarks": [
        {
          "system_user_company_id": "strin",
          "customer_number": "string",
          "customer_remark_id": "string",
          "importance_level_id": "PrimaryRemark",
          "facility_id": "strin",
          "date": "2019-08-24",
          "division": {
            "id": "str",
            "name": "string",
            "group_id": "str"
          },
          "type": {
            "id": "str",
            "name": "string"
          },
          "interlock_system_id": "str",
          "content": "string",
          "subject": "string",
          "output_timing": true,
          "youcom_hotel": {
            "id": "strin",
            "name": "string"
          },
          "youcom_sequence": 0,
          "create_info": {
            "host_name": "string",
            "time_stamp": "2019-08-24T14:15:22Z",
            "user_account_id": "string"
          },
          "change_info": {
            "host_name": "string",
            "time_stamp": "2019-08-24T14:15:22Z",
            "user_account_id": "string"
          }
        }
      ],
      "remak": [
        {
          "system_user_company_id": "strin",
          "customer_number": "string",
          "customer_remark_id": "string",
          "importance_level_id": "PrimaryRemark",
          "facility_id": "strin",
          "date": "2019-08-24",
          "division": {
            "id": "str",
            "name": "string",
            "group_id": "str"
          },
          "type": {
            "id": "str",
            "name": "string"
          },
          "interlock_system_id": "str",
          "content": "string",
          "subject": "string",
          "output_timing": true,
          "youcom_hotel": {
            "id": "strin",
            "name": "string"
          },
          "youcom_sequence": 0,
          "create_info": {
            "host_name": "string",
            "time_stamp": "2019-08-24T14:15:22Z",
            "user_account_id": "string"
          },
          "change_info": {
            "host_name": "string",
            "time_stamp": "2019-08-24T14:15:22Z",
            "user_account_id": "string"
          }
        }
      ],
      "id": "string",
      "customer_number": "string"
    }
  ],
  "room_type": {
    "code": "string",
    "standard_persons": 0,
    "max_persons": 0,
    "name": "string",
    "short_name": "string",
    "kana_name": "string",
    "foreign_name": "string",
    "foreign_short_name": "string"
  },
  "sales_control_type": "FREE",
  "sales_control_unit": "string",
  "extra_bed_count": 0,
  "stay_period": {
    "arrival_date": "2019-08-24",
    "arrival_time": "14:15:22Z",
    "departure_date": "2019-08-24",
    "departure_time": "14:15:22Z",
    "late_out": true
  },
  "reservation_route": {
    "reservationDisplayName": "string",
    "reservationRoutes": [
      {
        "code": "string",
        "name": "string",
        "short_name": "string",
        "kana_name": "string",
        "foreign_name": "string",
        "foreign_short_name": "string"
      }
    ]
  },
  "agent_reservation_number": "string",
  "agent_course": "string",
  "person_count": [
    0
  ],
  "pricing": {
    "sales_package": {
      "code": "string",
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string",
      "print_name": "string",
      "print_foreign_name": "string"
    },
    "discount_item": {
      "code": "string",
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string",
      "rate": 0,
      "amount": 0
    },
    "discount_rate": 100,
    "discount_amount": 0,
    "pricing_type": "GROSS",
    "price": 0
  },
  "provision_requests": [
    {
      "id": "string",
      "provision": {
        "code": "string",
        "name": "string",
        "short_name": "string",
        "kana_name": "string",
        "foreign_name": "string",
        "foreign_short_name": "string"
      },
      "from_date": "2019-08-24",
      "to_date": "2019-08-24",
      "stock_control": true,
      "quantity": 0,
      "note": "string",
      "reservation_ref": {
        "reservation_id": "string",
        "room_id": "string",
        "stay_id": "string",
        "reservation_number": "string",
        "room_number": "string"
      }
    }
  ],
  "meal_reservations": [
    {
      "id": "string",
      "meal_place": {
        "id": "string",
        "name": "string",
        "short_name": "string",
        "kana_name": "string",
        "foreign_name": "string",
        "foreign_short_name": "string"
      },
      "meal_type": {
        "id": "string",
        "meal_place_code": "string",
        "meal_time_code": "string",
        "start_time": "14:15:22Z",
        "end_time": "14:15:22Z",
        "person_count": 0,
        "table_count": 0
      },
      "meal_time_frame": {
        "id": "string",
        "name": "string",
        "short_name": "string",
        "kana_name": "string",
        "foreign_name": "string",
        "foreign_short_name": "string"
      },
      "use_date": "2019-08-24",
      "meal_kana_name": "string",
      "meal_name": "string",
      "meal_short_name": "string",
      "meal_item": {
        "code": "string",
        "name": "string",
        "short_name": "string",
        "kana_name": "string",
        "foreign_name": "string",
        "foreign_short_name": "string"
      },
      "person_count": 0,
      "person_type": "ADULT",
      "unit_price": 0,
      "pricing_type": "INCLUDED",
      "start_time": "14:15:22Z",
      "end_time": "14:15:22Z",
      "valid": true,
      "note": "string",
      "reservation_ref": {
        "reservation_id": "string",
        "room_id": "string",
        "stay_id": "string",
        "reservation_number": "string",
        "room_number": "string"
      }
    }
  ],
  "deposits": [
    {
      "id": "string",
      "account_date": "2019-08-24",
      "payment_method": {
        "code": "string",
        "name": "string",
        "short_name": "string",
        "kana_name": "string",
        "foreign_name": "string",
        "foreign_short_name": "string",
        "use_address": true
      },
      "billing_provider": {
        "code": "string",
        "name": "string",
        "short_name": "string",
        "kana_name": "string",
        "foreign_name": "string",
        "foreign_short_name": "string"
      },
      "amount": 0,
      "bill_index": 0,
      "bill_note": "string",
      "internal_note": "string",
      "provider_reference": "string",
      "reservation_ref": {
        "reservation_id": "string",
        "room_id": "string",
        "stay_id": "string",
        "reservation_number": "string",
        "room_number": "string"
      }
    }
  ],
  "slip_items": [
    {
      "id": "string",
      "date": "2019-08-24",
      "item": {
        "code": "string",
        "name": "string",
        "short_name": "string",
        "kana_name": "string",
        "foreign_name": "string",
        "price": 0
      },
      "price_per_item": 0,
      "quantity": 0,
      "total_price": 0,
      "bill_index": 0,
      "bill_note": "string",
      "internal_note": "string",
      "tax_free": true,
      "room_type": {
        "code": "string",
        "standard_persons": 0,
        "max_persons": 0,
        "name": "string",
        "short_name": "string",
        "kana_name": "string",
        "foreign_name": "string",
        "foreign_short_name": "string"
      },
      "reservation_ref": {
        "reservation_id": "string",
        "room_id": "string",
        "stay_id": "string",
        "reservation_number": "string",
        "room_number": "string"
      }
    }
  ],
  "extra_services": [
    {
      "id": "string",
      "service_item": {
        "code": "string",
        "name": "string",
        "kana_name": "string",
        "short_name": "string",
        "foreign_name": "string",
        "foreign_short_name": "string"
      },
      "service_period": {
        "arrival_date": "2019-08-24",
        "arrival_time": "14:15:22Z",
        "departure_date": "2019-08-24",
        "departure_time": "14:15:22Z",
        "late_out": true
      },
      "person_count": 0,
      "note": "string",
      "reservation_ref": {
        "reservation_id": "string",
        "room_id": "string",
        "stay_id": "string",
        "reservation_number": "string",
        "room_number": "string"
      }
    }
  ],
  "remarks": [
    {
      "id": "string",
      "division": {
        "id": "str",
        "name": "string",
        "group_id": "str"
      },
      "remarks_type": {
        "id": "str",
        "name": "string"
      },
      "importance_level": "Primary Remark",
      "subject": "string",
      "content": "string"
    }
  ],
  "price_changes": [
    {
      "date_range_end": "2019-08-24",
      "date_range_start": "2019-08-24",
      "prices": [
        {
          "discount_amount": 0,
          "discount_item_id": "string",
          "discount_item_name": "string",
          "discount_rate": 0,
          "person_count": [
            0
          ],
          "person_count_price_calc": 0,
          "price": 0,
          "pricing_type": "GROSS",
          "rate_id": "string",
          "room_type_code": "string",
          "sales_package_id": "string",
          "sales_package_name": "string"
        }
      ]
    }
  ]
}

```

Room Reservation

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|false|none|none|
|stay_registration_id|string|false|none|none|
|room_number|string|false|none|none|
|room_status|[RoomStatus](#schemaroomstatus)|false|none|none|
|guests|[[Guest](#schemaguest)]|false|none|[Model for a guest]|
|room_type|[RoomType](#schemaroomtype)|false|none|Model for a room type|
|sales_control_type|string|false|none|none|
|sales_control_unit|string|false|none|none|
|extra_bed_count|integer|false|none|none|
|stay_period|[StayPeriod](#schemastayperiod)|false|none|none|
|reservation_route|[ApiReservationRouteResponse](#schemaapireservationrouteresponse)|false|none|none|
|agent_reservation_number|string|false|none|none|
|agent_course|string|false|none|none|
|person_count|[PersonCount](#schemapersoncount)|false|none|none|
|pricing|[Pricing](#schemapricing)|false|none|none|
|provision_requests|[[Provision](#schemaprovision)]|false|none|[Model for a provision request]|
|meal_reservations|[[MealReservation](#schemamealreservation)]|false|none|[Describes detailed meal information for a given guest.]|
|deposits|[[Deposit](#schemadeposit)]|false|none|none|
|slip_items|[[SlipReservation](#schemaslipreservation)]|false|none|none|
|extra_services|[[ExtraServiceReservation](#schemaextraservicereservation)]|false|none|[Describe details for an extra service]|
|remarks|[[Remark](#schemaremark)]|false|none|[List of remarks]|
|price_changes|[[PriceChangeReservation](#schemapricechangereservation)]|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|sales_control_type|FREE|
|sales_control_type|AGENT|
|sales_control_type|BLOCK|
|sales_control_type|WAITING|
|sales_control_type|OOO|
|sales_control_type|TENTATIVE|

<h2 id="tocS_RoomStatus">RoomStatus</h2>
<!-- backwards compatibility -->
<a id="schemaroomstatus"></a>
<a id="schema_RoomStatus"></a>
<a id="tocSroomstatus"></a>
<a id="tocsroomstatus"></a>

```json
"Vacant"

```

RoomStatus

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|RoomStatus|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|RoomStatus|Vacant|
|RoomStatus|Stay|
|RoomStatus|DueOut|
|RoomStatus|Departed|
|RoomStatus|Cleaning|
|RoomStatus|Inspection|
|RoomStatus|OutOfOrder|
|RoomStatus|InterimCheckIn|

<h2 id="tocS_RoomType">RoomType</h2>
<!-- backwards compatibility -->
<a id="schemaroomtype"></a>
<a id="schema_RoomType"></a>
<a id="tocSroomtype"></a>
<a id="tocsroomtype"></a>

```json
{
  "code": "string",
  "standard_persons": 0,
  "max_persons": 0,
  "name": "string",
  "short_name": "string",
  "kana_name": "string",
  "foreign_name": "string",
  "foreign_short_name": "string"
}

```

RoomType

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|string|false|none|none|
|standard_persons|integer|false|none|none|
|max_persons|integer|false|none|none|
|name|string|false|none|none|
|short_name|string|false|none|none|
|kana_name|string|false|none|none|
|foreign_name|string|false|none|none|
|foreign_short_name|string|false|none|none|

<h2 id="tocS_Pricing">Pricing</h2>
<!-- backwards compatibility -->
<a id="schemapricing"></a>
<a id="schema_Pricing"></a>
<a id="tocSpricing"></a>
<a id="tocspricing"></a>

```json
{
  "sales_package": {
    "code": "string",
    "name": "string",
    "short_name": "string",
    "kana_name": "string",
    "foreign_name": "string",
    "foreign_short_name": "string",
    "print_name": "string",
    "print_foreign_name": "string"
  },
  "discount_item": {
    "code": "string",
    "name": "string",
    "short_name": "string",
    "kana_name": "string",
    "foreign_name": "string",
    "foreign_short_name": "string",
    "rate": 0,
    "amount": 0
  },
  "discount_rate": 100,
  "discount_amount": 0,
  "pricing_type": "GROSS",
  "price": 0
}

```

Pricing

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|sales_package|[SalesPackage](#schemasalespackage)|false|none|none|
|discount_item|[Discount](#schemadiscount)|false|none|none|
|discount_rate|number|false|none|none|
|discount_amount|number|false|none|none|
|pricing_type|string|false|none|none|
|price|number|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|pricing_type|GROSS|
|pricing_type|INCLUDE_SV|
|pricing_type|NET|
|pricing_type|DUTY_FREE|
|pricing_type|SERVICE_FREE|
|pricing_type|ROOM_CHARGE|
|pricing_type|COMPLIMENTARY|
|pricing_type|HOUSE_USE|
|pricing_type|SALES_PACKAGE|

<h2 id="tocS_SalesPackage">SalesPackage</h2>
<!-- backwards compatibility -->
<a id="schemasalespackage"></a>
<a id="schema_SalesPackage"></a>
<a id="tocSsalespackage"></a>
<a id="tocssalespackage"></a>

```json
{
  "code": "string",
  "name": "string",
  "short_name": "string",
  "kana_name": "string",
  "foreign_name": "string",
  "foreign_short_name": "string",
  "print_name": "string",
  "print_foreign_name": "string"
}

```

Package

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|string|false|none|none|
|name|string|false|none|none|
|short_name|string|false|none|none|
|kana_name|string|false|none|none|
|foreign_name|string|false|none|none|
|foreign_short_name|string|false|none|none|
|print_name|string|false|none|none|
|print_foreign_name|string|false|none|none|

<h2 id="tocS_Discount">Discount</h2>
<!-- backwards compatibility -->
<a id="schemadiscount"></a>
<a id="schema_Discount"></a>
<a id="tocSdiscount"></a>
<a id="tocsdiscount"></a>

```json
{
  "code": "string",
  "name": "string",
  "short_name": "string",
  "kana_name": "string",
  "foreign_name": "string",
  "foreign_short_name": "string",
  "rate": 0,
  "amount": 0
}

```

Discount

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|string|false|none|none|
|name|string|false|none|none|
|short_name|string|false|none|none|
|kana_name|string|false|none|none|
|foreign_name|string|false|none|none|
|foreign_short_name|string|false|none|none|
|rate|number|false|none|none|
|amount|number|false|none|none|

<h2 id="tocS_Deposit">Deposit</h2>
<!-- backwards compatibility -->
<a id="schemadeposit"></a>
<a id="schema_Deposit"></a>
<a id="tocSdeposit"></a>
<a id="tocsdeposit"></a>

```json
{
  "id": "string",
  "account_date": "2019-08-24",
  "payment_method": {
    "code": "string",
    "name": "string",
    "short_name": "string",
    "kana_name": "string",
    "foreign_name": "string",
    "foreign_short_name": "string",
    "use_address": true
  },
  "billing_provider": {
    "code": "string",
    "name": "string",
    "short_name": "string",
    "kana_name": "string",
    "foreign_name": "string",
    "foreign_short_name": "string"
  },
  "amount": 0,
  "bill_index": 0,
  "bill_note": "string",
  "internal_note": "string",
  "provider_reference": "string",
  "reservation_ref": {
    "reservation_id": "string",
    "room_id": "string",
    "stay_id": "string",
    "reservation_number": "string",
    "room_number": "string"
  }
}

```

Deposit

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|false|none|none|
|account_date|[Date](#schemadate)|false|none|日付(Date)|
|payment_method|[PaymentMethod](#schemapaymentmethod)|false|none|none|
|billing_provider|[BillingProvider](#schemabillingprovider)|false|none|none|
|amount|number|false|none|none|
|bill_index|integer|false|none|none|
|bill_note|string|false|none|none|
|internal_note|string|false|none|none|
|provider_reference|string|false|none|none|
|reservation_ref|[ReservationReference](#schemareservationreference)|false|none|none|

<h2 id="tocS_PaymentMethod">PaymentMethod</h2>
<!-- backwards compatibility -->
<a id="schemapaymentmethod"></a>
<a id="schema_PaymentMethod"></a>
<a id="tocSpaymentmethod"></a>
<a id="tocspaymentmethod"></a>

```json
{
  "code": "string",
  "name": "string",
  "short_name": "string",
  "kana_name": "string",
  "foreign_name": "string",
  "foreign_short_name": "string",
  "use_address": true
}

```

PaymentMethod

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|string|false|none|none|
|name|string|false|none|none|
|short_name|string|false|none|none|
|kana_name|string|false|none|none|
|foreign_name|string|false|none|none|
|foreign_short_name|string|false|none|none|
|use_address|boolean|false|none|none|

<h2 id="tocS_BillingProvider">BillingProvider</h2>
<!-- backwards compatibility -->
<a id="schemabillingprovider"></a>
<a id="schema_BillingProvider"></a>
<a id="tocSbillingprovider"></a>
<a id="tocsbillingprovider"></a>

```json
{
  "code": "string",
  "name": "string",
  "short_name": "string",
  "kana_name": "string",
  "foreign_name": "string",
  "foreign_short_name": "string"
}

```

BillingProvider

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|string|false|none|none|
|name|string|false|none|none|
|short_name|string|false|none|none|
|kana_name|string|false|none|none|
|foreign_name|string|false|none|none|
|foreign_short_name|string|false|none|none|

<h2 id="tocS_SlipReservation">SlipReservation</h2>
<!-- backwards compatibility -->
<a id="schemaslipreservation"></a>
<a id="schema_SlipReservation"></a>
<a id="tocSslipreservation"></a>
<a id="tocsslipreservation"></a>

```json
{
  "id": "string",
  "date": "2019-08-24",
  "item": {
    "code": "string",
    "name": "string",
    "short_name": "string",
    "kana_name": "string",
    "foreign_name": "string",
    "price": 0
  },
  "price_per_item": 0,
  "quantity": 0,
  "total_price": 0,
  "bill_index": 0,
  "bill_note": "string",
  "internal_note": "string",
  "tax_free": true,
  "room_type": {
    "code": "string",
    "standard_persons": 0,
    "max_persons": 0,
    "name": "string",
    "short_name": "string",
    "kana_name": "string",
    "foreign_name": "string",
    "foreign_short_name": "string"
  },
  "reservation_ref": {
    "reservation_id": "string",
    "room_id": "string",
    "stay_id": "string",
    "reservation_number": "string",
    "room_number": "string"
  }
}

```

SlipReservation

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|false|none|none|
|date|[Date](#schemadate)|false|none|日付(Date)|
|item|[SlipReservationItem](#schemaslipreservationitem)|false|none|none|
|price_per_item|number|false|none|none|
|quantity|integer|false|none|none|
|total_price|number|false|none|none|
|bill_index|integer|false|none|none|
|bill_note|string|false|none|none|
|internal_note|string|false|none|none|
|tax_free|boolean|false|none|none|
|room_type|[RoomType](#schemaroomtype)|false|none|Model for a room type|
|reservation_ref|[ReservationReference](#schemareservationreference)|false|none|none|

<h2 id="tocS_SlipReservationItem">SlipReservationItem</h2>
<!-- backwards compatibility -->
<a id="schemaslipreservationitem"></a>
<a id="schema_SlipReservationItem"></a>
<a id="tocSslipreservationitem"></a>
<a id="tocsslipreservationitem"></a>

```json
{
  "code": "string",
  "name": "string",
  "short_name": "string",
  "kana_name": "string",
  "foreign_name": "string",
  "price": 0
}

```

SlipReservationItem

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|string|false|none|none|
|name|string|false|none|none|
|short_name|string|false|none|none|
|kana_name|string|false|none|none|
|foreign_name|string|false|none|none|
|price|number|false|none|none|

<h2 id="tocS_PriceChangeReservation">PriceChangeReservation</h2>
<!-- backwards compatibility -->
<a id="schemapricechangereservation"></a>
<a id="schema_PriceChangeReservation"></a>
<a id="tocSpricechangereservation"></a>
<a id="tocspricechangereservation"></a>

```json
{
  "date_range_end": "2019-08-24",
  "date_range_start": "2019-08-24",
  "prices": [
    {
      "discount_amount": 0,
      "discount_item_id": "string",
      "discount_item_name": "string",
      "discount_rate": 0,
      "person_count": [
        0
      ],
      "person_count_price_calc": 0,
      "price": 0,
      "pricing_type": "GROSS",
      "rate_id": "string",
      "room_type_code": "string",
      "sales_package_id": "string",
      "sales_package_name": "string"
    }
  ]
}

```

PriceChangeReservation

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|date_range_end|[Date](#schemadate)|true|none|日付(Date)|
|date_range_start|[Date](#schemadate)|true|none|日付(Date)|
|prices|[[PriceChangeReservationPrice](#schemapricechangereservationprice)]|true|none|none|

<h2 id="tocS_PriceChangeReservationPrice">PriceChangeReservationPrice</h2>
<!-- backwards compatibility -->
<a id="schemapricechangereservationprice"></a>
<a id="schema_PriceChangeReservationPrice"></a>
<a id="tocSpricechangereservationprice"></a>
<a id="tocspricechangereservationprice"></a>

```json
{
  "discount_amount": 0,
  "discount_item_id": "string",
  "discount_item_name": "string",
  "discount_rate": 0,
  "person_count": [
    0
  ],
  "person_count_price_calc": 0,
  "price": 0,
  "pricing_type": "GROSS",
  "rate_id": "string",
  "room_type_code": "string",
  "sales_package_id": "string",
  "sales_package_name": "string"
}

```

PriceChangeReservationPrice

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|discount_amount|integer|false|none|none|
|discount_item_id|string|false|none|none|
|discount_item_name|string|false|read-only|none|
|discount_rate|integer|false|none|none|
|person_count|[PersonCount](#schemapersoncount)|true|none|none|
|person_count_price_calc|integer|false|none|none|
|price|integer|false|none|none|
|pricing_type|[PricingTypeId](#schemapricingtypeid)|true|none|none|
|rate_id|string|false|none|none|
|room_type_code|string|false|none|none|
|sales_package_id|string|false|none|none|
|sales_package_name|string|false|read-only|none|

<h2 id="tocS_PricingTypeId">PricingTypeId</h2>
<!-- backwards compatibility -->
<a id="schemapricingtypeid"></a>
<a id="schema_PricingTypeId"></a>
<a id="tocSpricingtypeid"></a>
<a id="tocspricingtypeid"></a>

```json
"GROSS"

```

PricingTypeId

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|PricingTypeId|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|PricingTypeId|GROSS|
|PricingTypeId|INCLUDE_SV|
|PricingTypeId|NET|
|PricingTypeId|DUTY_FREE|
|PricingTypeId|SERVICE_FREE|
|PricingTypeId|ROOM_CHARGE|
|PricingTypeId|COMPLIMENTARY|
|PricingTypeId|HOUSE_USE|
|PricingTypeId|SALES_PACKAGE|

<h2 id="tocS_MarketingArea">MarketingArea</h2>
<!-- backwards compatibility -->
<a id="schemamarketingarea"></a>
<a id="schema_MarketingArea"></a>
<a id="tocSmarketingarea"></a>
<a id="tocsmarketingarea"></a>

```json
{
  "code": "string",
  "name": "string",
  "foreign_name": "string"
}

```

MarketingArea

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|string|false|none|none|
|name|string|false|none|none|
|foreign_name|string|false|none|none|

<h2 id="tocS_Person">Person</h2>
<!-- backwards compatibility -->
<a id="schemaperson"></a>
<a id="schema_Person"></a>
<a id="tocSperson"></a>
<a id="tocsperson"></a>

```json
{
  "kana_name": "string",
  "name": "string",
  "address": {
    "postal_code": "string",
    "prefecture_code": "string",
    "city": "string",
    "address_line": [
      "string"
    ]
  },
  "phone_no": "000-0000-0000",
  "phone_no_mobile": "000-0000-0000",
  "phone_no_other": "000-0000-0000",
  "gender": "Male",
  "birthday": "2019-08-24",
  "email": "example@example.com",
  "email_sub": "example@example.com",
  "external_customer_Id": "string"
}

```

個人情報。phone_noはメイン番号、phone_no_mobileは携帯番号、phone_no_otherはその他の電話番号。emailはメインメールアドレス、email_subは予備のメールアドレス(Personal information.Phone_no is the main number,phone_no_mobile is the mobile number,phone_no_other is the other phone number.email is the main email address,email_sub is the spare email address.)

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|kana_name|string|false|none|none|
|name|string|false|none|none|
|address|[Address](#schemaaddress)|false|none|住所(Address)|
|phone_no|[PhoneNumber](#schemaphonenumber)|false|none|電話番号(PhoneNumber)|
|phone_no_mobile|[PhoneNumber](#schemaphonenumber)|false|none|電話番号(PhoneNumber)|
|phone_no_other|[PhoneNumber](#schemaphonenumber)|false|none|電話番号(PhoneNumber)|
|gender|[Gender](#schemagender)|false|none|性別(Gender)|
|birthday|[Date](#schemadate)|false|none|日付(Date)|
|email|[EMail](#schemaemail)|false|none|メールアドレス(EMail)|
|email_sub|[EMail](#schemaemail)|false|none|メールアドレス(EMail)|
|external_customer_Id|string|false|none|外部顧客ID|

<h2 id="tocS_Address">Address</h2>
<!-- backwards compatibility -->
<a id="schemaaddress"></a>
<a id="schema_Address"></a>
<a id="tocSaddress"></a>
<a id="tocsaddress"></a>

```json
{
  "postal_code": "string",
  "prefecture_code": "string",
  "city": "string",
  "address_line": [
    "string"
  ]
}

```

住所(Address)

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|postal_code|[PostalCode](#schemapostalcode)|false|none|郵便番号(PostalCode)|
|prefecture_code|[PrefectureCode](#schemaprefecturecode)|false|none|Ministry of Land, Infrastructure and Transport:Prefectural code[https://nlftp.mlit.go.jp/ksj/gmlold/codelist/PrefCode.html]|
|city|string|false|none|none|
|address_line|[string]|false|none|none|

<h2 id="tocS_PostalCode">PostalCode</h2>
<!-- backwards compatibility -->
<a id="schemapostalcode"></a>
<a id="schema_PostalCode"></a>
<a id="tocSpostalcode"></a>
<a id="tocspostalcode"></a>

```json
"string"

```

Postal Code

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|Postal Code|string(^[0-9\.\-]+)|false|none|郵便番号(PostalCode)|

<h2 id="tocS_PrefectureCode">PrefectureCode</h2>
<!-- backwards compatibility -->
<a id="schemaprefecturecode"></a>
<a id="schema_PrefectureCode"></a>
<a id="tocSprefecturecode"></a>
<a id="tocsprefecturecode"></a>

```json
"string"

```

Prefecture Code

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|Prefecture Code|string(^[0-9]{2,2})|false|none|Ministry of Land, Infrastructure and Transport:Prefectural code[https://nlftp.mlit.go.jp/ksj/gmlold/codelist/PrefCode.html]|

<h2 id="tocS_PhoneNumber">PhoneNumber</h2>
<!-- backwards compatibility -->
<a id="schemaphonenumber"></a>
<a id="schema_PhoneNumber"></a>
<a id="tocSphonenumber"></a>
<a id="tocsphonenumber"></a>

```json
"000-0000-0000"

```

Phone Number

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|Phone Number|string(^[0-9-()+]+)|false|none|電話番号(PhoneNumber)|

<h2 id="tocS_Gender">Gender</h2>
<!-- backwards compatibility -->
<a id="schemagender"></a>
<a id="schema_Gender"></a>
<a id="tocSgender"></a>
<a id="tocsgender"></a>

```json
"Male"

```

Gender

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|Gender|string|false|none|性別(Gender)|

#### Enumerated Values

|Property|Value|
|---|---|
|Gender|Male|
|Gender|Female|
|Gender|Other|

<h2 id="tocS_EMail">EMail</h2>
<!-- backwards compatibility -->
<a id="schemaemail"></a>
<a id="schema_EMail"></a>
<a id="tocSemail"></a>
<a id="tocsemail"></a>

```json
"example@example.com"

```

E-Mail Address

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|E-Mail Address|string(email)|false|none|メールアドレス(EMail)|

<h2 id="tocS_ExternalAgent">ExternalAgent</h2>
<!-- backwards compatibility -->
<a id="schemaexternalagent"></a>
<a id="schema_ExternalAgent"></a>
<a id="tocSexternalagent"></a>
<a id="tocsexternalagent"></a>

```json
{
  "external_agent_type": "TLL",
  "external_agent_code": "string",
  "external_agent_course_name": "string",
  "external_meal_type": "string",
  "external_room_type_id": "string",
  "external_facility_code": "string"
}

```

External Agent

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|external_agent_type|string|false|none|none|
|external_agent_code|string|false|none|none|
|external_agent_course_name|string|false|none|none|
|external_meal_type|string|false|none|none|
|external_room_type_id|string|false|none|none|
|external_facility_code|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|external_agent_type|TLL|
|external_agent_type|Neppan|
|external_agent_type|Rakutu|
|external_agent_type|Tema|

<h2 id="tocS_ApiCreateRequest">ApiCreateRequest</h2>
<!-- backwards compatibility -->
<a id="schemaapicreaterequest"></a>
<a id="schema_ApiCreateRequest"></a>
<a id="tocSapicreaterequest"></a>
<a id="tocsapicreaterequest"></a>

```json
{}

```

ApiCreateRequest

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|ApiCreateRequest|[ApiRequest](#schemaapirequest)|false|none|none|

<h2 id="tocS_ApiCreateResponse">ApiCreateResponse</h2>
<!-- backwards compatibility -->
<a id="schemaapicreateresponse"></a>
<a id="schema_ApiCreateResponse"></a>
<a id="tocSapicreateresponse"></a>
<a id="tocsapicreateresponse"></a>

```json
{
  "request": {
    "version": "string",
    "body": "string",
    "url": "string"
  },
  "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce"
}

```

ApiCreateResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|ApiCreateResponse|[ApiResponse](#schemaapiresponse)|false|none|none|

<h2 id="tocS_RoomTypeGroup">RoomTypeGroup</h2>
<!-- backwards compatibility -->
<a id="schemaroomtypegroup"></a>
<a id="schema_RoomTypeGroup"></a>
<a id="tocSroomtypegroup"></a>
<a id="tocsroomtypegroup"></a>

```json
{
  "id": "string",
  "name": "string",
  "short_name": "string",
  "kana_name": "string",
  "foereign_name": "string",
  "foreign_short_name": "string"
}

```

RoomTypeGroup

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|false|none|none|
|name|string|false|none|none|
|short_name|string|false|none|none|
|kana_name|string|false|none|none|
|foereign_name|string|false|none|none|
|foreign_short_name|string|false|none|none|

<h2 id="tocS_RoomNumber">RoomNumber</h2>
<!-- backwards compatibility -->
<a id="schemaroomnumber"></a>
<a id="schema_RoomNumber"></a>
<a id="tocSroomnumber"></a>
<a id="tocsroomnumber"></a>

```json
{
  "room_number": "string",
  "floor_id": "string",
  "room_type": {
    "code": "string",
    "standard_persons": 0,
    "max_persons": 0,
    "name": "string",
    "short_name": "string",
    "kana_name": "string",
    "foreign_name": "string",
    "foreign_short_name": "string"
  },
  "vacant_days": 0,
  "stay_count": 0
}

```

RoomNumber

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|room_number|string|false|none|none|
|floor_id|string|false|none|none|
|room_type|[RoomType](#schemaroomtype)|false|none|Model for a room type|
|vacant_days|integer|false|none|none|
|stay_count|integer|false|none|none|

<h2 id="tocS_SalesAccountItem">SalesAccountItem</h2>
<!-- backwards compatibility -->
<a id="schemasalesaccountitem"></a>
<a id="schema_SalesAccountItem"></a>
<a id="tocSsalesaccountitem"></a>
<a id="tocssalesaccountitem"></a>

```json
{
  "id": "string",
  "mid_group_id": "string",
  "kana_nane": "string",
  "name": "string",
  "short_name": "string",
  "use": true,
  "consumption_tax_calc_type_id": "st",
  "consumption_tax_charge": true,
  "sequence": 0,
  "base_unit_price": 0,
  "unit_price_exclude_tax": 0,
  "tax_rate": 0
}

```

SalesAccountItem

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|false|none|none|
|mid_group_id|string|false|none|none|
|kana_nane|string|false|none|none|
|name|string|false|none|none|
|short_name|string|false|none|none|
|use|boolean|false|none|none|
|consumption_tax_calc_type_id|string|false|none|none|
|consumption_tax_charge|boolean|false|none|none|
|sequence|integer|false|none|none|
|base_unit_price|number(double)|false|none|none|
|unit_price_exclude_tax|number(double)|false|none|none|
|tax_rate|number(double)|false|none|none|

<h2 id="tocS_Stay">Stay</h2>
<!-- backwards compatibility -->
<a id="schemastay"></a>
<a id="schema_Stay"></a>
<a id="tocSstay"></a>
<a id="tocsstay"></a>

```json
{
  "id ": "string",
  "reservation_number": "string",
  "check_in_date": "string",
  "check_out_date": "string",
  "room_sales_status": {
    "status": "Fix"
  },
  "control_status": {
    "status": "Reserve"
  },
  "person_count": [
    3,
    3,
    3,
    3,
    3,
    3
  ],
  "main_guest": {
    "person": {
      "kana_name": "string",
      "name": "string",
      "address": {
        "postal_code": "string",
        "prefecture_code": "string",
        "city": "string",
        "address_line": [
          "string"
        ]
      },
      "phone_no": "000-0000-0000",
      "phone_no_mobile": "000-0000-0000",
      "phone_no_other": "000-0000-0000",
      "gender": "Male",
      "birthday": "2019-08-24",
      "email": "example@example.com",
      "email_sub": "example@example.com",
      "external_customer_Id": "string"
    },
    "remarks": [
      {
        "system_user_company_id": "strin",
        "customer_number": "string",
        "customer_remark_id": "string",
        "importance_level_id": "PrimaryRemark",
        "facility_id": "strin",
        "date": "2019-08-24",
        "division": {
          "id": "str",
          "name": "string",
          "group_id": "str"
        },
        "type": {
          "id": "str",
          "name": "string"
        },
        "interlock_system_id": "str",
        "content": "string",
        "subject": "string",
        "output_timing": true,
        "youcom_hotel": {
          "id": "strin",
          "name": "string"
        },
        "youcom_sequence": 0,
        "create_info": {
          "host_name": "string",
          "time_stamp": "2019-08-24T14:15:22Z",
          "user_account_id": "string"
        },
        "change_info": {
          "host_name": "string",
          "time_stamp": "2019-08-24T14:15:22Z",
          "user_account_id": "string"
        }
      }
    ],
    "remak": [
      {
        "system_user_company_id": "strin",
        "customer_number": "string",
        "customer_remark_id": "string",
        "importance_level_id": "PrimaryRemark",
        "facility_id": "strin",
        "date": "2019-08-24",
        "division": {
          "id": "str",
          "name": "string",
          "group_id": "str"
        },
        "type": {
          "id": "str",
          "name": "string"
        },
        "interlock_system_id": "str",
        "content": "string",
        "subject": "string",
        "output_timing": true,
        "youcom_hotel": {
          "id": "strin",
          "name": "string"
        },
        "youcom_sequence": 0,
        "create_info": {
          "host_name": "string",
          "time_stamp": "2019-08-24T14:15:22Z",
          "user_account_id": "string"
        },
        "change_info": {
          "host_name": "string",
          "time_stamp": "2019-08-24T14:15:22Z",
          "user_account_id": "string"
        }
      }
    ],
    "id": "string",
    "customer_number": "string"
  },
  "reserved_by": {
    "person": {
      "kana_name": "string",
      "name": "string",
      "address": {
        "postal_code": "string",
        "prefecture_code": "string",
        "city": "string",
        "address_line": [
          "string"
        ]
      },
      "phone_no": "000-0000-0000",
      "phone_no_mobile": "000-0000-0000",
      "phone_no_other": "000-0000-0000",
      "gender": "Male",
      "birthday": "2019-08-24",
      "email": "example@example.com",
      "email_sub": "example@example.com",
      "external_customer_Id": "string"
    },
    "remarks": [
      {
        "system_user_company_id": "strin",
        "customer_number": "string",
        "customer_remark_id": "string",
        "importance_level_id": "PrimaryRemark",
        "facility_id": "strin",
        "date": "2019-08-24",
        "division": {
          "id": "str",
          "name": "string",
          "group_id": "str"
        },
        "type": {
          "id": "str",
          "name": "string"
        },
        "interlock_system_id": "str",
        "content": "string",
        "subject": "string",
        "output_timing": true,
        "youcom_hotel": {
          "id": "strin",
          "name": "string"
        },
        "youcom_sequence": 0,
        "create_info": {
          "host_name": "string",
          "time_stamp": "2019-08-24T14:15:22Z",
          "user_account_id": "string"
        },
        "change_info": {
          "host_name": "string",
          "time_stamp": "2019-08-24T14:15:22Z",
          "user_account_id": "string"
        }
      }
    ],
    "remak": [
      {
        "system_user_company_id": "strin",
        "customer_number": "string",
        "customer_remark_id": "string",
        "importance_level_id": "PrimaryRemark",
        "facility_id": "strin",
        "date": "2019-08-24",
        "division": {
          "id": "str",
          "name": "string",
          "group_id": "str"
        },
        "type": {
          "id": "str",
          "name": "string"
        },
        "interlock_system_id": "str",
        "content": "string",
        "subject": "string",
        "output_timing": true,
        "youcom_hotel": {
          "id": "strin",
          "name": "string"
        },
        "youcom_sequence": 0,
        "create_info": {
          "host_name": "string",
          "time_stamp": "2019-08-24T14:15:22Z",
          "user_account_id": "string"
        },
        "change_info": {
          "host_name": "string",
          "time_stamp": "2019-08-24T14:15:22Z",
          "user_account_id": "string"
        }
      }
    ],
    "id": "string",
    "customer_number": "string"
  },
  "remarks": [
    {
      "id": "string",
      "division": {
        "id": "str",
        "name": "string",
        "group_id": "str"
      },
      "remarks_type": {
        "id": "str",
        "name": "string"
      },
      "importance_level": "Primary Remark",
      "subject": "string",
      "content": "string"
    }
  ],
  "reservation_remarks": [
    {
      "id": "string",
      "division": {
        "id": "str",
        "name": "string",
        "group_id": "str"
      },
      "remarks_type": {
        "id": "str",
        "name": "string"
      },
      "importance_level": "Primary Remark",
      "subject": "string",
      "content": "string"
    }
  ],
  "room_reservation": {
    "id": "string",
    "stay_registration_id ": "string",
    "room_number": "string",
    "room_status": "Vacant",
    "guests": [
      {
        "person": {
          "kana_name": "string",
          "name": "string",
          "address": {
            "postal_code": "string",
            "prefecture_code": "string",
            "city": "string",
            "address_line": [
              "string"
            ]
          },
          "phone_no": "000-0000-0000",
          "phone_no_mobile": "000-0000-0000",
          "phone_no_other": "000-0000-0000",
          "gender": "Male",
          "birthday": "2019-08-24",
          "email": "example@example.com",
          "email_sub": "example@example.com",
          "external_customer_Id": "string"
        },
        "remarks": [
          {
            "system_user_company_id": "strin",
            "customer_number": "string",
            "customer_remark_id": "string",
            "importance_level_id": "PrimaryRemark",
            "facility_id": "strin",
            "date": "2019-08-24",
            "division": {
              "id": "str",
              "name": "string",
              "group_id": "str"
            },
            "type": {
              "id": "str",
              "name": "string"
            },
            "interlock_system_id": "str",
            "content": "string",
            "subject": "string",
            "output_timing": true,
            "youcom_hotel": {
              "id": "strin",
              "name": "string"
            },
            "youcom_sequence": 0,
            "create_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            },
            "change_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            }
          }
        ],
        "remak": [
          {
            "system_user_company_id": "strin",
            "customer_number": "string",
            "customer_remark_id": "string",
            "importance_level_id": "PrimaryRemark",
            "facility_id": "strin",
            "date": "2019-08-24",
            "division": {
              "id": "str",
              "name": "string",
              "group_id": "str"
            },
            "type": {
              "id": "str",
              "name": "string"
            },
            "interlock_system_id": "str",
            "content": "string",
            "subject": "string",
            "output_timing": true,
            "youcom_hotel": {
              "id": "strin",
              "name": "string"
            },
            "youcom_sequence": 0,
            "create_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            },
            "change_info": {
              "host_name": "string",
              "time_stamp": "2019-08-24T14:15:22Z",
              "user_account_id": "string"
            }
          }
        ],
        "id": "string",
        "customer_number": "string"
      }
    ],
    "room_type": {
      "code": "string",
      "standard_persons": 0,
      "max_persons": 0,
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    },
    "sales_control_type": "FREE",
    "sales_control_unit": "string",
    "extra_bed_count": 0,
    "stay_period": {
      "arrival_date": "2019-08-24",
      "arrival_time": "14:15:22Z",
      "departure_date": "2019-08-24",
      "departure_time": "14:15:22Z",
      "late_out": true
    },
    "reservation_route": {
      "reservationDisplayName": "string",
      "reservationRoutes": [
        {
          "code": "string",
          "name": "string",
          "short_name": "string",
          "kana_name": "string",
          "foreign_name": "string",
          "foreign_short_name": "string"
        }
      ]
    },
    "agent_reservation_number": "string",
    "agent_course": "string",
    "person_count": [
      0
    ],
    "pricing": {
      "sales_package": {
        "code": "string",
        "name": "string",
        "short_name": "string",
        "kana_name": "string",
        "foreign_name": "string",
        "foreign_short_name": "string",
        "print_name": "string",
        "print_foreign_name": "string"
      },
      "discount_item": {
        "code": "string",
        "name": "string",
        "short_name": "string",
        "kana_name": "string",
        "foreign_name": "string",
        "foreign_short_name": "string",
        "rate": 0,
        "amount": 0
      },
      "discount_rate": 100,
      "discount_amount": 0,
      "pricing_type": "GROSS",
      "price": 0
    },
    "provision_requests": [
      {
        "id": "string",
        "provision": {
          "code": "string",
          "name": "string",
          "short_name": "string",
          "kana_name": "string",
          "foreign_name": "string",
          "foreign_short_name": "string"
        },
        "from_date": "2019-08-24",
        "to_date": "2019-08-24",
        "stock_control": true,
        "quantity": 0,
        "note": "string",
        "reservation_ref": {
          "reservation_id": "string",
          "room_id": "string",
          "stay_id": "string",
          "reservation_number": "string",
          "room_number": "string"
        }
      }
    ],
    "meal_reservations": [
      {
        "id": "string",
        "meal_place": {
          "id": "string",
          "name": "string",
          "short_name": "string",
          "kana_name": "string",
          "foreign_name": "string",
          "foreign_short_name": "string"
        },
        "meal_type": {
          "id": "string",
          "meal_place_code": "string",
          "meal_time_code": "string",
          "start_time": "14:15:22Z",
          "end_time": "14:15:22Z",
          "person_count": 0,
          "table_count": 0
        },
        "meal_time_frame": {
          "id": "string",
          "name": "string",
          "short_name": "string",
          "kana_name": "string",
          "foreign_name": "string",
          "foreign_short_name": "string"
        },
        "use_date": "2019-08-24",
        "meal_kana_name": "string",
        "meal_name": "string",
        "meal_short_name": "string",
        "meal_item": {
          "code": "string",
          "name": "string",
          "short_name": "string",
          "kana_name": "string",
          "foreign_name": "string",
          "foreign_short_name": "string"
        },
        "person_count": 0,
        "person_type": "ADULT",
        "unit_price": 0,
        "pricing_type": "INCLUDED",
        "start_time": "14:15:22Z",
        "end_time": "14:15:22Z",
        "valid": true,
        "note": "string",
        "reservation_ref": {
          "reservation_id": "string",
          "room_id": "string",
          "stay_id": "string",
          "reservation_number": "string",
          "room_number": "string"
        }
      }
    ],
    "deposits": [
      {
        "id": "string",
        "account_date": "2019-08-24",
        "payment_method": {
          "code": "string",
          "name": "string",
          "short_name": "string",
          "kana_name": "string",
          "foreign_name": "string",
          "foreign_short_name": "string",
          "use_address": true
        },
        "billing_provider": {
          "code": "string",
          "name": "string",
          "short_name": "string",
          "kana_name": "string",
          "foreign_name": "string",
          "foreign_short_name": "string"
        },
        "amount": 0,
        "bill_index": 0,
        "bill_note": "string",
        "internal_note": "string",
        "provider_reference": "string",
        "reservation_ref": {
          "reservation_id": "string",
          "room_id": "string",
          "stay_id": "string",
          "reservation_number": "string",
          "room_number": "string"
        }
      }
    ],
    "slip_items": [
      {
        "id": "string",
        "date": "2019-08-24",
        "item": {
          "code": "string",
          "name": "string",
          "short_name": "string",
          "kana_name": "string",
          "foreign_name": "string",
          "price": 0
        },
        "price_per_item": 0,
        "quantity": 0,
        "total_price": 0,
        "bill_index": 0,
        "bill_note": "string",
        "internal_note": "string",
        "tax_free": true,
        "room_type": {
          "code": "string",
          "standard_persons": 0,
          "max_persons": 0,
          "name": "string",
          "short_name": "string",
          "kana_name": "string",
          "foreign_name": "string",
          "foreign_short_name": "string"
        },
        "reservation_ref": {
          "reservation_id": "string",
          "room_id": "string",
          "stay_id": "string",
          "reservation_number": "string",
          "room_number": "string"
        }
      }
    ],
    "extra_services": [
      {
        "id": "string",
        "service_item": {
          "code": "string",
          "name": "string",
          "kana_name": "string",
          "short_name": "string",
          "foreign_name": "string",
          "foreign_short_name": "string"
        },
        "service_period": {
          "arrival_date": "2019-08-24",
          "arrival_time": "14:15:22Z",
          "departure_date": "2019-08-24",
          "departure_time": "14:15:22Z",
          "late_out": true
        },
        "person_count": 0,
        "note": "string",
        "reservation_ref": {
          "reservation_id": "string",
          "room_id": "string",
          "stay_id": "string",
          "reservation_number": "string",
          "room_number": "string"
        }
      }
    ],
    "remarks": [
      {
        "id": "string",
        "division": {
          "id": "str",
          "name": "string",
          "group_id": "str"
        },
        "remarks_type": {
          "id": "str",
          "name": "string"
        },
        "importance_level": "Primary Remark",
        "subject": "string",
        "content": "string"
      }
    ],
    "price_changes": [
      {
        "date_range_end": "2019-08-24",
        "date_range_start": "2019-08-24",
        "prices": [
          {
            "discount_amount": 0,
            "discount_item_id": "string",
            "discount_item_name": "string",
            "discount_rate": 0,
            "person_count": [
              0
            ],
            "person_count_price_calc": 0,
            "price": 0,
            "pricing_type": "GROSS",
            "rate_id": "string",
            "room_type_code": "string",
            "sales_package_id": "string",
            "sales_package_name": "string"
          }
        ]
      }
    ]
  }
}

```

Stay

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|false|none|none|
|reservation_number|string|false|none|none|
|check_in_date|[DateWithTime](#schemadatewithtime)|false|none|none|
|check_out_date|[DateWithTime](#schemadatewithtime)|false|none|none|
|room_sales_status|[RoomSalesStatus](#schemaroomsalesstatus)|false|none|none|
|control_status|[ReservationControlStatus](#schemareservationcontrolstatus)|false|none|none|
|person_count|[integer]|false|none|Index「0」＝ManIndex「1」＝Women Index「2」= ChildA Index「3」= ChildA Index「4」= ChildC Index「5」= ChildD|
|main_guest|[Guest](#schemaguest)|false|none|Model for a guest|
|reserved_by|[Guest](#schemaguest)|false|none|Model for a guest|
|remarks|[[Remark](#schemaremark)]|false|none|[List of remarks]|
|reservation_remarks|[[Remark](#schemaremark)]|false|none|version 0.1 support|
|room_reservation|[RoomReservation](#schemaroomreservation)|false|none|Model for a room reservation|

<h2 id="tocS_Revenue">Revenue</h2>
<!-- backwards compatibility -->
<a id="schemarevenue"></a>
<a id="schema_Revenue"></a>
<a id="tocSrevenue"></a>
<a id="tocsrevenue"></a>

```json
{
  "date": "2019-08-24",
  "no": "string",
  "bill_index": "string",
  "pricing_type": "string",
  "name": "string",
  "standard_rate": "string",
  "sale_rate": "string",
  "package_rate_type": "string",
  "discount_rate": 0,
  "discount_amount": 0,
  "rate_per_person": 0,
  "rate_per_room": 0,
  "person_count": [
    0
  ],
  "number_of_use": 0,
  "number_of_room": 0,
  "sales_amount": 0,
  "service_charge": 0,
  "hotel_tax": 0,
  "bath_tax": 0,
  "meal_amount": 0,
  "tax_include": 0,
  "deposit": 0,
  "total": 0
}

```

Revenue

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|date|[Date](#schemadate)|false|none|日付(Date)|
|no|string|false|none|none|
|bill_index|string|false|none|none|
|pricing_type|string|false|none|none|
|name|string|false|none|none|
|standard_rate|string|false|none|none|
|sale_rate|string|false|none|none|
|package_rate_type|string|false|none|none|
|discount_rate|number(double)|false|none|none|
|discount_amount|number(double)|false|none|none|
|rate_per_person|number(double)|false|none|none|
|rate_per_room|number(double)|false|none|none|
|person_count|[PersonCount](#schemapersoncount)|false|none|none|
|number_of_use|integer|false|none|none|
|number_of_room|integer|false|none|none|
|sales_amount|number(double)|false|none|none|
|service_charge|number(double)|false|none|none|
|hotel_tax|number(double)|false|none|none|
|bath_tax|number(double)|false|none|none|
|meal_amount|number(double)|false|none|none|
|tax_include|number(double)|false|none|none|
|deposit|number(double)|false|none|none|
|total|number(double)|false|none|none|

<h2 id="tocS_OutOfOrder">OutOfOrder</h2>
<!-- backwards compatibility -->
<a id="schemaoutoforder"></a>
<a id="schema_OutOfOrder"></a>
<a id="tocSoutoforder"></a>
<a id="tocsoutoforder"></a>

```json
{
  "room_number": "string",
  "out_of_order_id": "string",
  "reason_name": "string",
  "room_floor_id": "string",
  "date_range_start": "2019-08-24",
  "date_range_end": "2019-08-24"
}

```

OutOfOrder

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|OutOfOrder|any|false|none|Out Of Order|

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[OutOfOrderStatic](#schemaoutoforderstatic)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[OutOfOrderDynamic](#schemaoutoforderdynamic)|false|none|none|

<h2 id="tocS_OutOfOrderStatic">OutOfOrderStatic</h2>
<!-- backwards compatibility -->
<a id="schemaoutoforderstatic"></a>
<a id="schema_OutOfOrderStatic"></a>
<a id="tocSoutoforderstatic"></a>
<a id="tocsoutoforderstatic"></a>

```json
{
  "room_number": "string"
}

```

OutOfOrderStatic

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|room_number|string|true|none|none|

<h2 id="tocS_OutOfOrderDynamic">OutOfOrderDynamic</h2>
<!-- backwards compatibility -->
<a id="schemaoutoforderdynamic"></a>
<a id="schema_OutOfOrderDynamic"></a>
<a id="tocSoutoforderdynamic"></a>
<a id="tocsoutoforderdynamic"></a>

```json
{
  "out_of_order_id": "string",
  "reason_name": "string",
  "room_floor_id": "string",
  "date_range_start": "2019-08-24",
  "date_range_end": "2019-08-24"
}

```

OutOfOrderDynamic

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|out_of_order_id|string|false|read-only|none|
|reason_name|string|false|none|none|
|room_floor_id|string|false|read-only|none|
|date_range_start|[Date](#schemadate)|true|none|日付(Date)|
|date_range_end|[Date](#schemadate)|true|none|日付(Date)|

<h2 id="tocS_BillingRequest">BillingRequest</h2>
<!-- backwards compatibility -->
<a id="schemabillingrequest"></a>
<a id="schema_BillingRequest"></a>
<a id="tocSbillingrequest"></a>
<a id="tocsbillingrequest"></a>

```json
{
  "bill_address_id": "string",
  "bill_address_name": "string",
  "bill_index": 0,
  "bill_to_name": "string",
  "bill_to_option_id": "Guest",
  "payment_method_id": "string",
  "payment_method_name": "string",
  "conditions": [
    {
      "item_id": "string",
      "item_name": "string"
    }
  ]
}

```

BillingRequest

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|bill_address_id|string|false|none|none|
|bill_address_name|string|false|read-only|none|
|bill_index|integer|false|read-only|none|
|bill_to_name|string|false|none|none|
|bill_to_option_id|[BillingToOption](#schemabillingtooption)|true|none|BillingToOption|
|payment_method_id|string|false|none|none|
|payment_method_name|string|false|read-only|none|
|conditions|[[BillingRequestCondition](#schemabillingrequestcondition)]|false|none|none|

<h2 id="tocS_BillingRequestCondition">BillingRequestCondition</h2>
<!-- backwards compatibility -->
<a id="schemabillingrequestcondition"></a>
<a id="schema_BillingRequestCondition"></a>
<a id="tocSbillingrequestcondition"></a>
<a id="tocsbillingrequestcondition"></a>

```json
{
  "item_id": "string",
  "item_name": "string"
}

```

BillingRequestCondition

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|item_id|string|false|none|none|
|item_name|string|false|read-only|none|

<h2 id="tocS_Time">Time</h2>
<!-- backwards compatibility -->
<a id="schematime"></a>
<a id="schema_Time"></a>
<a id="tocStime"></a>
<a id="tocstime"></a>

```json
"14:15:22Z"

```

Time

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|Time|string(time)|false|none|時間(Time)|

<h2 id="tocS_DateWithTime">DateWithTime</h2>
<!-- backwards compatibility -->
<a id="schemadatewithtime"></a>
<a id="schema_DateWithTime"></a>
<a id="tocSdatewithtime"></a>
<a id="tocsdatewithtime"></a>

```json
"string"

```

DateTime

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|DateTime|string|false|none|none|

<h2 id="tocS_Timestamp">Timestamp</h2>
<!-- backwards compatibility -->
<a id="schematimestamp"></a>
<a id="schema_Timestamp"></a>
<a id="tocStimestamp"></a>
<a id="tocstimestamp"></a>

```json
"2019-08-24T14:15:22Z"

```

Timestamp

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|Timestamp|string(date-time)|false|none|none|

<h2 id="tocS_ImportanceLevel">ImportanceLevel</h2>
<!-- backwards compatibility -->
<a id="schemaimportancelevel"></a>
<a id="schema_ImportanceLevel"></a>
<a id="tocSimportancelevel"></a>
<a id="tocsimportancelevel"></a>

```json
"PrimaryRemark"

```

ImportanceLevel

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|ImportanceLevel|string|false|none|ImportanceLevel|

#### Enumerated Values

|Property|Value|
|---|---|
|ImportanceLevel|PrimaryRemark|
|ImportanceLevel|High|
|ImportanceLevel|Standard|
|ImportanceLevel|Low|

<h2 id="tocS_Division">Division</h2>
<!-- backwards compatibility -->
<a id="schemadivision"></a>
<a id="schema_Division"></a>
<a id="tocSdivision"></a>
<a id="tocsdivision"></a>

```json
{
  "id": "str",
  "name": "string",
  "group_id": "str"
}

```

Division

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|false|none|none|
|name|string|false|none|none|
|group_id|string|false|none|DivisionGroupId|

<h2 id="tocS_CustomerNoteType">CustomerNoteType</h2>
<!-- backwards compatibility -->
<a id="schemacustomernotetype"></a>
<a id="schema_CustomerNoteType"></a>
<a id="tocScustomernotetype"></a>
<a id="tocscustomernotetype"></a>

```json
{
  "id": "str",
  "name": "string"
}

```

CustomerNoteType

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|false|none|none|
|name|string|false|none|none|

<h2 id="tocS_Facility_1">Facility_1</h2>
<!-- backwards compatibility -->
<a id="schemafacility_1"></a>
<a id="schema_Facility_1"></a>
<a id="tocSfacility_1"></a>
<a id="tocsfacility_1"></a>

```json
{
  "id": "strin",
  "name": "string"
}

```

Facility

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|false|none|none|
|name|string|false|none|none|

<h2 id="tocS_EditInfo">EditInfo</h2>
<!-- backwards compatibility -->
<a id="schemaeditinfo"></a>
<a id="schema_EditInfo"></a>
<a id="tocSeditinfo"></a>
<a id="tocseditinfo"></a>

```json
{
  "host_name": "string",
  "time_stamp": "2019-08-24T14:15:22Z",
  "user_account_id": "string"
}

```

EditInfo

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|host_name|string|false|none|none|
|time_stamp|string(date-time)|false|none|none|
|user_account_id|string|false|none|none|

<h2 id="tocS_RemarkType">RemarkType</h2>
<!-- backwards compatibility -->
<a id="schemaremarktype"></a>
<a id="schema_RemarkType"></a>
<a id="tocSremarktype"></a>
<a id="tocsremarktype"></a>

```json
{
  "id": "str",
  "name": "string"
}

```

RemarkType

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|false|none|none|
|name|string|false|none|none|

<h2 id="tocS_ApiReservationRouteResponse">ApiReservationRouteResponse</h2>
<!-- backwards compatibility -->
<a id="schemaapireservationrouteresponse"></a>
<a id="schema_ApiReservationRouteResponse"></a>
<a id="tocSapireservationrouteresponse"></a>
<a id="tocsapireservationrouteresponse"></a>

```json
{
  "reservationDisplayName": "string",
  "reservationRoutes": [
    {
      "code": "string",
      "name": "string",
      "short_name": "string",
      "kana_name": "string",
      "foreign_name": "string",
      "foreign_short_name": "string"
    }
  ]
}

```

ApiReservationRouteResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|reservationDisplayName|string|false|none|none|
|reservationRoutes|[[ReservationRoute](#schemareservationroute)]|false|none|none|

<h2 id="tocS_BillingToOption">BillingToOption</h2>
<!-- backwards compatibility -->
<a id="schemabillingtooption"></a>
<a id="schema_BillingToOption"></a>
<a id="tocSbillingtooption"></a>
<a id="tocsbillingtooption"></a>

```json
"Guest"

```

BillingToOption

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|BillingToOption|string|false|none|BillingToOption|

#### Enumerated Values

|Property|Value|
|---|---|
|BillingToOption|Guest|
|BillingToOption|Company|
|BillingToOption|OverWrite|
|BillingToOption|GueAndCom|
|BillingToOption|PrivateG|
|BillingToOption|PrivateC|
|BillingToOption|PrivateO|

<h2 id="tocS_ReservationRoute">ReservationRoute</h2>
<!-- backwards compatibility -->
<a id="schemareservationroute"></a>
<a id="schema_ReservationRoute"></a>
<a id="tocSreservationroute"></a>
<a id="tocsreservationroute"></a>

```json
{
  "code": "string",
  "name": "string",
  "short_name": "string",
  "kana_name": "string",
  "foreign_name": "string",
  "foreign_short_name": "string"
}

```

ReservationRoute

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|string|false|none|none|
|name|string|false|none|none|
|short_name|string|false|none|none|
|kana_name|string|false|none|none|
|foreign_name|string|false|none|none|
|foreign_short_name|string|false|none|none|

