# Week 1 — App Containerization
 Hey guys , welcome back to Week 1!
 For a beginner like me, I would like to present a few definitions beforewe get into the homework challenges and the stretch challenges too!
 
## Introduction
- This is Week 1 of the project bootcamp and we will be using Docker to ship our Cruddur application.

## Prerequisites
- For the purposes of this bootcamp, we need to know about what Docker is and the reason why its so common to ship most applications in todays modern world. Below we have a few basic definitions 

**What is a Container?**
- Allow developers to package up and to isolate applications from the host system, with all its libraries and dependencies, and ship it out.

**What is a Host system?**
- A software on the computer that works with the underlying hardware.

**What are Libraries?**
- Tools and functions that are pulled in to help support our application.

**What are the differences between Containers and Virtual Machines?**

**What is Docker?**
- Docker in written in Go and Version 1.0 was first released in 2014. It runs on Linux, Windows, Mac.
- The Docker mascot is a whale .

**Why Docker?**
- Provides a consistent development and deployment experience.
- Can be used on any machine .
- Can be asily scaled to meet demands due to their small sizes.
- Docker Images can be run anywhere that Docker can be installed.

**What is a Docker Image?**
- A read-only template that has a set of instructions for creating a containerthat can run on the Docker platform.

**What is a Dockerfile?**
- A text document with the necessary commands for creating a Docker image.

**What is a Container?**
- A single running/stopped instance of a Docker image.

**How do we run Containers in AWS?**
- AWS ECS
- AWS EKS
- AWS AppRunner
- AWS Fargate

## Use Case
- We need to launch our Cruddur application. We have the front-end and backend code written out, and we now need to Dockerise our application and ship it. 
- For the purposes of this application, we need create an image and run a container from it for both the front-end and backend. To create an image, we need to create Dockerfile within the front-end folder. We need to do the same for the back-end folder too.

## Tasks
**Step 1 - Created a new GitHub repo and Launched the repo within a Gitpod workspace**
- From the Msaghu/aws-bootcamp-cruddur-2023/journal/week-1/main page, then launch Gitpod from there.

**Step 2 - Configure Gitpod.yml configuration, eg. I’m VSCode Extensions**
- To make it easier to work with Docker in VSCode(do it also for your local VSCode environment), go to the Extensions tab on the left-hand side and search for Docker and click Install.

**Step 3 - Clone the frontend and backend repo and Explore the codebases**
- Take a look at the frontend and backend code and see how it runs.

**Step 4 - Ensure we can get the apps running locally(for the Backend)**
- Change into backend-flask *(cd backend-flask)* 
- In the terminal, paste the code and run it
``` pip3 install -r requirements.txt ```
 - To make sure that we get results, we need to set the environment variables,
 ```
 export FRONTEND_URL="*"
 export BACKEND_URL="*"
 ```
*If we do not set the variables, we will find that it gives **error 404 - Not Found** , this shows that the server is running but not receiving requests.*
- Then paste 
 ``` python3 -m flask run --host=0.0.0.0 --port=4567 ``` and run it

- Go into the ports tab and unlock the port for 4567(this is the default port that Fask runs on). Copy the link provided and paste into a new tab then add ```/api/activities/home``` to the end of the link then run it. 
- We now get a JSON response.
- We can then stop the container by entering Ctrl+C 

**Step 5 - Write a Dockerfile for each app**
- While still in backend-flask/ folder, copy code from the Omenking/aws-cruddur-bootcamp/week-1 code, and paste in the backend/Dockerfile and save.

```
FROM python:3.10-slim-buster

#Step:2  Make a new folder inside the container
WORKDIR /backend-flask

#Step 3: The libraries to run our application
COPY requirements.txt requirements.txt

#Step 3: Installs the python libraries used for our application
RUN pip3 install -r requirements.txt

#Step 4: Copies everything INTO the container
COPY . .

#Step 5: Sets Environment variables permanently while the container is running
ENV FLASK_ENV=development

EXPOSE ${PORT}

#python3 -m flask run --host=0.0.0.0 --port=4567
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]
```

 - Then we will unset the environment variables we set in **Step 4**. 
 ```
 unset FRONTEND_URL
 unset BACKEND_URL
 ```

**Step 6 - Ensure we get the apps running via individual container**
- Change into project directory *(cd ..)*
- Create an image from the dockerfile by running the above dockerfile 
```docker build -t  backend-flask ./backend-flask```
- To run the container while also setting the environment variables,
```docker run --rm -p 4567:4567 -it  -e FRONTEND_URL="*" -e BACKEND_URL="*" backend-flask```
*If run a container from the image that we created, without setting the variabl;es
```docker run --rm -p 4567:4567 -it backend-flask```
We will find that it gives **error 404 - Not Found** , this shows that the server is running but not receiving requests.*




**Step 7 - Create a docker-compose file and Ensure we can orchestrate multiple containers to run side by side**
- For any application that is interactive, the backend services have to be able to communicate to the front end.
- Docker-compose enables us to achieve this by ensuring that we can run both the backend and the frontend simultaneously thus showing us a display page.
- To be able to succeffully launch the application, we will cd into the front-end appliocation and run npm-install, reason being that we have a react front-end application.

```
$ ls
$ cd front-end-react-js
$ npm install
```

- Thereafter, we created a docker-compose.yml file in the directory(for me the application only runs if the file is ouside the back-end and front-end directories) and pasted the code into the file, saved then right-clicked on the **red** docker whale and chose **Docker up**.

```
version: "3.8"
services:
  backend-flask:
    environment:
      FRONTEND_URL: "https://3000-${GITPOD_WORKSPACE_ID}.${GITPOD_WORKSPACE_CLUSTER_HOST}"
      BACKEND_URL: "https://4567-${GITPOD_WORKSPACE_ID}.${GITPOD_WORKSPACE_CLUSTER_HOST}"
    build: ./backend-flask
    ports:
      - "4567:4567"
    volumes:
      - ./backend-flask:/backend-flask
  frontend-react-js:
    environment:
      REACT_APP_BACKEND_URL: "https://4567-${GITPOD_WORKSPACE_ID}.${GITPOD_WORKSPACE_CLUSTER_HOST}"
    build: ./frontend-react-js
    ports:
      - "3000:3000"
    volumes:
      - ./frontend-react-js:/frontend-react-js

# the name flag is a hack to change the default prepend folder
# name when outputting the image names
networks: 
  internal-network:
    driver: bridge
    name: cruddur
```

- We exposed port 3000 for the frontend and port 4567 for the backend, meaning that to see the landing page for our application, we had to open the ports tab in the terminal section of Gitpod, unlock it and click on the link, and vice versa for the backend.
- Incase of issues while launching the application , be sure to click on the docker extension to view logs on what could be preventing it from running. 

*The only downside that i experienced for docker-compose, was that to run and access a different application, I had to stop the other container.*


12. Mount directories so we can make changes while we codeation

**Step 8 - Created a new api endpoint**
- Opened our API file then opened the OpenAPI extension, and under paths, added a new path for our notifications feature.
- We then  edited the file and added the following code block,( I copied the code from AWS DynamoDB documentation and edited it as per the tutorial)

```
  /api/activities/notifications:
    get: 
      description: 'Return a feed of activity for all my following list'
      tags:
       - activities
      parameters: []
      responses:
        '200':
          description: Returns an array of activities
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Activity'
```



**Step 9 - Adding DynamoDB and Postgresql**
- From the AWS CLI , I searched and copied the commands on how to create a DynamoDB table

```
aws dynamodb create-table \
    --endpoint-url http://localhost:8000 \
    --table-name Music \
    --attribute-definitions AttributeName=Artist,AttributeType=S AttributeName=SongTitle,AttributeType=S \
    --key-schema AttributeName=Artist,KeyType=HASH AttributeName=SongTitle,KeyType=RANGE \
    --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 \
    --table-class STANDARD
```

- - To add items to the table created above, paste into the code below into the terminal.

```
aws dynamodb put-item \
    --endpoint-url http://localhost:8000 \
    --table-name Music \
    --item '{"Artist": {"S": "No One You Know"}, "SongTitle": {"S": "Call Me Today"}, "AlbumTitle": {"S": "Greatest Hits"}}' \
    --return-consumed-capacity TOTAL 

```
- Since we do not want to create a new JSON file in  **--item file://item.json \**  we will paste in the JSON code from the documentation 

- To view our available DynamoDB tables, we use the following command in the terminal.

```
aws dynamodb list-tables --endpoint-url http://localhost:8000 \
```

- We then scan the entire Music table, and then narrows the results to songs by the artist “No One You Know”. For each item, only the album title and song title are returned.

```
aws dynamodb scan --table-name cruddur_crud --query "Items" --endpoint-url http://localhost:8000 \
```

**Challenges**
- To launch/access the postgresql environment, 

## Next Steps - Additional Homework Challenges

1. Run the Dockerfile command as an external script.
2. Push and tag a image to DockerHub (they have a free tier).
3. Use multi-stage building for a Dockerfile build.
4. Implement a healthcheck in the V3 Docker compose file.
5. Research best practices of Dockerfiles and attempt to implement it in your Dockerfile.
6. Learn how to install Docker on your local machine and get the same containers running outside of Gitpod / Codespaces.
7. Launch an EC2 instance that has docker installed, and pull a container to demonstrate you can run your own docker processes.
8. I was also able to publish a blog post about Docker on my Dev.to blogpost.

**RESOURCES**
1. [Docker and Kubernetes - Full Course for Beginners](https://www.youtube.com/watch?v=Wf2eSG3owoA)
2. [AWS CLI DynamoDB Documentation - Create a table](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/create-table.html)
3. [AWS CLI DynamoDB Documentation - Put Item](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/put-item.html#examples)
4. [AWS CLI DynamoDB Documentation - List Tables](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/list-tables.html)
