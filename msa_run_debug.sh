# build in docker:
sudo docker compose up --build -d
# testing on feature-branch: build a seperate service and remeber to change config.env in compose.yml:
sudo docker-compose -p feature up -d

# DEBUGGING
# 1. debugging ist direkt in VSC implementiert: benutze "Python: Debug with config.env"

# # 2. python im terminal:
# # uv venv --python 3.12.8
# # uv pip install -r requirements.txt
# source .venv/bin/activate
# set -a
# source config.env
# python ./src/deye_docker_entrypoint.py r 146

# kbialek's direct run:
./local-run.sh

# aus portainer sh console heraus:
python ./deye_docker_entrypoint.py r 672
