# Generated from: e3d6750d-ea44-4466-b3b1-bb98fcc72eb2.json
# Description: This process outlines the intricate steps involved in establishing an urban vertical farm within a constrained city environment. It includes site evaluation for structural integrity, integrating IoT sensor networks for climate control, selecting crop varieties based on local demand analytics, deploying automated hydroponic systems, ensuring sustainable water recycling, managing energy consumption with renewable sources, coordinating multi-tier planting schedules, and implementing real-time yield monitoring. The process further involves compliance checks with municipal regulations, staff training on advanced farming technologies, and establishing supply chain logistics tailored for rapid urban distribution, ensuring the farm operates efficiently while maximizing crop output and minimizing environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey = Transition(label='Site Survey')
structural_check = Transition(label='Structural Check')
iot_setup = Transition(label='IoT Setup')
crop_selection = Transition(label='Crop Selection')
hydroponic_install = Transition(label='Hydroponic Install')
water_recycling = Transition(label='Water Recycling')
energy_audit = Transition(label='Energy Audit')
plant_scheduling = Transition(label='Plant Scheduling')
yield_monitoring = Transition(label='Yield Monitoring')
regulation_review = Transition(label='Regulation Review')
staff_training = Transition(label='Staff Training')
data_integration = Transition(label='Data Integration')
supply_setup = Transition(label='Supply Setup')
quality_audit = Transition(label='Quality Audit')
logistics_plan = Transition(label='Logistics Plan')

# Compliance and training partial order
compliance_and_training = StrictPartialOrder(
    nodes=[regulation_review, staff_training]
)
compliance_and_training.order.add_edge(regulation_review, staff_training)

# Supply chain partial order: data integration -> (quality audit -> supply setup) -> logistics plan
supply_chain = StrictPartialOrder(
    nodes=[data_integration, quality_audit, supply_setup, logistics_plan]
)
supply_chain.order.add_edge(data_integration, quality_audit)
supply_chain.order.add_edge(quality_audit, supply_setup)
supply_chain.order.add_edge(supply_setup, logistics_plan)

# Growing system partial order modeling the hydroponic farm setup:
# IoT Setup, Crop Selection, Hydroponic Install, Water Recycling, Energy Audit
growing_prep = StrictPartialOrder(
    nodes=[iot_setup, crop_selection, hydroponic_install, water_recycling, energy_audit]
)
# IoT Setup before Hydroponic Install and Water Recycling
growing_prep.order.add_edge(iot_setup, hydroponic_install)
growing_prep.order.add_edge(iot_setup, water_recycling)
# Crop Selection before Hydroponic Install
growing_prep.order.add_edge(crop_selection, hydroponic_install)
# Energy Audit after Hydroponic Install and Water Recycling
growing_prep.order.add_edge(hydroponic_install, energy_audit)
growing_prep.order.add_edge(water_recycling, energy_audit)

# Planting and monitoring partial order:
# plant scheduling before yield monitoring
plant_monitoring = StrictPartialOrder(
    nodes=[plant_scheduling, yield_monitoring]
)
plant_monitoring.order.add_edge(plant_scheduling, yield_monitoring)

# Site evaluation partial order: Site Survey -> Structural Check
site_evaluation = StrictPartialOrder(
    nodes=[site_survey, structural_check]
)
site_evaluation.order.add_edge(site_survey, structural_check)

# Compose the full partial order
# The process flows as:
# site evaluation -> growing prep -> plant and monitoring -> compliance_and_training and supply_chain (concurrent)

# First combine site evaluation and growing prep (site eval before growing prep)
phase1 = StrictPartialOrder(
    nodes=[site_evaluation, growing_prep]
)
phase1.order.add_edge(site_evaluation, growing_prep)

# Combine phase1 and plant_monitoring (phase1 before plant_monitoring)
phase2 = StrictPartialOrder(
    nodes=[phase1, plant_monitoring]
)
phase2.order.add_edge(phase1, plant_monitoring)

# compliance_and_training and supply_chain run concurrently after plant_monitoring
root = StrictPartialOrder(
    nodes=[phase2, compliance_and_training, supply_chain]
)
root.order.add_edge(phase2, compliance_and_training)
root.order.add_edge(phase2, supply_chain)