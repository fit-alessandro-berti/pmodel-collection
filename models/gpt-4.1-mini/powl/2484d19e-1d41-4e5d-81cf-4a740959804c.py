# Generated from: 2484d19e-1d41-4e5d-81cf-4a740959804c.json
# Description: This process outlines the complex steps involved in establishing a sustainable urban vertical farm within a densely populated city. It includes site analysis, modular design, environmental control calibration, nutrient cycling optimization, and integration of AI-driven monitoring systems. The process ensures minimal resource consumption by recycling water and organic waste, supports continuous crop growth through automated lighting schedules, and involves community engagement for local produce distribution. Additionally, it addresses regulatory compliance, supply chain logistics, and scalability assessment to adapt to changing urban demands, making it an atypical yet highly realistic business model in modern agriculture.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Material_Sourcing = Transition(label='Material Sourcing')
Module_Assembly = Transition(label='Module Assembly')
System_Wiring = Transition(label='System Wiring')
Climate_Setup = Transition(label='Climate Setup')
Water_Recycling = Transition(label='Water Recycling')
Nutrient_Mix = Transition(label='Nutrient Mix')
Lighting_Schedule = Transition(label='Lighting Schedule')
Sensor_Install = Transition(label='Sensor Install')
AI_Integration = Transition(label='AI Integration')
Crop_Seeding = Transition(label='Crop Seeding')
Growth_Monitoring = Transition(label='Growth Monitoring')
Waste_Processing = Transition(label='Waste Processing')
Yield_Analysis = Transition(label='Yield Analysis')
Regulation_Check = Transition(label='Regulation Check')
Market_Setup = Transition(label='Market Setup')

# Construct partial orders reflecting dependencies and concurrency:

# Phase 1: site analysis and design, sequential
phase1 = StrictPartialOrder(nodes=[Site_Survey, Design_Layout])
phase1.order.add_edge(Site_Survey, Design_Layout)

# Phase 2: sourcing and assembly (can be partially concurrent but wiring depends on assembly)
source_and_assemble = StrictPartialOrder(
    nodes=[Material_Sourcing, Module_Assembly, System_Wiring]
)
source_and_assemble.order.add_edge(Material_Sourcing, Module_Assembly)
source_and_assemble.order.add_edge(Module_Assembly, System_Wiring)

# Phase 3: environment setup (parallel steps after wiring)
env_setup = StrictPartialOrder(
    nodes=[Climate_Setup, Water_Recycling, Nutrient_Mix, Lighting_Schedule]
)
# No order edges inside env_setup - all can be concurrent once wiring is done

# Phase 4: sensor install and AI integration, sequential (depends on env setup)
sensors_ai = StrictPartialOrder(nodes=[Sensor_Install, AI_Integration])
sensors_ai.order.add_edge(Sensor_Install, AI_Integration)

# Phase 5: crop seeding follows AI integration
# Loop for growth monitoring, waste processing, yield analysis
monitoring_loop_body = StrictPartialOrder(
    nodes=[Growth_Monitoring, Waste_Processing, Yield_Analysis]
)
# All three concurrent in monitoring loop body (no edges inside)

monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitoring_loop_body, Crop_Seeding])
# meaning: do Crop_Seeding, then loop monitor_body then Crop_Seeding again or exit

# Phase 6: regulatory and market setup (can run in parallel after monitoring)
reg_and_market = StrictPartialOrder(nodes=[Regulation_Check, Market_Setup])
# no order edges inside - concurrent

# Aggregate partial orders with overall control flow:

# After phase1 and before source_and_assemble
root_phase1_to_source = StrictPartialOrder(nodes=[phase1, source_and_assemble])
root_phase1_to_source.order.add_edge(phase1, source_and_assemble)

# After source_and_assemble and before env_setup
root_source_to_env = StrictPartialOrder(nodes=[root_phase1_to_source, env_setup])
root_source_to_env.order.add_edge(root_phase1_to_source, env_setup)

# After env_setup comes sensors_ai
root_env_to_ai = StrictPartialOrder(nodes=[root_source_to_env, sensors_ai])
root_env_to_ai.order.add_edge(root_source_to_env, sensors_ai)

# After sensors_ai comes monitoring_loop
root_ai_to_monitoring = StrictPartialOrder(nodes=[root_env_to_ai, monitoring_loop])
root_ai_to_monitoring.order.add_edge(root_env_to_ai, monitoring_loop)

# After monitoring_loop comes reg_and_market
root_monitoring_to_end = StrictPartialOrder(nodes=[root_ai_to_monitoring, reg_and_market])
root_monitoring_to_end.order.add_edge(root_ai_to_monitoring, reg_and_market)

# Assign root
root = root_monitoring_to_end