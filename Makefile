start:
	docker-compose up

stop: 
	docker-compose down

docker-build:
	docker-compose -d --build