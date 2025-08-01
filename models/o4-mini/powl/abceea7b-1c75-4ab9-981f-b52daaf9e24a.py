# Generated from: abceea7b-1c75-4ab9-981f-b52daaf9e24a.json
# Description: This process outlines the setup of an urban vertical farming system integrating advanced hydroponics, IoT environmental controls, and renewable energy sources in a compact city environment. It involves site analysis, modular structure assembly, nutrient solution preparation, sensor calibration, automated planting, growth monitoring, pest management through biological agents, and yield forecasting using AI models. The process also includes waste recycling, community engagement for local distribution, and continuous system optimization based on real-time data analytics to maximize crop yield and sustainability within limited urban space.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_survey    = Transition(label='Site Survey')
design_layout  = Transition(label='Design Layout')
structure_build= Transition(label='Structure Build')
install_sensors= Transition(label='Install Sensors')
mix_nutrients  = Transition(label='Mix Nutrients')
calibrate_ctrl = Transition(label='Calibrate Controls')
seed_planting  = Transition(label='Seed Planting')
set_irrigation = Transition(label='Set Irrigation')
monitor_growth = Transition(label='Monitor Growth')
pest_control   = Transition(label='Pest Control')
data_analysis  = Transition(label='Data Analysis')
waste_recycle  = Transition(label='Waste Recycle')
energy_optimize= Transition(label='Energy Optimize')
forecast_yield = Transition(label='Forecast Yield')
community_meet = Transition(label='Community Meet')
system_update  = Transition(label='System Update')

# Body of the continuous optimization loop: these can run in parallel (no internal order)
optimization_body = StrictPartialOrder(
    nodes=[
        monitor_growth,
        pest_control,
        data_analysis,
        waste_recycle,
        energy_optimize
    ]
)
# No edges added: they are concurrent

# Define the loop: do optimization_body, then system_update, repeat or exit
optimization_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[optimization_body, system_update]
)

# Build the top‐level partial order
root = StrictPartialOrder(
    nodes=[
        site_survey,
        design_layout,
        structure_build,
        install_sensors,
        mix_nutrients,
        calibrate_ctrl,
        seed_planting,
        set_irrigation,
        optimization_loop,
        forecast_yield,
        community_meet
    ]
)

# Sequential dependencies for setup
root.order.add_edge(site_survey,    design_layout)
root.order.add_edge(design_layout,  structure_build)
root.order.add_edge(structure_build,install_sensors)
root.order.add_edge(install_sensors,mix_nutrients)
root.order.add_edge(mix_nutrients,  calibrate_ctrl)
root.order.add_edge(calibrate_ctrl, seed_planting)
root.order.add_edge(seed_planting,  set_irrigation)

# Connect setup to the optimization loop
root.order.add_edge(set_irrigation, optimization_loop)

# After looping, forecast and community engagement
root.order.add_edge(optimization_loop, forecast_yield)
root.order.add_edge(forecast_yield,   community_meet)