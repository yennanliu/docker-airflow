### Quick start 
```bash
git clone https://github.com/yennanliu/docker-airflow.git
cd docker-airflow
docker build --rm --build-arg AIRFLOW_DEPS="datadog,dask" -t yen/docker-airflow .
docker build --rm --build-arg PYTHON_DEPS="flask_oauthlib>=0.9" -t yen/docker-airflow .
docker run -d -p 8080:8080 yen/docker-airflow webserver
```