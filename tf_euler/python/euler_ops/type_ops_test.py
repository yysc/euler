# Copyright 2020 Alibaba Group Holding Limited. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""Euler type ops test"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import subprocess

from tensorflow.python.platform import test
import tensorflow as tf

from tf_euler.python.euler_ops import base
from tf_euler.python.euler_ops import type_ops as ops


class TypeOpsTest(test.TestCase):
    @classmethod
    def setUpClass(cls):
        base.initialize_graph({
            'mode': 'local',
            'data_path': '/tmp/euler',
            'sampler_type': 'all',
            'data_type': 'all'
        })

    def testGetNodeType(self):
        """Test euler get node type"""

        op = ops.get_node_type([1, 2, 3, 4, 5, 4])
        with tf.Session() as sess:
            node_types = sess.run(op)
            self.assertAllEqual([0, 1, 0, 1, 0, 1], node_types)


if __name__ == "__main__":
    test.main()
