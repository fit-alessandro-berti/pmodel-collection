# Generated from: c676dd42-1f5e-4761-b647-bda657f6b714.json
# Description: This process outlines the complex establishment of an urban vertical farming facility integrating hydroponics and IoT technology. It involves site analysis, modular design, nutrient solution management, sensor calibration, climate control optimization, waste recycling, and automated harvesting. The goal is to maximize crop yield in a limited space while maintaining sustainability through energy-efficient systems, data-driven growth monitoring, and community engagement programs. This atypical process requires coordination between agricultural scientists, engineers, software developers, and urban planners to create a self-sustaining ecosystem within a city environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Material_Sourcing = Transition(label='Material Sourcing')
System_Assembly = Transition(label='System Assembly')
Sensor_Install = Transition(label='Sensor Install')
Nutrient_Prep = Transition(label='Nutrient Prep')
Water_Testing = Transition(label='Water Testing')
Climate_Setup = Transition(label='Climate Setup')
Data_Integration = Transition(label='Data Integration')
Growth_Monitoring = Transition(label='Growth Monitoring')
Pest_Control = Transition(label='Pest Control')
Waste_Sorting = Transition(label='Waste Sorting')
Harvest_Plan = Transition(label='Harvest Plan')
Produce_Pack = Transition(label='Produce Pack')
Energy_Audit = Transition(label='Energy Audit')
Community_Setup = Transition(label='Community Setup')

# Nutrient solution management loop:
# (Nutrient_Prep then Water_Testing), looped until exit (simulate iterative testing and preparation)
Nutrient_Loop = OperatorPOWL(operator=Operator.LOOP, children=[Nutrient_Prep, Water_Testing])

# Growth monitoring and pest control choice and repeated monitoring:
# Growth_Monitoring followed by choice to either Pest_Control or skip, looped to monitor again or exit
Monitor_Choice = OperatorPOWL(operator=Operator.XOR, children=[Pest_Control, SilentTransition()])
Monitoring_Loop = OperatorPOWL(operator=Operator.LOOP, children=[Growth_Monitoring, Monitor_Choice])

# Waste recycling: Waste_Sorting and Energy_Audit can be done concurrently but both precede Community_Setup
Waste_PO = StrictPartialOrder(nodes=[Waste_Sorting, Energy_Audit])
# no order edges: concurrent

# After initial system assembly and sensor install, start climate setup and data integration (concurrent)
Climate_Data_PO = StrictPartialOrder(nodes=[Climate_Setup, Data_Integration])
# no order edges: concurrent

# High level partial order combining major phases:
root = StrictPartialOrder(nodes=[
    Site_Survey,
    Design_Layout,
    Material_Sourcing,
    System_Assembly,
    Sensor_Install,
    Nutrient_Loop,
    Climate_Data_PO,
    Monitoring_Loop,
    Waste_PO,
    Harvest_Plan,
    Produce_Pack,
    Community_Setup,
])

# Define ordering edges to reflect natural flow:

# Site Survey --> Design Layout
root.order.add_edge(Site_Survey, Design_Layout)

# Design Layout --> Material Sourcing
root.order.add_edge(Design_Layout, Material_Sourcing)

# Material Sourcing --> System Assembly
root.order.add_edge(Material_Sourcing, System_Assembly)

# System Assembly --> Sensor Install
root.order.add_edge(System_Assembly, Sensor_Install)

# Sensor Install --> Nutrient Loop (nutrient prep + water testing)
root.order.add_edge(Sensor_Install, Nutrient_Loop)

# Nutrient Loop --> Climate and Data Setup (concurrent)
root.order.add_edge(Nutrient_Loop, Climate_Data_PO)

# Climate and Data Setup --> Monitoring Loop
root.order.add_edge(Climate_Data_PO, Monitoring_Loop)

# Monitoring Loop --> Waste PO and Harvest Plan (Waste and Energy Audit concurrent)
root.order.add_edge(Monitoring_Loop, Waste_PO)
root.order.add_edge(Monitoring_Loop, Harvest_Plan)

# Waste PO --> Community Setup
root.order.add_edge(Waste_PO, Community_Setup)

# Harvest Plan --> Produce Pack
root.order.add_edge(Harvest_Plan, Produce_Pack)

# Produce Pack --> Community Setup
root.order.add_edge(Produce_Pack, Community_Setup)