# Generated from: 1e60bd33-9be2-4cfc-ae96-eee08ee67c12.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farm within a densely populated city environment. It includes site evaluation for structural integrity, microclimate analysis, and energy efficiency assessments. The workflow covers modular system design, nutrient solution formulation, and sensor network integration for real-time monitoring. It also incorporates regulatory compliance checks, community engagement initiatives, and iterative crop optimization cycles. The process concludes with a phased operational launch, continuous quality assurance, and adaptive resource management to maximize yield while minimizing environmental impact in an urban setting.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Site_Survey = Transition(label='Site Survey')
Structure_Test = Transition(label='Structure Test')
Climate_Study = Transition(label='Climate Study')
Energy_Audit = Transition(label='Energy Audit')

System_Design = Transition(label='System Design')
Nutrient_Mix = Transition(label='Nutrient Mix')
Sensor_Setup = Transition(label='Sensor Setup')

Regulation_Check = Transition(label='Regulation Check')
Community_Meet = Transition(label='Community Meet')

Crop_Trial = Transition(label='Crop Trial')
Monitor_Data = Transition(label='Monitor Data')
Yield_Review = Transition(label='Yield Review')
Adjust_Parameters = Transition(label='Adjust Parameters')

Resource_Plan = Transition(label='Resource Plan')
Launch_Phase = Transition(label='Launch Phase')
Quality_Audit = Transition(label='Quality Audit')

# Loop for Crop Optimization cycle: execute Crop_Trial, then Monitor_Data, then Yield_Review,
# then choose to exit or Adjust_Parameters then repeat cycle (B then A)
# A = Crop_Trial + Monitor_Data + Yield_Review (partial order)
crop_optimization_nodes = [Crop_Trial, Monitor_Data, Yield_Review]
crop_optimization_po = StrictPartialOrder(nodes=crop_optimization_nodes)
crop_optimization_po.order.add_edge(Crop_Trial, Monitor_Data)
crop_optimization_po.order.add_edge(Monitor_Data, Yield_Review)

loop_body = Adjust_Parameters
crop_optimization_loop = OperatorPOWL(operator=Operator.LOOP, children=[crop_optimization_po, loop_body])

# Concurrent modular system design activities: System_Design, Nutrient_Mix, Sensor_Setup
modular_design_po = StrictPartialOrder(nodes=[System_Design, Nutrient_Mix, Sensor_Setup])
# no order edges - fully concurrent

# Concurrent community/regulatory tasks: Regulation_Check, Community_Meet
community_regulation_po = StrictPartialOrder(nodes=[Regulation_Check, Community_Meet])
# no order edges - concurrent

# Concurrent finalization activities: Resource_Plan, Launch_Phase, Quality_Audit
finalization_po = StrictPartialOrder(nodes=[Resource_Plan, Launch_Phase, Quality_Audit])
# no order edges - concurrent

# Compose the start activities partial order: Site Survey --> Structure Test, Climate Study, Energy Audit after Structure Test
start_po = StrictPartialOrder(nodes=[Site_Survey, Structure_Test, Climate_Study, Energy_Audit])
start_po.order.add_edge(Site_Survey, Structure_Test)
start_po.order.add_edge(Structure_Test, Climate_Study)
start_po.order.add_edge(Structure_Test, Energy_Audit)

# Compose mid stage partial order:
# start_po --> modular_design_po and community_regulation_po concurrent
middle_po = StrictPartialOrder(nodes=[start_po, modular_design_po, community_regulation_po])
middle_po.order.add_edge(start_po, modular_design_po)
middle_po.order.add_edge(start_po, community_regulation_po)

# After middle, proceed to crop optimization loop
# Then finalization after loop
full_po = StrictPartialOrder(nodes=[middle_po, crop_optimization_loop, finalization_po])
full_po.order.add_edge(middle_po, crop_optimization_loop)
full_po.order.add_edge(crop_optimization_loop, finalization_po)

root = full_po