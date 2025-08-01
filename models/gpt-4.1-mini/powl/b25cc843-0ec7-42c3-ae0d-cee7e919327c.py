# Generated from: b25cc843-0ec7-42c3-ae0d-cee7e919327c.json
# Description: This process outlines the establishment of an urban vertical farm designed to maximize crop yield within limited city space by integrating hydroponics, IoT monitoring, and renewable energy systems. It begins with site analysis and structural assessment, followed by modular rack installation, nutrient solution preparation, and seedling placement. Subsequent activities involve sensor calibration, automated irrigation scheduling, LED lighting optimization, and continuous environmental data collection. The process also covers pest management through biological controls, yield forecasting using AI models, and energy consumption balancing with solar panels. Finally, the harvested produce undergoes quality inspection, packaging, and distribution to local markets, ensuring sustainability and freshness throughout the supply chain.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Activities
Site_Survey = Transition(label='Site Survey')
Structure_Check = Transition(label='Structure Check')
Rack_Setup = Transition(label='Rack Setup')
Seed_Prep = Transition(label='Seed Prep')
Nutrient_Mix = Transition(label='Nutrient Mix')
Seed_Sowing = Transition(label='Seed Sowing')
Sensor_Setup = Transition(label='Sensor Setup')
Irrigation_Plan = Transition(label='Irrigation Plan')
Light_Adjust = Transition(label='Light Adjust')
Data_Capture = Transition(label='Data Capture')
Pest_Control = Transition(label='Pest Control')
Yield_Forecast = Transition(label='Yield Forecast')
Energy_Sync = Transition(label='Energy Sync')
Harvest_Inspect = Transition(label='Harvest Inspect')
Pack_Dispatch = Transition(label='Pack Dispatch')

# Construct partial order

# Phase 1: site analysis and structural assessment (sequential)
phase1 = StrictPartialOrder(nodes=[Site_Survey, Structure_Check])
phase1.order.add_edge(Site_Survey, Structure_Check)

# Phase 2: modular rack installation and preparation activities (sequential)
phase2 = StrictPartialOrder(nodes=[Rack_Setup, Nutrient_Mix, Seed_Prep, Seed_Sowing])
phase2.order.add_edge(Rack_Setup, Nutrient_Mix)
phase2.order.add_edge(Nutrient_Mix, Seed_Prep)
phase2.order.add_edge(Seed_Prep, Seed_Sowing)

# Phase 3: sensor calibration, automated irrigation scheduling, lighting optimization, data capture (these can be considered partially ordered/concurrent after Seed Sowing)
phase3 = StrictPartialOrder(nodes=[Sensor_Setup, Irrigation_Plan, Light_Adjust, Data_Capture])
# No order edges implying concurrency

# Phase 4: pest management, yield forecasting, energy sync (these can be partially ordered or concurrent)
phase4 = StrictPartialOrder(nodes=[Pest_Control, Yield_Forecast, Energy_Sync])
# No order edges implying concurrency

# Phase 5: final harvest inspect, packing and dispatch (sequential)
phase5 = StrictPartialOrder(nodes=[Harvest_Inspect, Pack_Dispatch])
phase5.order.add_edge(Harvest_Inspect, Pack_Dispatch)

# Combine phases in order:
root = StrictPartialOrder(nodes=[phase1, phase2, phase3, phase4, phase5])

# phase1 --> phase2
root.order.add_edge(phase1, phase2)
# phase2 --> phase3
root.order.add_edge(phase2, phase3)
# phase3 --> phase4
root.order.add_edge(phase3, phase4)
# phase4 --> phase5
root.order.add_edge(phase4, phase5)