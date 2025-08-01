# Generated from: 2f34c772-00ed-43d1-8712-79a31f2bde92.json
# Description: This process outlines the detailed steps for establishing a bespoke urban farming system in densely populated city environments. It involves site analysis, modular design customization, integration of IoT sensors for real-time monitoring, adaptive irrigation scheduling based on microclimate data, community engagement for crop selection, and iterative yield optimization through data analytics. Additional activities include local regulatory compliance, vertical structure assembly, soil-less media preparation, renewable energy sourcing, pest management using bio-controls, and final harvest logistics coordination to ensure fresh produce delivery directly to consumers with minimal environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey     = Transition(label='Site Survey')
design_draft    = Transition(label='Design Draft')
reg_check       = Transition(label='Regulation Check')
structure_build = Transition(label='Structure Build')
media_prep      = Transition(label='Media Prep')
pest_control    = Transition(label='Pest Control')
energy_setup    = Transition(label='Energy Setup')
sensor_setup    = Transition(label='Sensor Setup')
community_meet  = Transition(label='Community Meet')
microclimate_map= Transition(label='Microclimate Map')
crop_selection  = Transition(label='Crop Selection')
irrigation_plan = Transition(label='Irrigation Plan')
data_analysis   = Transition(label='Data Analysis')
yield_adjust    = Transition(label='Yield Adjust')
harvest_plan    = Transition(label='Harvest Plan')
delivery_coord  = Transition(label='Delivery Coord')

# Loop for iterative yield optimization: execute Data Analysis, then optionally Yield Adjust and repeat
yield_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_analysis, yield_adjust])

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey, design_draft, reg_check, structure_build,
    media_prep, pest_control, energy_setup, sensor_setup,
    community_meet, microclimate_map, crop_selection,
    irrigation_plan, yield_loop, harvest_plan, delivery_coord
])

# Define ordering relations
root.order.add_edge(site_survey,     design_draft)
root.order.add_edge(design_draft,    reg_check)
root.order.add_edge(reg_check,       structure_build)
root.order.add_edge(structure_build, media_prep)
root.order.add_edge(media_prep,      pest_control)
root.order.add_edge(pest_control,    energy_setup)
root.order.add_edge(energy_setup,    sensor_setup)
root.order.add_edge(energy_setup,    community_meet)
root.order.add_edge(sensor_setup,    microclimate_map)
root.order.add_edge(community_meet,  crop_selection)
root.order.add_edge(microclimate_map, irrigation_plan)
root.order.add_edge(crop_selection,  irrigation_plan)
root.order.add_edge(irrigation_plan, yield_loop)
root.order.add_edge(yield_loop,      harvest_plan)
root.order.add_edge(harvest_plan,    delivery_coord)