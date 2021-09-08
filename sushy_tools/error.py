# Copyright 2018 Red Hat, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


class FishyError(Exception):
    """Create generic sushy-tools exception object"""

    def __init__(self, msg='Unknown error', code=500):
        super().__init__(msg)
        self.code = code


class AliasAccessError(FishyError):
    """Node access attempted via an alias, not UUID"""


class NotSupportedError(FishyError):
    """Feature not supported by resource driver"""


class NotFound(FishyError):
    """Entity not found."""

    def __init__(self, msg, code=404):
        super().__init__(msg, code)


class BadRequest(FishyError):
    """Malformed request."""

    def __init__(self, msg, code=400):
        super().__init__(msg, code)
