FROM python:3.11.10

# create non-root user and set the default user
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID
# Create group and user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

# Add sudo support
RUN apt-get update \
    && apt install -y software-properties-common \
    && apt-get update \
    && apt install -y sudo

# Configure sudo privileges
RUN echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# Clean up APT when done
RUN rm -rf /var/lib/apt/lists/*

USER $USERNAME

# set the PYTHONPATH to include src
ENV PYTHONPATH=src

# make all python tools installed by pip accesible
ENV PATH=$HOME/.local/bin:$PATH

# upgrade pip
RUN pip install --no-cache-dir pip --upgrade

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# install python tools
COPY requirements-dev.txt .
RUN pip install --no-cache-dir -r requirements-dev.txt
