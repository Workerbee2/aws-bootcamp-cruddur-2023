## Frontend React JS

**Step 1 - Ensure we can get the apps running locally(for the Frontend)**
- Make sure we are in the correct directory by running ``` pwd ```
- Change into frontend-flask *(cd frontend-flask)* 
- In the terminal, paste the code and run it
``` npm install ```

**Step 2 - Write a Dockerfile for each app(for the Frontend)**
- While still in frontend-flask/ folder, create a Dockerfile then copy code below, and paste in the frontend/Dockerfile and save.
```
FROM node:16.18

ENV PORT=3000

COPY . /frontend-react-js
WORKDIR /frontend-react-js
RUN npm install
EXPOSE ${PORT}
CMD ["npm", "start"]
```

