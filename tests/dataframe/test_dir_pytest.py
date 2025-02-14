#  Licensed to Elasticsearch B.V. under one or more contributor
#  license agreements. See the NOTICE file distributed with
#  this work for additional information regarding copyright
#  ownership. Elasticsearch B.V. licenses this file to you under
#  the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing,
#  software distributed under the License is distributed on an
#  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#  KIND, either express or implied.  See the License for the
#  specific language governing permissions and limitations
#  under the License.

# File called _pytest for PyCharm compatibility


from tests.common import TestData


class TestDataFrameDir(TestData):
    def test_flights_dir(self):
        ed_flights = self.ed_flights()

        print(dir(ed_flights))

        autocomplete_attrs = dir(ed_flights)

        for c in ed_flights.columns:
            # opensearch will save JSON values with sub-entries (like {A: {b: x}}) as A.b
            # these are not saved in pandas as attributes as they interfere with the naming convention
            # we ignore these for now
            if '.' not in c:
                assert c in autocomplete_attrs
