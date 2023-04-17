# makefile for circuits_2.0
google_sheet := 1IeOQEYtmFLlltHJrw4yC8FPtVd-0DtVZKhLIxoch2Ss


local-dev:
	python -m app

docker-build:
	docker build -t circuits .

docker-run:
	docker run -p 80:8080 circuits

docker-clean:
	docker container prune -f