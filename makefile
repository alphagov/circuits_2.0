# makefile for circuits_2.0
google_sheet := 1IeOQEYtmFLlltHJrw4yC8FPtVd-0DtVZKhLIxoch2Ss
image := europe-west2-docker.pkg.dev/circuits-2point0/circuits/circuits


local-dev:
	gunicorn circuits:app

docker-build:
	docker build -t $(image) .

docker-run:
	docker run -p 8000:8080 $(image)

docker-clean:
	docker container prune -f

gcloud-build:
	gcloud builds submit --tag $(image)

cloud-push:
	docker push $(image)