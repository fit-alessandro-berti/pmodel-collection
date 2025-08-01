# Generated from: 77fc7bc0-3b16-4ca9-ab27-6e54a76bf7b1.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farm within constrained city environments. It includes site evaluation, modular system design, environmental control calibration, nutrient flow optimization, and continuous monitoring. The process integrates sustainable energy sourcing, waste recycling, and crop rotation scheduling to maximize yield while minimizing resource consumption. Stakeholder coordination, regulatory compliance, and technology integration are critical to ensure operational efficiency and scalability in dense urban settings.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define basic activities
survey = Transition(label='Site Survey')
layout = Transition(label='Design Layout')
fabricate = Transition(label='System Fabricate')
energy = Transition(label='Energy Setup')
sensors = Transition(label='Install Sensors')
calibrate = Transition(label='Calibrate Controls')
nutrient = Transition(label='Nutrient Mix')
planting = Transition(label='Seed Planting')
monitor = Transition(label='Growth Monitor')
inspect = Transition(label='Pest Inspect')
tech = Transition(label='Tech Update')
harvest = Transition(label='Harvest Plan')
waste = Transition(label='Waste Recycle')
analyze = Transition(label='Data Analyze')
compliance = Transition(label='Compliance Check')
stakeholder = Transition(label='Stakeholder Meet')
crop = Transition(label='Crop Rotate')

# Silent transition for loop control
skip = SilentTransition()

# Define the body of the monitoring loop: monitor -> inspect -> tech update
body = StrictPartialOrder(nodes=[monitor, inspect, tech])
body.order.add_edge(monitor, inspect)
body.order.add_edge(inspect, tech)

# Loop: do (monitor->inspect->tech_update) repeatedly until exit
loop_monitor = OperatorPOWL(operator=Operator.LOOP, children=[body, skip])

# Build the top-level partial order
root = StrictPartialOrder(nodes=[
    survey, stakeholder, compliance, layout, fabricate,
    energy, sensors, calibrate, nutrient, planting,
    loop_monitor, harvest, waste, analyze, crop
])

# Stakeholder coordination and compliance before design
root.order.add_edge(survey, stakeholder)
root.order.add_edge(survey, compliance)
root.order.add_edge(stakeholder, layout)
root.order.add_edge(compliance, layout)

# Site survey -> design -> fabrication
root.order.add_edge(survey, layout)
root.order.add_edge(layout, fabricate)

# Fabrication -> energy setup & sensor installation (concurrent)
root.order.add_edge(fabricate, energy)
root.order.add_edge(fabricate, sensors)

# Energy & sensors -> calibration
root.order.add_edge(energy, calibrate)
root.order.add_edge(sensors, calibrate)

# Calibration -> nutrient mix -> planting
root.order.add_edge(calibrate, nutrient)
root.order.add_edge(nutrient, planting)

# Planting -> growth/inspection loop
root.order.add_edge(planting, loop_monitor)

# After loop exit -> harvest planning
root.order.add_edge(loop_monitor, harvest)

# Harvest -> waste recycling, data analysis, crop rotation (concurrent)
root.order.add_edge(harvest, waste)
root.order.add_edge(harvest, analyze)
root.order.add_edge(harvest, crop)