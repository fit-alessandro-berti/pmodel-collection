# Generated from: 853ec268-38ac-4cd2-9a41-6d8e1093e7a1.json
# Description: This process outlines the comprehensive steps involved in establishing an urban rooftop farm in a densely populated city environment. It begins with site analysis to evaluate structural integrity and sunlight exposure, followed by soil and water quality testing. Then, permits and zoning approvals are secured from local authorities. Afterward, the design phase includes selecting appropriate plant varieties adapted to urban climates and creating an efficient irrigation system. Installation involves assembling modular planters, setting up rainwater harvesting, and integrating renewable energy sources like solar panels for sustainable operations. The process continues with training staff on urban farming techniques, implementing pest management strategies suitable for rooftop ecosystems, and establishing a supply chain for distributing fresh produce to local markets. Finally, ongoing monitoring and adjustments ensure optimal crop yields while maintaining environmental compliance and community engagement.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all transitions
site_analysis = Transition(label='Site Analysis')
structure_check = Transition(label='Structure Check')
sunlight_mapping = Transition(label='Sunlight Mapping')
soil_testing = Transition(label='Soil Testing')
water_testing = Transition(label='Water Testing')
permit_filing = Transition(label='Permit Filing')
zoning_approval = Transition(label='Zoning Approval')
crop_selection = Transition(label='Crop Selection')
irrigation_setup = Transition(label='Irrigation Setup')
planter_assembly = Transition(label='Planter Assembly')
rainwater_install = Transition(label='Rainwater Install')
solar_paneling = Transition(label='Solar Paneling')
staff_training = Transition(label='Staff Training')
pest_control = Transition(label='Pest Control')
supply_chain = Transition(label='Supply Chain')
yield_monitoring = Transition(label='Yield Monitoring')
compliance_review = Transition(label='Compliance Review')
community_outreach = Transition(label='Community Outreach')

# Build the partial‐order graph
root = StrictPartialOrder(nodes=[
    site_analysis, structure_check, sunlight_mapping,
    soil_testing, water_testing,
    permit_filing, zoning_approval,
    crop_selection, irrigation_setup,
    planter_assembly, rainwater_install, solar_paneling,
    staff_training, pest_control, supply_chain,
    yield_monitoring, compliance_review, community_outreach
])

# Site analysis phase
root.order.add_edge(site_analysis, structure_check)
root.order.add_edge(site_analysis, sunlight_mapping)

# Testing phase
for src in [structure_check, sunlight_mapping]:
    for tgt in [soil_testing, water_testing]:
        root.order.add_edge(src, tgt)

# Approval phase
root.order.add_edge(soil_testing, permit_filing)
root.order.add_edge(water_testing, permit_filing)
root.order.add_edge(permit_filing, zoning_approval)

# Design phase
for tgt in [crop_selection, irrigation_setup]:
    root.order.add_edge(zoning_approval, tgt)

# Installation phase
for src in [crop_selection, irrigation_setup]:
    for tgt in [planter_assembly, rainwater_install, solar_paneling]:
        root.order.add_edge(src, tgt)

# Operations training phase
for src in [planter_assembly, rainwater_install, solar_paneling]:
    for tgt in [staff_training, pest_control, supply_chain]:
        root.order.add_edge(src, tgt)

# Monitoring & engagement phase
for src in [staff_training, pest_control, supply_chain]:
    for tgt in [yield_monitoring, compliance_review, community_outreach]:
        root.order.add_edge(src, tgt)