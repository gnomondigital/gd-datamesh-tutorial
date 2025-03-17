# gd-nasa-deployment

## Description
The `gd-nasa-deployment` project is designed to facilitate the deployment of NASA-related applications using Terraform. This repository contains the necessary configurations and scripts to manage infrastructure as code.

## Getting Started
To get started with this project, follow these steps:

Clone the repository:
   ```bash
   git clone https://gitlab.gnomondigital.com/gd-ksp/gd-nasa-deployment.git
   cd gd-nasa-deployment
   ```


## Project Structure
The project is structured as follows:

- `environments/`: Contains environment-specific configurations.
- `helper.yml`: CI/CD configurations for managing Terraform deployments.
- `images/`: Contains any relevant images for documentation or UI.
- `modules/`: Contains reusable Terraform modules.


### CI/CD Pipeline:
The project utilizes GitLab CI/CD for continuous integration and deployment. The following stages are defined:
  - `Validate`: Checks the Terraform configurations.
  - `Plan`: Creates an execution plan for Terraform.
  - `Apply`: Applies the planned changes to the infrastructure.
  - `Destroy`: Destroys the infrastructure when no longer needed.

### Usage
To validate, plan, and apply changes, use the following commands:

```bash
# Validate
terraform validate

# Plan
terraform plan

# Apply
terraform apply -auto-approve
```
## Run the code
### Foundation
Deploy the foundation environment:

```bash
cd environments/dev/foundation

# Validate
terraform init

# Plan
terraform plan

# Apply
terraform apply -auto-approve
```

Deploy the API gateway and cloud run:

```bash
cd environments/dev/gd-nasa-api

# Validate
terraform init

# Plan
terraform plan

# Apply
terraform apply -auto-approve
```


### Destroy :
Destroy all the deployments:

```bash
terraform destroy -auto-approve
```

## Connect with Us

- [LinkedIn](https://www.linkedin.com/company/gnomon-digital)
- [Medium](https://medium.com/gnomondigital)
- [Official Website](https://www.gnomondigital.com)