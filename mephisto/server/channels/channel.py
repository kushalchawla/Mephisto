#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from mephisto.abstractions.channel import *
import warnings

warnings.warn(
    "Import of the base Channel from `mephisto.server.channels.channel` is going away soon. "
    "Please replace all of your imports from mephisto.server.channels.channel "
    "to mephisto.abstractions.channel ",
    PendingDeprecationWarning,
)
