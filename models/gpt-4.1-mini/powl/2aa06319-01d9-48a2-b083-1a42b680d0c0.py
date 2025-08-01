# Generated from: 2aa06319-01d9-48a2-b083-1a42b680d0c0.json
# Description: This process outlines the complex and highly specialized steps required to establish a fully operational urban vertical farming system. It begins with site analysis and continues through modular assembly, hydroponic system integration, automated climate control calibration, nutrient solution formulation, and real-time crop monitoring. The process also involves managing energy consumption, pest prevention protocols, staff training on vertical farming technology, and the implementation of AI-driven yield optimization. Finally, the system undergoes rigorous testing before commercial crop production begins, ensuring sustainability, efficiency, and high-quality output in an urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Site_Analysis = Transition(label='Site Analysis')
Modular_Design = Transition(label='Modular Design')
Structure_Assembly = Transition(label='Structure Assembly')
Hydroponic_Setup = Transition(label='Hydroponic Setup')
Climate_Control = Transition(label='Climate Control')
Nutrient_Mixing = Transition(label='Nutrient Mixing')
Water_Circulation = Transition(label='Water Circulation')
Lighting_Config = Transition(label='Lighting Config')
Pest_Inspection = Transition(label='Pest Inspection')
Energy_Audit = Transition(label='Energy Audit')
Sensor_Install = Transition(label='Sensor Install')
Data_Integration = Transition(label='Data Integration')
Staff_Training = Transition(label='Staff Training')
AI_Calibration = Transition(label='AI Calibration')
Yield_Testing = Transition(label='Yield Testing')
System_Launch = Transition(label='System Launch')

# Build partial orders to represent concurrency and dependency:

# 1) Site analysis leads to modular design and structure assembly (structure assembly after modular design)
# Actually "modular assembly" is two steps: Modular Design -> Structure Assembly
# Hydroponic system integration: Hydroponic Setup
# Climate control calibration: Climate Control
# Nutrient solution formulation: Nutrient Mixing -> Water Circulation-> Lighting Config (some steps concurrent?)

# Pest prevention protocols: Pest Inspection
# Energy management: Energy Audit
# Sensor Install and Data Integration (related, likely sequential)
# Staff training
# AI-driven yield optimization: AI Calibration
# Testing before launch: Yield Testing -> System Launch

# Let's identify concurrency:

# After Site Analysis, Modular Design starts
# After Modular Design, Structure Assembly
# Once Structure Assembly done, Hydroponic Setup starts
# Climate Control and Nutrient Mixing can start concurrently after Hydroponic Setup
# Water Circulation depends on Nutrient Mixing
# Lighting Config can run concurrently with Water Circulation
# Pest Inspection and Energy Audit can run concurrently after Climate Control and Lighting Config
# Sensor Install depends on Hydroponic Setup and Climate Control
# Data Integration after Sensor Install
# Staff Training and AI Calibration can run after Data Integration, concurrently
# Yield Testing after Staff Training and AI Calibration
# Finally System Launch after Yield Testing

# So we structure nodes and dependencies:

# Create nodes list first
nodes = [
    Site_Analysis,
    Modular_Design,
    Structure_Assembly,
    Hydroponic_Setup,
    Climate_Control,
    Nutrient_Mixing,
    Water_Circulation,
    Lighting_Config,
    Pest_Inspection,
    Energy_Audit,
    Sensor_Install,
    Data_Integration,
    Staff_Training,
    AI_Calibration,
    Yield_Testing,
    System_Launch
]

root = StrictPartialOrder(nodes=nodes)
o = root.order

# Add order edges according to dependencies

# Site Analysis --> Modular Design
o.add_edge(Site_Analysis, Modular_Design)

# Modular Design --> Structure Assembly
o.add_edge(Modular_Design, Structure_Assembly)

# Structure Assembly --> Hydroponic Setup
o.add_edge(Structure_Assembly, Hydroponic_Setup)

# Hydroponic Setup --> Climate Control
o.add_edge(Hydroponic_Setup, Climate_Control)

# Hydroponic Setup --> Nutrient Mixing
o.add_edge(Hydroponic_Setup, Nutrient_Mixing)

# Nutrient Mixing --> Water Circulation
o.add_edge(Nutrient_Mixing, Water_Circulation)

# Hydroponic Setup --> Lighting Config (lighting setup can be concurrent with nutrient-related water circulation)
o.add_edge(Hydroponic_Setup, Lighting_Config)

# Climate Control --> Pest Inspection
o.add_edge(Climate_Control, Pest_Inspection)

# Lighting Config --> Pest Inspection
o.add_edge(Lighting_Config, Pest_Inspection)

# Climate Control --> Energy Audit
o.add_edge(Climate_Control, Energy_Audit)

# Lighting_Config --> Energy_Audit
o.add_edge(Lighting_Config, Energy_Audit)

# Hydroponic Setup --> Sensor Install (sensor install after hydroponic setup)
o.add_edge(Hydroponic_Setup, Sensor_Install)

# Climate Control --> Sensor Install (needs climate control to be ready)
o.add_edge(Climate_Control, Sensor_Install)

# Sensor Install --> Data Integration
o.add_edge(Sensor_Install, Data_Integration)

# Data Integration --> Staff Training
o.add_edge(Data_Integration, Staff_Training)

# Data Integration --> AI Calibration
o.add_edge(Data_Integration, AI_Calibration)

# Staff Training --> Yield Testing
o.add_edge(Staff_Training, Yield_Testing)

# AI Calibration --> Yield Testing
o.add_edge(AI_Calibration, Yield_Testing)

# Yield Testing --> System Launch
o.add_edge(Yield_Testing, System_Launch)