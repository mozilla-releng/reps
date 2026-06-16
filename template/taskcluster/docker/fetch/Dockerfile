FROM debian:bullseye-20260610@sha256:68cf0d859b046494f3c4288171bc477580e424f981d08f2a77742b982c32a38f

### Add worker user and setup its workspace.
RUN mkdir /builds && \
    groupadd -g 1000 worker && \
    useradd -u 1000 -g 1000 -d /builds/worker -s /bin/bash -m worker && \
    mkdir -p /builds/worker/workspace && \
    chown -R worker:worker /builds

# Declare default working folder
WORKDIR /builds/worker

RUN apt-get update && \
    apt-get install -y \
      gnupg \
      bzip2 \
      git \
      openssh-client \
      python3-requests \
      python3-zstd \
      unzip

# %include-run-task
