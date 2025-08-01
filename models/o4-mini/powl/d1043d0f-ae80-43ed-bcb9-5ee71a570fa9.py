# Generated from: d1043d0f-ae80-43ed-bcb9-5ee71a570fa9.json
# Description: This process outlines the comprehensive steps involved in establishing an urban vertical farm within a constrained city environment. It begins with site evaluation and environmental analysis, followed by modular structure design tailored to space limitations. Subsequent activities cover nutrient solution formulation, seed selection adapted to vertical growth, automated climate control integration, and installation of energy-efficient LED lighting. The process continues with IoT sensor deployment for real-time monitoring, pest management using biological agents, waste recycling protocols, hydroponic system testing, and staff training on operational procedures. Finally, it includes yield forecasting, market positioning strategies, and continuous improvement cycles based on data analytics to optimize production and sustainability in an urban setting.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as POWL Transitions
labels = [
    'Site Survey',
    'Env Analysis',
    'Module Design',
    'Seed Selection',
    'Nutrient Mix',
    'Climate Setup',
    'LED Install',
    'Sensor Deploy',
    'Pest Control',
    'Waste Recycle',
    'Hydro Test',
    'Staff Train',
    'Yield Forecast',
    'Market Plan',
    'Data Review'
]

activities = [Transition(label=lab) for lab in labels]

# Build a strict partial order reflecting the sequential flow
root = StrictPartialOrder(nodes=activities)
for i in range(len(activities) - 1):
    root.order.add_edge(activities[i], activities[i + 1])