# Generated from: 11676e90-cb77-4ecf-9c0d-bacd872209dc.json
# Description: This process involves establishing a multi-layered vertical farming system within an urban environment to maximize crop yield using limited space. It includes site analysis, modular structure assembly, hydroponic system installation, climate control calibration, nutrient solution formulation, automated lighting scheduling, pest monitoring with AI sensors, periodic crop health assessment, waste recycling integration, data collection for growth optimization, employee training on new technology, and continuous system maintenance to ensure sustainable production and minimal environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_survey       = Transition(label='Site Survey')
design_layout     = Transition(label='Design Layout')
structure_build   = Transition(label='Structure Build')
install_hydro     = Transition(label='Install Hydroponics')
calibrate_climate = Transition(label='Calibrate Climate')
prepare_nutrients = Transition(label='Prepare Nutrients')
set_lighting      = Transition(label='Set Lighting')
deploy_sensors    = Transition(label='Deploy Sensors')
train_staff       = Transition(label='Train Staff')

monitor_pests     = Transition(label='Monitor Pests')
assess_crops      = Transition(label='Assess Crops')
recycle_waste     = Transition(label='Recycle Waste')
collect_data      = Transition(label='Collect Data')
optimize_growth   = Transition(label='Optimize Growth')
maintenance_check = Transition(label='Maintenance Check')

# Initial setup sequence
initial_setup = StrictPartialOrder(nodes=[
    site_survey,
    design_layout,
    structure_build,
    install_hydro,
    calibrate_climate,
    prepare_nutrients,
    set_lighting,
    deploy_sensors,
    train_staff
])
initial_setup.order.add_edge(site_survey, design_layout)
initial_setup.order.add_edge(design_layout, structure_build)
initial_setup.order.add_edge(structure_build, install_hydro)
initial_setup.order.add_edge(install_hydro, calibrate_climate)
initial_setup.order.add_edge(calibrate_climate, prepare_nutrients)
initial_setup.order.add_edge(prepare_nutrients, set_lighting)
initial_setup.order.add_edge(set_lighting, deploy_sensors)
initial_setup.order.add_edge(deploy_sensors, train_staff)

# Repeating maintenance and monitoring tasks
repeat_tasks = StrictPartialOrder(nodes=[
    monitor_pests,
    assess_crops,
    recycle_waste,
    collect_data,
    optimize_growth,
    maintenance_check
])
repeat_tasks.order.add_edge(monitor_pests, assess_crops)
repeat_tasks.order.add_edge(assess_crops, recycle_waste)
repeat_tasks.order.add_edge(recycle_waste, collect_data)
repeat_tasks.order.add_edge(collect_data, optimize_growth)
repeat_tasks.order.add_edge(optimize_growth, maintenance_check)

# Loop: continue doing repeat_tasks until exit
skip = SilentTransition()
maintenance_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[skip, repeat_tasks]
)

# Combine initial setup and the loop
root = StrictPartialOrder(nodes=[initial_setup, maintenance_loop])
root.order.add_edge(initial_setup, maintenance_loop)