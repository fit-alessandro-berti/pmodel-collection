# Generated from: 0ab6f23e-f081-4f9e-a6b9-f665a0b8cbf6.json
# Description: This process outlines the comprehensive steps required to establish an urban vertical farming system in a repurposed industrial building. It involves site analysis, environmental control design, modular system installation, nutrient solution calibration, and continuous monitoring. The process integrates IoT sensor deployment for real-time data collection, adaptive lighting adjustments, and automated pest management to optimize plant growth. Additionally, it incorporates community engagement for local sourcing, waste recycling strategies, and a scalable business model to ensure sustainable urban food production. Each activity ensures operational efficiency, resource conservation, and product quality in a complex, space-constrained urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Site_Survey = Transition(label='Site Survey')
Structural_Check = Transition(label='Structural Check')
Layout_Design = Transition(label='Layout Design')
Sensor_Install = Transition(label='Sensor Install')
Env_Control = Transition(label='Env Control')
Module_Build = Transition(label='Module Build')
Nutrient_Mix = Transition(label='Nutrient Mix')
Lighting_Setup = Transition(label='Lighting Setup')
Irrigation_Test = Transition(label='Irrigation Test')
Pest_Scan = Transition(label='Pest Scan')
Data_Sync = Transition(label='Data Sync')
Growth_Audit = Transition(label='Growth Audit')
Waste_Sort = Transition(label='Waste Sort')
Community_Meet = Transition(label='Community Meet')
Market_Plan = Transition(label='Market Plan')
Scale_Review = Transition(label='Scale Review')

# First phase: Site survey and structural check (sequential)
initial_PO = StrictPartialOrder(nodes=[Site_Survey, Structural_Check, Layout_Design])
initial_PO.order.add_edge(Site_Survey, Structural_Check)
initial_PO.order.add_edge(Structural_Check, Layout_Design)

# Second phase: Sensor install and environment control design (sequential)
environment_PO = StrictPartialOrder(nodes=[Sensor_Install, Env_Control])
environment_PO.order.add_edge(Sensor_Install, Env_Control)

# Third phase: Modular system installation and testing (sequential)
module_PO = StrictPartialOrder(nodes=[Module_Build, Nutrient_Mix, Lighting_Setup, Irrigation_Test, Pest_Scan])
module_PO.order.add_edge(Module_Build, Nutrient_Mix)
module_PO.order.add_edge(Nutrient_Mix, Lighting_Setup)
module_PO.order.add_edge(Lighting_Setup, Irrigation_Test)
module_PO.order.add_edge(Irrigation_Test, Pest_Scan)

# Fourth phase: Data synchronization and growth audit (sequential)
data_PO = StrictPartialOrder(nodes=[Data_Sync, Growth_Audit])
data_PO.order.add_edge(Data_Sync, Growth_Audit)

# Fifth phase: Waste sort and community meet (these can be concurrent)
community_PO = StrictPartialOrder(nodes=[Waste_Sort, Community_Meet])

# Sixth phase: Market planning and scale review (sequential)
business_PO = StrictPartialOrder(nodes=[Market_Plan, Scale_Review])
business_PO.order.add_edge(Market_Plan, Scale_Review)

# Integrate IoT adaptive controls as a loop between Env_Control and Lighting_Setup
# Loop: Env_Control followed by a choice to exit or do Lighting_Setup + Pest_Scan then loop again
lighting_pest_PO = StrictPartialOrder(nodes=[Lighting_Setup, Pest_Scan])
lighting_pest_PO.order.add_edge(Lighting_Setup, Pest_Scan)
loop_body = StrictPartialOrder(nodes=[lighting_pest_PO])
# In POWL structure, the loop children: first is "do A" (Env_Control), second is "B" (lighting+pest control cycle)
loop = OperatorPOWL(operator=Operator.LOOP, children=[Env_Control, lighting_pest_PO])

# Because Env_Control appears already in environment_PO, rebuild environment_PO merging loop for adaptive control:
# Actually model environment_PO as Site: Sensor_Install --> loop

env_loop_PO = StrictPartialOrder(nodes=[Sensor_Install, loop])
env_loop_PO.order.add_edge(Sensor_Install, loop)

# Combine initial_PO, env_loop_PO, module_PO in a sequence (Site Survey/Structural/Layout)
# then Sensor Install + loop, then module build and tests

phase1_2_3_PO = StrictPartialOrder(
    nodes=[initial_PO, env_loop_PO, module_PO]
)
phase1_2_3_PO.order.add_edge(initial_PO, env_loop_PO)
phase1_2_3_PO.order.add_edge(env_loop_PO, module_PO)

# Combine data sync and growth audit as next phase after module_PO
phase1_to_data_PO = StrictPartialOrder(
    nodes=[phase1_2_3_PO, data_PO]
)
phase1_to_data_PO.order.add_edge(phase1_2_3_PO, data_PO)

# Waste sort and community meet are concurrent, but logically before business planning
# Combine with business plans in sequence after data audit
last_PO = StrictPartialOrder(
    nodes=[community_PO, business_PO]
)
last_PO.order.add_edge(community_PO, business_PO)

# Combine everything final in sequence:
root = StrictPartialOrder(
    nodes=[phase1_to_data_PO, last_PO]
)
root.order.add_edge(phase1_to_data_PO, last_PO)