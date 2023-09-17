# Data Engineering Take Home: ETL off a SQS Queue

Welcome to this project! The primary goal here is to craft an ETL pipeline that seamlessly fetches JSON data from an AWS SQS Queue, subtly masks the fields `device_id` and `ip` to ensure user privacy, and then diligently stores the transformed information into a PostgreSQL database.

## Requirements

- Python 3.11+
- PSQL
- Docker
- Docker Compose
- pip or pip3
- AWS CLI

## Getting Started

1. **Get the Code**: First things first, clone the repository:
   ```bash
   git clone https://github.com/dmohana1504/Fetch-Rewards-Take-Home.git
   ```

2. **Setting up**:
   - **For Windows users**: Simply right-click on `Run_Me_Windows` and choose 'Run with PowerShell'.
   - **For MacOS users**: Navigate to the repository folder in your terminal and execute:
     ```bash
     ./Run_Me_Mac.sh
     ```

3. **Database Details**: Whether you're on Windows or MacOS, our default PSQL credentials are:
   ```plaintext
   dbname: postgres
   user: postgres
   password: postgres
   host: localhost
   port: 5432
   ```

   If you're using different credentials, navigate to `Fetch-Rewards-Take-Home\Main` and adjust the values in the `connect_to_database` function within `DataOperations.py`.

4. **Connecting to the Database**:
   - **On Windows**: Open a PowerShell window and input:
     ```bash
     psql -d postgres -U postgres -p 5432 -h localhost -W
     ```

   - **On MacOS**: Fire up your SQL Shell (PSQL) and input:
     ```bash
     psql -d postgres -U postgres -p 5432 -h localhost -W
     ```

5. **Viewing the Data**: Once you're in the PSQL interface, simply use the following to view the table:
   ```sql
   SELECT * FROM user_logins;
   ```

## Troubleshooting & Tips

1. **Queue Messages**: If you stumble upon the "Queue is empty. No new messages to process." message, ensure that the localstack service is correctly set up with the pre-loaded messages. You can check the queue manually by running the command below using the Terminal or PowerShell:
   
   ```bash
   awslocal sqs receive-message --queue-url http://localhost:4566/000000000000/login-queue
   ```

3. **Docker Hiccups**: Ensure that Docker services are up and running before executing the script. If you have any issues run the commands below to restart docker manually:
   ```bash
   docker-compose down
   docker-compose up -d
   ```

4. **Running the Code**: Running into issues with the provided scripts? No worries! You can always run `Main.py` inside the `Fetch-Rewards-Take-Home\Main` directory using your favorite editor or terminal.

## Assumptions

- We're leaning on the expectation that the Localstack image is stocked up with SQS messages.
- Similarly, the Postgres image is believed to have all the initial configurations.

## Masking Mechanism

Wondering how we're ensuring user privacy? We're relying on SHA-256 hashing to elegantly mask the PII (Personal Identifiable Information). This ensures the original essence is scrambled beyond recognition, making it secure yet usable for analysis.

## Deployment Strategy

Here's how we'd do it:
   
- **Containerize Everything**: We'd fit our application into containers using Docker. Then, employ Kubernetes to orchestrate these containers, ensuring smooth scalability and management.

- **Automate the Workflow**: Introducing CI/CD pipelines (think Jenkins or GitLab CI) can automate deployments. A new feature or fix? Let the pipeline handle testing and deployment once changes are pushed.

## Enhancements & Additions

What's on the horizon?

- **Improved Monitoring**: Integrating tools like Prometheus and Grafana can give us a hawk-eye view of our application's performance.
- **Better Error Management**: Imagine a system where potential faults trigger alerts, allowing for quick action. We're eyeing tools like PagerDuty or Opsgenie for this.
- **Tightened Security**: This involves encrypting data, managing secrets wisely, and setting up rigid access controls for our database.
- **Database Safeguards**: Regularly backing up our Postgres database to minimize any chances of data loss.

## Scalability Solutions

With data burgeoning, how does this application stand tall?

- **Horizontal Scaling**: By adding more instances of the application, we can share the load and serve more users.
- **Database Sharding**: Distributing database load across servers helps in managing vast amounts of data efficiently.
- **Smart Caching**: Implementing caching mechanisms like Redis to reduce frequent trips to the database.
- **Optimize Data Retrievals**: Ensuring our SQL queries are swift and efficient is a continual process.

## Recovering Original Data

Given that we're using SHA-256 for masking, direct decryption isn't possible. For data recovery, one could consider maintaining a secure mapping or storing original data encrypted in a separate database. Only a handful with special privileges would have the keys to this treasure.
