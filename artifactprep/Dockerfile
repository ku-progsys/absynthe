FROM ubuntu:22.04
RUN apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get install -y software-properties-common git curl build-essential \
  libssl-dev libreadline-dev zlib1g-dev libsqlite3-dev python3-pip g++-10 libz3-dev

RUN update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-10 10
RUN pip3 install numpy==1.26.4 scipy matplotlib plumbum pandas==1.5.3 pygments

RUN git clone https://github.com/rbenv/rbenv.git /root/.rbenv
RUN git clone https://github.com/rbenv/ruby-build.git /root/.rbenv/plugins/ruby-build
RUN ./root/.rbenv/plugins/ruby-build/install.sh
ENV PATH=/root/.rbenv/bin:$PATH
RUN echo 'eval "$(rbenv init -)"' >> /etc/profile.d/rbenv.sh
RUN echo 'eval "$(rbenv init -)"' >> .bashrc
RUN echo 'eval "$(rbenv init -)"' >> $HOME/.bash_profile
RUN /bin/bash -c "source $HOME/.bash_profile"
ENV CONFIGURE_OPTS=--disable-install-doc

RUN rbenv install 3.1.2
RUN rbenv global 3.1.2
RUN bash -l -c 'gem install bundler -v 2.3.22'



CMD ["bin/bash"]
