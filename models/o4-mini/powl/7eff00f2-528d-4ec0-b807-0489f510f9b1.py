# Generated from: 7eff00f2-528d-4ec0-b807-0489f510f9b1.json
# Description: This process involves establishing an urban vertical farm within a repurposed warehouse. It includes site inspection, structural reinforcement, hydroponic system installation, environmental control configuration, crop selection, nutrient solution formulation, seedling propagation, automated lighting setup, pest monitoring, data analytics integration, staff training, harvest scheduling, packaging design, market testing, and waste recycling. The goal is to optimize space, reduce resource consumption, and deliver fresh produce efficiently to urban consumers while maintaining sustainability and scalability.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define the atomic activities
site_inspect        = Transition(label='Site Inspect')
structure_check     = Transition(label='Structure Check')
hydroponics_install = Transition(label='Hydroponics Install')
env_control         = Transition(label='Env Control')
crop_select         = Transition(label='Crop Select')
nutrient_mix        = Transition(label='Nutrient Mix')
seedling_grow       = Transition(label='Seedling Grow')
light_setup         = Transition(label='Light Setup')
pest_monitor        = Transition(label='Pest Monitor')
data_integrate      = Transition(label='Data Integrate')
staff_train         = Transition(label='Staff Train')
harvest_plan        = Transition(label='Harvest Plan')
pack_design         = Transition(label='Pack Design')
market_test         = Transition(label='Market Test')
waste_recycle       = Transition(label='Waste Recycle')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    site_inspect,
    structure_check,
    hydroponics_install,
    env_control,
    crop_select,
    nutrient_mix,
    seedling_grow,
    light_setup,
    pest_monitor,
    data_integrate,
    staff_train,
    harvest_plan,
    pack_design,
    market_test,
    waste_recycle
])

# Define the control‐flow dependencies
root.order.add_edge(site_inspect,        structure_check)
root.order.add_edge(structure_check,     hydroponics_install)
root.order.add_edge(structure_check,     env_control)

root.order.add_edge(hydroponics_install, crop_select)
root.order.add_edge(env_control,         crop_select)

root.order.add_edge(crop_select,         nutrient_mix)
root.order.add_edge(nutrient_mix,        seedling_grow)
root.order.add_edge(seedling_grow,       light_setup)

root.order.add_edge(light_setup,         pest_monitor)
root.order.add_edge(pest_monitor,        data_integrate)
root.order.add_edge(data_integrate,      staff_train)

root.order.add_edge(staff_train,         harvest_plan)
root.order.add_edge(harvest_plan,        pack_design)
root.order.add_edge(pack_design,         market_test)
root.order.add_edge(market_test,         waste_recycle)