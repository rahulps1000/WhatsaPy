from flask import Flask, request, make_response

def routes(app: Flask):
    @app.route('/', methods=["GET"])
    def verify():
        if request.args.get("hub.verify_token") == app.verify_token:
            response = make_response(request.args.get("hub.challenge"), 200)
            response.mimetype = "text/plain"
            return response
        return "Invalid Verify Token"

    @app.route('/', methods=["POST"])
    def hook():
        print(request.args)