VENV   := venv
PYTHON := ./$(VENV)/bin/python3
PIP    := ./$(VENV)/bin/pip
PYTEST := ./$(VENV)/bin/pytest

all: venv

relatorio.pdf: docs/analysis.md
	pandoc --from=markdown --output=$@ $<

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install --requirement requirements.txt

venv: $(VENV)/bin/activate

run: venv
	$(PYTHON) main.py

test: venv
	PYTHONPATH=. $(PYTEST)

clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete

.PHONY: all venv run clean
