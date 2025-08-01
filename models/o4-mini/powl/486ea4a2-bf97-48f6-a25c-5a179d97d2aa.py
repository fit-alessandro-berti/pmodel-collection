# Generated from: 486ea4a2-bf97-48f6-a25c-5a179d97d2aa.json
# Description: This process outlines the comprehensive steps involved in establishing an urban vertical farming operation within a constrained city environment. It includes securing appropriate permits, designing modular farm units, sourcing sustainable materials, implementing automated hydroponic systems, integrating IoT sensors for environmental monitoring, training specialized staff, establishing supply chain contracts for organic seeds and nutrients, conducting iterative growth trials, optimizing energy usage with renewable sources, setting up waste recycling for zero discharge, marketing niche urban produce, ensuring compliance with health regulations, and deploying a digital platform to manage farm operations and customer orders. The process demands cross-functional coordination across urban planning, agriculture technology, environmental science, and business development to successfully launch a profitable and sustainable vertical farm.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
permit = Transition(label='Permit Acquisition')
survey = Transition(label='Site Survey')
design = Transition(label='Design Layout')
sourcing = Transition(label='Material Sourcing')
assembly = Transition(label='System Assembly')
iot = Transition(label='IoT Integration')
training = Transition(label='Staff Training')
seed = Transition(label='Seed Procurement')
contracts = Transition(label='Supply Contracts')
growth = Transition(label='Growth Trials')
energy = Transition(label='Energy Optimization')
waste = Transition(label='Waste Recycling')
check = Transition(label='Regulation Check')
marketing = Transition(label='Marketing Launch')
platform = Transition(label='Platform Deployment')
onboarding = Transition(label='Customer Onboarding')
review = Transition(label='Performance Review')

# Define the loop body for iterative growth optimization
loop_body = StrictPartialOrder(nodes=[energy, waste, check])
# energy, waste, and regulation check can proceed concurrently in each iteration

# Define the growth trial loop: perform a growth trial, then optionally do optimization loop and repeat
growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth, loop_body])

# Assemble the root partial order
root = StrictPartialOrder(nodes=[
    permit, survey, design, sourcing,
    assembly, iot, training, contracts, seed,
    growth_loop,
    marketing, platform, onboarding, review
])

# Specify the control-flow dependencies
root.order.add_edge(permit, survey)
root.order.add_edge(survey, design)
root.order.add_edge(design, sourcing)
root.order.add_edge(sourcing, assembly)
root.order.add_edge(assembly, iot)

# After system assembly and IoT integration, set up staff, contracts, and seeds in parallel
root.order.add_edge(iot, training)
root.order.add_edge(iot, contracts)
root.order.add_edge(iot, seed)

# All three must complete before starting the growth loop
root.order.add_edge(training, growth_loop)
root.order.add_edge(contracts, growth_loop)
root.order.add_edge(seed, growth_loop)

# After completing the iterative growth loop, proceed to launch and deployment activities
root.order.add_edge(growth_loop, marketing)
root.order.add_edge(marketing, platform)
root.order.add_edge(platform, onboarding)
root.order.add_edge(onboarding, review)