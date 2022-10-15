import json

from flask import Flask, request

app = Flask(__name__)

@app.route("/callback/<client_id>",methods=['POST'])
def callback(client_id:str):
    data = request.get_json()
    
    client_data = data.get(client_id,"")

    resp = {"client_data":client_data}

    response = app.response_class(
        response=json.dumps(resp), status=200, mimetype="application/json"
    )
    return response

if __name__ == "__main__":
    app.run("0.0.0.0", 80, False)

"""
print("Server protocol:",request.environ.get('SERVER_PROTOCOL'))
print("\n\n**TCP DUMP BELOW****\n\n")
print(request.headers)
print(request.cookies)
print(request.data)
print(request.args)
print(request.form)
print(request.endpoint)
print(request.method)
print(request.remote_addr)    
"""