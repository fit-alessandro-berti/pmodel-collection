# Generated from: 7625c203-e639-411c-913f-b538f72bc756.json
# Description: This process involves the comprehensive management of an urban vertical farm, integrating hydroponic cultivation, environmental controls, resource recycling, and community engagement. The cycle begins with seed selection and preparation, followed by nutrient solution formulation and automated planting. Continuous monitoring adjusts lighting and humidity to optimize growth. Harvesting is coordinated with quality assessment and packaging. Waste biomass is processed into compost or bioenergy, closing the sustainability loop. Concurrently, data analytics drive yield optimization while educational workshops engage local communities. The process concludes with distribution logistics tailored for urban markets and feedback integration for continuous improvement.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
seed_prep      = Transition(label='Seed Prep')
nutr_mix       = Transition(label='Nutrient Mix')
auto_plant     = Transition(label='Automated Plant')
env_mon        = Transition(label='Env Monitor')
light_adj      = Transition(label='Light Adjust')
hum_con        = Transition(label='Humidity Control')
growth_chk     = Transition(label='Growth Check')
harvest_plan   = Transition(label='Harvest Plan')
quality_test   = Transition(label='Quality Test')
waste_process  = Transition(label='Waste Process')
compost_create = Transition(label='Compost Create')
data_analyze   = Transition(label='Data Analyze')
workshop_host  = Transition(label='Workshop Host')
market_pack    = Transition(label='Market Pack')
distribute_goods = Transition(label='Distribute Goods')

# Silent transitions for loop and waste‐choice
skip_loop  = SilentTransition()
skip_waste = SilentTransition()

# Build the growth‐monitoring cycle: Env Monitor → {Light Adjust, Humidity Control} → Growth Check
cycle = StrictPartialOrder(nodes=[env_mon, light_adj, hum_con, growth_chk])
cycle.order.add_edge(env_mon, light_adj)
cycle.order.add_edge(env_mon, hum_con)
cycle.order.add_edge(light_adj, growth_chk)
cycle.order.add_edge(hum_con, growth_chk)

# LOOP around that cycle: do cycle, then optionally repeat via a silent transition
loop_node = OperatorPOWL(operator=Operator.LOOP, children=[cycle, skip_loop])

# XOR for waste processing: either create compost or take the bioenergy branch (silent)
waste_xor = OperatorPOWL(operator=Operator.XOR, children=[compost_create, skip_waste])

# Root partial order with all nodes and cross‐dependencies
root = StrictPartialOrder(
    nodes=[
        # initial sequence
        seed_prep, nutr_mix, auto_plant,
        # the growth loop
        loop_node,
        # harvesting & packaging
        harvest_plan, quality_test, market_pack,
        # distribution of goods
        distribute_goods,
        # waste processing branch
        waste_process, waste_xor,
        # concurrent stakeholder activities
        data_analyze, workshop_host
    ]
)

# Sequence edges
root.order.add_edge(seed_prep, nutr_mix)
root.order.add_edge(nutr_mix, auto_plant)
root.order.add_edge(auto_plant, loop_node)
root.order.add_edge(loop_node, harvest_plan)
root.order.add_edge(harvest_plan, quality_test)
root.order.add_edge(quality_test, market_pack)

# Post‐packaging branches
root.order.add_edge(market_pack, distribute_goods)
root.order.add_edge(market_pack, waste_process)
root.order.add_edge(waste_process, waste_xor)
root.order.add_edge(market_pack, data_analyze)
root.order.add_edge(market_pack, workshop_host)