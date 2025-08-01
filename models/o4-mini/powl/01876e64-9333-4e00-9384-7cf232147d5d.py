# Generated from: 01876e64-9333-4e00-9384-7cf232147d5d.json
# Description: This process outlines the comprehensive steps required to establish and operate an urban vertical farming facility within a repurposed industrial building. It involves initial site analysis, structural modification, installation of climate control and hydroponic systems, integration of IoT sensors for real-time monitoring, seed selection and planting, nutrient delivery optimization, pest management using biological controls, automated harvesting, data-driven yield analysis, packaging, and distribution logistics tailored for local markets. The process emphasizes sustainability through energy-efficient practices and waste recycling, ensuring minimal environmental impact while maximizing crop output and quality in limited urban spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey      = Transition(label='Site Survey')
structural_assess= Transition(label='Structural Assess')
climate_setup    = Transition(label='Climate Setup')
hydroponic_install= Transition(label='Hydroponic Install')
sensor_network   = Transition(label='Sensor Network')
energy_audit     = Transition(label='Energy Audit')
seed_selection   = Transition(label='Seed Selection')
planting_phase   = Transition(label='Planting Phase')
nutrient_mix     = Transition(label='Nutrient Mix')
pest_control     = Transition(label='Pest Control')
growth_monitor   = Transition(label='Growth Monitor')
automated_harvest= Transition(label='Automated Harvest')
yield_analysis   = Transition(label='Yield Analysis')
waste_recycling  = Transition(label='Waste Recycling')
packaging_prep   = Transition(label='Packaging Prep')
local_dispatch   = Transition(label='Local Dispatch')

# Silent transition for loop construct
skip = SilentTransition()

# Body of the growth-monitoring loop: nutrient mix -> pest control -> growth monitor
growth_cycle = StrictPartialOrder(nodes=[nutrient_mix, pest_control, growth_monitor])
growth_cycle.order.add_edge(nutrient_mix, pest_control)
growth_cycle.order.add_edge(pest_control, growth_monitor)

# Loop: repeat the growth cycle until exit
growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[skip, growth_cycle])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey, structural_assess, climate_setup,
    hydroponic_install, sensor_network, energy_audit,
    seed_selection, planting_phase, growth_loop,
    automated_harvest, waste_recycling, yield_analysis,
    packaging_prep, local_dispatch
])

# Define the control-flow/order relations
root.order.add_edge(site_survey, structural_assess)
root.order.add_edge(structural_assess, climate_setup)
root.order.add_edge(climate_setup, hydroponic_install)
root.order.add_edge(hydroponic_install, sensor_network)
root.order.add_edge(climate_setup, energy_audit)

root.order.add_edge(sensor_network, seed_selection)
root.order.add_edge(seed_selection, planting_phase)
root.order.add_edge(planting_phase, growth_loop)

root.order.add_edge(growth_loop, automated_harvest)
root.order.add_edge(automated_harvest, waste_recycling)
root.order.add_edge(automated_harvest, yield_analysis)

root.order.add_edge(waste_recycling, packaging_prep)
root.order.add_edge(yield_analysis, packaging_prep)
root.order.add_edge(packaging_prep, local_dispatch)