# biotascape

## Docker Instructions

#### Building the Image
`docker build -t "mgietzmann/biotascape:latest" .`

#### Running the Image
`docker run -p 8888:8888 -p 8000:22 -d --name=biotascape mgietzmann/biotascape:latest`

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

