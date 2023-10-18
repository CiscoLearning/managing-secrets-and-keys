# README for Cisco Snack Minute Episode 122: Managing Secrets and Keys with .env, ConfigParser, and Hashicorp Vault

## Overview

Welcome to the repository for Cisco Snack Minute Episode 122, a supplemental material from the episode based on the content from the Cisco U DEVNAE course "Managing Secrets and Keys." This episode gives viewers an in-depth look into the utilization of .env files in Python, with additional insights into ConfigParser and Hashicorp Vault. If you're a student looking to secure your applications effectively, you're in the right place!

## Course Context

In the [Managing Secrets and Keys course](https://ondemandelearning.cisco.com/apollo-alpha/mc_naec10_10/pages/1), learners encounter a prevalent challenge: **how can developers store and access configuration data securely and portably**. This concern is further magnified when considering that sensitive data, such as database credentials, should not be a part of the codebase nor should it be visible in the version control system.

The DEVNAE Managing Secrets and Keys course covers multiple methodologies for managing such sensitive data:

- Using a configuration file
- Setting environment variables
- Passing command-line arguments
- Implementing application-based solutions like Ansible Vault or Hashicorp Vault

The knowledge imparted in the course is a crucial asset for both software developers and network automation engineers, ensuring they write code that's both secure and environment agnostic.

## Episode Focus: .env Files in Python

In this particular episode, our primary focus is on the usage of `.env` files in Python:

- **What are `.env` files?**  
  They are a type of configuration file that stores environment-specific variables. These files are generally kept outside of version control to prevent exposure of sensitive information.

- **Why use them?**  
  `.env` files offer a convenient way to switch between different environment configurations without altering the application's code.

- **How to use them in Python?**  
  There are various libraries, such as `python-dotenv`, which can read `.env` files and load their values into the environment, making it easy for Python applications to access them.

## Additional Insights: ConfigParser and Hashicorp Vault

While the episode's primary focus lies with `.env` files, in this Repo student will find some extra content about the ConfigParsers module and Hashicorp Vault:

- **ConfigParser**: A native Python library that allows developers to work with configuration files. It provides methods to read and write data from and to a configuration file, making it easier to manage application settings.

- **Hashicorp Vault**: An application-based solution designed for secret management. It securely stores and tightly controls access to secrets, providing a centralized source of truth.

## Get Started

To dive deeper into the content:

1. Watch Cisco Snack Minutes Episode 122.
2. Explore the code and resources provided in this repository.
3. Enroll in the [Cisco U](https://u.cisco.com/) DEVNAE course "Managing Secrets and Keys" for a comprehensive learning experience.

## Feedback and Contribution

Your feedback is invaluable. If you have suggestions, questions, or wish to contribute, please [open an issue](https://github.com/CiscoLearning/managing_secrets_and_keys/issues) or [submit a pull request](https://github.com/CiscoLearning/managing_secrets_and_keys/pulls).

Happy coding and stay secure!
[Barry Weiss, Technical Education Content Developer](barweiss@cisco.com)
