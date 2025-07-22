import os
import json
from flask import Flask, jsonify, Response
import requests
import logging
import random
app = Flask(__name__)


logging.basicConfig(level=logging.DEBUG)
@app.route('/health', methods=['GET'])
def health_check():
    app.logger.debug("Health check endpoint hit")
    return jsonify({"status": "healthy"})
  


@app.route("/inference/<token>", methods=['GET'])
def get_inference(token = "ETH"):
    app.logger.debug(f"Inference endpoint hit with token: {token}")

    if token == "ETH":
      y_pred = random.uniform(-0.001, 0.001)
      print("Log Return Prediction", y_pred)
      return Response(str(y_pred), status=200)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8008)
 

#---------- Test Locally without running docker----------
#get_inference(token = "ETH")
