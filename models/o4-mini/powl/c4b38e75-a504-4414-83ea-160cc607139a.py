# Generated from: c4b38e75-a504-4414-83ea-160cc607139a.json
# Description: This process outlines the establishment of a fully automated urban vertical farm within a repurposed high-rise building. It involves site evaluation, modular system design, climate control calibration, seed selection, hydroponic nutrient optimization, robotic planting, continuous environmental monitoring, pest detection through AI, data-driven growth analysis, automated harvesting, packaging customization, waste recycling integration, energy consumption auditing, and real-time market demand alignment. The goal is to create a sustainable, high-yield farm capable of responding dynamically to urban food supply needs while minimizing ecological footprint and operational costs.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey   = Transition(label='Site Survey')
design_modules = Transition(label='Design Modules')
install_sensors = Transition(label='Install Sensors')
calibrate_climate = Transition(label='Calibrate Climate')
select_seeds  = Transition(label='Select Seeds')
optimize_nutrients = Transition(label='Optimize Nutrients')
deploy_robots = Transition(label='Deploy Robots')
monitor_growth = Transition(label='Monitor Growth')
detect_pests  = Transition(label='Detect Pests')
analyze_data  = Transition(label='Analyze Data')
harvest_crops = Transition(label='Harvest Crops')
customize_pack = Transition(label='Customize Pack')
recycle_waste = Transition(label='Recycle Waste')
audit_energy  = Transition(label='Audit Energy')
align_demand  = Transition(label='Align Demand')

# Pre‐loop setup (site survey through robot deployment)
pre_setup = StrictPartialOrder(nodes=[
    site_survey, design_modules, install_sensors, calibrate_climate,
    select_seeds, optimize_nutrients, deploy_robots
])
pre_setup.order.add_edge(site_survey, design_modules)
pre_setup.order.add_edge(design_modules, install_sensors)
pre_setup.order.add_edge(install_sensors, calibrate_climate)
pre_setup.order.add_edge(calibrate_climate, select_seeds)
pre_setup.order.add_edge(select_seeds, optimize_nutrients)
pre_setup.order.add_edge(optimize_nutrients, deploy_robots)

# Loop body: continuous monitoring, pest detection, data analysis
loop_body = StrictPartialOrder(nodes=[monitor_growth, detect_pests, analyze_data])
loop_body.order.add_edge(monitor_growth, detect_pests)
loop_body.order.add_edge(detect_pests, analyze_data)

# Define the LOOP: do pre_setup once, then repeat loop_body until exit
farm_loop = OperatorPOWL(operator=Operator.LOOP, children=[pre_setup, loop_body])

# After loop: harvest, packaging, then parallel waste‐recycle, energy‐audit, demand‐align
root = StrictPartialOrder(nodes=[
    farm_loop, harvest_crops, customize_pack,
    recycle_waste, audit_energy, align_demand
])
root.order.add_edge(farm_loop, harvest_crops)
root.order.add_edge(harvest_crops, customize_pack)
root.order.add_edge(customize_pack, recycle_waste)
root.order.add_edge(customize_pack, audit_energy)
root.order.add_edge(customize_pack, align_demand)