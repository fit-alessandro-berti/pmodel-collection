# Generated from: 0551c1a1-5268-49d8-a4a3-8d13c905c273.json
# Description: This process involves establishing a fully operational urban vertical farm within a multi-story building. It begins with site analysis and design customization to maximize space utilization and light distribution. After structural modifications, hydroponic and aeroponic systems are installed, followed by climate control and sensor integration to monitor environmental parameters. Seed selection and planting schedules are coordinated with automated nutrient delivery systems. Staff training ensures proper maintenance and harvesting techniques. The process closes with quality assurance and market distribution planning to supply fresh produce locally, minimizing transportation footprint while maximizing yield and sustainability.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Site_Analysis = Transition(label='Site Analysis')
Design_Layout = Transition(label='Design Layout')
Structural_Mod = Transition(label='Structural Mod')
System_Install = Transition(label='System Install')
Climate_Setup = Transition(label='Climate Setup')
Sensor_Deploy = Transition(label='Sensor Deploy')
Seed_Select = Transition(label='Seed Select')
Planting_Plan = Transition(label='Planting Plan')
Nutrient_Flow = Transition(label='Nutrient Flow')
Automation_Tune = Transition(label='Automation Tune')
Staff_Training = Transition(label='Staff Training')
Harvest_Prep = Transition(label='Harvest Prep')
Quality_Check = Transition(label='Quality Check')
Market_Plan = Transition(label='Market Plan')
Distribution = Transition(label='Distribution')

# Create a strict partial order reflecting the described process flow:
# 1. Site Analysis --> Design Layout
# 2. Design Layout --> Structural Mod
# 3. Structural Mod --> System Install
# 4. System Install --> Climate Setup and Sensor Deploy in parallel (concurrent)
# 5. Climate Setup and Sensor Deploy --> Seed Select and Planting Plan in parallel
# 6. Seed Select and Planting Plan --> Nutrient Flow and Automation Tune in parallel
# 7. Nutrient Flow and Automation Tune --> Staff Training
# 8. Staff Training --> Harvest Prep
# 9. Harvest Prep --> Quality Check
# 10. Quality Check --> Market Plan
# 11. Market Plan --> Distribution

nodes = [
    Site_Analysis, Design_Layout, Structural_Mod, System_Install,
    Climate_Setup, Sensor_Deploy, Seed_Select, Planting_Plan,
    Nutrient_Flow, Automation_Tune, Staff_Training, Harvest_Prep,
    Quality_Check, Market_Plan, Distribution
]

root = StrictPartialOrder(nodes=nodes)

root.order.add_edge(Site_Analysis, Design_Layout)
root.order.add_edge(Design_Layout, Structural_Mod)
root.order.add_edge(Structural_Mod, System_Install)

# After System Install, Climate Setup and Sensor Deploy run concurrently - no order between them
root.order.add_edge(System_Install, Climate_Setup)
root.order.add_edge(System_Install, Sensor_Deploy)

# Seed Select and Planting Plan run concurrently after Climate Setup and Sensor Deploy
# To ensure both Climate_Setup and Sensor_Deploy precede both Seed_Select and Planting_Plan, add these edges:
root.order.add_edge(Climate_Setup, Seed_Select)
root.order.add_edge(Climate_Setup, Planting_Plan)
root.order.add_edge(Sensor_Deploy, Seed_Select)
root.order.add_edge(Sensor_Deploy, Planting_Plan)

# Nutrient Flow and Automation Tune run concurrently after Seed Select and Planting Plan
root.order.add_edge(Seed_Select, Nutrient_Flow)
root.order.add_edge(Seed_Select, Automation_Tune)
root.order.add_edge(Planting_Plan, Nutrient_Flow)
root.order.add_edge(Planting_Plan, Automation_Tune)

root.order.add_edge(Nutrient_Flow, Staff_Training)
root.order.add_edge(Automation_Tune, Staff_Training)

root.order.add_edge(Staff_Training, Harvest_Prep)
root.order.add_edge(Harvest_Prep, Quality_Check)
root.order.add_edge(Quality_Check, Market_Plan)
root.order.add_edge(Market_Plan, Distribution)