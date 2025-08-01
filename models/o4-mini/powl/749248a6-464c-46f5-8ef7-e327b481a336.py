# Generated from: 749248a6-464c-46f5-8ef7-e327b481a336.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farm within a repurposed industrial building. It encompasses site assessment, environmental control system design, selecting crop varieties optimized for vertical growth, and integrating IoT sensors for continuous monitoring. The process also involves securing permits, designing hydroponic and aeroponic systems, training staff on sustainable farming techniques, and establishing a supply chain for distribution. Emphasis is placed on energy efficiency, waste recycling, and community engagement to ensure both economic viability and social impact in densely populated urban areas.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all transitions for the activities
site_survey      = Transition(label="Site Survey")
permit_apply     = Transition(label="Permit Apply")
crop_select      = Transition(label="Crop Select")
system_design    = Transition(label="System Design")
energy_audit     = Transition(label="Energy Audit")
waste_plan       = Transition(label="Waste Plan")
hydro_setup      = Transition(label="Hydroponic Setup")
aero_install     = Transition(label="Aeroponic Install")
sensor_deploy    = Transition(label="Sensor Deploy")
irrigation_test  = Transition(label="Irrigation Test")
climate_control  = Transition(label="Climate Control")
quality_check    = Transition(label="Quality Check")
staff_train      = Transition(label="Staff Train")
community_meet   = Transition(label="Community Meet")
supply_chain     = Transition(label="Supply Chain")
launch_event     = Transition(label="Launch Event")

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey, permit_apply, crop_select, system_design,
    energy_audit, waste_plan,
    hydro_setup, aero_install, sensor_deploy,
    irrigation_test, climate_control, quality_check,
    staff_train, community_meet, supply_chain,
    launch_event
])

# Phase 1: Site Survey leads to permitting and environmental prep
root.order.add_edge(site_survey, permit_apply)
root.order.add_edge(site_survey, energy_audit)
root.order.add_edge(site_survey, waste_plan)

# Phase 2: Permit → Crop Selection → System Design
root.order.add_edge(permit_apply, crop_select)
root.order.add_edge(crop_select, system_design)

# Phase 3: System Design branches to hydroponic, aeroponic, and sensors
root.order.add_edge(system_design, hydro_setup)
root.order.add_edge(system_design, aero_install)
root.order.add_edge(system_design, sensor_deploy)

# Phase 4: Testing after setups
root.order.add_edge(hydro_setup, irrigation_test)
root.order.add_edge(aero_install, climate_control)

# Quality Check depends on all tests and sensor deployment
root.order.add_edge(irrigation_test, quality_check)
root.order.add_edge(climate_control, quality_check)
root.order.add_edge(sensor_deploy, quality_check)

# Phase 5: Post‐check activities in parallel
root.order.add_edge(quality_check, staff_train)
root.order.add_edge(quality_check, community_meet)
root.order.add_edge(quality_check, supply_chain)

# Final launch after all preparations
root.order.add_edge(staff_train, launch_event)
root.order.add_edge(community_meet, launch_event)
root.order.add_edge(supply_chain, launch_event)