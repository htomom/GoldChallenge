from flask import Flask, request, jsonify
import fungsiregex
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