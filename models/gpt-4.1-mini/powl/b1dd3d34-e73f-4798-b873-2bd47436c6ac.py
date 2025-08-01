# Generated from: b1dd3d34-e73f-4798-b873-2bd47436c6ac.json
# Description: This process outlines the comprehensive cycle of urban vertical farming, integrating advanced hydroponic techniques, climate control, and automated nutrient delivery to maximize crop yield within confined city spaces. It begins with seed selection and germination, followed by transplanting seedlings into vertically stacked trays. Continuous monitoring of environmental parameters such as humidity, temperature, and light ensures optimal growth conditions. The system employs robotic arms for pruning and harvesting, while integrated sensors detect pest presence or nutrient deficiencies, triggering corrective actions. Wastewater is recycled through a closed-loop system, minimizing environmental impact and resource consumption. Finally, harvested produce undergoes quality inspection and packaging before distribution to local markets, closing the sustainable urban agriculture loop.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Seed_Selection = Transition(label='Seed Selection')
Germinate_Seeds = Transition(label='Germinate Seeds')
Tray_Transplant = Transition(label='Tray Transplant')
Climate_Setup = Transition(label='Climate Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')
Monitor_Sensors = Transition(label='Monitor Sensors')
Adjust_Lighting = Transition(label='Adjust Lighting')
Pest_Detection = Transition(label='Pest Detection')
Robotic_Prune = Transition(label='Robotic Prune')
Harvest_Crop = Transition(label='Harvest Crop')
Wastewater_Recycle = Transition(label='Wastewater Recycle')
Quality_Inspect = Transition(label='Quality Inspect')
Package_Produce = Transition(label='Package Produce')
Market_Dispatch = Transition(label='Market Dispatch')
Data_Logging = Transition(label='Data Logging')

# Choice between Adjust Lighting or Pest Detection after monitoring sensors
adjust_or_pest = OperatorPOWL(operator=Operator.XOR, children=[Adjust_Lighting, Pest_Detection])

# Loop node representing continuous monitoring and corrective actions:
# Execute Monitor_Sensors, then choose to exit or execute (adjust_or_pest then Monitor_Sensors) again
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[Monitor_Sensors, adjust_or_pest])

# Partial order capturing main process flow
# Seed Selection -> Germinate Seeds -> Tray Transplant -> Climate Setup -> Nutrient Mix -> monitor_loop 
# After monitor_loop ends, proceed with robotic prune, harvest crop, wastewater recycle, quality inspect,
# package produce, market dispatch, data logging (data logging last)

nodes = [
    Seed_Selection,
    Germinate_Seeds,
    Tray_Transplant,
    Climate_Setup,
    Nutrient_Mix,
    monitor_loop,
    Robotic_Prune,
    Harvest_Crop,
    Wastewater_Recycle,
    Quality_Inspect,
    Package_Produce,
    Market_Dispatch,
    Data_Logging
]

root = StrictPartialOrder(nodes=nodes)

# Add edges to express partial order and sequence dependencies
root.order.add_edge(Seed_Selection, Germinate_Seeds)
root.order.add_edge(Germinate_Seeds, Tray_Transplant)
root.order.add_edge(Tray_Transplant, Climate_Setup)
root.order.add_edge(Climate_Setup, Nutrient_Mix)
root.order.add_edge(Nutrient_Mix, monitor_loop)
root.order.add_edge(monitor_loop, Robotic_Prune)
root.order.add_edge(Robotic_Prune, Harvest_Crop)
root.order.add_edge(Harvest_Crop, Wastewater_Recycle)
root.order.add_edge(Wastewater_Recycle, Quality_Inspect)
root.order.add_edge(Quality_Inspect, Package_Produce)
root.order.add_edge(Package_Produce, Market_Dispatch)
root.order.add_edge(Market_Dispatch, Data_Logging)