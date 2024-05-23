#!/bin/bash
rm -rf api-python-fast-images/
git clone https://github.com/jeremialcala/api-python-fast-images.git
cp config.env api-python-fast-images/config.env
cd api-python-fast-images/ || exit
git checkout develop
git pull

docker rm -f api-python-fast-images
docker rmi api-python-fast-images
docker system prune -a -f
docker build -t api-python-fast-images:latest .
docker run -it -p 5004:5002 --name api-python-fast-images --restart unless-stopped -d api-python-fast-images
