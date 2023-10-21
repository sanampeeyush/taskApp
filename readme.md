# TaskApp Django Project

This is a Django project called "TaskApp" that manages business information.

## Running the Project with Docker

1. **Clone the project repository:**

   ```shell
   git clone https://github.com/sanampeeyush/taskApp.git
   cd taskApp

2. **Build & Run the Docker container for the project:**
    ```shell
    # install and build
    docker compose build
    
    # run the project with test
    docker compoe up

    # run app only
    docker compose up app

    # run migration only
    docker compose up migrate
3. **The project should now be running at http://localhost:8000/**

4. **Run APIs over swagger at http://localhost:8000/swagger/ or http://localhost:8000/api/business/**

5. **To stop the project**
    ```
    docker compose down
## Running Test Cases and Coverage Report Generation

4. **Running pytest and generating Coverage Reports**
    ```shell
    docker compose up test    