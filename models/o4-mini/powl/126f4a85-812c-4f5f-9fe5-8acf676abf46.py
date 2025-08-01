# Generated from: 126f4a85-812c-4f5f-9fe5-8acf676abf46.json
# Description: This process outlines the establishment of an urban rooftop farm, integrating architectural assessments, environmental impact studies, and community engagement. It involves selecting suitable crops, designing modular planting systems, installing irrigation and lighting technologies, and coordinating with local authorities for compliance. The process also includes soil preparation using recycled materials, pest management through natural predators, and setting up data collection for crop monitoring. Post-installation, it emphasizes training staff, marketing the farm produce to local markets, and evaluating sustainability metrics to ensure long-term viability and community benefits.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
site_survey        = Transition(label='Site Survey')
permit_review      = Transition(label='Permit Review')
crop_selection     = Transition(label='Crop Selection')
system_design      = Transition(label='System Design')
material_sourcing  = Transition(label='Material Sourcing')
soil_prep          = Transition(label='Soil Prep')
irrigation_setup   = Transition(label='Irrigation Setup')
lighting_install   = Transition(label='Lighting Install')
pest_control       = Transition(label='Pest Control')
monitoring_setup   = Transition(label='Monitoring Setup')
staff_training     = Transition(label='Staff Training')
community_outreach = Transition(label='Community Outreach')
market_analysis    = Transition(label='Market Analysis')
harvest_planning   = Transition(label='Harvest Planning')
sustainability_audit = Transition(label='Sustainability Audit')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    site_survey, permit_review,
    crop_selection, system_design,
    material_sourcing, soil_prep,
    irrigation_setup, lighting_install,
    pest_control, monitoring_setup,
    staff_training, community_outreach,
    market_analysis, harvest_planning,
    sustainability_audit
])

# Initial phase: survey and permits
root.order.add_edge(site_survey, crop_selection)
root.order.add_edge(permit_review, system_design)
root.order.add_edge(crop_selection, system_design)

# Design and material sourcing
root.order.add_edge(system_design, material_sourcing)
root.order.add_edge(material_sourcing, soil_prep)

# Installation: soil prep → irrigation & lighting
root.order.add_edge(soil_prep, irrigation_setup)
root.order.add_edge(soil_prep, lighting_install)

# Operational setup: pest control, monitoring, training, outreach
for predecessor in (irrigation_setup, lighting_install):
    root.order.add_edge(predecessor, pest_control)
    root.order.add_edge(predecessor, monitoring_setup)
    root.order.add_edge(predecessor, staff_training)
    root.order.add_edge(predecessor, community_outreach)

# Marketing & planning
root.order.add_edge(community_outreach, market_analysis)
root.order.add_edge(crop_selection, harvest_planning)
for predecessor in (irrigation_setup, lighting_install, market_analysis):
    root.order.add_edge(predecessor, harvest_planning)

# Final sustainability audit
root.order.add_edge(harvest_planning, sustainability_audit)
root.order.add_edge(monitoring_setup, sustainability_audit)