run:
	docker build -t tasks_set .
	docker run --rm -it tasks_set /bin/sh
test:
	docker build -t tasks_set .
	docker run --rm -it tasks_set py.test -v test.py
