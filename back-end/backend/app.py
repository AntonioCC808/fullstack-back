import flask
from flask import Flask, request, redirect

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