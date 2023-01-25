up:
	docker compose -f docker-compose-local.yaml up -d --remove-orphans

down:
	docker compose -f docker-compose-local.yaml down && docker network prune --force