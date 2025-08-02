# Generated from: 25797ad5-e936-48b5-ae1f-d6d8bc318bcd.json
# Description: This process outlines the comprehensive cycle for managing an urban vertical farm, integrating advanced hydroponic techniques with IoT monitoring and AI-driven crop optimization. It begins with seed selection based on market trends, followed by environment calibration and nutrient balancing. Continuous monitoring of plant health through sensor data informs dynamic adjustments in lighting and humidity. Periodic pest detection triggers targeted bio-control interventions. Harvesting is scheduled according to real-time growth analytics, and post-harvest processing includes automated sorting and packaging. Waste is minimized via composting and resource recycling, ensuring sustainability. The entire cycle is documented for traceability and compliance with urban agriculture regulations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

Seed_Select = Transition(label='Seed Select')
Trend_Analyze = Transition(label='Trend Analyze')
Env_Calibrate = Transition(label='Env Calibrate')
Nutrient_Mix = Transition(label='Nutrient Mix')
Plant_Setup = Transition(label='Plant Setup')
Sensor_Deploy = Transition(label='Sensor Deploy')
Health_Monitor = Transition(label='Health Monitor')
Light_Adjust = Transition(label='Light Adjust')
Humidity_Control = Transition(label='Humidity Control')
Pest_Detect = Transition(label='Pest Detect')
Bio_Control = Transition(label='Bio-Control')
Growth_Track = Transition(label='Growth Track')
Harvest_Plan = Transition(label='Harvest Plan')
Auto_Sort = Transition(label='Auto Sort')
Package_Prep = Transition(label='Package Prep')
Waste_Compost = Transition(label='Waste Compost')
Resource_Recycle = Transition(label='Resource Recycle')
Compliance_Check = Transition(label='Compliance Check')
Trace_Document = Transition(label='Trace Document')

# Loop for periodic pest detection and targeted bio-control intervention
# LOOP body (B): Bio-Control
# LOOP condition (A): Pest Detect
pest_loop = OperatorPOWL(operator=Operator.LOOP, children=[Pest_Detect, Bio_Control])

# Partial order controlling the concurrent monitoring and adjustments branches after sensors deployment:
# Health monitoring -> (Light Adjust, Humidity Control) both concurrent

monitoring_POWL = StrictPartialOrder(
    nodes=[Health_Monitor, Light_Adjust, Humidity_Control]
)
monitoring_POWL.order.add_edge(Health_Monitor, Light_Adjust)
monitoring_POWL.order.add_edge(Health_Monitor, Humidity_Control)

# Another PO of pest detection loop & monitoring_POWL
concurrent_monitoring_and_pest = StrictPartialOrder(
    nodes=[monitoring_POWL, pest_loop]
)
# They are concurrent, no edges between these two

# Post-harvest processing partial order: Auto Sort -> Package Prep
post_harvest_POWL = StrictPartialOrder(
    nodes=[Auto_Sort, Package_Prep]
)
post_harvest_POWL.order.add_edge(Auto_Sort, Package_Prep)

# Waste processing partial order: Waste Compost -> Resource Recycle
waste_POWL = StrictPartialOrder(
    nodes=[Waste_Compost, Resource_Recycle]
)
waste_POWL.order.add_edge(Waste_Compost, Resource_Recycle)

# Final documentation partial order: Compliance Check -> Trace Document
documentation_POWL = StrictPartialOrder(
    nodes=[Compliance_Check, Trace_Document]
)
documentation_POWL.order.add_edge(Compliance_Check, Trace_Document)

# Compose the main partial order of the process, capturing the natural sequence:

# Phase 1: Seed Select -> Trend Analyze
# Phase 2: Env Calibrate -> Nutrient Mix
# Phase 3: Plant Setup -> Sensor Deploy
# Then the concurrent monitoring and pest detection loops
# Then: Growth Track -> Harvest Plan -> Post-harvest processing
# Then waste processing
# Then documentation

root = StrictPartialOrder(
    nodes=[
        Seed_Select,
        Trend_Analyze,
        Env_Calibrate,
        Nutrient_Mix,
        Plant_Setup,
        Sensor_Deploy,
        concurrent_monitoring_and_pest,
        Growth_Track,
        Harvest_Plan,
        post_harvest_POWL,
        waste_POWL,
        documentation_POWL
    ]
)

root.order.add_edge(Seed_Select, Trend_Analyze)
root.order.add_edge(Trend_Analyze, Env_Calibrate)
root.order.add_edge(Env_Calibrate, Nutrient_Mix)
root.order.add_edge(Nutrient_Mix, Plant_Setup)
root.order.add_edge(Plant_Setup, Sensor_Deploy)
root.order.add_edge(Sensor_Deploy, concurrent_monitoring_and_pest)
root.order.add_edge(concurrent_monitoring_and_pest, Growth_Track)
root.order.add_edge(Growth_Track, Harvest_Plan)
root.order.add_edge(Harvest_Plan, post_harvest_POWL)
root.order.add_edge(post_harvest_POWL, waste_POWL)
root.order.add_edge(waste_POWL, documentation_POWL)