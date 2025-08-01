# Generated from: 8108b6b1-58e2-4c88-b4ee-0598d4f23550.json
# Description: This process involves establishing a multi-level urban vertical farm designed to optimize limited city space for sustainable food production. It includes site selection, environmental analysis, modular system design, hydroponic installation, nutrient calibration, lighting optimization, climate control integration, pest monitoring, crop scheduling, yield tracking, waste recycling, energy management, market alignment, and community engagement to ensure efficient operation and social acceptance in urban environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
site_selection   = Transition(label="Site Selection")
env_analysis     = Transition(label="Env Analysis")
modular_design   = Transition(label="Modular Design")
hydroponic_setup = Transition(label="Hydroponic Setup")
nutrient_calib   = Transition(label="Nutrient Calibrate")
light_optimize   = Transition(label="Light Optimize")
climate_control  = Transition(label="Climate Control")
pest_monitor     = Transition(label="Pest Monitor")
crop_schedule    = Transition(label="Crop Schedule")
yield_track      = Transition(label="Yield Track")
waste_recycle    = Transition(label="Waste Recycle")
energy_manage    = Transition(label="Energy Manage")
market_align     = Transition(label="Market Align")
community_engage = Transition(label="Community Engage")
system_audit     = Transition(label="System Audit")

# Build a total-order workflow
nodes = [
    site_selection,
    env_analysis,
    modular_design,
    hydroponic_setup,
    nutrient_calib,
    light_optimize,
    climate_control,
    pest_monitor,
    crop_schedule,
    yield_track,
    waste_recycle,
    energy_manage,
    market_align,
    community_engage,
    system_audit
]

root = StrictPartialOrder(nodes=nodes)
for src, tgt in zip(nodes, nodes[1:]):
    root.order.add_edge(src, tgt)