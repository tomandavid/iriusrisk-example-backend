docker build -t fastapi_image  --platform linux/amd64  .
docker tag fastapi_image:latest davidtoman/iriusrisk:fastapi_image
docker push davidtoman/iriusrisk:fastapi_image