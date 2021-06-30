import infermedica_api


api = infermedica_api.APIv3Connector(app_id="***", app_key="***")
print(api.info())