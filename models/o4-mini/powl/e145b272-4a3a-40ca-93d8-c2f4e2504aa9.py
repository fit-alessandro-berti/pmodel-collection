# Generated from: e145b272-4a3a-40ca-93d8-c2f4e2504aa9.json
# Description: This process outlines the establishment of a fully automated urban vertical farm within a repurposed industrial building. It involves site assessment, modular system design, climate control integration, nutrient cycling optimization, and IoT sensor deployment. The operation includes real-time monitoring, AI-driven crop scheduling, waste recycling, and energy efficiency audits. Coordination with local regulators ensures compliance with zoning and environmental standards. The process culminates in continuous yield analysis and adaptive system upgrades to maximize sustainable food production in constrained urban spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
t_site = Transition(label='Site Survey')
t_design = Transition(label='System Design')
t_permit = Transition(label='Permit Filing')
t_build = Transition(label='Modular Build')
t_sensor = Transition(label='Sensor Install')
t_climate = Transition(label='Climate Setup')
t_nutrient = Transition(label='Nutrient Mix')
t_waste = Transition(label='Waste Setup')
t_iot = Transition(label='IoT Deploy')
t_ai = Transition(label='AI Scheduling')
t_audit = Transition(label='Energy Audit')
t_compliance = Transition(label='Compliance Check')
t_plant = Transition(label='Crop Planting')
t_yield = Transition(label='Yield Monitor')
t_data = Transition(label='Data Analysis')
t_upgrade = Transition(label='System Upgrade')

# Define the loop body (monitoring & analysis cycle)
cycle_body = StrictPartialOrder(nodes=[t_yield, t_data, t_ai, t_audit, t_compliance])
cycle_body.order.add_edge(t_yield, t_data)
cycle_body.order.add_edge(t_yield, t_ai)
cycle_body.order.add_edge(t_yield, t_audit)
cycle_body.order.add_edge(t_yield, t_compliance)

# Loop: do cycle_body, then optionally do an upgrade and repeat
loop_cycle = OperatorPOWL(operator=Operator.LOOP, children=[cycle_body, t_upgrade])

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    t_site, t_design, t_permit, t_build,
    t_sensor, t_climate, t_nutrient, t_waste,
    t_iot, t_plant, loop_cycle
])

# Site survey leads to design and permit in parallel
root.order.add_edge(t_site, t_design)
root.order.add_edge(t_site, t_permit)
# Both design and permit must finish before modular build
root.order.add_edge(t_design, t_build)
root.order.add_edge(t_permit, t_build)
# After build, integrate subsystems in parallel
root.order.add_edge(t_build, t_sensor)
root.order.add_edge(t_build, t_climate)
root.order.add_edge(t_build, t_nutrient)
root.order.add_edge(t_build, t_waste)
# Once all subsystems are in, deploy IoT
root.order.add_edge(t_sensor, t_iot)
root.order.add_edge(t_climate, t_iot)
root.order.add_edge(t_nutrient, t_iot)
root.order.add_edge(t_waste, t_iot)
# After deployment, plant the first crop
root.order.add_edge(t_iot, t_plant)
# Then enter the continuous monitoring‐analysis‐upgrade loop
root.order.add_edge(t_plant, loop_cycle)