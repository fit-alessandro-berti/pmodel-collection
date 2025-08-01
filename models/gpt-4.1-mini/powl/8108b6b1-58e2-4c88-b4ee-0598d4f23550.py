# Generated from: 8108b6b1-58e2-4c88-b4ee-0598d4f23550.json
# Description: This process involves establishing a multi-level urban vertical farm designed to optimize limited city space for sustainable food production. It includes site selection, environmental analysis, modular system design, hydroponic installation, nutrient calibration, lighting optimization, climate control integration, pest monitoring, crop scheduling, yield tracking, waste recycling, energy management, market alignment, and community engagement to ensure efficient operation and social acceptance in urban environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_selection = Transition(label='Site Selection')
env_analysis = Transition(label='Env Analysis')
modular_design = Transition(label='Modular Design')
hydroponic_setup = Transition(label='Hydroponic Setup')
nutrient_calibrate = Transition(label='Nutrient Calibrate')
light_optimize = Transition(label='Light Optimize')
climate_control = Transition(label='Climate Control')
pest_monitor = Transition(label='Pest Monitor')
crop_schedule = Transition(label='Crop Schedule')
yield_track = Transition(label='Yield Track')
waste_recycle = Transition(label='Waste Recycle')
energy_manage = Transition(label='Energy Manage')
market_align = Transition(label='Market Align')
community_engage = Transition(label='Community Engage')
system_audit = Transition(label='System Audit')

# Partial order representing the workflow
# According to process description and logical sequencing:
# Site Selection --> Env Analysis --> Modular Design
# Modular Design --> Hydroponic Setup --> Nutrient Calibrate
# Nutrient Calibrate --> Light Optimize --> Climate Control
# Climate Control --> Pest Monitor (monitor ongoing)
# Parallel post pest monitoring activities:
# Crop Schedule and Energy Manage can proceed concurrently
# Yield Track follows Crop Schedule
# Waste Recycle follows Yield Track and Energy Manage
# Market Align and Community Engage after Waste Recycle
# System Audit at the very end

root = StrictPartialOrder(
    nodes=[
        site_selection, env_analysis, modular_design,
        hydroponic_setup, nutrient_calibrate, light_optimize, climate_control,
        pest_monitor,
        crop_schedule, yield_track,
        waste_recycle,
        energy_manage,
        market_align, community_engage,
        system_audit
    ]
)

order = root.order
order.add_edge(site_selection, env_analysis)
order.add_edge(env_analysis, modular_design)

order.add_edge(modular_design, hydroponic_setup)
order.add_edge(hydroponic_setup, nutrient_calibrate)

order.add_edge(nutrient_calibrate, light_optimize)
order.add_edge(light_optimize, climate_control)

order.add_edge(climate_control, pest_monitor)

# After pest_monitor, crop_schedule and energy_manage run in parallel
order.add_edge(pest_monitor, crop_schedule)
order.add_edge(pest_monitor, energy_manage)

order.add_edge(crop_schedule, yield_track)

# Waste recycle depends on yield_track and energy_manage (join point)
order.add_edge(yield_track, waste_recycle)
order.add_edge(energy_manage, waste_recycle)

order.add_edge(waste_recycle, market_align)
order.add_edge(waste_recycle, community_engage)

# Both market_align and community_engage precede system_audit (join point)
order.add_edge(market_align, system_audit)
order.add_edge(community_engage, system_audit)