Example Services
================

There are two types of example services:

1.  The [Hello World examples](#hello-world-examples) are very simple versions of an IFTTT service in a couple different programming languages, designed to explain how a service can work.
2.  The [service templates](#service-templates) are frameworks based on services in popular categories on IFTTT. These can be cloned into your organization to give you a head start, though they don't have any example code behind them.

Hello World examples
--------------------

Let's get started by creating a "Hello World" service that runs on your local machine and communicates with IFTTT. These represent the simplest implementation of a service.

First, if you don't see a Hello World service in your account, simply click [here](https://ifttt.com/services/create_default) to create one. Then spin up one of these options:

*   [Getting started with Ruby on Rails](#getting-started-with-ruby-on-rails)
    *   [Using Docker](#hello-world-ruby-on-rails-using-docker)
    *   [Using your local Ruby and Rails](#hello-world-ruby-on-rails-using-your-local-ruby-and-rails)
*   [Getting started with Node.js using Glitch](#getting-started-with-node-js)
*   [Getting started with Python and FastAPI](#getting-started-with-python-and-fastapi)

In this tutorial, we’ll answer your questions and help get your service up and running on the IFTTT Platform quickly by creating a simple service. We'll verify that the service is working by using the IFTTT endpoint tests. If you'd prefer, feel free to skim over this section or dive right into the [Service API Reference](https://ifttt.com/docs/api_reference)!

_Note: Deleting the Hello World service is not recommended unless you have another service under your organization. Click [here](https://ifttt.com/services/create_default) to recreate the Hello World service if you're having issues accessing the IFTTT Platform._

### Getting started with Ruby on Rails

#### Hello World: Ruby on Rails using Docker

##### Run `hello_world.rb` via Docker

First, [install Docker](https://docs.docker.com/install/#supported-platforms).

Then, run the following in your command line to deploy the Hello World Ruby on Rails application within a Docker container (replace XXXXXX with [your service key](https://ifttt.com/mkt/api):

`docker run -e IFTTT_SERVICE_KEY='XXXXXX' -p 3000:3000 ifttt/hello-world-ruby`

Surf to http://localhost:3000/ to see it running. You should see a "Hello, World!" message.

Now you're ready to [expose your local server via ngrok](#expose-your-local-server-via-ngrok).

#### Hello World: Ruby on Rails using your local Ruby and Rails

##### Check your Ruby version

In order to run the Rails app you'll need version 2.2.2 or greater of the [Ruby](https://www.ruby-lang.org/en/) programming language installed. You can see which version of Ruby you have installed by running:

    ruby -v
    

If you run into any issues with your local version of Ruby, we recommend [using Docker](#hello-world-ruby-on-rails-using-docker) instead.

Then, copy the following to a file named `hello_world.rb` in your home directory:

```ruby
IFTTT_SERVICE_KEY = "REPLACE_ME"

require "bundler/inline"

gemfile do
  source "https://rubygems.org"
  gem "rails", "~> 5.0"
end

require "action_controller/railtie"
require "active_model/railtie"

class HelloWorld < Rails::Application
  routes.append do
    root to: "hello#world"
    get "/ifttt/v1/status", to: "ifttt#status"
    post "/ifttt/v1/test/setup", to: "ifttt#setup"
    post "/ifttt/v1/triggers/new_thing_created", to: "ifttt#new_thing_created"
    post "/ifttt/v1/queries/list_all_things", to: "ifttt#list_all_things"
    post "/ifttt/v1/actions/create_new_thing", to: "ifttt#create_new_thing"
  end

  config.cache_store = :memory_store
  config.eager_load = false
  config.logger = Logger.new(STDOUT)
  config.secret_key_base = SecureRandom.hex(30)
end

class Thing
  include ActiveModel::Model
  attr_accessor :created_at

  def self.all
    Rails.cache.fetch("things") do
      [
        Thing.new(created_at: Time.parse("Jan 1")),
        Thing.new(created_at: Time.parse("Jan 2")),
        Thing.new(created_at: Time.parse("Jan 3")),
      ]
    end
  end

  def self.create
    Thing.new.tap do |new_thing|
      new_thing.created_at = all.last.created_at + 1.day
      Rails.cache.write("things", all.push(new_thing))
    end
  end

  def id
    created_at.to_i
  end

  def to_trigger_json
    {
      created_at: created_at.iso8601,
      meta: { id: id, timestamp: created_at.to_i }
    }
  end

  def to_json
    { id: id, created_at: created_at.iso8601 }
  end

  def to_limited_json
    { id: id }
  end
end

class HelloController < ActionController::Base
  def world
    render plain: "Hello, World!" + "\n" + Thing.all.map(&:to_json).join("\n")
  end
end

class IftttController < ActionController::Base
  before_action :return_errors_unless_valid_service_key
  before_action :return_errors_unless_valid_action_fields, only: :create_new_thing

  def status
    head :ok
  end

  def setup
    data = {
      samples: {
        actionRecordSkipping: {
          create_new_thing: { invalid: "true" }
        }
      }
    }
    render plain: { data: data }.to_json
  end

  def new_thing_created
    data = Thing.all.sort_by(&:created_at).reverse.map(&:to_trigger_json).first(params[:limit] || 50)
    render plain: { data: data }.to_json
  end

  def list_all_things
    data = Thing.all.map(&:to_json).first(params[:limit] || 50)
    render plain: { data: data }.to_json
  end

  def create_new_thing
    data = [ Thing.create.to_limited_json ]
    render plain: { data: data }.to_json
  end

  private

  def return_errors_unless_valid_service_key
    unless request.headers["HTTP_IFTTT_SERVICE_KEY"] == IFTTT_SERVICE_KEY
      return render plain: { errors: [ { message: "401" } ] }.to_json, status: 401
    end
  end

  def return_errors_unless_valid_action_fields
    if params[:actionFields] && params[:actionFields][:invalid] == "true"
      return render plain: { errors: [ { status: "SKIP", message: "400" } ] }.to_json, status: 400
    end
  end
end

if IFTTT_SERVICE_KEY == "REPLACE_ME"
  raise "⚠️ Copy your service key (find yours at https://ift.tt/your-service-key) into the first line of this file, then try again."
end

HelloWorld.initialize!
Rack::Server.start app: HelloWorld, Host: "0.0.0.0", Port: 3000
```


##### Add your service key to your Rails app

Your service key is a secret key that is shared between your app and IFTTT. You'll need to copy and paste this key into your Rails app so IFTTT can correctly identify your service.

To get your key, visit [the API page for your service](https://ift.tt/your-service-key) and copy the service key. Then, open your local Rails app and set `IFTTT_SERVICE_KEY` to that value (at the beginning of the script).

##### Run the Rails app

You'll need to open your Terminal and install the bundler Ruby gem:

    gem install bundler
    

And then you'll be able to run the application:

    ruby hello_world.rb
    

Now, you can view the Rails app running at [http://0.0.0.0:3000/](http://0.0.0.0:3000/) in your browser. You should see a "Hello, World!" message. You'll need to keep your Terminal window open so the application keeps running.

Now you're ready to [expose your local server via ngrok](#expose-your-local-server-via-ngrok).

#### Expose your local server via ngrok

Now that the application is running on your local machine, you'll need a way to forward IFTTT's request to your local development environment. We recommend [ngrok](https://ngrok.com/) for this because it's easy to install and free for our simple use case.

Open a new Terminal window and follow the [ngrok installation instructions](https://ngrok.com/download). Once you have ngrok installed, you can expose the app running on your local machine to the internet. Just tell ngrok what port your web server is listening on. In this case, it should be port 3000:

    ngrok http 3000
    

You'll see some output which will include "Forwarding" URLs for http and https. These are the URLs where your application is accessible on the internet.

We'll be using the secure https URL, which will look something like this: https://abc123.ngrok.io (where the "abc123" will be some other random identifier.)

Visit the forwarding URL in your browser and you should see that "Hello, World!" message again.

You can now skip to the [Give IFTTT your API URL](#give-ifttt-your-api-url) section below.

### Getting started with Node.js

#### Hello World: Node.js using Glitch

Visit the [Hello World app](https://glitch.com/%7Eifttt-hello-world-service) on Glitch and click the “Remix To Edit” button. That will clone it and you’ll get your own version that you can later tweak and build upon.

After remixing the project you’ll notice a few files in your new Hello World project. You’ll see `server.js`, `package.json`, and `.env`. Until you decide to expand your service, these are the barebones that are needed.

Now, before we run all the tests for your service, let’s add the service key into your API.

#### Add your service key to your app

Your service key is a secret key that is shared between your app and IFTTT. You’ll need to use this key in your Node API so IFTTT can correctly identify your service.

First, to get your key visit the API page for your service [here](https://ifttt.com/mkt/api) and copy the service key.

Now inside of the .env file that you saw earlier, you’ll see a key called `IFTTT_KEY`. Paste your service key in there. It should be formatted like the following:

    IFTTT_KEY="rG4_x0f26jSfY…"
    

#### Give IFTTT your API URL

1.  If you used ngrok and already have a forwarding URL, you may skip to step 2. Otherwise, copy the URL by clicking the “Show” drop-down and then the "In A New Window" button.
    
2.  Visit your new service’s API page [here](https://ifttt.com/mkt/api), and input that URL into the IFTTT API URL field.
    

#### Run the endpoint tests

Visit the endpoint tests [here](https://ifttt.com/mkt/%2Fapi%2Fendpoint_tests), and click the Begin Test button. You should see that all the endpoint tests pass. Now go take a look at your Terminal or Glitch console to see the requests/responses from the endpoint test. Learn more about the endpoint tests [here](https://ifttt.com/docs/testing).

#### Build your own service

Try experimenting by adding new actions and triggers until you get the hang of things. Afterwards you can re-run the endpoint tests to see what happens. Then, check out the [service API documentation](https://ifttt.com/docs/api_reference) to start building your own service (or take a look at the [service templates](#service-templates) below)!

### Getting started with Python and FastAPI

#### Hello World: setting up the environment

Make sure you are running Python3.6+ in your development environment. Run the following command to [install FastAPI](https://fastapi.tiangolo.com/) and its dependencies:

    pip install fastapi
    

Create a new `hello_world.py` file and copy the following to it. 

```python
from fastapi import FastAPI, status, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
from datetime import datetime, timezone
import uuid

app = FastAPI()

class TriggerCheck(BaseModel):
    limit: Optional[int]

class QueryRun(BaseModel):
    limit: Optional[int]

IFTTT_SERVICE_KEY = 'Paste your service key here (find yours at https://ift.tt/your-service-key)'

# Check the validity of the IFTTT-Service-Key on each incoming request before passing it to the path operation

@app.middleware("http")
async def check_service_key(request: Request, call_next):
    headers = request.headers
    if 'IFTTT-Service-Key' not in headers or headers['IFTTT-Service-Key'] != IFTTT_SERVICE_KEY:
        content = {"errors": [{"message": "Unauthorized"}]}
        return JSONResponse(content=content, status_code=status.HTTP_401_UNAUTHORIZED)
    response = await call_next(request)
    return response

# Generate a mock event used in trigger and query responses

def generate_event():
    event = {
        'created_at': datetime.now(timezone.utc).isoformat(timespec='seconds'),
        'meta': {
            'id': str(uuid.uuid4()),
            'timestamp': int(datetime.now(timezone.utc).timestamp())
        }
    }
    return event

# Service health check

@app.get('/ifttt/v1/status', status_code=status.HTTP_200_OK)
def check():
    return

# Test data to run subsequent tests with

@app.post('/ifttt/v1/test/setup', status_code=status.HTTP_200_OK)
def test_setup():
    data = {
        'samples': {
            'actionRecordSkipping': {
                'create_new_thing': { 'invalid': 'true' }
            }
        }
    }
    return {'data': data}

# Trigger endpoint

@app.post('/ifttt/v1/triggers/new_thing_created', status_code=status.HTTP_200_OK)
def new_thing_created(trigger_check: TriggerCheck):
    data = []
    numOfItems = trigger_check.limit
    if numOfItems is None:
        numOfItems = 3
    if numOfItems >= 1:
        i = 0
        while i < numOfItems:
            i += 1
            data.append(generate_event())
    return {'data': data}

# Query endpoint

@app.post('/ifttt/v1/queries/list_all_things', status_code=status.HTTP_200_OK)
def list_all_things(query_run: QueryRun):
    data = []
    numOfItems = query_run.limit
    if numOfItems is None:
        numOfItems = 3
    if numOfItems >= 1:
        i = 0
        while i < numOfItems:
            i += 1
            data.append(generate_event())
    cursor = None
    if query_run.limit == 1:
        cursor = str(uuid.uuid4())
    return {
        'data': data,
        'cursor': cursor
    }

# Action endpoint

@app.post('/ifttt/v1/actions/create_new_thing', status_code=status.HTTP_200_OK)
def create_new_thing():
    id = str(uuid.uuid4())
    return {'data': [{'id': id}]}
```


##### Add your service key to your FastAPI app

Your service key is a secret key that is shared between your app and IFTTT. You'll need to copy and paste this key into your FastAPI app so IFTTT can correctly identify your service.

To get your key, visit [the API page for your service](https://ift.tt/your-service-key) and copy the service key. Then, open your local Python app and set `IFTTT_SERVICE_KEY` to that value (the IFTTT_SERVICE_KEY variable in the code above).

#### Run the app locally

To start the app run this command from your working directory:

    uvicorn hello_world:app
    

Now you're ready to [expose your local server via ngrok](#expose-your-local-server-via-ngrok) on port 8000.

#### Add the API URL to your service

Visit your new service’s API page [here](https://ifttt.com/mkt/api), and input the ngrok URL into the IFTTT API URL field.

#### Test the service

Visit the endpoint tests [here](https://ifttt.com/mkt/%2Fapi%2Fendpoint_tests), and click the Begin Test button. You should see that all the endpoint tests pass. Now go take a look at your Terminal to see the requests/responses from the endpoint test. Learn more about the endpoint tests [here](https://ifttt.com/docs/testing).

* * *

Service Templates
-----------------

[Sign up](https://ifttt.com/developer_sign_up/new) to view service templates.

* * *

#### Next steps:

*   Explore the [Service API](https://ifttt.com/docs/api_reference).
*   Learn about [testing your service](https://ifttt.com/docs/testing).
*   Create your first connection with our [Connect Quick Start Guide](https://ifttt.com/docs/getting_started_connect).