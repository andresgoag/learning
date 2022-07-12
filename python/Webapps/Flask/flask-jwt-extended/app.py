from datetime import timedelta

from flask import Flask, jsonify, request

from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required, JWTManager

app = Flask(__name__)


# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "super-secret"

# Configurar el tiempo de expirar un token
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)

jwt = JWTManager(app)


# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")
    if username != "andres" or password != 1234:
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username, fresh=True)
    refresh_token = create_refresh_token(identity=username)
    return {
        "access_token": access_token,
        "refresh_token": refresh_token
    }



# We are using the `refresh=True` options in jwt_required to only allow refresh tokens to access this route.
@app.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity, fresh=False)
    return {"access_token": access_token}



# Protect a route with jwt_required, which will kick out requests without a valid JWT present.
@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return {"logged_in_as": current_user}, 200



# Only allow fresh JWTs to access this route with the `fresh=True` arguement.
@app.route("/password", methods=["GET"])
@jwt_required(fresh=True)
def fresh_required():
    current_user = get_jwt_identity()
    return f"Bienvenido tiene un access_token fresh {current_user}"




if __name__ == "__main__":
    app.run(debug=True)
