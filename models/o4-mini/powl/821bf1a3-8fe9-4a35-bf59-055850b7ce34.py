# Generated from: 821bf1a3-8fe9-4a35-bf59-055850b7ce34.json
# Description: This process outlines the comprehensive steps involved in establishing a fully operational urban vertical farm within a repurposed industrial building. It includes activities from initial site assessment, modular system design, and environmental simulation to crop selection, nutrient cycling optimization, and integrated pest management. The process also covers automation integration, energy efficiency calibration, and community engagement for sustainable urban agriculture. Continuous monitoring and adaptive control ensure maximized yield and minimal resource consumption in a confined urban environment, creating a scalable and eco-friendly food production model.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL Transitions
site_survey      = Transition(label='Site Survey')
load_analysis    = Transition(label='Load Analysis')
system_design    = Transition(label='System Design')
env_simulation   = Transition(label='Env Simulation')
crop_select      = Transition(label='Crop Select')
seed_prep        = Transition(label='Seed Prep')
nutrient_mix     = Transition(label='Nutrient Mix')
module_setup     = Transition(label='Module Setup')
irrigation_tune  = Transition(label='Irrigation Tune')
lighting_adjust  = Transition(label='Lighting Adjust')
pest_control     = Transition(label='Pest Control')
energy_audit     = Transition(label='Energy Audit')
automation_sync  = Transition(label='Automation Sync')

yield_monitor    = Transition(label='Yield Monitor')
data_review      = Transition(label='Data Review')
waste_cycle      = Transition(label='Waste Cycle')
community_meet   = Transition(label='Community Meet')
system_upgrade   = Transition(label='System Upgrade')

# Define the monitoring-and-adaptation sequence as a partial order
monitor_seq = StrictPartialOrder(
    nodes=[yield_monitor, data_review, waste_cycle, community_meet, system_upgrade]
)
monitor_seq.order.add_edge(yield_monitor, data_review)
monitor_seq.order.add_edge(data_review, waste_cycle)
monitor_seq.order.add_edge(waste_cycle, community_meet)
monitor_seq.order.add_edge(community_meet, system_upgrade)

# Build a LOOP node: do one monitor_seq, then either exit or do monitor_seq again, etc.
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[monitor_seq, monitor_seq]
)

# Build the overall process: initial setup sequence, then enter the monitoring loop
root = StrictPartialOrder(nodes=[
    site_survey, load_analysis, system_design, env_simulation,
    crop_select, seed_prep, nutrient_mix, module_setup,
    irrigation_tune, lighting_adjust, pest_control,
    energy_audit, automation_sync, monitor_loop
])

# Add edges for the setup sequence
root.order.add_edge(site_survey, load_analysis)
root.order.add_edge(load_analysis, system_design)
root.order.add_edge(system_design, env_simulation)
root.order.add_edge(env_simulation, crop_select)
root.order.add_edge(crop_select, seed_prep)
root.order.add_edge(seed_prep, nutrient_mix)
root.order.add_edge(nutrient_mix, module_setup)
root.order.add_edge(module_setup, irrigation_tune)
root.order.add_edge(irrigation_tune, lighting_adjust)
root.order.add_edge(lighting_adjust, pest_control)
root.order.add_edge(pest_control, energy_audit)
root.order.add_edge(energy_audit, automation_sync)

# Edge from the last setup activity into the monitoring loop
root.order.add_edge(automation_sync, monitor_loop)