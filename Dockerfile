FROM ubuntu:latest
MAINTAINER "Marcel Gietzmann-Sanders" "marcelsanders96@gmail.com"

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -y update && \
	apt-get -y upgrade && \
	apt-get install -y build-essential && \
	apt-get install -y libpq-dev

# basic editor installation
RUN apt-get -y install vim

# add python and libraries
RUN apt-get -y install python3.6 && \
	apt-get -y install python3-pip && \
	pip3 install --upgrade setuptools pip
RUN echo "alias python=python3.6" >> /root/.bashrc

RUN pip install pandas==1.0.1 \
				scikit-learn==0.22.1 \
				seaborn==0.10.0 \
				jupyterlab==1.2.6 \
                tqdm==4.43.0 \
                flask==1.1.2 \
                flask-bootstrap==3.3.7.1

# setting up ssh server
RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN echo "root:biotascape" | chpasswd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22 8888 5000

# rmate for piping sublime
RUN wget -O /usr/local/bin/rmate https://raw.github.com/aurora/rmate/master/rmate
RUN chmod a+x /usr/local/bin/rmate

# install git
RUN apt-get -y install git

# clone ackbar
WORKDIR /root
RUN git clone https://github.com/erebuseternal/biotascape.git
WORKDIR /

CMD ["/usr/sbin/sshd", "-D"]