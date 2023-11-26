run:

ifeq ($(ARGS),$(NULL))
	echo "use command: make ARGS=[n_processes]"
else

ifeq ($(OS),Windows_NT)
	mpiexec -n $(ARGS) python3 .\task1.py
else
	mpirun -n $(ARGS) --oversubscribe --allow-run-as-root python task1.py
endif
endif

.PHONY: run