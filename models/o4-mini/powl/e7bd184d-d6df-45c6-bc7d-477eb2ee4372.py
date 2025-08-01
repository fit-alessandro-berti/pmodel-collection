# Generated from: e7bd184d-d6df-45c6-bc7d-477eb2ee4372.json
# Description: This process involves establishing an urban vertical farm within a repurposed industrial building. It starts with site analysis and structural assessment, followed by environmental system design including hydroponics and aeroponics integration. The process continues with procuring specialized lighting and water recycling systems, then installing modular growing racks. Next, seed selection and germination protocols are established alongside nutrient formula calibration. Staff training on automated monitoring and pest management takes place before launching a pilot crop cycle. Data collection and yield optimization conclude the process, ensuring sustainable urban agriculture with minimal environmental impact and maximized crop density in limited space.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
site_analysis     = Transition(label='Site Analysis')
structure_check   = Transition(label='Structure Check')
enviro_design     = Transition(label='Enviro Design')
hydro_setup       = Transition(label='Hydro Setup')
aeroponics_add    = Transition(label='Aeroponics Add')
lighting_procure  = Transition(label='Lighting Procure')
water_recycle     = Transition(label='Water Recycle')
rack_install      = Transition(label='Rack Install')
seed_select       = Transition(label='Seed Select')
germinate_seeds   = Transition(label='Germinate Seeds')
nutrient_mix      = Transition(label='Nutrient Mix')
staff_train       = Transition(label='Staff Train')
pest_control      = Transition(label='Pest Control')
pilot_crop        = Transition(label='Pilot Crop')
data_gather       = Transition(label='Data Gather')
yield_optimize    = Transition(label='Yield Optimize')

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_analysis, structure_check, enviro_design,
    hydro_setup, aeroponics_add,
    lighting_procure, water_recycle,
    rack_install,
    seed_select, germinate_seeds, nutrient_mix,
    staff_train, pest_control,
    pilot_crop, data_gather, yield_optimize
])

# Sequential flow: site analysis -> structure check -> environmental design
root.order.add_edge(site_analysis, structure_check)
root.order.add_edge(structure_check, enviro_design)

# After design, hydroponics and aeroponics in parallel
root.order.add_edge(enviro_design, hydro_setup)
root.order.add_edge(enviro_design, aeroponics_add)

# Lighting and water procurement wait for both hydro and aeroponics
root.order.add_edge(hydro_setup, lighting_procure)
root.order.add_edge(aeroponics_add, lighting_procure)
root.order.add_edge(hydro_setup, water_recycle)
root.order.add_edge(aeroponics_add, water_recycle)

# Rack installation after lighting and water systems
root.order.add_edge(lighting_procure, rack_install)
root.order.add_edge(water_recycle, rack_install)

# Seed selection and nutrient mixing after rack install
root.order.add_edge(rack_install, seed_select)
root.order.add_edge(rack_install, nutrient_mix)
# Germination after seed selection
root.order.add_edge(seed_select, germinate_seeds)

# Staff training and pest control after germination & nutrient mix
root.order.add_edge(germinate_seeds, staff_train)
root.order.add_edge(nutrient_mix, staff_train)
root.order.add_edge(germinate_seeds, pest_control)
root.order.add_edge(nutrient_mix, pest_control)

# Pilot crop after staff training and pest control
root.order.add_edge(staff_train, pilot_crop)
root.order.add_edge(pest_control, pilot_crop)

# Data gathering and yield optimization
root.order.add_edge(pilot_crop, data_gather)
root.order.add_edge(data_gather, yield_optimize)