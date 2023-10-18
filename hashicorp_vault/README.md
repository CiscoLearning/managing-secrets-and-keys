# Introduction to HashiCorp Vault

## Setting Up the Environment

Start the Vault container using Docker Compose.

```bash
docker compose up
```

## Accessing the Vault Container

Log in to the Vault container. Note that this is a development instance, and we'll explore basic features as the root user.

```bash
docker exec -it dev-vault /bin/sh
```

## Verifying Vault Status

Check if Vault is up and running.

```bash
vault status
```

## Understanding Secrets Engines

Vault supports various types of secret engines. The key/value secrets engine simply stores and reads data. Other secret engines can connect to external services to generate dynamic credentials or provide encryption as a service.

## Working with Key/Value Secrets Engine

Adding a Key-Value Pair
To add a key-value pair to the secrets engine, use the following command:

```bash
vault kv put -mount=secret dev_api_keys app_api_key=1234ABCD
```

Note: Vault uses similar logic like CRUD (Create, Read, Update, Delete) and file layout principles.

## Updating a Key-Value Pair

To update a key-value pair in the api_keys folder, use the patch verb.

```bash
vault kv patch -mount=secret dev_api_keys app2_api_key=1234ABCD
```

## Creating Another Path

You can create another path for storing secrets.

```bash
vault kv put -mount=secret prod_api_keys app_api_key=1234ABCD
```

## Listing and Retrieving Secrets

### Listing Paths

To list all the available paths, use the list command.

```bash
vault kv list -mount=secret
```

### Retrieving Keys

To retrieve keys from a specific path, use the get command.

```bash
vault kv get -mount=secret dev_api_keys
```

```bash
vault kv get -mount=secret prod_api_keys
```

## Exiting the Container

To exit the container, simply type `exit`.

## Using Curl for API Access

## Retrieve Secrets

To retrieve secrets using curl:

```bash
curl -k -H "X-Vault-Token: 1234QWer" https://127.0.0.1:8200/v1/secret/data/dev_api_keys | jq -r ".data"
```

## Update Secrets

To update secrets using curl:

```bash
curl -k -H "X-Vault-Token: 1234QWer" -H "Content-Type: application/merge-patch+json" -X PATCH --data '{ "data": {"new_api2": "1234ABCD"} }' https://127.0.0.1:8200/v1/secret/data/dev_api_keys | jq
```
