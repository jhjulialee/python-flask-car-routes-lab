#!/usr/bin/env python3

from flask import Flask


# Models that Flatiron Cars currently has in its fleet.
existing_models = ["Beedle", "Crossroads", "M2", "Panique"]

app = Flask(__name__)


@app.route("/")
def index():
    """Return the Flatiron Cars welcome message."""
    return "Welcome to Flatiron Cars"


@app.route("/<model>")
def model_details(model):
    """Return fleet availability information for a requested model."""
    if model in existing_models:
        return f"Flatiron {model} is in our fleet!"

    return f"No models called {model} exists in our catalog"


if __name__ == "__main__":
    app.run(port=5555, debug=True)