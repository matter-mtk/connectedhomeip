#
#    Copyright (c) 2023 Project CHIP Authors
#
#    Licensed under the Apache License, Version 2.0 (the 'License');
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an 'AS IS' BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from ..pseudo_cluster import PseudoCluster

_DEFINITION = '''<?xml version="1.0"?>
<configurator>
<cluster>
    <name>CommissionerCommands</name>
    <code>0xFFF1FD04</code>

    <command source="client" code="0" name="PairWithCode">
        <arg name="nodeId" type="node_id"/>
        <arg name="payload" type="char_string"/>
    </command>

    <command source="client" code="1" name="Unpair">
      <arg name="nodeId" type="node_id"/>
    </command>

    <command source="client" code="2" name="GetCommissionerNodeId" response="GetCommissionerNodeIdResponse">
    </command>

    <command source="server" code="0" name="GetCommissionerNodeIdResponse">
      <arg name="nodeId" type="node_id"/>
    </command>
</cluster>
</configurator>
'''


class CommissionerCommands(PseudoCluster):
    name = 'CommissionerCommands'
    definition = _DEFINITION
