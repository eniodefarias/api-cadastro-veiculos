.PHONY: help
-include makefiles/*.mk
ENV := -dev
# ENV := ""
VERSION := $(shell cat version)
PROJECT := veiculos-api


# Main variables
BASE_URL := http://localhost:8000

# ENVIRONMENT -----------------------------------------------------------------------------

# venv:
# python3 -m venv .venv
# source .venv/bin/activate
# source ~/.bashrc

help:			# exibe esta lista de comandos disponíveis
	@echo "---------------------------------------"
	@cat Makefile | grep -E '^[a-zA-Z0-9_-]+:.*?# .*$$' | awk 'BEGIN {FS = ":.*?# "}; {printf " make \033[36m%-15s\033[0m -> %s\n", $$1, $$2}'
	@echo "---------------------------------------"



setup:			# instala as dependencias python do projeto no venv local conforme o arquivo setup.py
	@echo "Iniciando SETUP \n"
	pip install -e ".[all]"
	@echo "\n SETUP completo"

api:			# executa a api via uvicorn localmente sem docker
	@echo "iniciando API web localmente"
	uvicorn veiculos-api.api.app:app --host 0.0.0.0 --port 8000 --reload --access-log  --log-level debug



# Build
build:			# realiza o build do projeto no docker local
	@echo "Realizando Docker Build ver:$(VERSION)"
	docker build --tag "veiculos-api-img-$(VERSION)" .
	@echo "Finalizado Docker Build ver:$(VERSION)"

stop:			# para o container docker local
	docker container stop "argus-ui-$(VERSION)"

run:			# executa o container docker local
	@echo "Realizando Docker RUN ver:$(VERSION)"
	docker run -it --rm -p 8000:8000 --name "veiculos-api-$(VERSION)" "veiculos-api-img-$(VERSION)"
	@echo "Finalizado Docker RUN ver:$(VERSION)"


docker-shell:	# abre uma sessão shell no docker local
	docker exec -it "veiculos-api-$(VERSION)" /bin/bash

# # TSURU
# tsuru-log:		# faz a chamada do log do tsuru
# 	tsuru app log -f -a "veiculos-api$(ENV)"

# tsuru-shell:	# abre uma sessão shell no tsuru
# 	tsuru app shell -a "veiculos-api$(ENV)"

# deploy:			# realiza o deploy diretamente no tsuru, mas verifique o ENV do Makefile antes de fazer isso. Tenha cuidado e atenção.
# 	tsuru app deploy -a "veiculos-api$(ENV)" --dockerfile .

