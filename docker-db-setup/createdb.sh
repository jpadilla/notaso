#!/bin/bash
echo "******CREATING NOTASO DATABASE******"
gosu postgres postgres --single <<- EOSQL
   CREATE DATABASE notaso;
   GRANT ALL PRIVILEGES ON DATABASE notaso to postgres;
EOSQL
echo ""
echo "******NOTASO DATABASE CREATED******"