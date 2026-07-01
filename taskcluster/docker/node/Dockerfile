# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

FROM node:lts-slim@sha256:b31e7a42fdf8b8aa5f5ed477c72d694301273f1069c5a2f71d53c6482e99a2fc
LABEL maintainer="Mozilla Release Engineering <release@mozilla.com>"

VOLUME /builds/worker/checkouts

# Add worker user (node:lts-slim ships a 'node' user at uid 1000; run-task requires
# worker to be exactly uid 1000, so remove the pre-existing user first)
RUN userdel -r node && \
    useradd -d /builds/worker -s /bin/bash -m worker && \
    mkdir -p /builds/worker/artifacts

# %include-run-task

RUN apt-get update && apt-get install -y --no-install-recommends \
    git ca-certificates python3 && \
    rm -rf /var/lib/apt/lists/*

RUN npm install -g renovate@43.227.0

ENV HOME=/builds/worker \
    PATH=/builds/worker/.local/bin:$PATH

RUN chown -R worker:worker /builds/worker

# Set a default command useful for debugging
CMD ["/bin/bash", "--login"]
