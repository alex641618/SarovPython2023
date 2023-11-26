run:
	python3 task2.py

clean:
ifeq ($(OS),Windows_NT)
	del /q /s movie.gif
else
	rm -rf ./movie.gif
endif

.PHONY: run clean