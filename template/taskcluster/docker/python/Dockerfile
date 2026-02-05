# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

FROM debian:13-slim
LABEL maintainer="Mozilla Release Engineering <release@mozilla.com>"

VOLUME /builds/worker/checkouts
VOLUME /builds/worker/.task-cache/uv

# Add worker user
RUN useradd -d /builds/worker -s /bin/bash -m worker && \
    mkdir -p /builds/worker/artifacts

# %include-run-task

RUN apt-get update \
 && apt-get install -y --force-yes --no-install-recommends \
    ca-certificates \
    build-essential \
    git \
    python3

ENV SHELL=/bin/bash \
    HOME=/builds/worker \
    PATH=/builds/worker/.local/bin:$PATH

COPY --from=ghcr.io/astral-sh/uv:0.12.1 /uv /bin/uv

# %ARG PYTHON_VERSIONS
RUN uv python install $PYTHON_VERSIONS

RUN chown -R worker:worker /builds/worker

# Set a default command useful for debugging
CMD ["/bin/bash", "--login"]
