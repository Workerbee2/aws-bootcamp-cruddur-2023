# Week 2 — Distributed Tracing
- Hey guys , welcome back to Week 2!
- I would like to present a few definitions before we get into the homework challenges and the stretch challenges too!
 
## Introduction
- In traditional software and application designs , we use logging which has its own downsides i.e there is alot of data with no context for why something is wrong and finding the root cause of a problem is like trying to find a needle in a hay-stack.
- And be honest, no one really reads logs for fun !!!

## Prerequisites
We will cover a few definitions here that are necessary for us to Understand Distributed Tracing and Logging.
For the purposes of this Class/week we need to have set up a few resources that will assist us and we will also learn about how to use them.
We also need to set up the following :
1. A Honeycomb.io account - Honeycomb makes it easy to understand and troubleshoot complex relationships within our distributed services.
2. A Rollbar account - Proactively discover, predict, and resolve errors in real-time with Rollbar’s error monitoring platform.
3. AWS SDK

**What are Microservices ?**
- Applications are simpler to build and maintain as smaller services.
- We can isolate software functionality into multiple independent modules that are individually responsible for perfoming precisely defined stand-alone tasks.
- The modules communicate to each other using APIs.

**What is Open Telemetry?**
- A standardized way of describing what distributed systems are doing. 
- **OpenTelemetry Project** a collection of tools, APIs and SDKs used to instrument, generate, collect and export telemetry data.

**What is Monitoring?**
- An action that we perform against our applications and systems to determine their state.
- It collects metrics and compares them against a defined state/value .
- Shows if they are ruunning or not, to also perfoming perfomance health checks.

**What is Observability?**
- Being able to look at data from outside the system about what is going on within the system.
- What can we unerstand from a system based on its output?
- ***Pattern Recognition*** - 

**What can we observe?**
The data types that show us the perfomance and health of our systems(MELT):
- Application Perfomance Monitoring - *(types of application perfomance monitoring tools include **Datadog**, **Honeycomb**, **New Relic**, **Dyna Trace**)*
- Infrastructure monitoring - *(**Monit**, **Nagios**, **Prometheus**)*
- Networks -
- Events monitoring - 
- Logs and log analysis - *(Log aggregation and searching for multiple applications such as **PaperTrail**, **ELK Stack** - Allows us to perform log aggregation and analytics)
- Tracing
- Databases

**What are Metrics?**
- Are measurements of specific data points aggregated over a period of time i.e CPU usage, memory and bandwidth.
- We can only collect metrics on what we know.

**What are Events?**
- A dicrete action that takes place at any moment in time.
- Add metadata for better serach capabilities.

**What is Logging?**
- Come directly from our application and transfer detailed data and detailed context for an event.
- To be able to view logs correctly of multiple applications at the same time, we need to make sure that we properly aggreagate the logs.
- ***Log Levels*** - allow us to see classifcations of logs within a log.
Debug, Info, Warnings, Critical, Error

What are the issues with logging
1. When we have Debug on that provides all information, we get log fatigue which can make it very easy easy to miss critical warnings.
2. Logs take up alot of disk space.

**What is Tracing/Distributed Tracing?**
- Information about individual transactions/requests i.e the time a request took, errors that occurred during the process.
- Will inform when things are not running correctly in a pattern match environment, ***but will not tell you what went wrong but will say something maybe wrong. Logs will clearly say what is wrong.***
- Better for microservices than monolithic applications.
- Helps us understand latency between applications.

**Tracing/Distributed Tracing terminologies**
- ***Span*** - the smallest unit in a trace, i.e a single HTTP request, a database query. Has a start time and duration. The smallest unit of work.
- ***span_id*** - unique identifier in a trace, it is only unique within a trace id, and can be reused.
- ***trace_id*** - determine its trace and is unique.
- ***parent_id*** - describe a hierarchy of where the calls came from.
- ***labels*** - set of key/value pairs.
- ***Span context*** - set of value that will be propagated.
- ***Logs*** - provide unique 'WTF' information.

## Use Cases
- 
1. We will be instrumenting HONEYCOMB to send traces/data about our backend application.


## Tasks

### Observability and Monitoring in AWS with Ashish
- Differentiating Factors that differentiate between Monitoring vs Observability?
1. Availability      - Is my system available vs How long was my system up?
2. Perfomance        - Is my system healthy vs What is my system doing?
3. Fault Management  - When & where did it occur vs Why did it occur?
4. Recovery          - Is my system back up vs What i can do better next time?

**What is Observability in AWS?**
The way we can break down the entire application into multiple processes , and have an exact trace of where a function is calling, where it is going for logging, what metric we can look out for metric capabilities?

**AWS Observability Services**
- AWS CloudWatch Logs
- AWS CloudWatch Metrics
- AWS X Ray Traces

**LAB - Intergrating AWS CloudTrail with CloudWatch Events**
- Creating a log group within Cloudwatch, so that we can then create metrics for the log group.

**How to enable a Central Observability Platform for Security**
- Enabling Central Observability Platform with AWS Securtiy Hub with Amazon Eventbridge.
- SIEM(Security Incident and Event Management)
- Enable and ELK stack
- Use Event Driven Architecture

### Instrumenting our backend Flask application with Honeycomb
**Step 1 - Instrument our backend flask application to use Open Telemetry (OTEL) with Honeycomb.io as the provider**
- First things first, we will configure the environment to use our Honeycomb.io account API key.
- Create a new environment in Honeycomb and copy its API key, then set the API key as an environment variable by running the following commands in the terminal:
```
export HONEYCOMB_API_KEY="2vWapikeyapikey"
gp env HONEYCOMB_API_KEY="2vWapikeyapikey"
```
- To see that its been set run ``` env grep  | HONEY_COMB ```

- To configure Open Telemetry to send to Honeycomb, we will set the following in the ```Docker-compose.yml``` file, just below the BACKEND_URL line(We should not to set the environment service name in the terminal as it will remain consistent over differently named projects).
```
OTEL_SERVICE_NAME: "backend-flask"
OTEL_EXPORTER_OTLP_ENDPOINT: "https://api.honeycomb.io"
OTEL_EXPORTER_OTLP_HEADERS: "x-honeycomb-team=${HONEYCOMB_API_KEY}"
```

- Change into the backend-flask folder and run the following commands:
```
cd backend-flask
pip install opentelemetry-api
```

- Since our backend is written in Python, we will use the Python tab to instrument our flask app with opentelemtry. Copy the code from the home page of honeycomb.io, Python page and paste into our requirements.txt file in the backend-flask-app folder.
```
opentelemetry-api 
opentelemetry-sdk 
opentelemetry-exporter-otlp-proto-http 
opentelemetry-instrumentation-flask 
opentelemetry-instrumentation-requests
```

- Then in the terminal ,run 
``` pip install -r requirements.txt ```

- In our app.py, paste the following code after the existing import statements(these will create and initialize a tracer and Flask instrumentation to send data to Honeycomb):
```
from opentelemetry import trace
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
```

- To initialize tracing and an exporter that can send data to Honeycomb, paste the follwoing into app.py:
```
provider = TracerProvider()
processor = BatchSpanProcessor(OTLPSpanExporter())
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)
```

- To initialize automatic instrumentation with Flask(do not copy app = Flask(__name__) as it already exists in our app.py page):
```
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()
```

- Move into the front-end folder then run npm install
```
cd ../frontend-react-js/
npm install
```

- To ensure that the ports are always open when we run Docker-compose up, copy the following code and paste into the ```.gotpod.yml``` file: 
```
ports:
  - name: frontend
    port: 3000
    onOpen: open-browser
    visibility: public
  - name: backend
    port: 4567
    visibility: public
  - name: xray-daemon
    port: 2000
    visibility: public
 ```
 
- Run Docker-compose up to make sure that the changes have been effected.
- To make sure that our application is returning the API endpoint, run the provided link in a new tab and confirm that you can see the page working.
- For the backend , paste the link in a new tab and add /api/activities/home at the end of the link
*If we do not add the /api/activities/home at the end we will meet a 404 error*

**Step 2 - Run queries to explore traces within Honeycomb.io**
- To set up or acquire a tracer to only use the OpenTelemetry API, paste the follopwing code in:
```
from opentelemetry import trace

tracer = trace.get_tracer("tracer.name.here")
```

- In the ```home_activities.py``` paste in the following:

```
from opentelemetry import trace

tracer = trace.get_tracer(__name__)
with tracer.start_as_current_span("http-handler"):
```

### Instrumenting our backend Flask application with AWS X-Ray
**Step 3 - Instrument AWS X-Ray into backend flask application**
- AWS uses an X-Ray daemon that runs alongside your application ,to which logs from your application are sent , and then they send the data to the X-Ray API.

- To make sure that we have the reactfolder loaded each trime, we will paste the follwoing into .gitpod.yml:
```  
    name: react-js
    command: |
      cd frontend-react-js
      npm i
```

- To install the AWS X-ray daemon in our terminal/environment, we will need to install the SDK. Therefore,paste the following line into requirements.txt 
```aws-xray-sdk```

- Change into backend-flask then in the terminal run 
```pip install -r requirements.txt```

- We will then install middleware into our app.py
```
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

xray_url = os.getenv("AWS_XRAY_URL")
xray_recorder.configure(service='Cruddur', dynamic_naming=xray_url)
XRayMiddleware(app, xray_recorder)
```

- To set up a sampling rule, we create an ```xray.json``` file in a new json folder and paste:
```
{
    "SamplingRule": {
        "RuleName": "Cruddur",
        "ResourceARN": "*",
        "Priority": 9000,
        "FixedRate": 0.1,
        "ReservoirSize": 5,
        "ServiceName": "backend-flask",
        "ServiceType": "*",
        "Host": "*",
        "HTTPMethod": "*",
        "URLPath": "*",
        "Version": 1
    }
  }
```

- To create a group in XRay paste the following (while still in backend-flask):
```
aws xray create-group \
   --group-name "Cruddur" \
   --filter-expression "service(\"backend-flask\")"
```

- To create a sampling rule
``` aws xray create-sampling-rule --cli-input-json file://aws/json/xray.json ```

**Step 4 - Configure and provision X-Ray daemon within docker-compose and send data back to X-Ray API**
- To install the XRay docker daemon, we paste the following code into Docker compose
```
  xray-daemon:
    image: "amazon/aws-xray-daemon"
    environment:
      AWS_ACCESS_KEY_ID: "${AWS_ACCESS_KEY_ID}"
      AWS_SECRET_ACCESS_KEY: "${AWS_SECRET_ACCESS_KEY}"
      AWS_REGION: "us-east-1"
    command:
      - "xray -o -b xray-daemon:2000"
    ports:
      - 2000:2000/udp
```

- And also to add environment variables , we paste the following code into the Docker-compose file:
```
      AWS_XRAY_URL: "*4567-${GITPOD_WORKSPACE_ID}.${GITPOD_WORKSPACE_CLUSTER_HOST}*"
      AWS_XRAY_DAEMON_ADDRESS: "xray-daemon:2000"
```

**Step 5 - Observe X-Ray traces within the AWS Console**

### Install WatchTower and write a custom logger to send application log data to a CloudWatch Log group
**Step 6 - Connect our logs to CloudWatch to implement Cloud Watch logs for our application**
- In our requirements.txt in the backend-flask folder, paste in:
``` watchtower ```

- Change into the backend-flask folder, then run:
```
cd backend-flask
pip i -r requirements.txt
```

- Then go to the ```app.py``` file and paste:
```
import watchtower
import logging
from time import strftime
```

- Then we will also configure a Logger to use Cloudwatch by pasting in app.py:
```
# Configuring Logger to Use CloudWatch
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
cw_handler = watchtower.CloudWatchLogHandler(log_group='cruddur')
LOGGER.addHandler(console_handler)
LOGGER.addHandler(cw_handler)
LOGGER.info("test log")

```

- To log errors after every request, we will also paste in:
```
@app.after_request
def after_request(response):
    timestamp = strftime('[%Y-%b-%d %H:%M]')
    LOGGER.error('%s %s %s %s %s %s', timestamp, request.remote_addr, request.method, request.scheme, request.full_path, response.status)
    return response
```

- In home_activities.py, also add in:
```
# CloudWatch Logs ----
import logging

```

- In the Docker-compose file, we will then add environment variables that Watchtower will use for the backend-flask application:
```
AWS_DEFAULT_REGION: "${AWS_DEFAULT_REGION}"
AWS_ACCESS_KEY_ID: "${AWS_ACCESS_KEY_ID}"
AWS_SECRET_ACCESS_KEY: "${AWS_SECRET_ACCESS_KEY}"
```


### Instrumenting our backend Flask application iwth Rollbar for Error Logging
**Step 7 - Integrate Rollbar for Error Logging**
- Paste the following into requirements.txt in the backend-folder then run it:
```
blinker
rollbar
pip install -r requirements.txt
```

- Then from the rollbar page, we will take the access token for our flask application and set it as an environment variable(it appears like below):
```
# access token
'3d78xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
export ROLLBAR_ACCESS_TOKEN="'3d78xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'"
gp env ROLLBAR_ACCESS_TOKEN="'3d78xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'"
env | grep ROLLBAR 
```

- To instrument our code, we will paste the following from the rollbar page into app.py:
```
import os
import rollbar
import rollbar.contrib.flask
from flask import got_request_exception
```

- To enable initialization for our application, we will paste the code below into 
```
rollbar_access_token = os.getenv('ROLLBAR_ACCESS_TOKEN')
@app.before_first_request
def init_rollbar():
    """init rollbar module"""
    rollbar.init(
        # access token
        rollbar_access_token,
        # environment name
        'production',
        # server root directory, makes tracebacks prettier
        root=os.path.dirname(os.path.realpath(__file__)),
        # flask already sets up logging
        allow_logging_basic_config=False)

    # send exceptions from `app` to rollbar, using flask's signal system.
    got_request_exception.connect(rollbar.contrib.flask.report_exception, app)
```

- To have our first endpoint , we will paste the following into app.py:
```
@app.route('/rollbar/test')
def rollbar_test():
    rollbar.report_message('Hello World!', 'warning')
    return "Hello World!"
```

- Add the following to the Docker-compose file:
``` ROLLBAR_ACCESS_TOKEN: "${ROLLBAR_ACCESS_TOKEN}" ```


## Next Steps - Additional Homework Challenges
1. Instrument Honeycomb for the frontend-application to observe network latency between frontend and backend[HARD]
2. Add custom instrumentation to Honeycomb to add more attributes eg. UserId, Add a custom span
3. Run custom queries in Honeycomb and save them later eg. Latency by UserID, Recent Traces
4. Add segment and subsegments to our Xray query.
5. Add additional infoprmation to Rollbar to trigger an error and observe.

**RESOURCES**
1. [Honeycomb Documentation](https://ui.honeycomb.io/gettingstarted/environments/bootcamp2023/send-data#)
2. [MasterMnd DevOps/SRE Roles - Observability](https://www.youtube.com/watch?v=N2sOzYMwxJs&list=PLleOCN2eBn8KYJlW2kZ90ZNiUaYOy2fI4&index=8)
3. [AWS SDK -Python Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html0)
