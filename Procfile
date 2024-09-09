
# obs.: o app.log só é alimentado dentro da sessão Unit do tsuru veiculos-api-app
web: uvicorn veiculos-api.api.app:app --host 0.0.0.0 --port 8000 --reload --access-log --log-level debug  2>&1 | tee -a /var/log/app.log
