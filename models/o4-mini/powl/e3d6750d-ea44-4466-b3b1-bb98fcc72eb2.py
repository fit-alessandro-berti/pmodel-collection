# Generated from: e3d6750d-ea44-4466-b3b1-bb98fcc72eb2.json
# Description: This process outlines the intricate steps involved in establishing an urban vertical farm within a constrained city environment. It includes site evaluation for structural integrity, integrating IoT sensor networks for climate control, selecting crop varieties based on local demand analytics, deploying automated hydroponic systems, ensuring sustainable water recycling, managing energy consumption with renewable sources, coordinating multi-tier planting schedules, and implementing real-time yield monitoring. The process further involves compliance checks with municipal regulations, staff training on advanced farming technologies, and establishing supply chain logistics tailored for rapid urban distribution, ensuring the farm operates efficiently while maximizing crop output and minimizing environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
site_survey       = Transition(label='Site Survey')
structural_check  = Transition(label='Structural Check')
iot_setup         = Transition(label='IoT Setup')
data_integration  = Transition(label='Data Integration')
crop_selection    = Transition(label='Crop Selection')
hydroponic_install= Transition(label='Hydroponic Install')
water_recycling   = Transition(label='Water Recycling')
energy_audit      = Transition(label='Energy Audit')
plant_scheduling  = Transition(label='Plant Scheduling')
regulation_review = Transition(label='Regulation Review')
staff_training    = Transition(label='Staff Training')
supply_setup      = Transition(label='Supply Setup')
logistics_plan    = Transition(label='Logistics Plan')
yield_monitoring  = Transition(label='Yield Monitoring')
quality_audit     = Transition(label='Quality Audit')

# Build the partial‐order model
root = StrictPartialOrder(nodes=[
    site_survey, structural_check, iot_setup, data_integration,
    crop_selection, hydroponic_install, water_recycling, energy_audit,
    plant_scheduling, regulation_review, staff_training,
    supply_setup, logistics_plan, yield_monitoring, quality_audit
])

# Define precedence constraints
root.order.add_edge(site_survey,       structural_check)
root.order.add_edge(structural_check,  iot_setup)
root.order.add_edge(iot_setup,         data_integration)
root.order.add_edge(data_integration,  crop_selection)
root.order.add_edge(crop_selection,    hydroponic_install)

# Parallel water & energy checks before scheduling
root.order.add_edge(hydroponic_install, water_recycling)
root.order.add_edge(hydroponic_install, energy_audit)
root.order.add_edge(water_recycling,    plant_scheduling)
root.order.add_edge(energy_audit,       plant_scheduling)

# Regulatory & training before supply chain
root.order.add_edge(plant_scheduling,   regulation_review)
root.order.add_edge(regulation_review,  staff_training)
root.order.add_edge(plant_scheduling,   staff_training)

# Supply setup → logistics
root.order.add_edge(staff_training,     supply_setup)
root.order.add_edge(supply_setup,       logistics_plan)

# Final monitoring and audit
root.order.add_edge(plant_scheduling,   yield_monitoring)
root.order.add_edge(yield_monitoring,   quality_audit)
root.order.add_edge(logistics_plan,     quality_audit)