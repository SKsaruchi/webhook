from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def index():
    return request.base_url
def return_response():
    print(request.json);
    ## Do something with the request.json data.
    return Response(status=200)
if __name__ == "__main__": app.run(host="localhost",port=5000, debug=True)

# =============================================================================
# @app.route('/webhook', methods=['POST'])
# def webhook():
#     if request.method == 'POST':
#         print("Data received from Webhook is: ", request.json)
#         return "Webhook received!", 200
#     else:
#         abort(400)
#         
#         
# if __name__ == "__main__":
#     app.run()
# =============================================================================


# '/https://webhook.site/a27c65c7-09ce-41d7-a027-b4cf0315d69e'
# =============================================================================
#  from flask import Flask, request, Response
# app = Flask(__name__)
# @app.route('/my_webhook', methods=['POST'])
# def return_response():
#     print(request.json);
#     ## Do something with the request.json data.
#     return Response(status=200)
# if __name__ == "__main__": app.run()
# =============================================================================
