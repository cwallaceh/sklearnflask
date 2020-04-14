# POST method predict
curl -d '[{"Pclass": 1, "Age": 23, "SibSp": 1, "Parch": 1, "Fare": 0}]' \
     -H "Content-Type: application/json" \
     -X POST http://localhost:8080/predict && \
    echo -e "\n -> predict OK"

# GET method info
curl -X GET http://localhost:8080/info && \
    echo -e "\n -> info OK"
