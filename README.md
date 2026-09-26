# 🏦 InsureFlow

## Enterprise Insurance Management & End-to-End DevOps Platform

  Build • Test • Secure • Containerize • Automate • Deploy • Monitor</strong>



  A production-oriented insurance management application built with Python, FastAPI, SQLAlchemy and modern DevOps practices.




## 📌 Project Overview

**InsureFlow** is an enterprise-style insurance management platform designed to demonstrate the complete software development and DevOps lifecycle.

The application provides core insurance business capabilities including:

* 🔐 User Registration & Authentication
* 👤 Customer Management
* 📄 Policy Management
* 🧾 Claims Management
* 📊 Dashboard & Business Metrics
* 📈 Analytics
* 👤 Profile Management
* ❤️ Application Health Monitoring
* 🧪 Automated API Testing

The project is being developed with a **DevOps-first architecture**, with the long-term goal of implementing:

* Git & GitHub
* Docker
* SonarQube
* Kubernetes
* Minikube
* Helm
* Terraform
* AWS
* Jenkins CI/CD
* Prometheus
* Grafana
* CloudWatch

The implementation is being developed incrementally, with each DevOps capability validated locally before moving toward AWS deployment.

---

# 🎯 Project Vision

The goal of InsureFlow is to demonstrate how a real-world application can move through the complete DevOps lifecycle:


Application Development
        ↓
Version Control
        ↓
Automated Testing
        ↓
Code Quality & Security
        ↓
Containerization
        ↓
Kubernetes Orchestration
        ↓
Infrastructure as Code
        ↓
AWS Infrastructure
        ↓
CI/CD Automation
        ↓
Monitoring & Observability
```

The project focuses on:

* Automation
* Reliability
* Security
* Infrastructure as Code
* Continuous Integration
* Continuous Delivery
* Containerization
* Kubernetes orchestration
* Cloud infrastructure
* Monitoring
* Operational visibility

---

# 🏢 Insurance Business Domain

InsureFlow simulates an insurance management platform where users can manage customers, insurance policies and claims.

### Core Business Flow

```
Customer
   ↓
Insurance Policy
   ↓
Claim
   ↓
Claim Processing
   ↓
Business Analytics
```

### Example

A customer can:

1. Create an account
2. Log in securely
3. Manage profile information
4. Register as a customer
5. Have insurance policies
6. Submit insurance claims
7. Track claim status
8. View insurance-related information through dashboards

---

# ✨ Application Features

## 🔐 Authentication

InsureFlow provides application-level authentication using:

* User registration
* Secure password hashing
* Login
* JWT access tokens
* Bearer authentication
* Authenticated user profile
* Password change
* Account deletion
* Active/inactive account validation

Authentication endpoints include:

POST /api/auth/register
POST /api/auth/login
GET  /api/auth/me
PUT  /api/auth/profile
PUT  /api/auth/password
DELETE /api/auth/account
```



## 👤 Customer Management

The customer management module provides APIs for managing insurance customers.

### Capabilities

* Create customers
* View customers
* Retrieve customer by ID
* Delete customers
* Validate customer information
* Prevent duplicate customer IDs
* Prevent duplicate email addresses

### API Endpoints


GET    /api/customers/
GET    /api/customers/{customer_id}
POST   /api/customers/
DELETE /api/customers/{customer_id}
```

---

# 📄 Policy Management

The policy management module manages insurance policies associated with customers.

### Supported Information

* Policy number
* Customer ID
* Policy type
* Premium amount
* Coverage amount
* Start date
* End date
* Policy status

### Business Validation

A policy cannot be created for a customer who does not exist.

### API Endpoints

```
GET    /api/policies/
GET    /api/policies/{policy_number}
POST   /api/policies/
DELETE /api/policies/{policy_number}
```

---

# 🧾 Claims Management

The claims module allows users to create and manage insurance claims.

### Claim Information

* Claim number
* Policy number
* Claim type
* Claim amount
* Claim date
* Claim description
* Claim status

### Business Validation

The application validates that:

* The referenced policy exists
* Claim numbers are unique
* Claim amounts are greater than zero

### API Endpoints

```
GET    /api/claims/
GET    /api/claims/{claim_number}
POST   /api/claims/
DELETE /api/claims/{claim_number}
```

---

# 📊 Dashboard

InsureFlow provides a professional dashboard for displaying application and insurance metrics.

The dashboard is designed to provide visibility into:

* Total customers
* Active policies
* Total claims
* Platform health
* Insurance distribution
* Business activity

---

# 📈 Analytics

The analytics module provides business-level information such as:

* Customer statistics
* Policy statistics
* Active policy count
* Policy distribution
* Claims overview
* Claim status distribution

The analytics layer is designed to provide a foundation for future monitoring and reporting capabilities.

---

# 🎨 Premium User Interface

InsureFlow uses a professional enterprise-oriented UI design.

### UI Design Goals

* Premium visual appearance
* Responsive layout
* Clean navigation
* Consistent typography
* Professional dashboard
* Insurance-focused visual language
* Clear data presentation
* User-friendly forms
* Enterprise-style settings page

The UI is designed to resemble a modern business/insurance platform rather than a basic demonstration application.

---

# 🏗️ Application Architecture

```
                         ┌──────────────────────┐
                         │      End User        │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   Premium Web UI     │
                         │ HTML / CSS / JS      │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │      FastAPI         │
                         │    Application       │
                         └──────────┬───────────┘
                                    │
                 ┌──────────────────┼──────────────────┐
                 │                  │                  │
                 ▼                  ▼                  ▼
          Authentication       Business APIs      Health API
                 │                  │                  │
                 ▼                  ▼                  ▼
               Users       Customers / Policies    Monitoring
                                / Claims
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │      SQLAlchemy      │
                         │        ORM           │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │    SQLite Database   │
                         │    Local Development │
                         └──────────────────────┘
```

---

# 🧩 Application Architecture Layers

The application follows a modular structure:

```
Presentation Layer
        ↓
FastAPI Routes
        ↓
Business Logic
        ↓
Schemas / Validation
        ↓
SQLAlchemy ORM
        ↓
Database
```

### Main Components

| Component  | Responsibility              |
| ---------- | --------------------------- |
| FastAPI    | Web framework and REST APIs |
| SQLAlchemy | Database ORM                |
| Pydantic   | Request validation          |
| JWT        | Authentication tokens       |
| pwdlib     | Password hashing            |
| Jinja2     | HTML templates              |
| SQLite     | Local development database  |
| Pytest     | Automated testing           |

---

# 🗄️ Database Architecture

The current application uses SQLite for local development.

### Main Entities

```
User
 │
 └── Authentication / Profile

Customer
 │
 └── Insurance Customer

Policy
 │
 └── Customer Insurance Policy

Claim
 │
 └── Policy Claim
```

### Current Models

```
users
customers
policies
claims
```

The database design can later be extended for production cloud environments.

---

# 👤 User Model

The user model contains information such as:

* User ID
* Full name
* Email
* Password hash
* Phone number
* Role
* Active status

Passwords are stored as password hashes rather than plain text.

---

# 👥 Customer Model

Customer information includes:

* Customer ID
* Full name
* Email
* Phone
* City
* Customer status

---

# 📄 Policy Model

Policy information includes:

* Policy number
* Customer ID
* Policy type
* Premium amount
* Coverage amount
* Start date
* End date
* Policy status

---

# 🧾 Claim Model

Claim information includes:

* Claim number
* Policy number
* Claim type
* Claim amount
* Claim date
* Claim status
* Description

---

# 🔐 Authentication Architecture

InsureFlow uses JWT-based authentication.


User
 ↓
Login
 ↓
Credential Validation
 ↓
Password Verification
 ↓
JWT Token Generation
 ↓
Client
 ↓
Authorization: Bearer <token>
 ↓
Protected API
 ↓
Token Validation
 ↓
Authenticated User
```

---

# 🔑 Password Security

Passwords are not stored directly in the database.

The application uses password hashing through:


pwdlib
```

The authentication process is:


Plain Password
      ↓
Password Hashing
      ↓
Stored Password Hash
```

During login:


Entered Password
      ↓
Hash Verification
      ↓
Authentication Result
```

---

# 🌐 REST API

InsureFlow exposes REST-style APIs through FastAPI.

FastAPI automatically provides interactive API documentation.

### Swagger UI

```
http://127.0.0.1:8000/docs
```

### ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# ❤️ Health Check

The application provides a health endpoint:

```
GET /health
```

Example response:

```json
{
  "application": "InsureFlow",
  "status": "UP"
}
```

This endpoint will later be useful for:

* Docker health checks
* Kubernetes probes
* Load balancers
* Monitoring systems
* CI/CD validation
* AWS deployment validation

---

# 🧪 Automated Testing

Automated API testing is implemented using:

```
Pytest
FastAPI TestClient
HTTPX
SQLite test database
```

The test suite validates important application functionality.

### Current Tests

```
Authentication
    ├── User registration
    ├── User login
    ├── Current user retrieval
    └── Invalid password handling

Customer
    └── Customer creation

Policy
    └── Policy creation

Claims
    └── Claim creation

Health
    └── Application health check
```

### Current Test Result

```
8 tests passed
```

Run the complete test suite:

```powershell
pytest -v
```

---

# 🧪 Test Commands

Run all tests:

```powershell
pytest -v
```

Run authentication tests:

```powershell
pytest tests/test_auth.py -v
```

Run customer tests:

```powershell
pytest tests/test_customers.py -v
```

Run policy tests:

```powershell
pytest tests/test_policies.py -v
```

Run claims tests:

```powershell
pytest tests/test_claims.py -v
```

Run health test:

```powershell
pytest tests/test_health.py -v
```

---

# 🐳 Docker

## Status: Planned

The application will be containerized using Docker.

Planned architecture:


FastAPI Application
        ↓
Dockerfile
        ↓
Docker Image
        ↓
Docker Container
        ↓
Application
```

Planned Docker capabilities:

* Application containerization
* Reproducible environments
* Docker image versioning
* Container health checks
* Local container testing

---

# 🔎 SonarQube

## Status: Planned

SonarQube will be integrated into the CI/CD pipeline for:

* Static code analysis
* Code quality checks
* Security analysis
* Maintainability analysis
* Code smell detection
* Quality gates

Planned pipeline:


Git Push
   ↓
Jenkins
   ↓
Tests
   ↓
SonarQube Analysis
   ↓
Quality Gate

---

# ☸️ Kubernetes

## Status: Planned

Kubernetes will be used for container orchestration.

The project will demonstrate:

* Pods
* Deployments
* Services
* ConfigMaps
* Secrets
* Namespaces
* Health probes
* Scaling

Target architecture:

Kubernetes
    │
    ├── Namespace
    │
    ├── Deployment
    │       │
    │       └── InsureFlow Pods
    │
    ├── Service
    │
    ├── ConfigMap
    │
    └── Secret
```

---

# 🧪 Minikube

## Status: Planned

Minikube will be used for local Kubernetes validation before cloud deployment.

Expected workflow:


Docker Image
     ↓
Minikube
     ↓
Kubernetes Deployment
     ↓
Service
     ↓
InsureFlow Application
```

This allows Kubernetes configuration to be tested locally before AWS deployment.

---

# ⛵ Helm

## Status: Planned

Helm will be introduced to package Kubernetes resources.

Expected structure:

```
Helm Chart
   ├── Chart.yaml
   ├── values.yaml
   └── templates/
          ├── deployment.yaml
          ├── service.yaml
          ├── configmap.yaml
          └── secret.yaml
```

Helm will simplify Kubernetes application deployment and configuration management.

---

# 🏗️ Terraform

## Status: Planned

Terraform will be used as the Infrastructure as Code solution.

Planned responsibilities:

* AWS infrastructure provisioning
* Networking
* Security configuration
* Compute resources
* IAM configuration
* Infrastructure variables
* Outputs
* Resource lifecycle management

Expected workflow:

Terraform Code
      ↓
terraform init
      ↓
terraform plan
      ↓
terraform apply
      ↓
AWS Infrastructure
```

---

# ☁️ AWS Cloud

## Status: Planned

AWS will be introduced for cloud deployment.

The AWS architecture will be designed with cost awareness because this project is intended for a learning and portfolio environment.

Potential AWS components include:


AWS
 │
 ├── EC2
 ├── IAM
 ├── VPC
 ├── Security Groups
 ├── CloudWatch
 └── Supporting Infrastructure
```

The final AWS architecture will be implemented incrementally and validated before moving to production-style deployment.

---

# 💰 AWS Cost Optimization

Cost control is an important part of the project.

The project will avoid unnecessary infrastructure such as:

* Large EC2 instances
* NAT Gateway where not required
* Managed Kubernetes clusters for local demonstrations
* Unnecessary databases
* Unused load balancers
* Unused storage resources

The objective is to demonstrate practical cloud engineering while keeping infrastructure costs controlled.

---

# 🔄 Jenkins CI/CD

## Status: Planned

Jenkins will be used to automate the CI/CD lifecycle.

Planned pipeline:


Developer
    ↓
Git Push
    ↓
Jenkins
    ↓
Checkout
    ↓
Install Dependencies
    ↓
Run Tests
    ↓
SonarQube Analysis
    ↓
Quality Gate
    ↓
Docker Build
    ↓
Docker Image
    ↓
Deployment
    ↓
Health Check
```

---

# 📊 Monitoring & Observability

## Status: Planned

Monitoring will be implemented using multiple tools.

### Prometheus

Prometheus will be used for metrics collection.

### Grafana

Grafana will be used for visualization and dashboards.

### AWS CloudWatch

CloudWatch will be used for AWS infrastructure and application monitoring.

Target architecture:


Application
    │
    ├──────────► Prometheus
    │                 │
    │                 ▼
    │              Grafana
    │
    └──────────► CloudWatch
```

---

# 🔐 Security Strategy

Security will be integrated throughout the DevOps lifecycle.

Planned security practices include:

* Secure password hashing
* JWT authentication
* Environment-based configuration
* Secret management
* IAM least privilege
* Security Groups
* Code quality scanning
* Dependency management
* Container security
* Kubernetes Secrets
* Secure CI/CD practices

---

# 🔑 Configuration & Secrets

Development configuration should remain separate from production configuration.

Sensitive information should not be committed to Git.

Examples include:


SECRET_KEY
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
DATABASE_URL
API_KEYS
```

These values will eventually be managed through environment variables and appropriate secret-management mechanisms.

---

# 📁 Project Structure

The project follows a modular structure:


InsureFlow/
│
├── app/
│   ├── database/
│   │   └── database.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   ├── customer.py
│   │   ├── policy.py
│   │   └── claim.py
│   │
│   ├── routes/
│   │   ├── auth.py
│   │   ├── customers.py
│   │   ├── policies.py
│   │   └── claims.py
│   │
│   ├── schemas/
│   │   ├── auth.py
│   │   ├── customer.py
│   │   └── policy.py
│   │
│   ├── templates/
│   │   ├── dashboard.html
│   │   ├── customers.html
│   │   ├── policies.html
│   │   ├── claims.html
│   │   ├── analytics.html
│   │   ├── login.html
│   │   ├── register.html
│   │   └── settings.html
│   │
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   │
│   └── main.py
│
├── tests/
│   ├── conftest.py
│   ├── test_auth.py
│   ├── test_customers.py
│   ├── test_policies.py
│   ├── test_claims.py
│   └── test_health.py
│
├── docs/
│
├── terraform/
│
├── kubernetes/
│
├── jenkins/
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

# 💻 Local Development

## Prerequisites

The project currently uses:


Python 3.13+
Git
Visual Studio Code
PowerShell
```

Future stages will additionally require:


Docker
Jenkins
SonarQube
kubectl
Minikube
Helm
Terraform
AWS CLI
```

---

# ▶️ Run the Application

Activate the Python virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Start the FastAPI application:

```powershell
uvicorn app.main:app --reload
```

The application will be available at:


http://127.0.0.1:8000
```

---

# 📚 API Documentation

Once the application is running:

### Swagger UI


http://127.0.0.1:8000/docs
```

### ReDoc

http://127.0.0.1:8000/redoc
```

### Application


http://127.0.0.1:8000/
```

### Health Check


http://127.0.0.1:8000/health
```

---

# 🧰 Technology Stack

## Application

| Technology | Purpose                          |
| ---------- | -------------------------------- |
| Python     | Application programming language |
| FastAPI    | Backend API framework            |
| SQLAlchemy | ORM                              |
| Pydantic   | Data validation                  |
| Jinja2     | Server-side HTML templates       |
| SQLite     | Local development database       |
| JWT        | Authentication                   |
| pwdlib     | Password hashing                 |

## Testing

| Technology         | Purpose                     |
| ------------------ | --------------------------- |
| Pytest             | Automated testing           |
| FastAPI TestClient | API testing                 |
| HTTPX              | HTTP client/testing support |

## DevOps

| Technology | Purpose                 | Status         |
| ---------- | ----------------------- | -------------- |
| Git        | Version control         | ✅ In Use       |
| GitHub     | Source code hosting     | 🔄 In Progress |
| Docker     | Containerization        | ⏳ Planned      |
| SonarQube  | Code quality/security   | ⏳ Planned      |
| Kubernetes | Container orchestration | ⏳ Planned      |
| Minikube   | Local Kubernetes        | ⏳ Planned      |
| Helm       | Kubernetes packaging    | ⏳ Planned      |
| Terraform  | Infrastructure as Code  | ⏳ Planned      |
| AWS        | Cloud platform          | ⏳ Planned      |
| Jenkins    | CI/CD automation        | ⏳ Planned      |
| Prometheus | Metrics                 | ⏳ Planned      |
| Grafana    | Visualization           | ⏳ Planned      |
| CloudWatch | AWS monitoring          | ⏳ Planned      |

---

# 🔄 DevOps Lifecycle

The target InsureFlow DevOps lifecycle is:


                ┌──────────────┐
                │   Developer  │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │     Git      │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │    GitHub    │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │    Jenkins   │
                └──────┬───────┘
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
       Automated Tests      SonarQube
             │                   │
             └─────────┬─────────┘
                       ▼
                ┌──────────────┐
                │    Docker    │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │  Kubernetes  │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │   Terraform  │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │     AWS      │
                └──────┬───────┘
                       │
              ┌────────┴────────┐
              ▼                 ▼
         Prometheus          CloudWatch
              │
              ▼
           Grafana
```

---

# 📋 Project Roadmap

| Phase | Component                        | Status         |
| ----- | -------------------------------- | -------------- |
| 1     | FastAPI Application              | ✅ Completed    |
| 2     | Authentication                   | ✅ Completed    |
| 3     | Customer Management              | ✅ Completed    |
| 4     | Policy Management                | ✅ Completed    |
| 5     | Claims Management                | ✅ Completed    |
| 6     | Dashboard                        | ✅ Completed    |
| 7     | Analytics                        | ✅ Completed    |
| 8     | Automated Testing                | ✅ Completed    |
| 9     | Git Repository                   | ✅ Completed    |
| 10    | GitHub Repository                | 🔄 In Progress |
| 11    | Docker                           | ⏳ Planned      |
| 12    | SonarQube                        | ⏳ Planned      |
| 13    | Kubernetes                       | ⏳ Planned      |
| 14    | Minikube                         | ⏳ Planned      |
| 15    | Helm                             | ⏳ Planned      |
| 16    | Terraform                        | ⏳ Planned      |
| 17    | AWS Infrastructure               | ⏳ Planned      |
| 18    | AWS Deployment                   | ⏳ Planned      |
| 19    | Jenkins CI/CD                    | ⏳ Planned      |
| 20    | Prometheus                       | ⏳ Planned      |
| 21    | Grafana                          | ⏳ Planned      |
| 22    | CloudWatch                       | ⏳ Planned      |
| 23    | Final DevOps Documentation       | ⏳ Planned      |
| 24    | Resume & Interview Documentation | ⏳ Planned      |

---

# 📸 Screenshots

Application screenshots will be added as the project progresses.

Planned screenshots include:

* Login page
* Registration page
* Dashboard
* Customer management
* Policy management
* Claims management
* Analytics
* Settings
* Swagger API documentation
* Automated test execution
* Docker containers
* SonarQube dashboard
* Kubernetes resources
* Jenkins pipeline
* AWS infrastructure
* Monitoring dashboards

---

# 🛠️ Troubleshooting Approach

The project follows a structured troubleshooting process:


Identify Problem
      ↓
Check Application Logs
      ↓
Check Configuration
      ↓
Validate Dependencies
      ↓
Test Locally
      ↓
Check Infrastructure
      ↓
Validate Network / Security
      ↓
Apply Fix
      ↓
Retest
      ↓
Document Solution
```

This approach is intended to demonstrate practical DevOps troubleshooting rather than simply deploying an application.

---

# 📈 Reliability Strategy

The project will progressively introduce reliability practices including:

* Automated testing
* Health checks
* Container health checks
* Kubernetes readiness probes
* Kubernetes liveness probes
* Infrastructure as Code
* CI/CD automation
* Monitoring
* Logging
* Failure detection
* Deployment validation

---

# 💰 Infrastructure Cost Philosophy

InsureFlow is designed as a portfolio and learning project.

The cloud architecture will therefore prioritize:


Required Infrastructure
        +
Security
        +
Reliability
        +
Low Cost
```

Unnecessary cloud services will be avoided wherever possible.

The goal is to demonstrate practical AWS and DevOps knowledge without creating unnecessary infrastructure expenses.

---

# 📚 Documentation Roadmap

The project will eventually contain documentation for:

docs/
├── architecture.md
├── api.md
├── docker.md
├── kubernetes.md
├── terraform.md
├── aws.md
├── jenkins.md
├── monitoring.md
├── troubleshooting.md
└── deployment.md
```

---

# 🎓 DevOps Concepts Demonstrated

The project is designed to demonstrate practical knowledge of:

### Source Control

* Git
* GitHub
* Branching
* Commits
* Pull Requests
* Repository management

### CI/CD

* Jenkins
* Automated testing
* Quality gates
* Docker builds
* Deployment automation

### Containers

* Docker
* Dockerfiles
* Images
* Containers
* Container networking
* Health checks

### Kubernetes

* Pods
* Deployments
* Services
* ConfigMaps
* Secrets
* Namespaces
* Helm
* Health probes

### Infrastructure as Code

* Terraform
* Variables
* Outputs
* Modules
* State
* AWS infrastructure provisioning

### Cloud

* AWS
* EC2
* IAM
* VPC
* Security Groups
* CloudWatch

### Monitoring

* Prometheus
* Grafana
* CloudWatch
* Application health
* Infrastructure metrics

---

# 🚀 Project Outcomes

The completed project is intended to demonstrate the ability to:

* Develop a Python-based enterprise application
* Build REST APIs
* Implement authentication
* Design database models
* Write automated tests
* Use Git professionally
* Containerize applications
* Implement CI/CD
* Perform code quality analysis
* Deploy applications to Kubernetes
* Provision infrastructure using Terraform
* Deploy workloads to AWS
* Implement monitoring and observability
* Troubleshoot application and infrastructure issues
* Document a complete DevOps lifecycle

---

# 🔮 Future Enhancements

Potential future improvements include:

* Role-based access control
* Admin portal
* Advanced claims workflow
* Policy renewal management
* Email notifications
* Document upload
* Insurance document management
* PostgreSQL production database
* Redis caching
* Centralized logging
* Advanced monitoring
* Automated security scanning
* Blue-Green deployment
* Rolling deployments
* Disaster recovery
* Backup automation

---

# 📌 Current Project Status


Application Development      ████████████████████  Completed
Authentication               ████████████████████  Completed
Business Modules             ████████████████████  Completed
Automated Testing            ████████████████████  Completed
Git Repository               ████████████████████  Completed
GitHub                       ████░░░░░░░░░░░░░░░░  In Progress
Docker                       ░░░░░░░░░░░░░░░░░░░░  Planned
SonarQube                    ░░░░░░░░░░░░░░░░░░░░  Planned
Kubernetes                   ░░░░░░░░░░░░░░░░░░░░  Planned
Terraform                    ░░░░░░░░░░░░░░░░░░░░  Planned
AWS                          ░░░░░░░░░░░░░░░░░░░░  Planned
Jenkins                      ░░░░░░░░░░░░░░░░░░░░  Planned
Monitoring                   ░░░░░░░░░░░░░░░░░░░░  Planned
```

---

# 💼 Resume Project Description

A concise resume description for this project:

> **InsureFlow – Enterprise Insurance Management & DevOps Platform**
> Developed a Python/FastAPI-based insurance management platform with JWT authentication, customer, policy and claims modules, SQLAlchemy persistence, premium web UI, REST APIs and automated Pytest-based testing. Designed an end-to-end DevOps roadmap incorporating GitHub, Docker, SonarQube, Kubernetes, Helm, Terraform, AWS, Jenkins and Prometheus/Grafana monitoring.

---

# 🏆 Why InsureFlow?

InsureFlow combines:


Business Application
        +
Backend Development
        +
Database
        +
Authentication
        +
Automated Testing
        +
Git
        +
Docker
        +
Kubernetes
        +
Terraform
        +
AWS
        +
CI/CD
        +
Monitoring
```

This makes the project suitable for demonstrating an end-to-end DevOps engineering workflow.

---

# 🧭 InsureFlow DevOps Journey

The project follows the philosophy:


Code
 ↓
Commit
 ↓
Test
 ↓
Analyze
 ↓
Build
 ↓
Containerize
 ↓
Orchestrate
 ↓
Provision
 ↓
Deploy
 ↓
Monitor
 ↓
Improve
```

The objective is to continuously improve the application from a local development project into a cloud-ready, automated and observable platform.

---

# 📄 License

This project is currently intended for educational, portfolio and demonstration purposes.

A formal open-source license can be added when the project is prepared for public distribution.

---

# ⭐ InsureFlow

### Enterprise Insurance Management & End-to-End DevOps Platform

**Build → Test → Secure → Containerize → Orchestrate → Provision → Deploy → Monitor**

> A complete application and DevOps journey built around a realistic insurance-domain platform.
