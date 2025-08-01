# Generated from: 09a867ef-7547-439b-a30b-ac627c857f08.json
# Description: This process outlines the establishment of a custom urban farming system tailored to specific client locations and environmental conditions. It involves initial site assessment, soil and pollution testing, modular farm design, sourcing of specialized seeds and nutrients, installation of IoT sensors for real-time monitoring, integration of renewable energy sources, staff training on sustainable practices, and ongoing performance optimization. The process ensures maximized yield with minimal environmental impact, adapting to urban constraints while promoting local food production and community engagement through workshops and digital platforms for farm management.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ss = Transition(label="Site Survey")
soil = Transition(label="Soil Testing")
pollution = Transition(label="Pollution Check")
design = Transition(label="Farm Design")
seed = Transition(label="Seed Sourcing")
nutrient = Transition(label="Nutrient Plan")
sensor = Transition(label="Sensor Setup")
energy = Transition(label="Energy Integration")
irrigation = Transition(label="Irrigation Install")
training = Transition(label="Staff Training")
reg_review = Transition(label="Regulation Review")
workshop = Transition(label="Community Workshop")

# Define the monitoring-analysis-upgrade loop
data_mon = Transition(label="Data Monitoring")
yield_an = Transition(label="Yield Analysis")
upgrade = Transition(label="System Upgrade")

# Sequence for one iteration: Data Monitoring -> Yield Analysis -> System Upgrade
po_body = StrictPartialOrder(nodes=[data_mon, yield_an, upgrade])
po_body.order.add_edge(data_mon, yield_an)
po_body.order.add_edge(yield_an, upgrade)

# Silent transition for loop branching
tau = SilentTransition()

# LOOP operator: after executing po_body once, either exit or do tau then po_body again
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[po_body, tau])

# Root partial order
root = StrictPartialOrder(nodes=[
    ss, soil, pollution, design,
    seed, nutrient, sensor, energy, irrigation,
    reg_review, training, workshop,
    monitor_loop
])

# Define ordering (dependencies)
root.order.add_edge(ss, soil)
root.order.add_edge(ss, pollution)

root.order.add_edge(soil, design)
root.order.add_edge(pollution, design)

root.order.add_edge(design, seed)
root.order.add_edge(design, nutrient)
root.order.add_edge(design, sensor)
root.order.add_edge(design, energy)
root.order.add_edge(design, irrigation)
root.order.add_edge(design, reg_review)

# System installation tasks must complete before staff training
root.order.add_edge(sensor, training)
root.order.add_edge(energy, training)
root.order.add_edge(irrigation, training)

# After sensor setup, begin the ongoing monitoring-analysis-upgrade loop
root.order.add_edge(sensor, monitor_loop)

# Community workshop follows staff training
root.order.add_edge(training, workshop)