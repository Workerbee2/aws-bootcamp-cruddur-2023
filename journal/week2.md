# Week 2 — Distributed Tracing
- Hey guys , welcome back to Week 2!
-For a beginner like me, I would like to present a few definitions before we get into the homework challenges and the stretch challenges too!
 
## Introduction
-

## Prerequisites
We will cover a few definitions here that are necessary for us to Understand Distributed Tracing and Logging.

For the purposes of this Class/week we need to have set up a few resources that will assist us and we will also learn about how to use them.

**What are Metrics?**
- Are measurements of specific data points aggregated over a period of time i.e CPU usage, memory and bandwidth.
- We can only collect metrics on what we know.

**What is Monitoring?***
- An action that we perform against our applications and systems to determine their state.
- It collects metrics and compares them against a defined state/value .
- Shows if they are ruunning or not, to also perfoming perfomance health checks.
- 

**What is Observability?**
- Being able to look at data from outside the system about what is going on within the system.
- ***Pattern Recognition*** - 

**What is Logging?**
- jjhh
- To be able to view logs correctly of multiple applications at the same time, we need to make sure that we properly aggreagate the logs.
- ***Log Levels*** - allow us to see classifcations of logs within a log.
Debug, Info, Warnings, Critical, Error

What are the issues with logging
1. When we have Debug on that provides all information, we get log fatigue which can make it very easy easy to miss critical warnings.
2. Logs take up alot of disk space.

**What is Tracing?**
- Information about individual transactions/requests i.e the time a request took, errors that occurred during the process.
- Will inform when things are not running correctly in a pattern match environment, but will not tell you what went wrong but will say something maybe wrong. Logs will clearly say what is wrong.
- Better for microservices than monolithic applications.
- Helps us understand latency between applications.

**Tracing terminologies**
- ***Span*** - the smallest unit in a trace i.e a single HTTP request, a database query.
- ***span_id*** - unique identifier in a trace, it is only unique within a trace id, and can be reused.
- ***trace_id*** - determine its trace and is unique.
- ***parent_id*** - describe a hierarchy of where the calls came from.
- ***labels*** - set of key/value pairs.
- ***Span context*** - set of value that will be propagated.
- ***Logs*** - provide unique 'WTF' information.

**What can we observe?**
- Application Perfomance Monitoring - *(types of application perfomance monitoring tools include **Datadog**, **Honeycomb**, **New Relic**, **Dyna Trace**)*
- Infrastructure monitoring - *(**Monit**, **Nagios**, **Prometheus**)*
- Networks -
- Events monitoring - 
- Databases
- Logs and log analysis - *(Log aggregation and searching for multiple applications such as **PaperTrail**, **ELK Stack** - Allows us to perform log aggregation and analytics)

**What is Open Telemetry?**
- A standardized way of describing what distributed systems are doing. 
- **OpenTelemetry Project** a collection of tools, APIs and SDKs used to instrument, generate, collect and export telemetry data.

## Use Cases


## Tasks

**Step 1 - Instrument our backend flask application to use Open Telemetry (OTEL) with Honeycomb.io as the provider**


**Step 2 - Run queries to explore traces within Honeycomb.io**


**Step 3 - Instrument AWS X-Ray into backend flask application**


**Step 4 - Configure and provision X-Ray daemon within docker-compose and send data back to X-Ray API**


**Step 5 - Observe X-Ray traces within the AWS Console**


**Step 6 - Integrate Rollbar for Error Logging**


**Step 7 - Trigger an error an observe an error with Rollbar**


**Step 8 - Install WatchTower and write a custom logger to send application log data to - CloudWatch Log group**


## Next Steps - Additional Homework Challenges
1. Prometheus
2. Istio Service Mesh

**RESOURCES**
1. [MasterMnd DevOps/SRE Roles - Observability](https://www.youtube.com/watch?v=N2sOzYMwxJs&list=PLleOCN2eBn8KYJlW2kZ90ZNiUaYOy2fI4&index=8)
