# Generated from: bafb7c0a-eae3-49a7-a210-235d7d22f2f1.json
# Description: This process outlines the complex and atypical steps involved in establishing an urban vertical farm within a densely populated city environment. It starts with site analysis and zoning compliance, followed by microclimate assessment and modular system design. Procurement of specialized hydroponic equipment and nutrient solutions is critical, alongside integration of IoT sensors for real-time monitoring. Installation requires coordination with utility providers for optimized energy and water usage. Post-installation, seed selection and planting are carefully managed to match urban growth cycles. Continuous environmental adjustments, pest management using biological controls, and automated harvesting complete the cycle. Finally, produce packaging and distribution focus on minimizing carbon footprint while ensuring freshness, targeting local markets and restaurants. This process demands interdisciplinary collaboration between agronomists, engineers, urban planners, and supply chain experts to balance sustainability, efficiency, and profitability in a confined urban space.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define the activities
site_analysis = Transition(label='Site Analysis')
zoning_check = Transition(label='Zoning Check')
microclimate_study = Transition(label='Microclimate Study')
system_design = Transition(label='System Design')
equipment_order = Transition(label='Equipment Order')
nutrient_prep = Transition(label='Nutrient Prep')
sensor_setup = Transition(label='Sensor Setup')
utility_coordination = Transition(label='Utility Coordination')
installation_phase = Transition(label='Installation Phase')
seed_selection = Transition(label='Seed Selection')
planting_stage = Transition(label='Planting Stage')
environmental_tune = Transition(label='Environmental Tune')
pest_control = Transition(label='Pest Control')
automated_harvest = Transition(label='Automated Harvest')
packaging_ops = Transition(label='Packaging Ops')
distribution_plan = Transition(label='Distribution Plan')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    site_analysis, zoning_check,
    microclimate_study, system_design,
    equipment_order, nutrient_prep, sensor_setup,
    utility_coordination, installation_phase,
    seed_selection, planting_stage,
    environmental_tune, pest_control,
    automated_harvest, packaging_ops, distribution_plan
])

# Define the control‐flow dependencies
root.order.add_edge(site_analysis, zoning_check)
root.order.add_edge(zoning_check, microclimate_study)
root.order.add_edge(zoning_check, system_design)

root.order.add_edge(microclimate_study, equipment_order)
root.order.add_edge(microclimate_study, nutrient_prep)
root.order.add_edge(microclimate_study, sensor_setup)
root.order.add_edge(system_design, equipment_order)
root.order.add_edge(system_design, nutrient_prep)
root.order.add_edge(system_design, sensor_setup)

root.order.add_edge(equipment_order, utility_coordination)
root.order.add_edge(nutrient_prep, utility_coordination)
root.order.add_edge(sensor_setup, utility_coordination)

root.order.add_edge(utility_coordination, installation_phase)
root.order.add_edge(installation_phase, seed_selection)
root.order.add_edge(seed_selection, planting_stage)

root.order.add_edge(planting_stage, environmental_tune)
root.order.add_edge(planting_stage, pest_control)

root.order.add_edge(environmental_tune, automated_harvest)
root.order.add_edge(pest_control, automated_harvest)

root.order.add_edge(automated_harvest, packaging_ops)
root.order.add_edge(packaging_ops, distribution_plan)