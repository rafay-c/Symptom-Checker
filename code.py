import infermedica_api

api = infermedica_api.APIv3Connector(app_id="APP_ID", app_key="APPKEY")

# Prepare initial patients diagnostic information. User Input
sex = "female"
age = 32
evidence = [
    {"id": "s_8", "choice_id": "present", "source": "initial"},
    {"id": "s_611", "choice_id": "present", "source": "initial"},
    {"id": "s_19", "choice_id": "present"}
]

# call diagnosis
response = api.diagnosis(evidence=evidence, sex=sex, age=age)

# Access question asked by API
print(response["question"])
# print(response["question"]["text"])  # actual text of the question
# print(response["question"]["items"])  # list of related evidence with possible answers
# print(response["question"]["items"][0]["id"])
# print(response["question"]["items"][0]["name"])
# print(response["question"]["items"][0]["choices"])  # list of possible answers
# print(response["question"]["items"][0]["choices"][0]["id"])  # answer id
# print(response["question"]["items"][0]["choices"][0]["label"])  # answer label

# Check the "should_stop" flag
#print(response["should_stop"])

# Next update the request and get next question:
evidence.append({
    "id": response["question"]["items"][0]["id"],
    "choice_id": response["question"]["items"][0]["choices"][0]["id"]  # Just example, the choice_id shall be taken from the real user answer
})

# call diagnosis method again
response = api.diagnosis(evidence=evidence, sex=sex, age=age)

# ... and so on, continue the interview and watch for the "should_stop" flag. 
# Once the API returns a "should_stop" flag with the value set to true, the interview questions should stop and you can present the condition results:

# Access list of conditions with probabilities
print(response["conditions"])
# print(response["conditions"][0]["id"])
# print(response["conditions"][0]["name"])
# print(response["conditions"][0]["probability"])
