### Quick start 
```bash
git clone https://github.com/yennanliu/docker-airflow.git
cd docker-airflow
docker build --rm --build-arg AIRFLOW_DEPS="datadog,dask" -t yennanliu/docker-airflow .
docker build --rm --build-arg PYTHON_DEPS="flask_oauthlib>=0.9" -t yennanliu/docker-airflow .

```