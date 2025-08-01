# Generated from: 36a7803e-5cce-43a7-a81d-a5050b5230c2.json
# Description: This process outlines the establishment of an urban vertical farm within a repurposed industrial building. It involves site assessment, modular rack installation, hydroponic system configuration, environmental control calibration, crop selection based on urban climate, seedling propagation, nutrient solution formulation, automated monitoring integration, pest management planning, energy optimization, harvesting scheduling, post-harvest processing, packaging design, distribution logistics coordination, and sustainability compliance verification to ensure efficient production of fresh produce in a city environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
Site_Assess = Transition(label='Site Assess')
Rack_Install = Transition(label='Rack Install')
Hydro_Setup = Transition(label='Hydro Setup')
Env_Control = Transition(label='Env Control')
Crop_Select = Transition(label='Crop Select')
Seedling_Prep = Transition(label='Seedling Prep')
Nutrient_Mix = Transition(label='Nutrient Mix')
Automation_Set = Transition(label='Automation Set')
Pest_Plan = Transition(label='Pest Plan')
Energy_Audit = Transition(label='Energy Audit')
Harvest_Plan = Transition(label='Harvest Plan')
Post_Harvest = Transition(label='Post Harvest')
Pack_Design = Transition(label='Pack Design')
Logistics_Map = Transition(label='Logistics Map')
Sustain_Verify = Transition(label='Sustain Verify')

# Model sequential partial order across all activities, as they follow the order given
nodes = [Site_Assess, Rack_Install, Hydro_Setup, Env_Control, Crop_Select, Seedling_Prep,
         Nutrient_Mix, Automation_Set, Pest_Plan, Energy_Audit, Harvest_Plan,
         Post_Harvest, Pack_Design, Logistics_Map, Sustain_Verify]

root = StrictPartialOrder(nodes=nodes)

# Add edges to reflect the described process order (strict linear ordering)
for i in range(len(nodes) - 1):
    root.order.add_edge(nodes[i], nodes[i + 1])