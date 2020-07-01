### Quick start 

#### Base build and run
```bash
# base build, and run 
git clone https://github.com/yennanliu/docker-airflow.git
cd docker-airflow
docker build --rm --build-arg AIRFLOW_DEPS="datadog,dask" -t yen/docker-airflow .
docker build --rm --build-arg PYTHON_DEPS="flask_oauthlib>=0.9" -t yen/docker-airflow .
docker run -d -p 8080:8080 yen/docker-airflow webserver
# Airflow UI : localhost:8080
```
#### LocalExecutor
```bash
# run from docker hub, docker-compose and run with LocalExecutor
git clone https://github.com/yennanliu/docker-airflow.git
cd docker-airflow
docker-compose -f docker-compose-LocalExecutor.yml up -d 
# Airflow UI : localhost:8080
```
#### CeleryExecutor
```bash
# run from docker hub, docker-compose and run with CeleryExecutor
git clone https://github.com/yennanliu/docker-airflow.git
cd docker-airflow
docker-compose -f docker-compose-CeleryExecutor.yml up -d 
# Airflow UI : localhost:8080
```