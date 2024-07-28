docker kill fastapi_iriusrisk_container
docker rm fastapi_iriusrisk_container
docker pull davidtoman/iriusrisk:fastapi_image
docker run -d --name fastapi_iriusrisk_container -p 8101:80 davidtoman/iriusrisk:fastapi_image