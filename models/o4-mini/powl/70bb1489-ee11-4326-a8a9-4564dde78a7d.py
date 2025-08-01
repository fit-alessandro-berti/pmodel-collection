# Generated from: 70bb1489-ee11-4326-a8a9-4564dde78a7d.json
# Description: This process outlines the complex setup and operationalization of an urban vertical farming system that integrates hydroponics, IoT sensors, automated climate control, and waste recycling. The procedure includes site assessment, modular installation, nutrient balancing, real-time monitoring, pest management, and yield optimization. Each phase involves cross-disciplinary collaboration between agronomists, engineers, and data analysts to ensure sustainable production of fresh produce within constrained city spaces, minimizing resource consumption and environmental impact while maximizing output and quality.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey      = Transition(label='Site Survey')
design_layout    = Transition(label='Design Layout')
install_frames   = Transition(label='Install Frames')
setup_hydro      = Transition(label='Setup Hydroponics')
configure_sens   = Transition(label='Configure Sensors')
calibrate_clim   = Transition(label='Calibrate Climate')
nutrient_mix     = Transition(label='Nutrient Mix')
seed_planting    = Transition(label='Seed Planting')
monitor_growth   = Transition(label='Monitor Growth')
adjust_lighting  = Transition(label='Adjust Lighting')
pest_control     = Transition(label='Pest Control')
waste_recycle    = Transition(label='Waste Recycle')
data_analysis    = Transition(label='Data Analysis')
harvest_crops    = Transition(label='Harvest Crops')
quality_check    = Transition(label='Quality Check')
market_dispatch  = Transition(label='Market Dispatch')

# Concurrent operations inside the monitoring loop
concurrent_ops = StrictPartialOrder(
    nodes=[adjust_lighting, pest_control, waste_recycle, data_analysis]
    # no internal edges: all four can happen in parallel
)

# Loop: monitor growth, then optionally do concurrent ops and repeat, else exit
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[monitor_growth, concurrent_ops]
)

# Build the top‐level partial order
root = StrictPartialOrder(
    nodes=[
        site_survey,
        design_layout,
        install_frames,
        setup_hydro,
        configure_sens,
        calibrate_clim,
        nutrient_mix,
        seed_planting,
        monitor_loop,
        harvest_crops,
        quality_check,
        market_dispatch
    ]
)

# Sequence edges for setup and teardown
root.order.add_edge(site_survey,      design_layout)
root.order.add_edge(design_layout,    install_frames)
root.order.add_edge(install_frames,   setup_hydro)
root.order.add_edge(setup_hydro,      configure_sens)
root.order.add_edge(configure_sens,   calibrate_clim)
root.order.add_edge(calibrate_clim,   nutrient_mix)
root.order.add_edge(nutrient_mix,     seed_planting)
root.order.add_edge(seed_planting,    monitor_loop)
root.order.add_edge(monitor_loop,     harvest_crops)
root.order.add_edge(harvest_crops,    quality_check)
root.order.add_edge(quality_check,    market_dispatch)