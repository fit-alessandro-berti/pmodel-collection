# Generated from: b0c5e5a6-ecb6-4c96-ae43-b8b33bd457ec.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farming system within a repurposed industrial building. It includes site analysis, modular system design, integration of hydroponic and aeroponic technologies, environmental control calibration, nutrient solution preparation, automated seeding, growth monitoring through IoT sensors, pest management using biological agents, data-driven yield optimization, energy consumption balancing with renewable sources, and final product packaging for local distribution. The process demands multidisciplinary coordination between architects, agronomists, engineers, and supply chain managers to ensure sustainability, efficiency, and scalability within a constrained urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site         = Transition(label='Site Survey')
design       = Transition(label='Design Layout')
tech         = Transition(label='Tech Integration')
env          = Transition(label='Env Control')
nutrient     = Transition(label='Nutrient Mix')
seed         = Transition(label='Seed Automation')
monitor      = Transition(label='Growth Monitor')
pest         = Transition(label='Pest Control')
analysis     = Transition(label='Data Analysis')
energy       = Transition(label='Energy Balance')
harvest      = Transition(label='Harvest Plan')
packaging    = Transition(label='Packaging Prep')
supply_chain = Transition(label='Supply Chain')
audit        = Transition(label='Quality Audit')
market       = Transition(label='Market Launch')

# Concurrency of monitoring, pest control, data analysis, and energy balancing
concurrent_ops = StrictPartialOrder(nodes=[monitor, pest, analysis, energy])

# Build the overall partial order
root = StrictPartialOrder(
    nodes=[
        site,
        design,
        tech,
        env,
        nutrient,
        seed,
        concurrent_ops,
        harvest,
        packaging,
        supply_chain,
        audit,
        market
    ]
)

# Sequential dependencies
root.order.add_edge(site, design)
root.order.add_edge(design, tech)
root.order.add_edge(tech, env)
root.order.add_edge(env, nutrient)
root.order.add_edge(nutrient, seed)
root.order.add_edge(seed, concurrent_ops)
root.order.add_edge(concurrent_ops, harvest)
root.order.add_edge(harvest, packaging)
root.order.add_edge(packaging, supply_chain)
root.order.add_edge(supply_chain, audit)
root.order.add_edge(audit, market)