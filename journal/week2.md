# Week 2 — Distributed Tracing
- Hey guys , welcome back to Week 2!
-For a beginner like me, I would like to present a few definitions before we get into the homework challenges and the stretch challenges too!
 
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

## Tasks

**Step 1 - Instrument our backend flask application to use Open Telemetry (OTEL) with Honeycomb.io as the provider**
- First we will configure the environment to use our Honeycomb.io account API key.
- Create a new onment in Honeycomb and copy its API key then
```
export HONEYCOMB_API_KEY="2vWapikeyapikey"
gp env HONEYCOMB_API_KEY="2vWapikeyapikey"
```

- To see that its been set
``` env grep  | HONEY_COMB ```

- To configure Open Telemtry to send to Honeycomb, we will set the following in the Docker-compose.yml file, just below the BACKEND_URL line.
```
OTEL_EXPORTER_OTLP_ENDPOINT: "https://api.honeycomb.io"
OTEL_EXPORTER_OTLP_HEADERS: "x-honeycomb-team=${HONEYCOMB_API_KEY}"
```

- Change into the backend-flask folder and run the following commands:
```
cd backend-flask
pip install opentelemetry-api
```

- Since our backend is written in Python, we will use the Python tab to instrument our flask app with opentelemtry. Copy the code from the honeycomb.io page and paste into our requirements.txt file in the backend-flask-app folder.
```
opentelemetry-api 
opentelemetry-sdk 
opentelemetry-exporter-otlp-proto-http 
opentelemetry-instrumentation-flask 
opentelemetry-instrumentation-requests
```

- Then run 
``` pip install -r requirements.txt ```

- In our app.py, paste the foolowing code:
```
from opentelemetry import trace
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
```

- Top enable tracing
```
provider = TracerProvider()
processor = BatchSpanProcessor(OTLPSpanExporter())
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)
```

- To initialize automatic instrumentation with Flask:
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

-

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

**Step 3 - Instrument AWS X-Ray into backend flask application**
- 

**Step 4 - Configure and provision X-Ray daemon within docker-compose and send data back to X-Ray API**
-

**Step 5 - Observe X-Ray traces within the AWS Console**
-

**Step 6 - Integrate Rollbar for Error Logging**


**Step 7 - Trigger an error an observe an error with Rollbar**


**Step 8 - Install WatchTower and write a custom logger to send application log data to a CloudWatch Log group**


## Next Steps - Additional Homework Challenges
1. Instrument Honeycomb for the frontend-application to observe network latency between frontend and backend[HARD]
2. Add custom instrumentation to Honeycomb to add more attributes eg. UserId, Add a custom span
3. Run custom queries in Honeycomb and save them later eg. Latency by UserID, Recent Traces


**RESOURCES**
1. [Honeycomb Documentation](https://ui.honeycomb.io/gettingstarted/environments/bootcamp2023/send-data#)
2. [MasterMnd DevOps/SRE Roles - Observability](https://www.youtube.com/watch?v=N2sOzYMwxJs&list=PLleOCN2eBn8KYJlW2kZ90ZNiUaYOy2fI4&index=8)
3. [AWS SDK -Python Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html0)
