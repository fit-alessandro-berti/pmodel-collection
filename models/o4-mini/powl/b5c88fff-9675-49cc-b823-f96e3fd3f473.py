# Generated from: b5c88fff-9675-49cc-b823-f96e3fd3f473.json
# Description: This process outlines the complex and multifaceted steps required to launch an urban vertical farming operation within a dense metropolitan area. It involves site selection, environmental impact analysis, technology integration for hydroponics and aeroponics systems, regulatory compliance checks, community stakeholder engagement, and supply chain coordination. The process also includes pilot crop cycles, real-time data monitoring setup, energy optimization, waste recycling protocols, and marketing strategies tailored to urban consumers. Each activity ensures sustainability, efficiency, and scalability while addressing unique urban constraints and opportunities to create a resilient local food production system.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site        = Transition(label='Site Survey')
impact      = Transition(label='Impact Study')
design      = Transition(label='System Design')
tech        = Transition(label='Tech Setup')
reg         = Transition(label='Regulation Check')
stakeholder = Transition(label='Stakeholder Meet')
supply      = Transition(label='Supply Align')
pilot       = Transition(label='Pilot Planting')
crop        = Transition(label='Crop Cycle')
data        = Transition(label='Data Monitor')
energy      = Transition(label='Energy Audit')
waste       = Transition(label='Waste Plan')
feedback    = Transition(label='Feedback Loop')
market      = Transition(label='Market Launch')
scale       = Transition(label='Scale Strategy')

# Build the loop continuation: concurrent monitoring tasks feeding back
b_po = StrictPartialOrder(nodes=[data, energy, waste, feedback])
b_po.order.add_edge(data,    feedback)
b_po.order.add_edge(energy,  feedback)
b_po.order.add_edge(waste,   feedback)

# Define the LOOP operator: Crop Cycle + monitoring-feedback as loop body
loop = OperatorPOWL(operator=Operator.LOOP, children=[crop, b_po])

# Assemble the overall partial order
root = StrictPartialOrder(
    nodes=[
        site, impact, design,
        tech, reg, stakeholder, supply,
        pilot, loop,
        market, scale
    ]
)

# Add the control‐flow dependencies
root.order.add_edge(site,        impact)
root.order.add_edge(impact,      design)
root.order.add_edge(design,      tech)
root.order.add_edge(design,      reg)
root.order.add_edge(design,      stakeholder)
root.order.add_edge(reg,         supply)
root.order.add_edge(tech,        pilot)
root.order.add_edge(supply,      pilot)
root.order.add_edge(stakeholder, pilot)
root.order.add_edge(pilot,       loop)
root.order.add_edge(loop,        market)
root.order.add_edge(market,      scale)