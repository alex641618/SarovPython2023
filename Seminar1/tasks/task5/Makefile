run:
	python3 task5.py

clean:
ifeq ($(OS),Windows_NT)
	rmdir /q /s include\__pycache__
else
	rm -rf ./include/__pycache__
endif

.PHONY: run clean