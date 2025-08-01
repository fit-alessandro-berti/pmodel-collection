# Generated from: 1f75a14b-3cf2-42f6-880c-3223d5ca77b6.json
# Description: This process outlines the comprehensive steps required to establish a fully operational urban vertical farm within a repurposed industrial building. It involves site assessment, modular system design, advanced hydroponic installation, climate control calibration, automated nutrient delivery setup, energy optimization, crop planning, integrated pest management, and digital monitoring system integration. Additionally, it incorporates workforce training, regulatory compliance checks, pilot harvesting, data analysis, continuous improvement loops, and community engagement initiatives to ensure sustainability, productivity, and scalability in an unconventional agricultural environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

site = Transition(label='Site Assess')
design = Transition(label='Design Modules')
install = Transition(label='Install Hydroponics')
climate = Transition(label='Calibrate Climate')
nutrients = Transition(label='Setup Nutrients')
energy = Transition(label='Optimize Energy')
plan = Transition(label='Plan Crops')
pests = Transition(label='Manage Pests')
sensors = Transition(label='Integrate Sensors')
train = Transition(label='Train Staff')
compliance = Transition(label='Compliance Check')
harvest = Transition(label='Pilot Harvest')
analyze = Transition(label='Analyze Data')
improve = Transition(label='Improve Process')
engage = Transition(label='Engage Community')

loop = OperatorPOWL(operator=Operator.LOOP, children=[analyze, improve])

root = StrictPartialOrder(nodes=[
    site, design, install, climate, nutrients, energy, plan, pests,
    sensors, train, compliance, harvest, loop, engage
])

root.order.add_edge(site, design)
root.order.add_edge(design, install)
root.order.add_edge(install, climate)
root.order.add_edge(climate, nutrients)
root.order.add_edge(nutrients, energy)
root.order.add_edge(energy, plan)
root.order.add_edge(plan, pests)
root.order.add_edge(pests, sensors)
root.order.add_edge(sensors, train)
root.order.add_edge(train, compliance)
root.order.add_edge(compliance, harvest)
root.order.add_edge(harvest, loop)
root.order.add_edge(loop, engage)