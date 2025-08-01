# Generated from: 5d1785c7-b7a5-4ae9-96f8-8e7bd1e5e8de.json
# Description: This process outlines the comprehensive steps involved in establishing an urban vertical farm in a dense metropolitan area. It includes securing permits, designing modular grow units optimized for limited spaces, integrating automated nutrient delivery systems, and implementing advanced climate controls. The process also covers sourcing heirloom seeds, training staff on hydroponic techniques, and establishing partnerships with local restaurants for produce distribution. Continuous monitoring through IoT sensors ensures optimal plant health, while waste recycling loops convert organic matter into compost. Marketing efforts target eco-conscious consumers, and periodic audits maintain regulatory compliance and sustainability certifications. This atypical process blends agriculture, technology, and urban planning to create a self-sustaining food production ecosystem.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Atomic activities
permit = Transition(label='Permit Securing')
survey = Transition(label='Site Survey')
design = Transition(label='Unit Design')
setup = Transition(label='System Setup')
nutrient = Transition(label='Nutrient Mix')
climate = Transition(label='Climate Tune')
seed = Transition(label='Seed Sourcing')
training = Transition(label='Staff Training')
iot_install = Transition(label='IoT Install')
plant = Transition(label='Planting Phase')
growth = Transition(label='Growth Monitor')
feedback = Transition(label='Feedback Loop')
quality = Transition(label='Quality Audit')
partner = Transition(label='Partner Align')
market = Transition(label='Market Launch')
compliance = Transition(label='Compliance Check')
waste = Transition(label='Waste Cycle')

# Silent transition for loop exit
skip = SilentTransition()

# Subprocess: detailed system setup (System Setup -> Nutrient Mix -> Climate Tune)
system_setup_po = StrictPartialOrder(nodes=[setup, nutrient, climate])
system_setup_po.order.add_edge(setup, nutrient)
system_setup_po.order.add_edge(nutrient, climate)

# Waste recycling loop: repeat Waste Cycle until exit
waste_loop = OperatorPOWL(operator=Operator.LOOP, children=[waste, skip])

# Growth-monitoring feedback loop: Growth Monitor then optionally Feedback Loop, repeat
growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth, feedback])

# Root partial order of the overall process
root = StrictPartialOrder(nodes=[
    permit, survey, design,            # initial approvals & survey
    system_setup_po,                    # system setup subprocess
    seed,                               # seeds sourcing
    training, iot_install,              # staff training & IoT install
    plant,                              # planting
    growth_loop,                        # growth & feedback loop
    waste_loop,                         # waste recycling loop
    quality,                            # quality audit
    partner, market,                    # distribution channels in parallel
    compliance                          # final compliance check
])

# Sequence edges
root.order.add_edge(permit, survey)
root.order.add_edge(survey, design)
root.order.add_edge(design, system_setup_po)
root.order.add_edge(system_setup_po, seed)
root.order.add_edge(seed, training)
root.order.add_edge(seed, iot_install)
root.order.add_edge(training, plant)
root.order.add_edge(iot_install, plant)
root.order.add_edge(plant, growth_loop)
root.order.add_edge(growth_loop, waste_loop)
root.order.add_edge(growth_loop, quality)
root.order.add_edge(quality, partner)
root.order.add_edge(quality, market)
root.order.add_edge(partner, compliance)
root.order.add_edge(market, compliance)