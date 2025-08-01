# Generated from: 87e0ba80-3d37-4eee-80ae-bc3dc971130a.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farming system within a repurposed industrial building. It starts with site evaluation and environmental analysis, followed by modular farm design and infrastructure retrofitting. Subsequent activities include hydroponic system installation, automated climate control setup, nutrient solution calibration, and crop selection based on urban demand analytics. The process further involves staff training for system operation, IoT sensor integration for real-time monitoring, pest control strategy implementation, and energy consumption optimization. It concludes with market launch preparations, ongoing yield assessment, and iterative process improvements to ensure sustainable, high-efficiency urban food production in constrained spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_eval = Transition(label='Site Eval')
env_analysis = Transition(label='Env Analysis')
design_modules = Transition(label='Design Modules')
retrofit_build = Transition(label='Retrofit Build')
install_hydroponics = Transition(label='Install Hydroponics')
setup_climate = Transition(label='Setup Climate')
calibrate_nutrients = Transition(label='Calibrate Nutrients')
select_crops = Transition(label='Select Crops')
train_staff = Transition(label='Train Staff')
integrate_sensors = Transition(label='Integrate Sensors')
implement_pest = Transition(label='Implement Pest')
optimize_energy = Transition(label='Optimize Energy')
launch_market = Transition(label='Launch Market')

# Loop for ongoing assessment and improvement
assess_yield = Transition(label='Assess Yield')
improve_process = Transition(label='Improve Process')
loop = OperatorPOWL(operator=Operator.LOOP, children=[assess_yield, improve_process])

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_eval,
    env_analysis,
    design_modules,
    retrofit_build,
    install_hydroponics,
    setup_climate,
    calibrate_nutrients,
    select_crops,
    train_staff,
    integrate_sensors,
    implement_pest,
    optimize_energy,
    launch_market,
    loop
])

# Define control-flow dependencies
root.order.add_edge(site_eval, env_analysis)
root.order.add_edge(env_analysis, design_modules)
root.order.add_edge(design_modules, retrofit_build)
root.order.add_edge(retrofit_build, install_hydroponics)
root.order.add_edge(install_hydroponics, setup_climate)
root.order.add_edge(setup_climate, calibrate_nutrients)
root.order.add_edge(calibrate_nutrients, select_crops)
root.order.add_edge(select_crops, train_staff)
root.order.add_edge(train_staff, integrate_sensors)
root.order.add_edge(integrate_sensors, implement_pest)
root.order.add_edge(implement_pest, optimize_energy)
root.order.add_edge(optimize_energy, launch_market)
root.order.add_edge(launch_market, loop)  # start the iterative assessment loop