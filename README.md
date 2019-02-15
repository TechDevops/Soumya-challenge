# Deploying running instance of a webserver  in AWS using Ansible

## Ansible 

### Roles:
  - ngnix
  - Infrastructure for  EC2 Provision in AWS
  - Used ami_template for auto scaling

#### executing Playbook:
  - Update  env variables in awsenvvars.yml in files directory
  - Add the ec2 .pem file in files directory
  - Update main.yml in roles specified  ec2 role and ami role
  - Update main.yml in defaults in snapshot_ami_template role
  - Execute ansible  playbook

##### Python script for validating credit card numbers:
  - Evaluate given set of credit card numbers valid or invalid


