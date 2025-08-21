# inf1407
Aulas de INF-1407 - Programação para web

iniciar virtual env:
    $cd docker
    $source  venv/bin/activate

encerrar virtual env:
    $deactivate

subir o container:
    $cd docker/static-site
    $sudo docker-compose up --build

interromper o container:
    $docker stop prog_web

informações sobre containers:
    $docker ps -a