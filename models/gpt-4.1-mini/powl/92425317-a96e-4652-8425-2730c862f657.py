# Generated from: 92425317-a96e-4652-8425-2730c862f657.json
# Description: This process outlines the comprehensive steps involved in establishing an urban vertical farming system within a repurposed industrial building. The workflow begins with site analysis and environmental assessment, followed by modular farm design, nutrient solution formulation, and system integration of hydroponics and aeroponics. It includes procurement of specialized lighting, sensor calibration, and automation programming for climate control. Subsequent activities involve crop selection based on market trends, seedling propagation, and installation of water recycling mechanisms. Continuous monitoring, pest management using biological controls, and yield forecasting are also integral. The process concludes with packaging design, supply chain coordination, and community engagement to promote sustainable urban agriculture.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
# Define all activities as transitions
site_analysis = Transition(label='Site Analysis')
env_assessment = Transition(label='Env Assessment')
modular_design = Transition(label='Modular Design')
nutrient_mix = Transition(label='Nutrient Mix')
system_setup = Transition(label='System Setup')
lighting_install = Transition(label='Lighting Install')
sensor_setup = Transition(label='Sensor Setup')
automation_prog = Transition(label='Automation Prog')
crop_selection = Transition(label='Crop Selection')
seedling_start = Transition(label='Seedling Start')
water_recycle = Transition(label='Water Recycle')
pest_control = Transition(label='Pest Control')
yield_forecast = Transition(label='Yield Forecast')
packaging_plan = Transition(label='Packaging Plan')
supply_sync = Transition(label='Supply Sync')
community_out = Transition(label='Community Out')

# Build partial order with correctness in control flow and concurrency.
# The description is linear mostly, but some parts can be concurrent:
# For instance, Lighting Install, Sensor Setup and Automation Prog can be done after System Setup, possibly concurrently.

# Construct the PO
nodes = [
    site_analysis,
    env_assessment,
    modular_design,
    nutrient_mix,
    system_setup,
    lighting_install,
    sensor_setup,
    automation_prog,
    crop_selection,
    seedling_start,
    water_recycle,
    pest_control,
    yield_forecast,
    packaging_plan,
    supply_sync,
    community_out
]

root = StrictPartialOrder(nodes=nodes)

# Add ordering edges as per description

# Site Analysis --> Env Assessment --> Modular Design
root.order.add_edge(site_analysis, env_assessment)
root.order.add_edge(env_assessment, modular_design)

# Modular Design --> Nutrient Mix --> System Setup
root.order.add_edge(modular_design, nutrient_mix)
root.order.add_edge(nutrient_mix, system_setup)

# After System Setup:
# Lighting Install, Sensor Setup, Automation Prog happen; described as sequential but can be concurrent?
# The text says "procurement of specialized lighting, sensor calibration, and automation programming..."
# Interpreted possibly parallel after System Setup because they are distinct setup tasks
root.order.add_edge(system_setup, lighting_install)
root.order.add_edge(system_setup, sensor_setup)
root.order.add_edge(system_setup, automation_prog)
# no order edges among lighting_install, sensor_setup and automation_prog to allow concurrency

# After these three, Crop Selection --> Seedling Start --> Water Recycle
# The description suggests sequence so:
# Assume Crop Selection after lighting_install, sensor_setup and automation_prog finish
# So all three must finish before Crop Selection, so:
root.order.add_edge(lighting_install, crop_selection)
root.order.add_edge(sensor_setup, crop_selection)
root.order.add_edge(automation_prog, crop_selection)

root.order.add_edge(crop_selection, seedling_start)
root.order.add_edge(seedling_start, water_recycle)

# Pest Control and Yield Forecast are integral after water recycling, can be concurrent
root.order.add_edge(water_recycle, pest_control)
root.order.add_edge(water_recycle, yield_forecast)
# no order edge between pest_control and yield_forecast (concurrent)

# Packaging Plan after pest control and yield forecast (both must finish)
root.order.add_edge(pest_control, packaging_plan)
root.order.add_edge(yield_forecast, packaging_plan)

# Supply Sync after Packaging Plan
root.order.add_edge(packaging_plan, supply_sync)

# Community Outreach last
root.order.add_edge(supply_sync, community_out)