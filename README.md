# Flask Application for Educational Purposes: Visualizing HTTP Requests on AWS EC2

## About the Project

This project is a Flask application designed to capture and display detailed information about HTTP requests, including headers, cookies, form data, and specific network information such as the client's IP address and headers added by AWS services like CloudFront and ALB. The primary purpose of this project is to demonstrate how a server-side application can access and display HTTP request details that are not available when using client-side JavaScript within a web browser.
This project complements another project I have developed, [HTTP Headers Tool](https://biagolini.github.io/WebPageShowHttpHeaders/), which explores how to analyze HTTP headers using JavaScript on the client side. The source code for that project can be found at [WebPageShowHttpHeaders](https://github.com/biagolini/WebPageShowHttpHeaders). Together, these projects provide a comprehensive understanding of HTTP headers from both server-side and client-side perspectives.

## Objective

The objective of this project is to provide a simple, educational tool for visualizing HTTP request data on a server running on AWS EC2. This project is intended solely for study and demonstration purposes, allowing users to see the differences between what can be captured on the server versus in the browser.
**Note**: This project is not intended for production use. Any attempt to deploy it in a production environment is done at the user's own risk.

## How to Deploy on AWS EC2

### 1. Update and Install Dependencies

```
sudo yum update -y
sudo yum install -y git gcc python3-devel
```

### 2. Install pip

```
curl -O https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
sudo pip3 install Flask gunicorn
```

### 3. Set Up Project Directory

```
sudo mkdir -p /var/pythonscript
cd /var/pythonscript
```

### 4. Clone the Project Repository

```
sudo rm -rf /var/pythonscript/{*,.*}
sudo git clone https://github.com/biagolini/PythonWebPageShowHttpRequestInfo /var/pythonscript
sudo chown -R ec2-user:ec2-user /var/pythonscript
sudo chmod -R 755 /var/pythonscript
```

### 5. Create a systemd Service File for Gunicorn

Create a new service file using your preferred text editor:

```
sudo nano /etc/systemd/system/pythonscript.service
```

Add the following content to the file:

```
[Unit]
Description=Gunicorn instance to serve Flask application
After=network.target

[Service]
User=root
Group=root
WorkingDirectory=/var/pythonscript
ExecStart=/usr/local/bin/gunicorn --workers 4 --bind 0.0.0.0:80 app:app
Restart=always

[Install]
WantedBy=multi-user.target
```

**Note**: In Linux, only the root user can bind to ports below 1024 by default. Since this project is intended for educational purposes only, it is configured to run as the root user for simplicity. In a production environment, alternative solutions should be considered, such as:

- Running Gunicorn on a higher port.
- Setting up a web server (such as Nginx or Apache) as a reverse proxy.

Explanation of the service file:

- [Unit]: Defines the service and its dependencies.
- [Service]:
  - User and Group: Specifies the user and group under which the service runs.
  - WorkingDirectory: Sets the directory where the service operates.
  - ExecStart: Command to start Gunicorn with the specified number of workers and binding address.
- [Install]: Specifies when the service should start.

### 6. Start and Enable the Service

```
sudo systemctl daemon-reload
sudo systemctl start pythonscript.service
sudo systemctl enable pythonscript.service
```

Verify that the service is running correctly:

```
sudo systemctl status pythonscript.service
```

## Conclusion

This project serves as an educational tool for understanding how HTTP requests are handled and processed on the server side in a Flask application hosted on AWS EC2. It complements the [HTTP Headers Tool](https://biagolini.github.io/WebPageShowHttpHeaders/) project, providing a insight into HTTP headers and other request details that are not accessible via client-side JavaScript.

## Limitations

- This project is intended for educational purposes only and should not be used in other context (such as production environments).
- The use of root privileges to bind to port 80 is done purely for simplicity in this demonstration. In a real-world scenario, this approach is not recommended due to security concerns.

## Contributing

Feel free to submit issues, create pull requests, or fork the repository to help improve the project.

## License and Disclaimer

This project is open-source and available under [MIT License](https://opensource.org/licenses/MIT). You are free to copy, modify, and use the project as you wish. However, any responsibility for the use of the code is solely yours. Please use it at your own risk and discretion.
