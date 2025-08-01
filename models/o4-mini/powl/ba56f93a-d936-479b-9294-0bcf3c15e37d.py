# Generated from: ba56f93a-d936-479b-9294-0bcf3c15e37d.json
# Description: This process outlines the entire operational cycle of an urban vertical farming facility that integrates IoT sensors, AI-driven climate control, and automated harvesting systems. Starting from seed selection and nutrient calibration, it includes environmental monitoring, pest management via bio-controls, growth optimization through AI analytics, and automated packaging for local distribution. The process also incorporates waste recycling, energy usage tracking, and community engagement for crop feedback, ensuring sustainability and efficiency in a confined urban environment where space and resources are limited but demand for fresh produce is high.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
seed = Transition(label='Seed Selection')
nutrient = Transition(label='Nutrient Mix')
iot_setup = Transition(label='IoT Setup')
climate = Transition(label='Climate Adjust')
monitor = Transition(label='Growth Monitor')
pest = Transition(label='Pest Control')
ai = Transition(label='AI Analysis')
harvest_prep = Transition(label='Harvest Prep')
auto_harvest = Transition(label='Auto Harvest')
qc = Transition(label='Quality Check')
pack = Transition(label='Pack Produce')
delivery = Transition(label='Delivery Plan')
water_recycle = Transition(label='Water Recycle')
energy_audit = Transition(label='Energy Audit')
waste_manage = Transition(label='Waste Manage')
feedback = Transition(label='Feedback Loop')

# Define a small loop around the feedback step (optional repeat)
skip = SilentTransition()
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback, skip])

# Assemble the overall partial‐order workflow
root = StrictPartialOrder(nodes=[
    seed, nutrient, iot_setup, climate, monitor, pest, ai,
    harvest_prep, auto_harvest, qc, pack, delivery,
    water_recycle, energy_audit, waste_manage,
    feedback_loop
])

# Sequence edges for the main cultivation‐to‐delivery flow
root.order.add_edge(seed, nutrient)
root.order.add_edge(nutrient, iot_setup)
root.order.add_edge(iot_setup, climate)
root.order.add_edge(climate, monitor)
root.order.add_edge(monitor, pest)
root.order.add_edge(pest, ai)
root.order.add_edge(ai, harvest_prep)
root.order.add_edge(harvest_prep, auto_harvest)
root.order.add_edge(auto_harvest, qc)
root.order.add_edge(qc, pack)
root.order.add_edge(pack, delivery)
root.order.add_edge(delivery, feedback_loop)

# Concurrent sustainability sub‐processes after quality check
root.order.add_edge(qc, water_recycle)
root.order.add_edge(qc, energy_audit)
root.order.add_edge(qc, waste_manage)