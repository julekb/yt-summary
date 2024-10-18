l-build:
	docker build -t docker-image:yt-summary .

l-run:
	docker run -p 9000:8080 --name "lambda-yt-container" docker-image:yt-summary

l-bash:
	docker exec -it lambda-yt-container bash

l-curl:
	curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'

l-rebuild:
	docker stop lambda-yt-container
	docker rm lambda-yt-container
	make l-build

format:
	black src
	isort src

test:
	pytest src
