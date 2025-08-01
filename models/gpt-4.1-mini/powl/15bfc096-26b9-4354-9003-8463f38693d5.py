# Generated from: 15bfc096-26b9-4354-9003-8463f38693d5.json
# Description: This process details the establishment of an urban vertical farming system within a repurposed industrial warehouse. It involves site assessment, modular rack installation, climate control calibration, nutrient solution preparation, seed selection and planting, automated monitoring setup, pest management protocols, and harvest scheduling. The process requires integration of IoT sensors for real-time data analysis, energy optimization strategies, waste recycling plans, and distribution logistics coordination to ensure sustainable local food production. Each step demands cross-functional collaboration between agronomists, engineers, and supply chain managers, emphasizing innovation and environmental impact mitigation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions (activities)
site_survey = Transition(label='Site Survey')
rack_install = Transition(label='Rack Install')
climate_setup = Transition(label='Climate Setup')
seed_selection = Transition(label='Seed Selection')
planting_seeds = Transition(label='Planting Seeds')
nutrient_mix = Transition(label='Nutrient Mix')
sensor_deploy = Transition(label='Sensor Deploy')
data_monitor = Transition(label='Data Monitor')
pest_control = Transition(label='Pest Control')
growth_check = Transition(label='Growth Check')
energy_audit = Transition(label='Energy Audit')
waste_cycle = Transition(label='Waste Cycle')
harvest_plan = Transition(label='Harvest Plan')
logistics_prep = Transition(label='Logistics Prep')
quality_test = Transition(label='Quality Test')
market_launch = Transition(label='Market Launch')

# Create partial order representing the overall process flow
# Logical ordering based on descriptions and dependencies:

# Phase 1: Setup and Installation
# Site Survey -> Rack Install -> Climate Setup
phase1 = StrictPartialOrder(nodes=[site_survey, rack_install, climate_setup])
phase1.order.add_edge(site_survey, rack_install)
phase1.order.add_edge(rack_install, climate_setup)

# Phase 2: Nutrient and Seed preparation
# Nutrient Mix runs before seed selection and planting seeds
# Seed Selection -> Planting Seeds
phase2 = StrictPartialOrder(nodes=[nutrient_mix, seed_selection, planting_seeds])
phase2.order.add_edge(nutrient_mix, seed_selection)
phase2.order.add_edge(seed_selection, planting_seeds)

# Phase 3: Sensor deployment and automated monitoring
# Sensor Deploy -> Data Monitor
phase3 = StrictPartialOrder(nodes=[sensor_deploy, data_monitor])
phase3.order.add_edge(sensor_deploy, data_monitor)

# Phase 4: Pest control and growth check loop until harvesting decisions
# Represent loop: Growth Check (check growth) and Pest Control (manage pests) repeat until exit to harvest planning
loop_body = StrictPartialOrder(nodes=[pest_control, growth_check])
loop_body.order.add_edge(pest_control, growth_check)
growth_cycle = OperatorPOWL(operator=Operator.LOOP, children=[growth_check, loop_body])

# Phase 5: Energy audit and waste cycling (can be concurrent)
phase5 = StrictPartialOrder(nodes=[energy_audit, waste_cycle])
# No order between energy audit and waste cycle - concurrent

# Phase 6: Harvest planning and logistics preparation
phase6 = StrictPartialOrder(nodes=[harvest_plan, logistics_prep])
phase6.order.add_edge(harvest_plan, logistics_prep)

# Phase 7: Quality test and final market launch
phase7 = StrictPartialOrder(nodes=[quality_test, market_launch])
phase7.order.add_edge(quality_test, market_launch)

# Assemble the top-level partial order
root = StrictPartialOrder(
    nodes=[
        phase1,
        phase2,
        phase3,
        growth_cycle,
        phase5,
        phase6,
        phase7
    ]
)

# Add edges between phases reflecting logical order/dependencies:
# Phase1 -> Phase2 -> Phase3 -> Growth cycle -> Phase5 -> Phase6 -> Phase7

root.order.add_edge(phase1, phase2)
root.order.add_edge(phase2, phase3)
root.order.add_edge(phase3, growth_cycle)
root.order.add_edge(growth_cycle, phase5)
root.order.add_edge(phase5, phase6)
root.order.add_edge(phase6, phase7)