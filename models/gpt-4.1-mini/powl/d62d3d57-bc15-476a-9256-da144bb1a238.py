# Generated from: d62d3d57-bc15-476a-9256-da144bb1a238.json
# Description: This process outlines the comprehensive steps involved in establishing an urban vertical farming operation within a repurposed industrial building. It includes site evaluation, structural modification, environmental system integration, crop selection based on market trends, automated nutrient delivery configuration, pest monitoring via AI sensors, workforce training in hydroponic techniques, regulatory compliance checks, and continuous yield optimization. The process culminates in launching a sustainable, tech-driven farm that maximizes space efficiency and produces high-quality crops year-round for local distribution, catering to both retail and wholesale clients while minimizing environmental impact and operational costs.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
Site_Survey = Transition(label='Site Survey')
Structure_Assess = Transition(label='Structure Assess')
System_Design = Transition(label='System Design')
Crop_Select = Transition(label='Crop Select')
Permit_Obtain = Transition(label='Permit Obtain')
Enviro_Setup = Transition(label='Enviro Setup')
Irrigation_Plan = Transition(label='Irrigation Plan')
Sensor_Install = Transition(label='Sensor Install')
AI_Calibration = Transition(label='AI Calibration')
Staff_Train = Transition(label='Staff Train')
Nutrient_Mix = Transition(label='Nutrient Mix')
Pest_Monitor = Transition(label='Pest Monitor')
Yield_Analyze = Transition(label='Yield Analyze')
Market_Align = Transition(label='Market Align')
Launch_Farm = Transition(label='Launch Farm')

# Partial orders for structural modification and environmental integration
# Structural modification: Site Survey --> Structure Assess --> System Design
struct_mod = StrictPartialOrder(nodes=[Site_Survey, Structure_Assess, System_Design])
struct_mod.order.add_edge(Site_Survey, Structure_Assess)
struct_mod.order.add_edge(Structure_Assess, System_Design)

# Enviro setup: System Design --> Enviro Setup --> Irrigation Plan --> Sensor Install --> AI Calibration
enviro_integ = StrictPartialOrder(nodes=[System_Design, Enviro_Setup, Irrigation_Plan, Sensor_Install, AI_Calibration])
enviro_integ.order.add_edge(System_Design, Enviro_Setup)
enviro_integ.order.add_edge(Enviro_Setup, Irrigation_Plan)
enviro_integ.order.add_edge(Irrigation_Plan, Sensor_Install)
enviro_integ.order.add_edge(Sensor_Install, AI_Calibration)

# Crop and market alignment choices: Crop Select and Market Align run concurrently
crop_market = StrictPartialOrder(nodes=[Crop_Select, Market_Align])

# Nutrient delivery and pest monitoring with staff training:
# Nutrient Mix must be done before Pest Monitor;
# Staff Train can be concurrent to Nutrient Mix and Pest Monitor but both before Yield Analyze
nutrient_pest = StrictPartialOrder(nodes=[Nutrient_Mix, Pest_Monitor, Staff_Train, Yield_Analyze])
nutrient_pest.order.add_edge(Nutrient_Mix, Pest_Monitor)
nutrient_pest.order.add_edge(Nutrient_Mix, Yield_Analyze)
nutrient_pest.order.add_edge(Pest_Monitor, Yield_Analyze)
nutrient_pest.order.add_edge(Staff_Train, Yield_Analyze)

# Permit Obtain can be done any time after Crop Select and Market Align but before Launch Farm
permit_flow = StrictPartialOrder(nodes=[Crop_Select, Market_Align, Permit_Obtain])
permit_flow.order.add_edge(Crop_Select, Permit_Obtain)
permit_flow.order.add_edge(Market_Align, Permit_Obtain)

# Final launching: Yield Analyze and Permit Obtain both must complete before Launch Farm
final_phase = StrictPartialOrder(nodes=[Yield_Analyze, Permit_Obtain, Launch_Farm])
final_phase.order.add_edge(Yield_Analyze, Launch_Farm)
final_phase.order.add_edge(Permit_Obtain, Launch_Farm)

# Now combine all partial orders respecting their dependencies:
# Site Survey --> Structure Assess --> System Design --+
#                                                     +--> Enviro Setup ... AI Calibration
# Crop Select and Market Align run concurrently with prior
# Nutrient_Pest depends on AI Calibration finished (implicitly on System Design through Enviro Setup)
# We merge them with explicit edges for logical flow:

# First combine struct_mod and enviro_integ:
struct_enviro = StrictPartialOrder(nodes=[Site_Survey, Structure_Assess, System_Design, Enviro_Setup, Irrigation_Plan, Sensor_Install, AI_Calibration])
struct_enviro.order.add_edge(Site_Survey, Structure_Assess)
struct_enviro.order.add_edge(Structure_Assess, System_Design)
struct_enviro.order.add_edge(System_Design, Enviro_Setup)
struct_enviro.order.add_edge(Enviro_Setup, Irrigation_Plan)
struct_enviro.order.add_edge(Irrigation_Plan, Sensor_Install)
struct_enviro.order.add_edge(Sensor_Install, AI_Calibration)

# Combine crop_market and permit_flow (permit depends on both)
crop_permit = StrictPartialOrder(nodes=[Crop_Select, Market_Align, Permit_Obtain])
crop_permit.order.add_edge(Crop_Select, Permit_Obtain)
crop_permit.order.add_edge(Market_Align, Permit_Obtain)

# Nutrient_pest and final_phase to be merged respecting dependency on AI_Calibration (i.e., AI_Calibration --> Nutrient_Mix)
nutrient_pest_final_nodes = [Nutrient_Mix, Pest_Monitor, Staff_Train, Yield_Analyze, Permit_Obtain, Launch_Farm]
nutrient_pest_final = StrictPartialOrder(nodes=nutrient_pest_final_nodes)
nutrient_pest_final.order.add_edge(Nutrient_Mix, Pest_Monitor)
nutrient_pest_final.order.add_edge(Nutrient_Mix, Yield_Analyze)
nutrient_pest_final.order.add_edge(Pest_Monitor, Yield_Analyze)
nutrient_pest_final.order.add_edge(Staff_Train, Yield_Analyze)
nutrient_pest_final.order.add_edge(Yield_Analyze, Launch_Farm)
nutrient_pest_final.order.add_edge(Permit_Obtain, Launch_Farm)

# Create root POWL with all nodes:
root_nodes = [
    Site_Survey, Structure_Assess, System_Design, Enviro_Setup, Irrigation_Plan, Sensor_Install, AI_Calibration,
    Crop_Select, Market_Align,
    Permit_Obtain,
    Nutrient_Mix, Pest_Monitor, Staff_Train,
    Yield_Analyze,
    Launch_Farm
]
root = StrictPartialOrder(nodes=root_nodes)

# Add structural modification and enviro setup order edges (they form a main sequence)
root.order.add_edge(Site_Survey, Structure_Assess)
root.order.add_edge(Structure_Assess, System_Design)
root.order.add_edge(System_Design, Enviro_Setup)
root.order.add_edge(Enviro_Setup, Irrigation_Plan)
root.order.add_edge(Irrigation_Plan, Sensor_Install)
root.order.add_edge(Sensor_Install, AI_Calibration)

# Crop_Select and Market_Align concurrent with main sequence but Permit_Obtain depends on them
root.order.add_edge(Crop_Select, Permit_Obtain)
root.order.add_edge(Market_Align, Permit_Obtain)

# AI Calibration before Nutrient Mix (makes logical sense, nutrients depend on systems configured)
root.order.add_edge(AI_Calibration, Nutrient_Mix)

# Nutrient Mix before Pest Monitor and Yield Analyze
root.order.add_edge(Nutrient_Mix, Pest_Monitor)
root.order.add_edge(Nutrient_Mix, Yield_Analyze)

# Pest Monitor before Yield Analyze
root.order.add_edge(Pest_Monitor, Yield_Analyze)

# Staff Train before Yield Analyze (parallel with Nutrient & Pest)
root.order.add_edge(Staff_Train, Yield_Analyze)

# Yield Analyze and Permit Obtain before Launch Farm
root.order.add_edge(Yield_Analyze, Launch_Farm)
root.order.add_edge(Permit_Obtain, Launch_Farm)