# Week 1 — App Containerization
 Hey guys , welcome back to Week 1!
 For a beginner like me, I would like to present a few definitions beforewe get into the homework challenges and the stretch challenges too!
 
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
-
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

## Tasks
**1. Create a new GitHub repo**
- From the Msaghu/aws-bootcamp-cruddur-2023/journal/week-1/main page, then launch Gitpod from there.

**2. Launch the repo within a Gitpod workspace**


3. Configure Gitpod.yml configuration, eg. I’m VSCode Extensions
4. Clone the frontend and backend repo
5. Explore the codebases
6. Ensure we can get the apps running locally
7. Write a Dockerfile for each app
8. Ensure we get the apps running via individual container

**Create a docker-compose file and Ensure we can orchestrate multiple containers to run side by side**
- For any application that is interactive, the backend services have to be able to communicate to the front end.
- Docker-compose enables us to achieve this by ensuring that we can run both the backend and the frontend simultaneously thus showing us a display page.
- Therefore, we created a docker-compose.yml file in the directory(for me the application only runs if the file is ouside the back-end and front-end directories).
- We exposed port 3000 for the frontend and port 4567 for the backend, meaning that to see the landing page for our application, we had to open the ports tab in the terminal section of Gitpod, unlock it and click on the link, and vice versa for the backend.

*The only downside that i experienced for docker-compose, was that to run and access a different application, I had to stop the other container.


12. Mount directories so we can make changes while we codeation

**How do we run Containers in AWS?**
- AWS ECS
- AWS EKS
- AWS AppRunner
- AWS Fargate

##Additional Homework Challenges
1. Run the Dockerfile command as an external script.
2. Push and tag a image to DockerHub (they have a free tier).
3. Use multi-stage building for a Dockerfile build.
4. Implement a healthcheck in the V3 Docker compose file.
5. Research best practices of Dockerfiles and attempt to implement it in your Dockerfile.
6. Learn how to install Docker on your local machine and get the same containers running outside of Gitpod / Codespaces.
7. Launch an EC2 instance that has docker installed, and pull a container to demonstrate you can run your own docker processes.
