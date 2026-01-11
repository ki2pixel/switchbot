# IFTTT Service API reference

This document specifies how to implement an API that complies with the IFTTT Service Protocol. Treat it as a reference while following the workflow described in the [overview](/docs) guide.

> **Tip:** IFTTT also provides an [OpenAPI definition](#openapi-definition) you can use to scaffold parts of your implementation.

## General API requirements

### HTTPS

Your production API **must** be served over HTTPS.

### API URL prefix

Define a dedicated **API URL prefix** for every endpoint exposed by your service.

**Examples**

- `https://api.service.com`
- `https://service.com/api`

### Endpoint paths

Scope every endpoint to the IFTTT protocol version by appending `/ifttt/v1` to your API URL prefix.

**Examples**

- `{{api_url_prefix}}/ifttt/v1/triggers/any_new_photo`
- `{{api_url_prefix}}/ifttt/v1/actions/post_photo`

### Headers

Respond with **UTF-8** encoding, enable HTTP **compression**, and expect IFTTT to send the following headers:

```http
Accept: application/json
Accept-Charset: utf-8
Accept-Encoding: gzip, deflate
Content-Type: application/json
```

### HTTP status codes

Use this canonical set of HTTP responses:

| Status | Description |
| :----- | :---------- |
| `200` | The request succeeded. |
| `400` | Invalid data was sent by IFTTT. Return a descriptive error body. |
| `401` | The OAuth2 access token provided by IFTTT is invalid. |
| `404` | IFTTT attempted to reach an unknown URL. |
| `500` | Your application encountered an unexpected error. |
| `503` | Your service is temporarily unavailable; IFTTT should retry later. |

### Response body format

Return JSON payloads with a top-level `data` wrapper on success and an `errors` array on failure.

#### Success body

```json
{
  "data": {
    // Value varies per endpoint (object or array)
  }
}
```

#### Error body

```json
{
  "errors": [
    {
      "message": "Something went wrong!"
    }
  ]
}
```

Errors following this structure appear directly in users' activity feeds.

## Service authentication

Users must connect (authenticate) your service before using its Applets. Authentication happens in two steps:

1. Complete the [authentication flow](#authentication-flow) so IFTTT can act on behalf of the user.
2. Fetch the [user information](#user-information) payload and store it for display in IFTTT.

> **Note:** Any service that touches user data must require authentication. Avoid exposing API keys or similar shortcuts through trigger/action fields.

### Authentication flow

IFTTT supports the standard [OAuth2](https://datatracker.ietf.org/doc/html/rfc6749) authorization code flow, including optional [refresh tokens](#token-refresh). Each access token should uniquely map to a single user/resource owner. If you do not issue refresh tokens, your access tokens must not expire; otherwise, refresh tokens must be non-expiring.

#### IFTTT client credentials

Provide IFTTT with a **client ID** and **client secret** in your service configuration. They are required for all token-related calls.

#### IFTTT authorization

To start the flow, IFTTT redirects the user to your OAuth2 Authorization URL.

**Request**

```http
GET https://<your-authorization-url>?client_id=...&response_type=code&...
```

**Parameters**

- **client_id** — IFTTT’s client ID for your service.
- **response_type** — Always `code`.
- **scope** — Use `ifttt` so the token covers every trigger, query, and action (override only if you configure a different scope in the service settings).
- **state** — Anti-forgery token supplied by IFTTT; echo it back unchanged.
- **redirect_uri** — `https://ifttt.com/channels/{{service_id}}/authorize`
  - `service_id` is the slug you configure to identify your service in URLs.

**Example**

```http
https://api.example-service.org/oauth2/authorize?client_id=94b26e58a3a88d5c&response_type=code&redirect_uri=https%3A%2F%2Fifttt.com%2Fchannels%2Fexample_channel%2Fauthorize&scope=ifttt&state=a00caec8dbd08e50
```

#### Authorization grant

After authenticating the user and receiving consent, redirect them back to IFTTT’s channel authorization URL with an authorization code.

**Redirect**

- URL: `https://ifttt.com/channels/{{service_id}}/authorize`

**Parameters**

- **code** — Authorization code you generated.
- **state** — The original anti-forgery token.

**Example**

```http
https://ifttt.com/channels/example_channel/authorize?code=67a8ad40341224c1&state=a00caec8dbd08e50
```

#### User denies IFTTT

If the user refuses access, redirect them to IFTTT with an error flag.

```http
https://ifttt.com/channels/{{service_id}}/authorize?error=access_denied
```

#### Token exchange

Once IFTTT holds the authorization code, it exchanges it for an access token using your OAuth2 Token URL.

**Request**

```http
POST /oauth2/token HTTP/1.1
Host: api.example-service.com
Content-Type: application/x-www-form-urlencoded

grant_type=authorization_code&
code=67a8ad40341224c1&
client_id=83465ab42&
client_secret=c4f7defe91df9b23&
redirect_uri=https%3A%2F%2Fifttt.com%2Fchannels%2Fservice_id%2Fauthorize
```

**Response (success)**

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

{
  "token_type": "Bearer",
  "access_token": "b29a71b4c58c22af116578a6be6402d2",
  "refresh_token": "optional-if-enabled"
}
```

**Response (invalid code)**

```http
HTTP/1.1 400 Bad Request
Content-Type: application/json; charset=utf-8

{
  "error": "invalid_grant",
  "error_description": "The code or token used is not valid"
}
```

### Token refresh

If your service issues expiring access tokens, IFTTT will use the refresh token to obtain a new access token when a `401` status is received.

**Request**

```http
POST /oauth2/token HTTP/1.1
Host: api.example-service.com
Content-Type: application/x-www-form-urlencoded

grant_type=refresh_token&
client_id=83465ab42&
client_secret=c4f7defe91df9b23&
refresh_token=c8764378d9879ffeadfcc233effafb23bbdbfe
```

**Response (success)**

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

{
  "access_token": "c547cdfecf7e86cde678bc87de6fc87",
  "refresh_token": "d7676beda76c38762349bac98cba799"
}
```

### User information

After acquiring an access token, IFTTT periodically calls your **user information endpoint** both to display account context to the user and to verify tokens.

```http
GET {{api_url_prefix}}/ifttt/v1/user/info HTTP/1.1
Host: api.example-service.com
Authorization: Bearer {{user_access_token}}
Accept: application/json
Accept-Charset: utf-8
Accept-Encoding: gzip, deflate
X-Request-ID: {{random_uuid}}
```

Respond with:

- Status: `200`
- Headers: `Content-Type: application/json; charset=utf-8`
- Body: JSON containing `data` with the fields below.

| Field | Type | Details |
| :---- | :--- | :------ |
| `name` | string | Name or identifier shown to the user. |
| `id` | string | Stable identifier (max 200 chars). Avoid mutable values such as emails or tokens. |
| `url` | string (optional) | Link to the user’s dashboard/config page. |

```json
{
  "data": {
    "name": "Walter White",
    "id": "heisenberg",
    "url": "http://example.com/users/heisenberg"
  }
}
```

Return `401` for invalid or expired access tokens.

## Triggers

Each trigger requires a unique API endpoint. IFTTT polls each trigger’s endpoint roughly once per hour to fire Applets on new items.

**Note:** For realtime expectations, triggers must support the [Realtime API](#realtime-api).

Return the 50 most recent events by default (descending order), but respect the `limit` parameter if provided. Events should never expire.

### Request

```http
POST {{api_url_prefix}}/ifttt/v1/triggers/{{trigger_slug}} HTTP/1.1
Host: api.example-service.com
Authorization: Bearer {{user_access_token}}
Accept: application/json
Accept-Charset: utf-8
Accept-Encoding: gzip, deflate
Content-Type: application/json
X-Request-ID: {{random_uuid}}
```

Body:

```json
{
  "trigger_identity": "92429d82a41e93048",
  "triggerFields": {
    "album_name": "Street Art",
    "hashtag": "banksy"
  },
  "limit": 50,
  "user": {
    "timezone": "America/Los_Angeles"
  },
  "ifttt_source": {
    "id": "2",
    "url": "https://ifttt.com/myrecipes/personal/2"
  }
}
```

### Response

Return an array of items, each with ingredients and metadata.

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

{
  "data": [
    {
      "image_url": "http://example.com/images/128",
      "tags": "banksy, brooklyn",
      "posted_at": "2013-11-04T09:23:00-07:00",
      "meta": {
        "id": "14b9-1fd2-acaa-5df5",
        "timestamp": 1383597267
      }
    }
  ]
}
```

### Trigger Identity

A `trigger_identity` is a unique signature sent when an Applet is enabled and with every subsequent trigger request. It represents a specific user, trigger, and field combination. You can use it to optimize polling or notify when Applets are deleted.

**Note:** This field is optional to ignore but useful for troubleshooting.

#### DELETE request for cleanup

When an Applet is deleted, IFTTT sends:

```http
DELETE {{api_url_prefix}}/ifttt/v1/triggers/{{trigger_slug}}/trigger_identity/{{trigger_identity}} HTTP/1.1
Host: api.example-service.com
Authorization: Bearer {{user_access_token}}
Accept: application/json
Accept-Charset: utf-8
Accept-Encoding: gzip, deflate
Content-Type: application/json
X-Request-ID: {{random_uuid}}
```

Respond with `200` and an empty body.

### Realtime API

For realtime triggers, notify IFTTT of new events via the Realtime API instead of waiting for polls.

**Request**

```http
POST https://realtime.ifttt.com/v1/notifications HTTP/1.1
Host: realtime.ifttt.com
IFTTT-Service-Key: {{ifttt_service_key}}
Accept: application/json
Accept-Charset: utf-8
Accept-Encoding: gzip, deflate
Content-Type: application/json
X-Request-ID: {{random_uuid}}

{
  "data": [
    {
      "user_id": "23489759"
    },
    {
      "trigger_identity": "c5559d12d393b25c140364d891292e02233933a5"
    }
  ]
}
```

This reduces polling frequency for better performance.

### Trigger fields

Trigger fields can have dynamic validation, location-based input, or dynamic dropdowns (manual or API-driven).

#### Dynamic dropdowns

Options have a label (user sees) and value (sent). Categories are supported (one level deep).

**Request**

```http
POST {{api_url_prefix}}/ifttt/v1/triggers/{{trigger_slug}}/fields/{{trigger_field_slug}}/options HTTP/1.1
Host: api.example-service.com
Authorization: Bearer {{user_access_token}}
Accept: application/json
Accept-Charset: utf-8
Accept-Encoding: gzip, deflate
X-Request-ID: {{random_uuid}}

{}
```

**Response**

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

{
  "data": [
    {
      "label": "Street Art",
      "value": "12345"
    },
    {
      "label": "Animals",
      "values": [
        {
          "label": "Cats",
          "value": "32143"
        }
      ]
    }
  ]
}
```

#### Dynamic validation

For text fields, validate user input dynamically.

**Request**

```http
POST {{api_url_prefix}}/ifttt/v1/triggers/{{trigger_slug}}/fields/{{trigger_field_slug}}/validate HTTP/1.1
Host: api.example-service.com
Authorization: Bearer {{user_access_token}}
Accept: application/json
Accept-Charset: utf-8
Accept-Encoding: gzip, deflate
Content-Type: application/json
X-Request-ID: {{random_uuid}}

{
  "value": "Street Art"
}
```

**Response**

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

{
  "data": {
    "valid": true,
    "message": "optional error message"
  }
}
```

#### Contextual validation

Validates multiple fields in one request when validation depends on other fields. Enable via support.

**Request**

```http
POST {{api_url_prefix}}/ifttt/v1/triggers/{{trigger_slug}}/validate HTTP/1.1
Host: api.example-service.com
Authorization: Bearer {{user_access_token}}
Accept: application/json
Accept-Charset: utf-8
Accept-Encoding: gzip, deflate
Content-Type: application/json
X-Request-ID: {{random_uuid}}

{
  "values": {
    "board": "New Features",
    "card": "Potential Ideas"
  }
}
```

**Response**

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

{
  "data": {
    "board": {
      "valid": true
    },
    "card": {
      "valid": false,
      "message": "Sorry, no card exists with the name \"Potential Ideas\" in the \"New Features\" board."
    }
  }
}
```

#### Location-based input

Enables users to specify points, areas, entering, exiting, or entering/exiting areas. Supports dynamic validation.

**Example**

```json
{
  "triggerFields": {
    "location": {
      "lat": 37.783923707779095,
      "lng": -122.40864549999998,
      "radius": 0,
      "address": "923 Market St, San Francisco, CA 94103, USA",
      "description": "923 Market St, San Francisco, CA 94103, USA",
      "zoom": 16
    }
  }
}
```

## Applet Templates

When creating triggers, provide examples of how they can be used in different action categories to help users build powerful Applets.

#### Mobile push notification tips

- Friendly and personal (use 'you' instead of 'my').
- Keep content concise; inform of the most important information.
- Avoid URL ingredients.

#### Short message tips

- Contextual to the event using key ingredients.
- Mind character limits; include URLs if available.

#### Long post tips

- Use 'Post body' for rich content (HTML allowed).
- 'Post title' is the email subject, 'Post body' is the body.

#### Plaintext file tips

- Great for record keeping; use all relevant ingredients.
- Static filenames append; dynamic filenames create new files.
- Folder paths are created if needed.

#### Spreadsheet tips

- Use all relevant ingredients.
- Separate cells with ||| (e.g. "`{{Ingredient1}}`||| `{{Ingredient2}}`").
- For images: =IMAGE("`{{ingredient}}`";1).

#### Phone call tips

- Content will be read aloud; reference notification template.

#### Calendar event tips

- Include at least one timestamp in 'Quick add text' for event creation.
- Use start/end times if available (e.g. "Event from `{{StartTime}}` to `{{EndTime}}`").

## Actions

Each action requires a unique endpoint.

### Request

```http
POST {{api_url_prefix}}/ifttt/v1/actions/{{action_slug}} HTTP/1.1
Host: api.example-service.com
Authorization: Bearer {{user_access_token}}
Accept: application/json
Accept-Charset: utf-8
Accept-Encoding: gzip, deflate
Content-Type: application/json
X-Request-ID: {{random_uuid}}

{
  "actionFields": {
    "title": "New Banksy photo!",
    "body": "Check out a new Bansky photo: http://example.com/images/125"
  },
  "user": {
    "timezone": "America/Los_Angeles"
  },
  "ifttt_source": {
    "id": "2",
    "url": "https://ifttt.com/myrecipes/personal/2"
  }
}
```

### Response

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

{
  "data": [
    {
      "id": "234325",
      "url": "http://example.com/posts/234325"
    }
  ]
}
```

### Action fields

Action fields support static text input or dropdowns (manual or dynamic). No dynamic validation.

#### Dynamic dropdowns

Options have label and value. Categories supported (one level deep).

**Request**

```http
POST {{api_url_prefix}}/ifttt/v1/actions/{{action_slug}}/fields/{{action_field_slug}}/options HTTP/1.1
Host: api.example-service.com
Authorization: Bearer {{user_access_token}}
Accept: application/json
Accept-Charset: utf-8
Accept-Encoding: gzip, deflate
X-Request-ID: {{random_uuid}}

{}
```

**Response**

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

{
  "data": [
    {
      "label": "Street Art",
      "value": "12345"
    }
  ]
}
```

#### Dynamic checkboxes

Options have label and value.

**Request**

```http
POST {{api_url_prefix}}/ifttt/v1/actions/{{action_slug}}/fields/{{action_field_slug}}/options HTTP/1.1
Host: api.example-service.com
Authorization: Bearer {{user_access_token}}
Accept: application/json
Accept-Charset: utf-8
Accept-Encoding: gzip, deflate
X-Request-ID: {{random_uuid}}

{}
```

**Response**

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

{
  "data": [
    {
      "label": "Street Art",
      "value": "12345"
    }
  ]
}
```

## Queries

Each query requires a unique endpoint.

**Note:** For services published before August 2020, IFTTT may automatically generate query endpoints based on triggers (e.g., "History of new events").

### Request

```http
POST {{api_url_prefix}}/ifttt/v1/queries/{{query_slug}} HTTP/1.1
Host: api.example-service.com
Authorization: Bearer {{user_access_token}}
Accept: application/json
Accept-Charset: utf-8
Accept-Encoding: gzip, deflate
Content-Type: application/json
X-Request-ID: {{random_uuid}}

{
  "queryFields": {
    "album_name": "Street Art"
  },
  "cursor": "optional",
  "limit": 50,
  "user": {
    "timezone": "America/Los_Angeles"
  },
  "ifttt_source": {
    "id": "2",
    "url": "https://ifttt.com/myrecipes/personal/2"
  }
}
```

### Response

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

{
  "data": [
    {
      "image_url": "http://example.com/images/128",
      "tags": "banksy, brooklyn",
      "posted_at": "2013-11-04T09:23:00-07:00"
    }
  ]
}
```

### Pagination

Queries support pagination with `cursor` and `limit`. Return `limit` rows (default 50), and include `cursor` for next page if more data exists.

**Example paginated response**

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

{
  "data": [
    {
      "image_url": "http://example.com/images/128",
      "tags": "banksy, brooklyn",
      "posted_at": "2013-11-04T09:23:00-07:00"
    }
  ],
  "cursor": "seijjh24ks"
}
```

### Query fields

Query fields support dynamic dropdowns. Options have label and value, with categories.

#### Dynamic options

**Request**

```http
POST {{api_url_prefix}}/ifttt/v1/queries/{{query_slug}}/fields/{{query_field_slug}}/options HTTP/1.1
Host: api.example-service.com
Authorization: Bearer {{user_access_token}}
Accept: application/json
Accept-Charset: utf-8
Accept-Encoding: gzip, deflate
X-Request-ID: {{random_uuid}}

{}
```

**Response**

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

{
  "data": [
    {
      "label": "Street Art",
      "value": "12345"
    }
  ]
}
```

## Ingredients

Ingredients are data points returned by triggers or queries. Responses are tabular: rows of ingredients.

### String ingredients

Simple strings (String, Image URL, Web URL, File URL).

### Date and time ingredients

Timestamps in W3C ISO8601 format.

**Examples**

- Date only: `2013-12-31`
- Date & time: `2013-11-04T09:23:00Z` or `2013-11-04T09:23:00-07:00`

### Nested ingredients

Queries that can include results from other queries, useful for hierarchical data structures in query contexts.

## Service status

Provide an endpoint for IFTTT to check your service availability. Not user-specific.

**Request**

```http
GET {{api_url_prefix}}/ifttt/v1/status HTTP/1.1
Host: api.example-service.com
IFTTT-Service-Key: {{ifttt_service_key}}
Accept: application/json
Accept-Charset: utf-8
Accept-Encoding: gzip, deflate
X-Request-ID: {{random_uuid}}
```

**Response**

- Status: `200` or `503`
- Body: none

**Example OK**

```http
HTTP/1.1 200 OK
```

**Example unavailable**

```http
HTTP/1.1 503 Unavailable
```

## OpenAPI definition

IFTTT provides an OpenAPI definition to scaffold your implementation.

### What is OpenAPI

A standard for describing APIs.

### How to use it

Use tools like OpenAPI Generator or Swagger Codegen. Example with Gradle:

Initialize project:

```
$ mkdir service-api-example
$ cd service-api-example
$ gradle wrapper --gradle-version 6.7.1
$ mkdir -p src/main/resources
$ mkdir -p src/main/java/com/example/service/
```

Create `build.gradle`:

```groovy
plugins {
  id 'org.openapi.generator' version '4.3.1'
  id 'org.springframework.boot' version '2.3.4.RELEASE'
  id 'io.spring.dependency-management' version '1.0.10.RELEASE'
  id 'java'
}

group = 'com.example.service'
version = '0.0.1-SNAPSHOT'

repositories {
  mavenCentral()
}

// Configuration for the OpenAPI Generate Gradle Plugin
openApiGenerate {
  // OpenAPI definition file location
  inputSpec = "${projectDir}/src/main/resources/service-api.yaml"
  // Which generator to use (see https://openapi-generator.tech/docs/generators#server-generators)
  generatorName = 'spring'
  // https://openapi-generator.tech/docs/generators/spring
  configOptions = [
    dateLibrary         : "java8",
    interfaceOnly       : "true",
    skipDefaultInterface: "false",
    openApiNullable     : "false",
    apiPackage          : "${group}.${name}",
    modelPackage        : "${group}.${name}.model",
  ]
}

sourceSets.main.java.srcDirs += 'build/generate-resources/main/src/main/java'

dependencies {
  implementation 'org.springframework.boot:spring-boot-starter-web'
  annotationProcessor 'org.springframework.boot:spring-boot-configuration-processor'
  implementation 'org.springframework:spring-webmvc:5.2.9.RELEASE'
  implementation 'io.swagger:swagger-annotations:1.6.2'
  implementation 'com.fasterxml.jackson.core:jackson-annotations:2.11.3'
  implementation 'org.openapitools:jackson-databind-nullable:0.2.1'
  implementation 'javax.annotation:javax.annotation-api:1.3.2'
  compileOnly 'javax.servlet:javax.servlet-api:4.0.1'
}
```

Download [OpenAPI definition for IFTTT Service API](https://github.com/IFTTT/service-api/blob/master/service-api.yaml) into `src/main/resources/service-api.yaml`.

Generate server stubs `./gradlew openApiGenerate`.

You should be able to find generated code at `build/generate-resources/main/src/main/java/com/example/service/service_api_example/IftttApi.java`.

Now we can add our own implementation. For this example we'll implement just one endpoint: `/ifttt/v1/status`.

Create API implementation `src/main/java/com/example/service/IftttApiController.java`

```java
package com.example.service;

import com.example.service.service_api_example.IftttApi;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class IftttApiController implements IftttApi {
    @Override
    public ResponseEntity getStatus() {
        return ResponseEntity.ok().build();
    }
}
```

Create the main class `src/main/java/com/example/service/Application.java`

```java
package com.example.service;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Application {
   public static void main(String[] args) {
     SpringApplication.run(Application.class, args);
   }
}
```

Run the app `./gradlew bootRun`.

Check the app status `curl --verbose localhost:8080/ifttt/v1/status`. You should see a successful 200 response with no body.

### Next steps:

*   Learn about [testing your service](/docs/testing).
*   Explore the [Connect API](/docs/connect_api).

