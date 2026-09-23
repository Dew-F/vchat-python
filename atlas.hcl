data "external_schema" "sqlalchemy" {
    program = [
        "python",
        "load_models.py",
    ]
}

env "sqlalchemy" {
    src = data.external_schema.sqlalchemy.url

    url = "sqlite://data/vchat.db"

    dev = "sqlite://dev?mode=memory&_fk=1"

    migration {
        dir = "file://migrations"
    }

    format {
        migrate {
            diff = "{{ sql . \"  \" }}"
        }
    }
}