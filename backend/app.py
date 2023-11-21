"""Flask App"""

import flask
from flask import Flask, request, redirect, Response

app = Flask(__name__)


@app.route("/pizza", methods=['POST'])
def get_form_data() -> flask.Response:
    """
    Process a form submission at the "/pizza" route.

    This function handles a POST request containing form data with 'nombre' and
    'apellidos' parameters.

    It retrieves the values of 'nombre' and 'apellidos' from the form data,
    prints them to the console, and then redirects the client to
    "http://localhost/solicita_pedido.html".

    Returns
    -------
    flask.Response
        A Flask Response object for redirecting to
        "http://localhost/solicita_pedido.html".
    """
    nombre = request.form.get("nombre")
    apellidos = request.form.get("apellidos")
    print(f"{nombre} {apellidos}")
    return redirect("http://localhost/solicita_pedido.html", code=302)


@app.route("/checksize", methods=['POST'])
def checksize():
    """
    Endpoint to check the availability of a size.

    Returns
    -------
    Response
        A Flask Response containing the availability
         message with appropriate status code and headers.
    """
    # Get the size from the form data in the request
    size = request.form.get("size")

    # Check if the size is not "pequeña"
    if size == "S":
        mensaje = "No disponible"
    elif size == "":
        mensaje = ""
    else:
        mensaje = "Disponible"

    # Create a Flask Response with the availability message,
    # status code 200, and CORS header
    response = Response(
        mensaje, 200, {'Access-Control-Allow-Origin': '*'}
    )

    return response
