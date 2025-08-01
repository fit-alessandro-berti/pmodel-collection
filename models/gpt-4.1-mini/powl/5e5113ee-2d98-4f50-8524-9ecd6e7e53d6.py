# Generated from: 5e5113ee-2d98-4f50-8524-9ecd6e7e53d6.json
# Description: This process involves the planning, installation, and optimization of a multi-layer vertical farming system within an urban environment. It begins with site analysis and environmental assessment, followed by modular structure assembly, hydroponic system integration, and LED lighting calibration. Subsequent steps include seed selection, nutrient solution preparation, and automated climate control programming. Throughout the cycle, continuous monitoring, pest management, and data analytics are conducted to ensure optimal growth conditions. The process concludes with harvest scheduling, yield evaluation, and equipment maintenance to sustain long-term productivity in constrained city spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
site_survey = Transition(label='Site Survey')
light_analysis = Transition(label='Light Analysis')
structure_build = Transition(label='Structure Build')
hydro_setup = Transition(label='Hydro Setup')
led_install = Transition(label='LED Install')
seed_select = Transition(label='Seed Select')
nutrient_mix = Transition(label='Nutrient Mix')
climate_program = Transition(label='Climate Program')
sensor_deploy = Transition(label='Sensor Deploy')
growth_monitor = Transition(label='Growth Monitor')
pest_control = Transition(label='Pest Control')
data_logging = Transition(label='Data Logging')
harvest_plan = Transition(label='Harvest Plan')
yield_review = Transition(label='Yield Review')
system_clean = Transition(label='System Clean')

# Define partial orders according to process sequence and concurrency

# Initial analysis: Site Survey --> Light Analysis
init_analysis = StrictPartialOrder(nodes=[site_survey, light_analysis])
init_analysis.order.add_edge(site_survey, light_analysis)

# Modular assembly and installation: Structure Build --> Hydro Setup --> LED Install
assembly_install = StrictPartialOrder(
    nodes=[structure_build, hydro_setup, led_install])
assembly_install.order.add_edge(structure_build, hydro_setup)
assembly_install.order.add_edge(hydro_setup, led_install)

# Seed and nutrient preparation: Seed Select --> Nutrient Mix
seed_nutrient = StrictPartialOrder(nodes=[seed_select, nutrient_mix])
seed_nutrient.order.add_edge(seed_select, nutrient_mix)

# Climate programming: Climate Program (single activity)
climate_prog = climate_program

# Continuous activities done in parallel during growth:
# Sensor Deploy, Growth Monitor, Pest Control, Data Logging
# No ordering between these four (concurrent)
continuous_monitoring = StrictPartialOrder(
    nodes=[sensor_deploy, growth_monitor, pest_control, data_logging])

# Final wrap-up sequence: Harvest Plan --> Yield Review --> System Clean
finalization = StrictPartialOrder(
    nodes=[harvest_plan, yield_review, system_clean])
finalization.order.add_edge(harvest_plan, yield_review)
finalization.order.add_edge(yield_review, system_clean)

# Combine sequences in a global partial order reflecting process flow:
# (init_analysis) --> (assembly_install) --> (seed_nutrient) --> climate_prog --> continuous_monitoring --> finalization

root = StrictPartialOrder(
    nodes=[
        init_analysis,
        assembly_install,
        seed_nutrient,
        climate_prog,
        continuous_monitoring,
        finalization
    ])

root.order.add_edge(init_analysis, assembly_install)
root.order.add_edge(assembly_install, seed_nutrient)
root.order.add_edge(seed_nutrient, climate_prog)
root.order.add_edge(climate_prog, continuous_monitoring)
root.order.add_edge(continuous_monitoring, finalization)