import os

from flask import Flask, render_template

# Initialize the Flask web application
app = Flask(__name__)

# Retrieve environment variables to configure the application
port = os.environ['port']                # Port on which the application will run
environment = os.environ['environment']  # Application environment (e.g., 'prod' or 'dev')
hostname = os.environ['hostname']        # Hostname for the application
theme_type = os.environ['theme_type']    # UI Theme type (e.g., 'light' or 'dark')
debug = os.environ['debug_on']           # Debug mode for the application (True or False)


@app.route('/', methods=['GET'])
def index():
    """
    Handles the root endpoint of the application and returns the rendered index.html template.

    The template uses variables like hostname, theme_type, and environment to customize its content.

    Returns:
        render_template: A rendered HTML template.
    """
    return render_template(
        'index.html',
        hostname=hostname,
        theme_type=theme_type,
        environment=environment,
    )


if __name__ == "__main__":
    # This block ensures the Flask app runs only if this script is executed directly
    # and not imported as a module elsewhere.
    app.run(host='0.0.0.0', port=port, debug=debug)
