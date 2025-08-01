# Generated from: 36a352e8-78eb-489e-8ea7-7719b7de69ce.json
# Description: This process outlines the comprehensive cycle of urban vertical farming, integrating advanced hydroponics, automated nutrient delivery, and environmental controls to maximize crop yield in limited city spaces. It involves seed selection, germination monitoring, nutrient mixing, growth tracking, pest control, harvesting automation, and waste recycling. Data from IoT sensors continuously optimize conditions for plant health, while logistics ensure fresh produce distribution within tight urban supply chains. The process also includes energy management for sustainable operation and post-harvest quality assessment to maintain food safety standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
seed_selection    = Transition(label='Seed Selection')
germination_check = Transition(label='Germination Check')
nutrient_mix      = Transition(label='Nutrient Mix')
planting_setup    = Transition(label='Planting Setup')
environment_adjust= Transition(label='Environment Adjust')
growth_monitor    = Transition(label='Growth Monitor')
pest_inspection   = Transition(label='Pest Inspection')
irrigation_control= Transition(label='Irrigation Control')
light_calibration = Transition(label='Light Calibration')
harvest_schedule  = Transition(label='Harvest Schedule')
automated_picking = Transition(label='Automated Picking')
waste_sorting     = Transition(label='Waste Sorting')
energy_audit      = Transition(label='Energy Audit')
quality_assess    = Transition(label='Quality Assess')
produce_packing   = Transition(label='Produce Packing')
supply_dispatch   = Transition(label='Supply Dispatch')

# Define the daily environmental control set as partial order (concurrent)
daily_controls = StrictPartialOrder(nodes=[
    growth_monitor,
    pest_inspection,
    irrigation_control,
    light_calibration
])
# no order edges => fully concurrent

# Define the harvest-loop: check schedule, then either exit or do daily controls and repeat
harvest_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[harvest_schedule, daily_controls]
)

# Build the full process as a strict partial order
root = StrictPartialOrder(nodes=[
    seed_selection,
    germination_check,
    nutrient_mix,
    planting_setup,
    environment_adjust,
    energy_audit,
    harvest_loop,
    automated_picking,
    waste_sorting,
    quality_assess,
    produce_packing,
    supply_dispatch
])

# Add sequential control-flow edges
root.order.add_edge(seed_selection,    germination_check)
root.order.add_edge(germination_check, nutrient_mix)
root.order.add_edge(nutrient_mix,      planting_setup)
root.order.add_edge(planting_setup,    environment_adjust)

# energy audit runs concurrently with the harvesting loop
root.order.add_edge(environment_adjust, energy_audit)
root.order.add_edge(environment_adjust, harvest_loop)

# after loop ends, proceed to picking and downstream steps
root.order.add_edge(harvest_loop,    automated_picking)
root.order.add_edge(automated_picking, waste_sorting)
root.order.add_edge(waste_sorting,     quality_assess)
root.order.add_edge(quality_assess,    produce_packing)
root.order.add_edge(produce_packing,   supply_dispatch)