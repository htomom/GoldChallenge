import pandas as pd
import re
from flask_cors import request
from flasgger import Swagger, LazyString, LazyJSONEncoder
from flasgger import swag_from
from flask import Flask, request, jsonify
import fungsi

app.json_encoder = LazyJSONEncoder
swagger_template = dict(
info = {
    'title': LazyString(lambda: 'API Documentation for Data Processing and Modeling'),
    'version': LazyString(lambda: '1.0.0'),
    'description': LazyString(lambda: 'Dokumentasi API untuk Data Processing dan Modeling'),
    },
    host = LazyString(lambda: request.host)
)
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'docs',
            "route": '/docs.json',
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs/"
}
swagger = Swagger(app, template=swagger_template,             
                  config=swagger_config)






app = Flask(__name__)


# @app.route("/")
# def getData():
#     objgetData = getdata.getDatas()
#     data = objgetData.getAllData()
#     if len(data):
#         response = jsonify({
#             "result" : data,
#             "status" : 200,
#         })
#     elif:
#         response = jsonify({
#             "result" : [],
#             "status" : 400,
#         })
#     return response

# app.run("0.0.0.0", debug=True)