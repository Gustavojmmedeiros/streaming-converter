ARG UBUNTU_VERSION=24.04
FROM ubuntu:${UBUNTU_VERSION}

ARG PYENV_VERSION=2.3.35
ARG POETRY_VERSION=1.7.1
ARG PYTHON_VERSION=3.12.1

##############################################################################################################
# Initial Container Setup
##############################################################################################################

# Updating Packages (and installing pre-requisite for .dotfiles)
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt upgrade -y && apt install -y git locales

# Copy custom scripts and set the required permissions
COPY custom-scripts/ /tmp/scripts/
RUN chmod +x /tmp/scripts/*

# Install General Tools
RUN apt install -y nano htop

##############################################################################################################
# Install and Setup Python
##############################################################################################################

# Setup Locales
RUN echo "LC_ALL=en_US.UTF-8" >> /etc/environment \
    && echo "en_US.UTF-8 UTF-8" | tee -a /etc/locale.gen \
    && echo "LANG=en_US.UTF-8" | tee -a /etc/locale.conf \
    && locale-gen en_US.UTF-8

# Install Pyenv (for non-root user please change the /root in ENV PYENV_ROOT)
ENV PYENV_ROOT="/root/.pyenv"
ENV PATH="${PATH}:${PYENV_ROOT}/bin"
ENV PYENV_GIT_TAG=v${PYENV_VERSION}
RUN apt-get install -y \
    build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev \
    libsqlite3-dev curl libncursesw5-dev xz-utils tk-dev libxml2-dev \
    libxmlsec1-dev libffi-dev liblzma-dev \
    && curl https://pyenv.run | bash \
    && pyenv install ${PYTHON_VERSION} && pyenv global ${PYTHON_VERSION}

# Install Poetry
RUN unset PYENV_VERSION \
    && curl -sSL https://install.python-poetry.org | POETRY_VERSION=${POETRY_VERSION} pyenv exec python3 -
