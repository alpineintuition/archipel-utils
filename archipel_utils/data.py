"""Copyright Alpine Intuition Sàrl team.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import io

import numpy as np


def serialize_array(array: np.ndarray) -> bytes:
    """Serialize a numpy array into bytes."""
    buffer = io.BytesIO()
    np.save(buffer, array)
    return buffer.getvalue()


def deserialize_array(serialized_array: bytes) -> np.ndarray:
    """Serialize a bytes variable into numpy array."""
    return np.load(io.BytesIO(serialized_array))
