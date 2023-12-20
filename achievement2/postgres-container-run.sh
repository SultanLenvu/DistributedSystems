docker run -d -p 5432:5432 --name postgres-container -e POSTGRES_DB=testdb -e POSTGRES_USER=sultan -e POSTGRES_PASSWORD=lenvu postgres

docker run -d -p 5000:5000 --name app-container --link postgres-container sultanlenvu/node13_pyapp

curl -X POST name-13.hse.ru:30080/ -H "Content-Type: application/json" -d '{ "number": 1 }'

curl -X POST -H "Content-Type: application/json" -d '{"number": 1}' name-13.hse.ru:30080

