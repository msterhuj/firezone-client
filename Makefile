env:
	docker compose down
	rm -rfv docker/
	rm -fv .token
	docker compose up -d
	docker compose run --rm firezone bin/migrate
	docker compose run --rm firezone bin/create-or-reset-admin
	docker compose exec firezone bin/create-api-token > .token
