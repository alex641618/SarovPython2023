run:
	python3 task3.py

clean:
ifeq ($(OS),Windows_NT)
	rmdir /q /s include\__pycache__
	rmdir /q /s saves
else
	rm -rf ./include/__pycache__
	rm -rf ./saves
endif

.PHONY: run clean