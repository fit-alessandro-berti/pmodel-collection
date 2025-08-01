# Generated from: 4bd82eb5-49a2-4073-b827-5f1d42be5ccd.json
# Description: This process outlines the comprehensive steps involved in establishing a sustainable urban rooftop farm on a commercial building. It includes site assessment, structural analysis, soil preparation using hydroponic techniques, and installation of automated irrigation systems. The process also covers regulatory compliance checks, sourcing of organic seeds, pest control planning, and community engagement for local produce distribution. Continuous monitoring of crop health through IoT sensors and data analytics ensures optimal growth conditions while minimizing resource use. Finally, the process integrates seasonal crop rotation planning and waste recycling protocols to maintain long-term farm productivity and environmental sustainability.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities
site_survey      = Transition(label="Site Survey")
structure_check  = Transition(label="Structure Check")
soil_prep        = Transition(label="Soil Prep")
hydroponic_setup = Transition(label="Hydroponic Setup")
irrigation_install = Transition(label="Irrigation Install")

compliance_review = Transition(label="Compliance Review")
seed_sourcing     = Transition(label="Seed Sourcing")
pest_plan         = Transition(label="Pest Plan")
community_meet    = Transition(label="Community Meet")

sensor_deploy = Transition(label="Sensor Deploy")
data_monitor  = Transition(label="Data Monitor")

harvest_plan   = Transition(label="Harvest Plan")
distribution   = Transition(label="Distribution")
crop_rotation  = Transition(label="Crop Rotation")
waste_manage   = Transition(label="Waste Manage")

# Define a loop for continuous monitoring (execute Data Monitor repeatedly)
skip = SilentTransition()
loop_monitor = OperatorPOWL(operator=Operator.LOOP, children=[data_monitor, skip])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey, structure_check, soil_prep, hydroponic_setup, irrigation_install,
    compliance_review, seed_sourcing, pest_plan, community_meet,
    sensor_deploy, loop_monitor,
    harvest_plan, distribution,
    crop_rotation, waste_manage
])

# Phase 1: site assessment and installation
root.order.add_edge(site_survey, structure_check)
root.order.add_edge(structure_check, soil_prep)
root.order.add_edge(soil_prep, hydroponic_setup)
root.order.add_edge(hydroponic_setup, irrigation_install)

# Phase 2: compliance, sourcing, planning, engagement (all after irrigation install)
root.order.add_edge(irrigation_install, compliance_review)
root.order.add_edge(irrigation_install, seed_sourcing)
root.order.add_edge(irrigation_install, pest_plan)
root.order.add_edge(irrigation_install, community_meet)

# Phase 3: once all four are done, deploy sensors
for prev in [compliance_review, seed_sourcing, pest_plan, community_meet]:
    root.order.add_edge(prev, sensor_deploy)

# Phase 4: continuous monitoring loop
root.order.add_edge(sensor_deploy, loop_monitor)

# Phase 5: harvesting and distribution
root.order.add_edge(loop_monitor, harvest_plan)
root.order.add_edge(harvest_plan, distribution)

# Phase 6: seasonal rotation and waste recycling
root.order.add_edge(distribution, crop_rotation)
root.order.add_edge(distribution, waste_manage)