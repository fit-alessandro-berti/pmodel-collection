# Generated from: e771c32b-3447-4078-be78-99a9a223c7ed.json
# Description: This process outlines the comprehensive steps involved in establishing an urban vertical farming operation within a repurposed warehouse space. It includes site assessment, climate control design, hydroponic system installation, and integration of AI-driven monitoring tools. The process also covers sourcing specialized seeds, nutrient solution formulation, labor training for crop management, and implementation of sustainable energy solutions. Post-installation activities involve trial cultivation cycles, yield analysis, and continuous optimization of environmental parameters to maximize productivity and minimize resource consumption. Additionally, the process addresses regulatory compliance, waste recycling protocols, and community engagement initiatives to promote urban agriculture awareness.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey   = Transition(label='Site Survey')
climate_plan  = Transition(label='Climate Plan')
system_design = Transition(label='System Design')
ai_setup      = Transition(label='AI Setup')
seed_sourcing = Transition(label='Seed Sourcing')
nutrient_mix  = Transition(label='Nutrient Mix')
install_hydro = Transition(label='Install Hydro')
energy_audit  = Transition(label='Energy Audit')
staff_training= Transition(label='Staff Training')
trial_growth  = Transition(label='Trial Growth')
yield_measure = Transition(label='Yield Measure')
optimize_env  = Transition(label='Optimize Environment')
compliance    = Transition(label='Compliance Check')
waste_cycle   = Transition(label='Waste Cycle')
community_meet= Transition(label='Community Meet')
market_study  = Transition(label='Market Study')

# Loop body: trial cycle -> yield measure -> optimize environment
loop_body = StrictPartialOrder(nodes=[trial_growth, yield_measure, optimize_env])
loop_body.order.add_edge(trial_growth, yield_measure)
loop_body.order.add_edge(yield_measure, optimize_env)

# Silent transition for loop repetition
skip = SilentTransition()

# LOOP operator: repeat the trial-yield-optimize cycle until exit
main_loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, skip])

# Assemble the full process as a strict partial order
root = StrictPartialOrder(nodes=[
    site_survey, climate_plan, system_design, ai_setup,
    seed_sourcing, nutrient_mix, install_hydro, energy_audit,
    staff_training, main_loop, compliance, waste_cycle,
    community_meet, market_study
])

# Define the control-flow relations
root.order.add_edge(site_survey,   climate_plan)
root.order.add_edge(climate_plan,  system_design)
root.order.add_edge(system_design, ai_setup)
root.order.add_edge(ai_setup,      seed_sourcing)
root.order.add_edge(seed_sourcing, nutrient_mix)
root.order.add_edge(nutrient_mix,  install_hydro)
root.order.add_edge(install_hydro, energy_audit)
root.order.add_edge(energy_audit,  staff_training)
root.order.add_edge(staff_training,main_loop)
root.order.add_edge(main_loop,     compliance)
root.order.add_edge(compliance,    waste_cycle)
root.order.add_edge(waste_cycle,   community_meet)
root.order.add_edge(waste_cycle,   market_study)