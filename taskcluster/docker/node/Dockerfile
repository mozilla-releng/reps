# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

FROM node:lts-slim@sha256:ba849c60be29959425b8734d57b8b4b7d56f98edd9504c9af091d5281095a71e
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

RUN npm install -g renovate@44.51.0

ENV HOME=/builds/worker \
    PATH=/builds/worker/.local/bin:$PATH

RUN chown -R worker:worker /builds/worker

# Set a default command useful for debugging
CMD ["/bin/bash", "--login"]
