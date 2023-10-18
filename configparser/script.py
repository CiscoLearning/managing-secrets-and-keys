import configparser
from textwrap import dedent

from jinja2 import Template

__author__ = "Barry Weiss - barweiss@cisco.com"

"""
This script generates a Docker Compose file for a Python web application.
It reads the configuration from a .ini file, then uses the Jinja2 template
library to render the Docker Compose configuration with the settings from
the .ini file. This script is meant for educational purposes.
"""

# Set up an instance of ConfigParser to read .ini files
config = configparser.ConfigParser()

# Load the configuration from the 'config.ini' file
config.read('config.ini')

# Retrieve the desired environment (prod or dev) from the configuration,
# with 'dev' as the default if not specified
environment = config.get('DEFAULT', 'environment', fallback='dev')

# Fetch the settings for the desired environment from the .ini file
py_version = config.get(f'web.app.{environment}', 'py_version')
version = config.get(f'web.app.{environment}', 'version')
ip = config.get(f'web.app.{environment}', 'ip')
port = config.getint(f'web.app.{environment}', 'port')  # get as integer
hostname = config.get(f'web.app.{environment}', 'hostname')
theme_type = config.get('web.app.theme', 'type', fallback='light')
debug_on = config.getboolean('web.app.logging', 'debug_on')  # get as boolean

# Define the Docker Compose template with placeholders for the Jinja2 library
dockercompose_template = dedent("""\
    # Docker Compose version
    version: "3"

    # Define the services for our app
    services:
      {{ hostname }}:
        build:
          # Current directory as build context
          context: .
          # Inline Dockerfile definition
          dockerfile_inline: |
            FROM python:{{ py_version }}-bookworm

            LABEL environment={{ environment }}
            LABEL version={{ version }}

            # Working directory in the container
            WORKDIR /app

            # Copying app dependencies
            COPY ./requirements.txt .

            # Copying the app source code
            COPY ./app/ /app

            # Installing app dependencies
            RUN pip install -U pip && \\
              pip install -r requirements.txt

            # Setting environment variables in the container
            ENV hostname={{ hostname }}
            ENV environment={{ environment }}
            ENV theme_type={{ theme_type }}
            ENV port={{ port }}
            ENV debug_on={{ debug_on }}

            # Expose the desired port for the service
            EXPOSE {{ port }}

            # Command to run on container start
            CMD ["python3", "main.py"]
        container_name: {{ hostname }}
        hostname: {{ hostname }}
        networks:
          # Use different networks based on environment
          {{ 'dev-appnet' if environment == 'dev' else 'prod-appnet' }}:
            ipv4_address: "{{ ip }}"
        ports:
          - "{{ port }}:{{ port }}"  # Map host port to container port

    # Define the networks used in services
    networks:
      dev-appnet:
        ipam:
          config:
            - subnet: 172.22.0.0/24
      prod-appnet:
        ipam:
          config:
            - subnet: 172.22.1.0/24
""")

# Create a Jinja2 template instance from the Docker Compose template
jinja_env = Template(dockercompose_template)

# Render the Docker Compose configuration using the values from the .ini file
dockercompose = jinja_env.render(
    py_version=py_version,
    version=version,
    environment=environment,
    hostname=hostname,
    theme_type=theme_type,
    debug_on=debug_on,
    ip=ip,
    port=port,
    )

# Write the rendered Docker Compose configuration to a file
with open('docker-compose.yml', 'w', encoding='UTF-8') as f:
    f.write(dockercompose)

# Display the rendered Docker Compose configuration for user verification
print("="*80, "\n DOCKER COMPOSE FILE RENDERED:\n\n")
print(dockercompose)
print("="*80, "\nTo run the application enter the following:\n\n > docker compose up --build")
