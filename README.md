# FastAPI Application

This repository contains a FastAPI application that provides a threat modeling service.

## Development

To run the application for development, use the following command:

```bash
docker-compose up
```

This will start the application and its dependencies in Docker containers.

## Deployment

To deploy the application manually, follow these steps:

1. Build and push the application to Docker Hub using the `docker-hub-push.sh` script.
2. Pull the application from Docker Hub and run it on an AWS EC2 server using the `docker-hub-pull.sh` script.

Make sure to set the following environmental variables before running the application:

- `SUPABASE_KEY`: The API key for Supabase.
- `SUPABASE_URL`: The URL for Supabase.
- `OPENAI_API_KEY`: The API key for OpenAI.

## Testing

To run the pytest tests, execute the following command:

```bash
pytest
```

This will run all the tests in the project.
