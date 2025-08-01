# Generated from: dcc961c5-86a2-44f2-a5d9-420d123b4bb9.json
# Description: This process outlines the complex setup and operational workflow for establishing an urban vertical farm within a densely populated city environment. It involves site assessment, modular design, climate control calibration, hydroponic nutrient balancing, automated seeding, integrated pest management, energy optimization, data-driven growth monitoring, waste recycling, and community engagement initiatives. The process requires coordination between architects, agronomists, engineers, and local authorities to ensure sustainable production, regulatory compliance, and minimal ecological footprint while maximizing yield and quality of fresh produce in a constrained urban space.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
labels = [
    'Site Survey', 'Design Layout', 'Permit Acquire', 'Modular Build',
    'Climate Setup', 'Nutrient Mix', 'Seed Automation', 'Pest Control',
    'Energy Audit', 'Sensor Install', 'Growth Monitor', 'Waste Process',
    'Data Analysis', 'Staff Train', 'Community Link', 'Yield Report'
]
ts = {lbl: Transition(label=lbl) for lbl in labels}

# Loop for integrated pest management: can repeat pest control until exit
loop_pest = OperatorPOWL(
    operator=Operator.LOOP,
    children=[SilentTransition(), ts['Pest Control']]
)

# Loop for data‐driven growth monitoring and analysis
loop_growth = OperatorPOWL(
    operator=Operator.LOOP,
    children=[ts['Growth Monitor'], ts['Data Analysis']]
)

# Build the overall partial‐order model
root = StrictPartialOrder(
    nodes=[
        ts['Site Survey'], ts['Design Layout'], ts['Permit Acquire'],
        ts['Modular Build'], ts['Climate Setup'], ts['Sensor Install'],
        ts['Nutrient Mix'], ts['Seed Automation'], loop_pest,
        ts['Energy Audit'], loop_growth, ts['Waste Process'],
        ts['Staff Train'], ts['Community Link'], ts['Yield Report']
    ]
)

# Define the control‐flow dependencies
root.order.add_edge(ts['Site Survey'], ts['Design Layout'])
root.order.add_edge(ts['Design Layout'], ts['Permit Acquire'])
root.order.add_edge(ts['Permit Acquire'], ts['Modular Build'])
root.order.add_edge(ts['Modular Build'], ts['Climate Setup'])
root.order.add_edge(ts['Climate Setup'], ts['Sensor Install'])
root.order.add_edge(ts['Sensor Install'], ts['Nutrient Mix'])
root.order.add_edge(ts['Nutrient Mix'], ts['Seed Automation'])

root.order.add_edge(ts['Seed Automation'], loop_pest)
root.order.add_edge(loop_pest, ts['Energy Audit'])

root.order.add_edge(ts['Energy Audit'], loop_growth)
root.order.add_edge(loop_growth, ts['Waste Process'])

# After waste processing, staff training and community engagement run in parallel
root.order.add_edge(ts['Waste Process'], ts['Staff Train'])
root.order.add_edge(ts['Waste Process'], ts['Community Link'])

# Final yield reporting waits for both training and community link
root.order.add_edge(ts['Staff Train'], ts['Yield Report'])
root.order.add_edge(ts['Community Link'], ts['Yield Report'])