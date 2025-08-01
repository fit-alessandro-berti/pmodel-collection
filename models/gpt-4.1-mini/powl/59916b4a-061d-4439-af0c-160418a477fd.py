# Generated from: 59916b4a-061d-4439-af0c-160418a477fd.json
# Description: This process outlines the establishment of a vertical urban farm in a densely populated city environment. It integrates unconventional site selection, modular hydroponic system design, and multi-tiered crop scheduling. The process requires coordination between environmental impact analysis, energy optimization, and community engagement to ensure sustainable urban agriculture. Activities include securing rooftop leases, customizing nutrient delivery, implementing AI-driven climate control, and managing crop rotation cycles. The process culminates in local distribution partnerships and continuous feedback integration to enhance yield and reduce waste in an atypical but scalable urban farming operation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
Site_Survey = Transition(label='Site Survey')
Lease_Negotiation = Transition(label='Lease Negotiation')
Design_Layout = Transition(label='Design Layout')
System_Build = Transition(label='System Build')
Nutrient_Prep = Transition(label='Nutrient Prep')
Seed_Selection = Transition(label='Seed Selection')
Planting_Cycle = Transition(label='Planting Cycle')
Climate_Setup = Transition(label='Climate Setup')
AI_Calibration = Transition(label='AI Calibration')
Growth_Monitoring = Transition(label='Growth Monitoring')
Pest_Control = Transition(label='Pest Control')
Harvest_Plan = Transition(label='Harvest Plan')
Local_Partner = Transition(label='Local Partner')
Waste_Recycle = Transition(label='Waste Recycle')
Feedback_Loop = Transition(label='Feedback Loop')
Energy_Audit = Transition(label='Energy Audit')
Community_Meet = Transition(label='Community Meet')

# Construct partial orders to represent concurrency and dependencies

# Site selection phase: Site Survey -> Lease Negotiation (sequential)
site_selection = StrictPartialOrder(nodes=[Site_Survey, Lease_Negotiation])
site_selection.order.add_edge(Site_Survey, Lease_Negotiation)

# Design and Build phase: Design Layout -> System Build (sequential)
design_build = StrictPartialOrder(nodes=[Design_Layout, System_Build])
design_build.order.add_edge(Design_Layout, System_Build)

# Nutrient preparation and seed selection can be done concurrently before planting cycle
nutrient_and_seed = StrictPartialOrder(nodes=[Nutrient_Prep, Seed_Selection])

# Planting cycle preparation phase: Nutrient Prep and Seed Selection -> Planting Cycle
planting_prep = StrictPartialOrder(nodes=[nutrient_and_seed, Planting_Cycle])
planting_prep.order.add_edge(nutrient_and_seed, Planting_Cycle)

# Climate control setup: Climate Setup -> AI Calibration (sequential)
climate_control = StrictPartialOrder(nodes=[Climate_Setup, AI_Calibration])
climate_control.order.add_edge(Climate_Setup, AI_Calibration)

# Crop monitoring and management loop:
# loop on (Growth Monitoring -> Pest Control -> Harvest Plan), repeated, with exit leading to next phase
crop_management_loop_body = StrictPartialOrder(nodes=[Growth_Monitoring, Pest_Control, Harvest_Plan])
crop_management_loop_body.order.add_edge(Growth_Monitoring, Pest_Control)
crop_management_loop_body.order.add_edge(Pest_Control, Harvest_Plan)

crop_management_loop = OperatorPOWL(operator=Operator.LOOP, children=[crop_management_loop_body, SilentTransition()])

# After crop management: Local partnerships, Waste recycling, Feedback integration can happen concurrently
post_harvest = StrictPartialOrder(nodes=[Local_Partner, Waste_Recycle, Feedback_Loop])

# Sustainability efforts: Energy Audit and Community Meet can happen concurrently
sustainability = StrictPartialOrder(nodes=[Energy_Audit, Community_Meet])

# High level ordering relationships

# site_selection -> design_build -> planting_prep -> climate_control -> crop_management_loop -> post_harvest -> sustainability
root = StrictPartialOrder(nodes=[site_selection, design_build, planting_prep, climate_control, crop_management_loop, post_harvest, sustainability])
root.order.add_edge(site_selection, design_build)
root.order.add_edge(design_build, planting_prep)
root.order.add_edge(planting_prep, climate_control)
root.order.add_edge(climate_control, crop_management_loop)
root.order.add_edge(crop_management_loop, post_harvest)
root.order.add_edge(post_harvest, sustainability)