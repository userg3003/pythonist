PYTHONPATH=.
REQ=requirements


ifndef PYTHON
	PYTHON=python
endif
ifndef PIP
	PIP=pip
endif


.PHONY: config build publish clean deps run run-env run-full run-rebuild test-integration test-unit test




clean:
	rm -rf build/
	rm -rf dist/
	rm -rf grader_v2_auth_service.egg-info
	rm -rf data/test/temp/

deps:
	$(ENVS) $(PIP) install -r $(REQ)

