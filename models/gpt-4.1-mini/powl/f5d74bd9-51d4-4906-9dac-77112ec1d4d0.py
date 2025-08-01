# Generated from: f5d74bd9-51d4-4906-9dac-77112ec1d4d0.json
# Description: This process outlines the complex and atypical steps involved in establishing an urban vertical farm within a repurposed industrial building. It includes site analysis, environmental impact assessment, structural modifications, hydroponic system installation, crop selection, nutrient management, pest control, automated monitoring integration, staff training, regulatory compliance checks, product packaging design, distribution channel setup, community engagement, and ongoing sustainability evaluations. The goal is to create a highly efficient, scalable, and sustainable urban farm that maximizes yield while minimizing resource consumption and environmental footprint in a dense city environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_review = Transition(label='Site Review')
impact_study = Transition(label='Impact Study')
design_plan = Transition(label='Design Plan')
structure_mod = Transition(label='Structure Mod')
hydroponics_setup = Transition(label='Hydroponics Setup')
crop_select = Transition(label='Crop Select')
nutrient_mix = Transition(label='Nutrient Mix')
pest_control = Transition(label='Pest Control')
sensor_install = Transition(label='Sensor Install')
staff_train = Transition(label='Staff Train')
compliance_audit = Transition(label='Compliance Audit')
packaging_dev = Transition(label='Packaging Dev')
logistics_plan = Transition(label='Logistics Plan')
community_engage = Transition(label='Community Engage')
sustainability_check = Transition(label='Sustainability Check')

# Construct the main partial order according to logical sequencing:
# Site Review -> Impact Study -> Design Plan
# Design Plan -> Structure Mod and Crop Select (can be concurrent after Design Plan)
# Structure Mod -> Hydroponics Setup
# Crop Select -> Nutrient Mix -> Pest Control (sequential)
# Hydroponics Setup -> Sensor Install
# Pest Control -> Staff Train
# Sensor Install and Staff Train -> Compliance Audit (concurrent join)
# Compliance Audit -> Packaging Dev
# Packaging Dev -> Logistics Plan
# Logistics Plan -> Community Engage
# Community Engage -> Sustainability Check

# Define nodes of the POWL model
nodes = [
    site_review, impact_study, design_plan,
    structure_mod, hydroponics_setup,
    crop_select, nutrient_mix, pest_control,
    sensor_install, staff_train, compliance_audit,
    packaging_dev, logistics_plan,
    community_engage, sustainability_check,
]

root = StrictPartialOrder(nodes=nodes)

# Add edges for partial order dependencies
root.order.add_edge(site_review, impact_study)
root.order.add_edge(impact_study, design_plan)

# From Design Plan, Structure Mod and Crop Select are parallel (no order between them),
# but both depend on Design Plan
root.order.add_edge(design_plan, structure_mod)
root.order.add_edge(design_plan, crop_select)

# Structure Mod -> Hydroponics Setup
root.order.add_edge(structure_mod, hydroponics_setup)

# Crop Select -> Nutrient Mix -> Pest Control (sequential)
root.order.add_edge(crop_select, nutrient_mix)
root.order.add_edge(nutrient_mix, pest_control)

# Hydroponics Setup -> Sensor Install
root.order.add_edge(hydroponics_setup, sensor_install)

# Pest Control -> Staff Train
root.order.add_edge(pest_control, staff_train)

# Sensor Install and Staff Train both precede Compliance Audit
root.order.add_edge(sensor_install, compliance_audit)
root.order.add_edge(staff_train, compliance_audit)

# Compliance Audit -> Packaging Dev -> Logistics Plan -> Community Engage -> Sustainability Check
root.order.add_edge(compliance_audit, packaging_dev)
root.order.add_edge(packaging_dev, logistics_plan)
root.order.add_edge(logistics_plan, community_engage)
root.order.add_edge(community_engage, sustainability_check)