# Generated from: 10636b6f-ed79-4221-8e8b-27c552618784.json
# Description: This process outlines the comprehensive steps involved in establishing an urban vertical farm within a repurposed industrial building. It begins with site evaluation considering sunlight exposure and structural integrity, followed by modular rack installation optimized for hydroponic systems. Subsequent activities include nutrient solution formulation, LED light calibration, and climate control automation setup. The process also incorporates seed selection based on local market demand, pest management protocols adapted to enclosed environments, and workforce training in specialized agricultural techniques. Final stages involve integration of IoT sensors for real-time monitoring, data analytics for yield prediction, and compliance verification with urban agricultural regulations. This atypical yet realistic process merges urban planning, advanced agriculture, and technology implementation to create sustainable food production in city settings.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Site_Survey = Transition(label='Site Survey')
Rack_Install = Transition(label='Rack Install')
Solution_Mix = Transition(label='Solution Mix')
Light_Setup = Transition(label='Light Setup')
Climate_Tune = Transition(label='Climate Tune')
Seed_Select = Transition(label='Seed Select')
Pest_Control = Transition(label='Pest Control')
Staff_Train = Transition(label='Staff Train')
IoT_Deploy = Transition(label='IoT Deploy')
Data_Analyze = Transition(label='Data Analyze')
Regulate_Check = Transition(label='Regulate Check')
Yield_Monitor = Transition(label='Yield Monitor')
Water_Cycle = Transition(label='Water Cycle')
Harvest_Plan = Transition(label='Harvest Plan')
Market_Sync = Transition(label='Market Sync')
System_Test = Transition(label='System Test')

# Build partial orders to capture concurrency and precedence

# Step 1: Site Survey precedes Rack Install
# Rack Install precedes Solution Mix and Light Setup (which are concurrent)
# Climate Tune can be done after Light Setup
# Seed Select precedes Pest Control and Staff Train (concurrent)
# Pest Control precedes IoT Deploy
# Staff Train precedes System Test
# IoT Deploy precedes Data Analyze
# Data Analyze precedes Yield Monitor and Regulate Check (concurrent)
# Water Cycle precedes Harvest Plan
# Harvest Plan precedes Market Sync and System Test (concurrent)
#
# System Test is after Staff Train and Harvest Plan and Market Sync

# Construct nodes list first
nodes = [
    Site_Survey,
    Rack_Install,
    Solution_Mix,
    Light_Setup,
    Climate_Tune,
    Seed_Select,
    Pest_Control,
    Staff_Train,
    IoT_Deploy,
    Data_Analyze,
    Regulate_Check,
    Yield_Monitor,
    Water_Cycle,
    Harvest_Plan,
    Market_Sync,
    System_Test
]

root = StrictPartialOrder(nodes=nodes)

# Add edges according to the description

# Site Survey --> Rack Install
root.order.add_edge(Site_Survey, Rack_Install)

# Rack Install --> Solution Mix
root.order.add_edge(Rack_Install, Solution_Mix)
# Rack Install --> Light Setup
root.order.add_edge(Rack_Install, Light_Setup)

# Light Setup --> Climate Tune
root.order.add_edge(Light_Setup, Climate_Tune)

# Seed Select --> Pest Control
root.order.add_edge(Seed_Select, Pest_Control)
# Seed Select --> Staff Train
root.order.add_edge(Seed_Select, Staff_Train)

# Pest Control --> IoT Deploy
root.order.add_edge(Pest_Control, IoT_Deploy)

# Staff Train --> System Test
root.order.add_edge(Staff_Train, System_Test)

# IoT Deploy --> Data Analyze
root.order.add_edge(IoT_Deploy, Data_Analyze)

# Data Analyze --> Yield Monitor
root.order.add_edge(Data_Analyze, Yield_Monitor)
# Data Analyze --> Regulate Check
root.order.add_edge(Data_Analyze, Regulate_Check)

# Water Cycle --> Harvest Plan
root.order.add_edge(Water_Cycle, Harvest_Plan)

# Harvest Plan --> Market Sync
root.order.add_edge(Harvest_Plan, Market_Sync)
# Harvest Plan --> System Test
root.order.add_edge(Harvest_Plan, System_Test)

# Market Sync --> System Test
root.order.add_edge(Market_Sync, System_Test)

# Additional flows inferred to ensure the process is continuous:
# Seed Select should occur after Climate Tune and Solution Mix (to reflect selection of seeds after environment is tuned)
root.order.add_edge(Solution_Mix, Seed_Select)
root.order.add_edge(Climate_Tune, Seed_Select)

# Water Cycle relates to Climate Tune and Solution Mix (environmental control)
root.order.add_edge(Climate_Tune, Water_Cycle)
root.order.add_edge(Solution_Mix, Water_Cycle)

# Yield Monitor and Regulate Check probably should precede System Test to finalize validations
root.order.add_edge(Yield_Monitor, System_Test)
root.order.add_edge(Regulate_Check, System_Test)

# Harvest Plan and Water Cycle parallel with Yield Monitor, Regulate Check, Market Sync and System Test can happen after
# The order already established

# Final graph models the partial order and concurrency
