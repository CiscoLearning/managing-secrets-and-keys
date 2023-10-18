#! /usr/bin/env python3

import configparser
from textwrap import dedent

from jinja2 import Template

# Set config parser instance
config = configparser.ConfigParser()

# Load the Config .ini file
config.read('config.ini')

# Set Prod or Dev Environment
environment = config.get('DEFAULT', 'environment', fallback='dev')

# Save key values into script
py_version = config.get(f'web.app.{environment}', 'py_version')
version = config.get(f'web.app.{environment}', 'version')
ip = config.get(f'web.app.{environment}', 'ip')
port = config.getint(f'web.app.{environment}', 'port')
hostname = config.get(f'web.app.{environment}', 'hostname')
theme_type = config.get('web.app.theme', 'type', fallback='light')
debug_on = config.getboolean('web.app.logging', 'debug_on')


dockercompose_template = dedent("""\
    version: "3"

    services:
      {{ hostname }}:
        build:
          context: .
          dockerfile_inline: |
            FROM python:{{ py_version }}-bookworm

            LABEL environment={{ environment }}
            LABEL version={{ version }}

            WORKDIR /app

            COPY ./requirements.txt .

            COPY ./app/ /app

            RUN pip install -U pip && \\
              pip install -r requirements.txt

            ENV hostname={{ hostname }}
            ENV environment={{ environment }}
            ENV theme_type={{ theme_type }}
            ENV port={{ port }}
            ENV debug_on={{ debug_on }}

            EXPOSE {{ port }}

            CMD ["python3", "main.py"]
        container_name: {{ hostname }}
        hostname: {{ hostname }}
        networks:
          {{ 'dev-appnet' if environment == 'dev' else 'prod-appnet' }}:
            ipv4_address: "{{ ip }}"
        ports:
          - "{{ port }}:{{ port }}"

    networks:
      dev-appnet:
        ipam:
          config:
            - subnet: 172.19.0.0/24
      prod-appnet:
        ipam:
          config:
            - subnet: 172.20.0.0/24
""")

jinja_env = Template(dockercompose_template)

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

with open('docker-compose.yml', 'w', encoding='UTF-8') as f:
    f.write(dockercompose)

print("="*80, "\n DOCKER COMPOSE FILE RENDERED:\n\n")
print(dockercompose)
print("="*80, "\nTo run the application enter the following:\n\n > docker compose up")
