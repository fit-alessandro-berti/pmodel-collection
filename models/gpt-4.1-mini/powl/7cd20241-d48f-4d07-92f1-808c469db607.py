# Generated from: 7cd20241-d48f-4d07-92f1-808c469db607.json
# Description: This process outlines the steps for reclaiming and repurposing remote or stranded physical assets, such as equipment or vehicles, located in inaccessible or hazardous environments. It involves remote assessment, coordination with local authorities, specialized transport logistics, environmental compliance checks, and final reintegration into the operational inventory. The process ensures minimal downtime, cost efficiency, and adherence to safety regulations while handling assets that require unconventional retrieval methods due to geographic, legal, or operational constraints.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Asset_Audit = Transition(label='Asset Audit')
Risk_Survey = Transition(label='Risk Survey')
Permit_Request = Transition(label='Permit Request')
Stakeholder_Notify = Transition(label='Stakeholder Notify')
Remote_Inspect = Transition(label='Remote Inspect')
Local_Liaison = Transition(label='Local Liaison')
Transport_Plan = Transition(label='Transport Plan')
Safety_Brief = Transition(label='Safety Brief')
Equipment_Prep = Transition(label='Equipment Prep')
Extraction_Execute = Transition(label='Extraction Execute')
Environmental_Check = Transition(label='Environmental Check')
Damage_Assess = Transition(label='Damage Assess')
Reconditioning = Transition(label='Reconditioning')
Inventory_Update = Transition(label='Inventory Update')
Report_Submit = Transition(label='Report Submit')

# Logical flow:
# 1. Initial assessment and coordination:
# Asset Audit and Risk Survey concurrent start
# then Permit Request and Stakeholder Notify concurrent
# then Remote Inspect and Local Liaison concurrent
# then Transport Plan and Safety Brief concurrent
# then Equipment Prep
# then Extraction Execute
# then Environmental Check and Damage Assess concurrent
# then Reconditioning
# then Inventory Update
# then Report Submit

# Construct partial orders for concurrent activities at each stage
stage1 = StrictPartialOrder(nodes=[Asset_Audit, Risk_Survey])
# no internal order - concurrent

stage2 = StrictPartialOrder(nodes=[Permit_Request, Stakeholder_Notify])
# no internal order - concurrent

stage3 = StrictPartialOrder(nodes=[Remote_Inspect, Local_Liaison])
# no internal order - concurrent

stage4 = StrictPartialOrder(nodes=[Transport_Plan, Safety_Brief])
# no internal order - concurrent

stage5 = Equipment_Prep
stage6 = Extraction_Execute

stage7 = StrictPartialOrder(nodes=[Environmental_Check, Damage_Assess])
# no internal order - concurrent

stage8 = Reconditioning
stage9 = Inventory_Update
stage10 = Report_Submit

# Now build sequential order of stages by making PO combining them and adding order edges

# We build from start to end:

# Level 1: stage1
# Level 2: stage2
# Level 3: stage3
# Level 4: stage4
# Level 5: stage5 (Equipment Prep)
# Level 6: stage6 (Extraction Execute)
# Level 7: stage7
# Level 8: stage8 (Reconditioning)
# Level 9: stage9 (Inventory Update)
# Level 10: stage10 (Report Submit)

# Build PO stepwise:

# PO_12 combines stage1 --> stage2
PO_12_nodes = [stage1, stage2]
PO_12 = StrictPartialOrder(nodes=PO_12_nodes)
PO_12.order.add_edge(stage1, stage2)

# PO_123 combines PO_12 --> stage3
PO_123_nodes = [PO_12, stage3]
PO_123 = StrictPartialOrder(nodes=PO_123_nodes)
PO_123.order.add_edge(PO_12, stage3)

# PO_1234 combines PO_123 --> stage4
PO_1234_nodes = [PO_123, stage4]
PO_1234 = StrictPartialOrder(nodes=PO_1234_nodes)
PO_1234.order.add_edge(PO_123, stage4)

# PO_12345 combines PO_1234 --> stage5
PO_12345_nodes = [PO_1234, stage5]
PO_12345 = StrictPartialOrder(nodes=PO_12345_nodes)
PO_12345.order.add_edge(PO_1234, stage5)

# PO_123456 combines PO_12345 --> stage6
PO_123456_nodes = [PO_12345, stage6]
PO_123456 = StrictPartialOrder(nodes=PO_123456_nodes)
PO_123456.order.add_edge(PO_12345, stage6)

# PO_1234567 combines PO_123456 --> stage7
PO_1234567_nodes = [PO_123456, stage7]
PO_1234567 = StrictPartialOrder(nodes=PO_1234567_nodes)
PO_1234567.order.add_edge(PO_123456, stage7)

# PO_12345678 combines PO_1234567 --> stage8
PO_12345678_nodes = [PO_1234567, stage8]
PO_12345678 = StrictPartialOrder(nodes=PO_12345678_nodes)
PO_12345678.order.add_edge(PO_1234567, stage8)

# PO_123456789 combines PO_12345678 --> stage9
PO_123456789_nodes = [PO_12345678, stage9]
PO_123456789 = StrictPartialOrder(nodes=PO_123456789_nodes)
PO_123456789.order.add_edge(PO_12345678, stage9)

# PO_12345678910 combines PO_123456789 --> stage10
PO_12345678910_nodes = [PO_123456789, stage10]
root = StrictPartialOrder(nodes=PO_12345678910_nodes)
root.order.add_edge(PO_123456789, stage10)