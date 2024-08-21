from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def request_details():
    # Get the HTTP method
    method = request.method

    # Get the requested path
    path = request.path

    # Get query string parameters, sorted by key
    query_params = dict(sorted(request.args.items()))

    # Get request headers, sorted by key
    headers = dict(sorted(request.headers.items()))

    # Get cookies, sorted by key
    cookies = dict(sorted(request.cookies.items()))

    # Get form data if any, sorted by key
    form_data = dict(sorted(request.form.items()))

    # Get the client's IP address
    remote_addr = request.remote_addr

    # Get the referrer
    referrer = request.referrer

    # Get the User-Agent
    user_agent = request.headers.get('User-Agent')

    # Get the HTTP version
    http_version = request.environ.get('SERVER_PROTOCOL')

    # Get the Host header
    host = request.headers.get('Host')

    # Get the Content-Type header
    content_type = request.headers.get('Content-Type')

    # Get the Authorization header
    authorization = request.headers.get('Authorization')

    # Get the Accept header
    accept = request.headers.get('Accept')

    # Get the Accept-Encoding header
    accept_encoding = request.headers.get('Accept-Encoding')

    # Get the Accept-Language header
    accept_language = request.headers.get('Accept-Language')

    # Get the X-Forwarded-For header (commonly used by proxies)
    x_forwarded_for = request.headers.get('X-Forwarded-For')

    # HTML template with Bootstrap
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Request Details</title>
        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="bg-light">
        <div class="container mt-5">
            <h1 class="mb-4">Request Details</h1>

            <h2>Request Headers</h2>
            <table class="table table-bordered table-striped">
                <thead class="thead-dark">
                    <tr>
                        <th scope="col">Header</th>
                        <th scope="col">Value</th>
                    </tr>
                </thead>
                <tbody>
                    {% for header, value in headers.items() %}
                        <tr>
                            <td>{{ header }}</td>
                            <td>{{ value }}</td>
                        </tr>
                    {% endfor %}
                </tbody>
            </table>

            <h2>Cookies</h2>
            <table class="table table-bordered table-striped">
                <thead class="thead-dark">
                    <tr>
                        <th scope="col">Cookie</th>
                        <th scope="col">Value</th>
                    </tr>
                </thead>
                <tbody>
                    {% if cookies %}
                        {% for cookie, value in cookies.items() %}
                            <tr>
                                <td>{{ cookie }}</td>
                                <td>{{ value }}</td>
                            </tr>
                        {% endfor %}
                    {% else %}
                        <tr><td colspan="2">No cookies</td></tr>
                    {% endif %}
                </tbody>
            </table>

            <h2>Form Data</h2>
            <table class="table table-bordered table-striped">
                <thead class="thead-dark">
                    <tr>
                        <th scope="col">Field</th>
                        <th scope="col">Value</th>
                    </tr>
                </thead>
                <tbody>
                    {% if form_data %}
                        {% for field, value in form_data.items() %}
                            <tr>
                                <td>{{ field }}</td>
                                <td>{{ value }}</td>
                            </tr>
                        {% endfor %}
                    {% else %}
                        <tr><td colspan="2">No form data</td></tr>
                    {% endif %}
                </tbody>
            </table>

            <h2>HTTP Method</h2>
            <table class="table table-bordered table-striped">
                <thead class="thead-dark">
                    <tr>
                        <th scope="col">Method</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>{{ method }}</td>
                    </tr>
                </tbody>
            </table>

            <h2>Requested Path</h2>
            <table class="table table-bordered table-striped">
                <thead class="thead-dark">
                    <tr>
                        <th scope="col">Path</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>{{ path }}</td>
                    </tr>
                </tbody>
            </table>

            <h2>Query Parameters</h2>
            <table class="table table-bordered table-striped">
                <thead class="thead-dark">
                    <tr>
                        <th scope="col">Parameter</th>
                        <th scope="col">Value</th>
                    </tr>
                </thead>
                <tbody>
                    {% if query_params %}
                        {% for param, values in query_params.items() %}
                            <tr>
                                <td>{{ param }}</td>
                                <td>{{ values }}</td>
                            </tr>
                        {% endfor %}
                    {% else %}
                        <tr><td colspan="2">No query parameters</td></tr>
                    {% endif %}
                </tbody>
            </table>

            <h2>Client Information</h2>
            <table class="table table-bordered table-striped">
                <thead class="thead-dark">
                    <tr>
                        <th scope="col">Info</th>
                        <th scope="col">Value</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>IP Address</td>
                        <td>{{ remote_addr }}</td>
                    </tr>
                    <tr>
                        <td>Referrer</td>
                        <td>{{ referrer or 'No referrer' }}</td>
                    </tr>
                    <tr>
                        <td>User-Agent</td>
                        <td>{{ user_agent }}</td>
                    </tr>
                    <tr>
                        <td>HTTP Version</td>
                        <td>{{ http_version }}</td>
                    </tr>
                    <tr>
                        <td>Host</td>
                        <td>{{ host }}</td>
                    </tr>
                    <tr>
                        <td>Content-Type</td>
                        <td>{{ content_type or 'Not provided' }}</td>
                    </tr>
                    <tr>
                        <td>Authorization</td>
                        <td>{{ authorization or 'Not provided' }}</td>
                    </tr>
                    <tr>
                        <td>Accept</td>
                        <td>{{ accept }}</td>
                    </tr>
                    <tr>
                        <td>Accept-Encoding</td>
                        <td>{{ accept_encoding }}</td>
                    </tr>
                    <tr>
                        <td>Accept-Language</td>
                        <td>{{ accept_language }}</td>
                    </tr>
                    <tr>
                        <td>X-Forwarded-For</td>
                        <td>{{ x_forwarded_for or 'Not provided' }}</td>
                    </tr>
                </tbody>
            </table>

        </div>
    </body>
    </html>
    """

    # Render the template with request data
    return render_template_string(html_content, method=method, path=path, query_params=query_params, headers=headers, cookies=cookies, form_data=form_data, remote_addr=remote_addr, referrer=referrer, user_agent=user_agent, http_version=http_version, host=host, content_type=content_type, authorization=authorization, accept=accept, accept_encoding=accept_encoding, accept_language=accept_language, x_forwarded_for=x_forwarded_for)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
