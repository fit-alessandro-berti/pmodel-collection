# Generated from: f20af8b1-f5f7-4b87-950c-920f47f8455d.json
# Description: This process outlines the comprehensive steps required to establish an urban vertical farm within a city environment. It begins with site evaluation and environmental analysis to determine optimal conditions, followed by modular infrastructure assembly and hydroponic system installation. Subsequent activities include seed selection tailored to urban microclimates, nutrient solution formulation, and automated climate control calibration. Crop monitoring integrates sensor data and AI predictions to refine growth parameters. Post-harvest handling involves automated sorting, packaging, and distribution logistics designed for rapid delivery to local markets. The process also incorporates sustainability audits and energy consumption optimization to ensure minimal environmental impact while maximizing yield and profitability in confined urban spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activity transitions
site_survey        = Transition(label='Site Survey')
env_analysis       = Transition(label='Env Analysis')
modular_build      = Transition(label='Modular Build')
hydroponic_setup   = Transition(label='Hydroponic Setup')
seed_select        = Transition(label='Seed Select')
nutrient_prep      = Transition(label='Nutrient Prep')
climate_calibrate  = Transition(label='Climate Calibrate')
sensor_install     = Transition(label='Sensor Install')
ai_integration     = Transition(label='AI Integration')
crop_monitor       = Transition(label='Crop Monitor')
growth_adjust      = Transition(label='Growth Adjust')
harvest_sort       = Transition(label='Harvest Sort')
packaging          = Transition(label='Packaging')
distribution_plan  = Transition(label='Distribution Plan')
sustain_audit      = Transition(label='Sustain Audit')
energy_optimize    = Transition(label='Energy Optimize')

# Loop for continuous monitoring and adjustment
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[crop_monitor, growth_adjust]
)

# Assemble the partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    env_analysis,
    modular_build,
    hydroponic_setup,
    seed_select,
    nutrient_prep,
    climate_calibrate,
    sensor_install,
    ai_integration,
    monitor_loop,
    harvest_sort,
    packaging,
    distribution_plan,
    sustain_audit,
    energy_optimize
])

# Define the control-flow dependencies
root.order.add_edge(site_survey,       env_analysis)
root.order.add_edge(env_analysis,      modular_build)
root.order.add_edge(modular_build,     hydroponic_setup)
root.order.add_edge(hydroponic_setup,  seed_select)
root.order.add_edge(seed_select,       nutrient_prep)
root.order.add_edge(nutrient_prep,     climate_calibrate)

# Sensor install and AI integration can proceed in parallel after calibration
root.order.add_edge(climate_calibrate, sensor_install)
root.order.add_edge(climate_calibrate, ai_integration)

# Both sensor and AI must complete before entering the monitoring loop
root.order.add_edge(sensor_install,    monitor_loop)
root.order.add_edge(ai_integration,    monitor_loop)

# After monitoring loop, proceed to harvest and post-harvest tasks
root.order.add_edge(monitor_loop,      harvest_sort)
root.order.add_edge(harvest_sort,      packaging)
root.order.add_edge(packaging,         distribution_plan)

# Final audits and optimizations run in parallel after distribution planning
root.order.add_edge(distribution_plan, sustain_audit)
root.order.add_edge(distribution_plan, energy_optimize)