docker_build:
	echo "Prepare docker here..."
	docker build -t ppkwu_lab1:latest .
docker_start:
	echo "Start docker here..."
	docker run -p 4080:4080 --name ppkwu_lab1_container ppkwu_lab1:latest &
docker_stop:
	echo "Stop docker here..."
	docker kill ppkwu_lab1_container
	docker container rm ppkwu_lab1_container
docker_clean:
	echo "Clean docker here..."
	-docker container rm ppkwu_lab1_container
	docker image rm ppkwu_lab1