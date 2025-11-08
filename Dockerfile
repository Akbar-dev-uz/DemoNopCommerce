FROM ghcr.io/astral-sh/uv:python3.13-alpine

WORKDIR /app

COPY ./ /app

RUN uv sync

CMD ["uv", "run", "python3", "manage.py", "runserver", "0:8000"]

# docker build -t docker_drf_image .
# docker run --name dc_drf_container -p 8006:8000 -d docker_drf_image
# docker exec -it dc_drf_container sh
# docker cp
# uv run python3 manage.py migrate

# docker exec -it dc_drf_container sh -c 'uv run python3 manage.py migrate'
# docker exec -it dc_drf_container sh -c 'uv run python3 manage.py createsuperuser --username admin'

# docker tag docker_drf_image akbardevyz/docker_drf_image
# docker push akbardevyz/docker_drf_image
# docker run --name dc_drf_container -p 8006:8000 -d akbardevyz/docker_drf_image

# uv, dockerhub


