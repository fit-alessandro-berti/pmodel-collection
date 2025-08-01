# Generated from: 39f719ae-3b71-4c93-adf3-f776109a8ead.json
# Description: This process outlines the complex, atypical workflow of managing an urban vertical farm that integrates hydroponics, AI-driven climate control, and automated harvesting. Starting with seed selection based on predictive analytics, it includes nutrient solution calibration, multi-layer crop monitoring, pest bio-control deployment, and dynamic light spectrum adjustment. The cycle further incorporates waste recycling into compost, energy consumption optimization, and real-time data reporting to stakeholders. This holistic approach ensures sustainable production, maximizes yield within confined urban spaces, and adapts continuously to environmental changes and market demands.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define basic activities
seed = Transition(label='Seed Selection')
solution = Transition(label='Solution Mix')
climate = Transition(label='Climate Setup')
light = Transition(label='Light Tuning')
monitor = Transition(label='Crop Monitoring')
analysis = Transition(label='Growth Analysis')
pest = Transition(label='Pest Control')
energy_audit = Transition(label='Energy Audit')
water_recycle = Transition(label='Water Recycling')
nutrient_refill = Transition(label='Nutrient Refill')
waste_compost = Transition(label='Waste Compost')
harvest_prep = Transition(label='Harvest Prep')
automated_pick = Transition(label='Automated Pick')
data_report = Transition(label='Data Reporting')
market_sync = Transition(label='Market Sync')
equipment_check = Transition(label='Equipment Check')
system_update = Transition(label='System Update')

# Silent skip for optional branches
skip = SilentTransition()

# Optional pest control
pest_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[pest, skip]
)

# Optional nutrient refill
nutrient_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[nutrient_refill, skip]
)

# Define the monitoring-analysis partial order (loop init)
init_cycle = StrictPartialOrder(
    nodes=[monitor, analysis]
)
init_cycle.order.add_edge(monitor, analysis)

# Define the loop body: optional pest then optional nutrient refill
body_cycle = StrictPartialOrder(
    nodes=[pest_choice, nutrient_choice]
)
body_cycle.order.add_edge(pest_choice, nutrient_choice)

# Loop: perform monitor->analysis, then zero or more cycles of (pest? -> nutrient? -> back)
crop_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[init_cycle, body_cycle]
)

# Build the main workflow as a strict partial order
root = StrictPartialOrder(
    nodes=[
        seed, solution, climate, light,
        crop_loop,
        harvest_prep, automated_pick,
        waste_compost, water_recycle, energy_audit,
        equipment_check, system_update,
        data_report, market_sync
    ]
)

# Define the sequence edges
root.order.add_edge(seed, solution)
root.order.add_edge(solution, climate)
root.order.add_edge(climate, light)
root.order.add_edge(light, crop_loop)
root.order.add_edge(crop_loop, harvest_prep)
root.order.add_edge(harvest_prep, automated_pick)

# After harvest: compost, recycle, audit can run in parallel
root.order.add_edge(automated_pick, waste_compost)
root.order.add_edge(automated_pick, water_recycle)
root.order.add_edge(automated_pick, energy_audit)

# Equipment check and system update must wait for all three post-harvest tasks
for prev in [waste_compost, water_recycle, energy_audit]:
    root.order.add_edge(prev, equipment_check)
    root.order.add_edge(prev, system_update)

# Reporting follows checks and updates
root.order.add_edge(equipment_check, data_report)
root.order.add_edge(system_update, data_report)
root.order.add_edge(data_report, market_sync)