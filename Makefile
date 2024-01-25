.PHONY: test update-packages

test:
	@pytest tests/

update-packages:
	@poetry install
