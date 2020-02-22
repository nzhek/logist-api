#!/usr/bin/env python
from migrate.versioning.shell import main

if __name__ == '__main__':
    main(repository='logist_db', url='postgresql://postgres:postgres@localhost:5432/logist_api', debug='False')
