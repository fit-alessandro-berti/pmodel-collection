# Generated from: 0335df5a-1ce0-4a77-b36a-8f7b9b308a07.json
# Description: This process outlines the complex steps involved in establishing a sustainable urban rooftop farm on a commercial building. It involves assessing structural integrity, securing permits, designing the layout for optimal sunlight and water usage, installing irrigation and hydroponic systems, sourcing organic seeds, training local staff, implementing pest control measures, monitoring crop growth using IoT sensors, coordinating harvest logistics, and marketing fresh produce directly to urban consumers. The process also includes waste recycling, seasonal crop rotation planning, integrating renewable energy sources, and continuous community engagement to promote urban agriculture awareness and education.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey     = Transition(label="Site Survey")
structure_check = Transition(label="Structure Check")
permit_filing   = Transition(label="Permit Filing")
layout_design   = Transition(label="Layout Design")
water_setup     = Transition(label="Water Setup")
energy_setup    = Transition(label="Energy Setup")
seed_sourcing   = Transition(label="Seed Sourcing")
staff_training  = Transition(label="Staff Training")
pest_control    = Transition(label="Pest Control")
iot_monitoring  = Transition(label="IoT Monitoring")
crop_harvest    = Transition(label="Crop Harvest")
market_plan     = Transition(label="Market Plan")

waste_recycling = Transition(label="Waste Recycling")
crop_rotation   = Transition(label="Crop Rotation")
community_engage= Transition(label="Community Engage")

# Silent transition for loop initialization
skip = SilentTransition()

# Loops for recurring tasks
waste_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[skip, waste_recycling]
)

rotation_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[skip, crop_rotation]
)

community_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[skip, community_engage]
)

# Build the top‐level partial order
root = StrictPartialOrder(
    nodes=[
        site_survey,
        structure_check,
        permit_filing,
        layout_design,
        water_setup,
        energy_setup,
        seed_sourcing,
        staff_training,
        pest_control,
        iot_monitoring,
        crop_harvest,
        market_plan,
        waste_loop,
        rotation_loop,
        community_loop
    ]
)

# Sequential control‐flow edges
edges = [
    (site_survey, structure_check),
    (structure_check, permit_filing),
    (permit_filing, layout_design),
    (layout_design, water_setup),
    (water_setup, energy_setup),
    (energy_setup, seed_sourcing),
    (seed_sourcing, staff_training),
    (staff_training, pest_control),
    (pest_control, iot_monitoring),
    (iot_monitoring, crop_harvest),
    (crop_harvest, market_plan)
]

for src, tgt in edges:
    root.order.add_edge(src, tgt)

# Integrate loops
# After each harvest you may recycle waste and plan the next rotation before marketing
root.order.add_edge(crop_harvest, waste_loop)
root.order.add_edge(waste_loop, rotation_loop)
root.order.add_edge(rotation_loop, market_plan)

# Community engagement runs continuously after the initial survey
root.order.add_edge(site_survey, community_loop)