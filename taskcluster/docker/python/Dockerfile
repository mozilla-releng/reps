# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

FROM debian:12-slim
LABEL maintainer="Mozilla Release Engineering <release@mozilla.com>"

VOLUME /builds/worker/checkouts
VOLUME /builds/worker/.cache

# Add worker user
RUN mkdir -p /builds && \
    useradd -d /builds/worker -s /bin/bash -m worker && \
    mkdir /builds/worker/artifacts && \
    chown worker:worker /builds/worker/artifacts

# %include-run-task

RUN apt-get update \
 && apt-get install -y --force-yes --no-install-recommends \
    ca-certificates \
    build-essential \
    openssh-client \
    python3 \
    python3-pip \
    python3-setuptools \
    python3-wheel \
    sudo \
    unzip \
    curl \
    ucf \
    git

ENV PATH=/builds/worker/bin:$PATH \
    SHELL=/bin/bash \
    HOME=/builds/worker

# %ARG UV_VERSION
COPY --from=ghcr.io/astral-sh/uv:$UV_VERSION /uv /bin/uv

# %ARG PYTHON_VERSIONS
RUN uv python install $PYTHON_VERSIONS
