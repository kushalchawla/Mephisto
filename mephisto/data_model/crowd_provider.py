#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from mephisto.abstractions.crowd_provider import *
import warnings

warnings.warn(
    "Import of crowd provider content from `data_model` is going away soon. "
    "Please replace all of your imports from mephisto.data_model.crowd_provider "
    "to mephisto.abstractions.crowd_provider. ",
    PendingDeprecationWarning,
)
