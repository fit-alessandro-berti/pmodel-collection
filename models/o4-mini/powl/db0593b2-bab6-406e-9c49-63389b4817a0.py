# Generated from: db0593b2-bab6-406e-9c49-63389b4817a0.json
# Description: This process outlines the establishment of an urban vertical farming system within a repurposed industrial building. It involves site assessment, environmental analysis, modular structure installation, automated irrigation setup, crop selection based on local demand and climate simulation, nutrient solution formulation, lighting system calibration, pest monitoring using AI-driven sensors, staff training on hydroponic techniques, integration of renewable energy sources, real-time data analytics implementation for crop health, waste recycling strategy, marketing channel development for fresh produce, and continuous process optimization to maximize yield while minimizing resource consumption and environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define atomic activities
site_assess        = Transition(label="Site Assess")
env_analysis      = Transition(label="Env Analysis")
modular_install   = Transition(label="Modular Install")
irrigation_setup  = Transition(label="Irrigation Setup")
climate_simulate  = Transition(label="Climate Simulate")
crop_selection    = Transition(label="Crop Selection")
nutrient_mix      = Transition(label="Nutrient Mix")
lighting_calibrate= Transition(label="Lighting Calibrate")
pest_monitor      = Transition(label="Pest Monitor")
staff_training    = Transition(label="Staff Training")
energy_integrate  = Transition(label="Energy Integrate")
data_analytics    = Transition(label="Data Analytics")
waste_recycle     = Transition(label="Waste Recycle")
market_develop    = Transition(label="Market Develop")
yield_optimize    = Transition(label="Yield Optimize")

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    site_assess, env_analysis, modular_install, irrigation_setup,
    climate_simulate, crop_selection,
    nutrient_mix, lighting_calibrate, pest_monitor, staff_training,
    energy_integrate, data_analytics, waste_recycle, market_develop,
    yield_optimize
])

# Sequential ordering for initial assessment and setup
root.order.add_edge(site_assess,       env_analysis)
root.order.add_edge(env_analysis,     modular_install)
root.order.add_edge(modular_install,  irrigation_setup)
root.order.add_edge(irrigation_setup, climate_simulate)
root.order.add_edge(climate_simulate, crop_selection)

# After crop selection, the preparatory tasks can proceed concurrently
for preparatory in [
    nutrient_mix, lighting_calibrate, pest_monitor, staff_training,
    energy_integrate, data_analytics, waste_recycle, market_develop
]:
    root.order.add_edge(crop_selection, preparatory)
    # after each preparatory activity, feed into optimization
    root.order.add_edge(preparatory, yield_optimize)

# The final optimization step
# (no outgoing edges: end of process)