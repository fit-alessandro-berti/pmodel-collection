# Generated from: 5e5113ee-2d98-4f50-8524-9ecd6e7e53d6.json
# Description: This process involves the planning, installation, and optimization of a multi-layer vertical farming system within an urban environment. It begins with site analysis and environmental assessment, followed by modular structure assembly, hydroponic system integration, and LED lighting calibration. Subsequent steps include seed selection, nutrient solution preparation, and automated climate control programming. Throughout the cycle, continuous monitoring, pest management, and data analytics are conducted to ensure optimal growth conditions. The process concludes with harvest scheduling, yield evaluation, and equipment maintenance to sustain long-term productivity in constrained city spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey     = Transition(label='Site Survey')
light_analysis  = Transition(label='Light Analysis')
structure_build = Transition(label='Structure Build')
hydro_setup     = Transition(label='Hydro Setup')
led_install     = Transition(label='LED Install')
seed_select     = Transition(label='Seed Select')
nutrient_mix    = Transition(label='Nutrient Mix')
climate_program = Transition(label='Climate Program')
sensor_deploy   = Transition(label='Sensor Deploy')
growth_monitor  = Transition(label='Growth Monitor')
pest_control    = Transition(label='Pest Control')
data_logging    = Transition(label='Data Logging')
harvest_plan    = Transition(label='Harvest Plan')
yield_review    = Transition(label='Yield Review')
system_clean    = Transition(label='System Clean')

# Build the looping sub‐process: continuous monitoring, pest control, data logging
monitoring_po = StrictPartialOrder(
    nodes=[growth_monitor, pest_control, data_logging]
)
# No ordering => they run concurrently in each iteration

# Use a silent transition as the loop‐exit placeholder
skip = SilentTransition()

# LOOP(operator=LOOP, children=[A, B])
# where A = the concurrent monitoring block,
#       B = skip (so after each iteration, either exit or skip then repeat A)
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[monitoring_po, skip]
)

# Assemble the full process as one big partial order
root = StrictPartialOrder(
    nodes=[
        site_survey,
        light_analysis,
        structure_build,
        hydro_setup,
        led_install,
        seed_select,
        nutrient_mix,
        climate_program,
        sensor_deploy,
        monitor_loop,
        harvest_plan,
        yield_review,
        system_clean
    ]
)

# Add the sequential dependencies
root.order.add_edge(site_survey,     light_analysis)
root.order.add_edge(light_analysis,  structure_build)
root.order.add_edge(structure_build, hydro_setup)
root.order.add_edge(hydro_setup,     led_install)
root.order.add_edge(led_install,     seed_select)
root.order.add_edge(seed_select,     nutrient_mix)
root.order.add_edge(nutrient_mix,    climate_program)
root.order.add_edge(climate_program, sensor_deploy)
root.order.add_edge(sensor_deploy,   monitor_loop)
root.order.add_edge(monitor_loop,    harvest_plan)
root.order.add_edge(harvest_plan,    yield_review)
root.order.add_edge(yield_review,    system_clean)