# Generated from: f093d7ef-a523-4370-8dd9-32ec08de122b.json
# Description: This process outlines the intricate steps involved in establishing a fully operational urban vertical farm, integrating hydroponic technology, renewable energy, and automated climate control systems. It encompasses site analysis, modular structure assembly, nutrient solution formulation, seed selection, environmental calibration, pest monitoring, and yield optimization. The process further includes data integration from IoT sensors, AI-driven growth prediction, and community engagement for sustainable local food production, ensuring efficiency and minimal ecological footprint within dense city environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Module_Build = Transition(label='Module Build')
System_Install = Transition(label='System Install')
Water_Prep = Transition(label='Water Prep')
Seed_Selection = Transition(label='Seed Selection')
Nutrient_Mix = Transition(label='Nutrient Mix')
Climate_Setup = Transition(label='Climate Setup')
Sensor_Deploy = Transition(label='Sensor Deploy')
Pest_Scan = Transition(label='Pest Scan')
Growth_Monitor = Transition(label='Growth Monitor')
Data_Sync = Transition(label='Data Sync')
Energy_Manage = Transition(label='Energy Manage')
Harvest_Plan = Transition(label='Harvest Plan')
Community_Link = Transition(label='Community Link')

# Partial order to model the workflow reflecting dependencies and concurrency:
# Stepwise sequence (site survey to system install)
preparation = StrictPartialOrder(nodes=[Site_Survey, Design_Layout, Module_Build, System_Install])
preparation.order.add_edge(Site_Survey, Design_Layout)
preparation.order.add_edge(Design_Layout, Module_Build)
preparation.order.add_edge(Module_Build, System_Install)

# Nutrient and seed prep parallel to system install (these can proceed after design layout)
nutrient_seed = StrictPartialOrder(nodes=[Seed_Selection, Nutrient_Mix, Water_Prep])
nutrient_seed.order.add_edge(Seed_Selection, Nutrient_Mix)
# Water prep can run concurrently with seed selection and nutrient mix
# No edges mean concurrency

# Environment calibration (Climate Setup) after system install and water prep done
calibration = StrictPartialOrder(nodes=[Climate_Setup])
# It requires System Install and Water Prep to complete, so we will add edges later in root

# Sensor Deploy and Pest Scan can start after calibration
environment_monitoring = StrictPartialOrder(nodes=[Sensor_Deploy, Pest_Scan])
# They are concurrent, no edges

# Growth Monitor and Data Sync after monitoring
growth_data_sync = StrictPartialOrder(nodes=[Growth_Monitor, Data_Sync])
growth_data_sync.order.add_edge(Growth_Monitor, Data_Sync)

# Energy Manage concurrent with data sync and growth monitor (assuming continuous)
energy_manage = StrictPartialOrder(nodes=[Energy_Manage])

# Harvest Plan and Community Link after growth monitor and energy manage
harvest_community = StrictPartialOrder(nodes=[Harvest_Plan, Community_Link])
# They are concurrent; both depend on Growth Monitor and Energy Manage, edges will be added in root

# Combine all parts into one StrictPartialOrder with all nodes
all_nodes = [Site_Survey, Design_Layout, Module_Build, System_Install,
             Seed_Selection, Nutrient_Mix, Water_Prep,
             Climate_Setup,
             Sensor_Deploy, Pest_Scan,
             Growth_Monitor, Data_Sync,
             Energy_Manage,
             Harvest_Plan, Community_Link]

root = StrictPartialOrder(nodes=all_nodes)

# Add edges for preparation
root.order.add_edge(Site_Survey, Design_Layout)
root.order.add_edge(Design_Layout, Module_Build)
root.order.add_edge(Module_Build, System_Install)

# Nutrient and seed ordering
root.order.add_edge(Seed_Selection, Nutrient_Mix)
# Water Prep concurrent with Seed Selection and Nutrient Mix

# Climate Setup after System Install and Water Prep
root.order.add_edge(System_Install, Climate_Setup)
root.order.add_edge(Water_Prep, Climate_Setup)

# Sensor Deploy and Pest Scan after Climate Setup
root.order.add_edge(Climate_Setup, Sensor_Deploy)
root.order.add_edge(Climate_Setup, Pest_Scan)

# Growth Monitor after Sensor Deploy and Pest Scan
root.order.add_edge(Sensor_Deploy, Growth_Monitor)
root.order.add_edge(Pest_Scan, Growth_Monitor)

# Data Sync after Growth Monitor
root.order.add_edge(Growth_Monitor, Data_Sync)

# Energy Manage concurrent starting after System Install (assuming energy manage begins post install in parallel)
root.order.add_edge(System_Install, Energy_Manage)

# Harvest Plan and Community Link after Growth Monitor and Energy Manage
root.order.add_edge(Growth_Monitor, Harvest_Plan)
root.order.add_edge(Energy_Manage, Harvest_Plan)
root.order.add_edge(Growth_Monitor, Community_Link)
root.order.add_edge(Energy_Manage, Community_Link)