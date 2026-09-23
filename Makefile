.PHONY: db-diff db-apply db-status

db-diff:
	atlas migrate diff $(name) --env sqlalchemy

db-apply:
	atlas migrate apply --env sqlalchemy

db-status:
	atlas migrate status --env sqlalchemy

run:
	fastapi dev app/main.py
