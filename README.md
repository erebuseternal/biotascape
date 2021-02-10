# biotascape

## Docker Instructions

#### Building the Image
`docker build -t "mgietzmann/biotascape:latest" .`

#### Running the Image
`docker run -p 8888:8888 -p 8000:22 -p 5000:5000 -d --name=biotascape mgietzmann/biotascape:latest`

#### SSH into the Container
`ssh root@localhost -p 8000`

#### Stopping the Container
`docker container stop biotascape`

#### Removing the Container
`docker container rm biotascape`

## Jupyter Instructions

#### Running Jupyter Lab
```
ssh root@localhost -p 8000
jupyter lab --ip=0.0.0.0 --allow-root
exit
```

## Sublime Instructions
First you'll need to install rsub on sublime (see the first step here: https://acarril.github.io/posts/ssh-sripts-st3)

Then with the container running, open a tunnel with:
`ssh -R 52698:localhost:52698 root@localhost -p 8000`

Then within the container run `rmate <file>` to pipe that file up to sublime.

## Setting Up SSL

Taken from https://blog.miguelgrinberg.com/post/running-your-flask-application-over-https

### Generate the Certificate

```bash
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
```

Fill out the info

```bash
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:US
State or Province Name (full name) [Some-State]:Massachusetts
Locality Name (eg, city) []:Quincy
Organization Name (eg, company) [Internet Widgits Pty Ltd]:Biotascape
Organizational Unit Name (eg, section) []:Developers
Common Name (e.g. server FQDN or YOUR name) []:Biotascape
Email Address []:marcelsanders96@gmail.com
```

This will create a `key.pem` and `cert.pem` file. Simply move those to the top directory of the `webapp` folder and you're good to go!

## User Login (for now)
For now we'll be using a sqlite database to store everything as there's no need for anything more exciting than that while we're developing stuff. User login will all be there but you just need to setup the database. You can do so by going into the top directory of biotascape and going into a python interactive session and executing 

```python
from webapp import db, create_app
db.create_all(app=create_app())
```

The login setup was drawn from this lovely tutorial: https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login

## iNaturalist Auth

### Some Notes
If you run into issues with the `cryptography` library this worked for me:

```bash
pip install cryptography --force-reinstall
```

Here's the tutorial I drew from: https://github.com/authlib/demo-oauth-client/blob/master/flask-google-login/app.py