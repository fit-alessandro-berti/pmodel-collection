# Generated from: 1e60bd33-9be2-4cfc-ae96-eee08ee67c12.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farm within a densely populated city environment. It includes site evaluation for structural integrity, microclimate analysis, and energy efficiency assessments. The workflow covers modular system design, nutrient solution formulation, and sensor network integration for real-time monitoring. It also incorporates regulatory compliance checks, community engagement initiatives, and iterative crop optimization cycles. The process concludes with a phased operational launch, continuous quality assurance, and adaptive resource management to maximize yield while minimizing environmental impact in an urban setting.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
site_survey     = Transition(label='Site Survey')
structure_test  = Transition(label='Structure Test')
climate_study   = Transition(label='Climate Study')
energy_audit    = Transition(label='Energy Audit')
system_design   = Transition(label='System Design')
nutrient_mix    = Transition(label='Nutrient Mix')
sensor_setup    = Transition(label='Sensor Setup')
regulation_check= Transition(label='Regulation Check')
community_meet  = Transition(label='Community Meet')
crop_trial      = Transition(label='Crop Trial')
monitor_data    = Transition(label='Monitor Data')
yield_review    = Transition(label='Yield Review')
adjust_params   = Transition(label='Adjust Parameters')
resource_plan   = Transition(label='Resource Plan')
launch_phase    = Transition(label='Launch Phase')
quality_audit   = Transition(label='Quality Audit')

# Build the iterative crop‐optimization cycle: Crop Trial → Monitor Data → Yield Review
cycle = StrictPartialOrder(nodes=[crop_trial, monitor_data, yield_review])
cycle.order.add_edge(crop_trial, monitor_data)
cycle.order.add_edge(monitor_data, yield_review)

# The "redo" step: Adjust Parameters
redo = adjust_params

# LOOP operator: execute cycle, then either exit or do redo + cycle again
loop = OperatorPOWL(operator=Operator.LOOP, children=[cycle, redo])

# Assemble the full partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    structure_test,
    climate_study,
    energy_audit,
    system_design,
    nutrient_mix,
    sensor_setup,
    regulation_check,
    community_meet,
    loop,
    resource_plan,
    launch_phase,
    quality_audit
])

# 1. Site evaluation -> structural / climate / energy assessments
root.order.add_edge(site_survey, structure_test)
root.order.add_edge(site_survey, climate_study)
root.order.add_edge(site_survey, energy_audit)

# 2. After assessments, parallel design steps
for src in (structure_test, climate_study, energy_audit):
    root.order.add_edge(src, system_design)
    root.order.add_edge(src, nutrient_mix)
    root.order.add_edge(src, sensor_setup)

# 3. After design/nutrient/sensor → compliance and community
for src in (system_design, nutrient_mix, sensor_setup):
    root.order.add_edge(src, regulation_check)
    root.order.add_edge(src, community_meet)

# 4. Both regulation and community must finish before the loop
root.order.add_edge(regulation_check, loop)
root.order.add_edge(community_meet, loop)

# 5. After the iterative loop → resource planning → launch → quality audit
root.order.add_edge(loop, resource_plan)
root.order.add_edge(resource_plan, launch_phase)
root.order.add_edge(launch_phase, quality_audit)