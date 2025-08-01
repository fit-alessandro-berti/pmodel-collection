# Generated from: e41ae81c-ecbc-4dbb-9787-6afd0dba5661.json
# Description: This process outlines the establishment of an urban vertical farming facility within a repurposed multi-story building. It involves site evaluation, structural modifications to support hydroponic systems, installation of climate control technologies, and integration of AI-driven monitoring tools. The procedure further includes sourcing organic seeds, setting up nutrient delivery systems, training staff on crop management, and establishing supply chain logistics tailored for fresh produce delivery in dense urban markets. Continuous optimization cycles are incorporated to maximize yield and sustainability while minimizing resource consumption and environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
site_survey = Transition(label='Site Survey')
structure_reinforce = Transition(label='Structure Reinforce')
hydroponic_setup = Transition(label='Hydroponic Setup')
climate_install = Transition(label='Climate Install')
ai_integration = Transition(label='AI Integration')
seed_sourcing = Transition(label='Seed Sourcing')
nutrient_prep = Transition(label='Nutrient Prep')
system_testing = Transition(label='System Testing')
staff_training = Transition(label='Staff Training')
crop_planting = Transition(label='Crop Planting')

growth_monitor = Transition(label='Growth Monitor')
pest_control = Transition(label='Pest Control')
harvest_schedule = Transition(label='Harvest Schedule')
quality_check = Transition(label='Quality Check')
market_dispatch = Transition(label='Market Dispatch')
waste_recycle = Transition(label='Waste Recycle')
data_analysis = Transition(label='Data Analysis')

# Silent transition for loop exit
skip = SilentTransition()

# Define the optimization loop body: one cycle of monitoring, control, harvest, etc.
iteration_po = StrictPartialOrder(nodes=[
    growth_monitor, pest_control, harvest_schedule,
    quality_check, market_dispatch, waste_recycle, data_analysis
])
iteration_po.order.add_edge(growth_monitor, pest_control)
iteration_po.order.add_edge(pest_control, harvest_schedule)
iteration_po.order.add_edge(harvest_schedule, quality_check)
iteration_po.order.add_edge(quality_check, market_dispatch)
iteration_po.order.add_edge(market_dispatch, waste_recycle)
iteration_po.order.add_edge(waste_recycle, data_analysis)

# Loop: repeat the iteration body until exit
optimization_loop = OperatorPOWL(operator=Operator.LOOP, children=[iteration_po, skip])

# Build the main process partial order
root = StrictPartialOrder(nodes=[
    site_survey, structure_reinforce, hydroponic_setup, climate_install,
    ai_integration, seed_sourcing, nutrient_prep, system_testing,
    staff_training, crop_planting, optimization_loop
])
root.order.add_edge(site_survey, structure_reinforce)
root.order.add_edge(structure_reinforce, hydroponic_setup)
root.order.add_edge(hydroponic_setup, climate_install)
root.order.add_edge(climate_install, ai_integration)
root.order.add_edge(ai_integration, seed_sourcing)
root.order.add_edge(seed_sourcing, nutrient_prep)
root.order.add_edge(nutrient_prep, system_testing)
root.order.add_edge(system_testing, staff_training)
root.order.add_edge(staff_training, crop_planting)
root.order.add_edge(crop_planting, optimization_loop)