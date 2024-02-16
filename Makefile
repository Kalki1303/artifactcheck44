.PHONY: explain

CI ?= false

.PHONY: install
install: install-npm

LOCUST_USERS = 1
LOCUST_RUNTIME = 10
LOCUST_ITERATION=1

.PHONY: install-locust
install-locust: ## Install Locust
	@echo "-Installing locust...."
ifeq ($(CI),true)
	pip install locust
	pip install locust-plugins
	@echo "-Done"
endif

.PHONY: run-api-automation
run-api-automation:
	@echo "-running script...."
	locust -f src/automation.py --headless -u $(LOCUST_USERS) -t $(LOCUST_RUNTIME) -r $(LOCUST_ITERATION) --html report.html
