# Generated from: 8cdb6c9a-21bc-4ad5-834d-f2cf76a4c97b.json
# Description: This process involves the complex coordination of multiple stakeholders and resources to establish an urban vertical farm within a densely populated city. It begins with site identification and environmental impact assessments, followed by securing permits and designing modular vertical farming units. The process includes sourcing specialized hydroponic equipment, integrating IoT-based monitoring systems, and implementing energy-efficient LED lighting. Staff recruitment focuses on agronomists and technicians trained in controlled environment agriculture. Concurrently, partnerships with local markets and distributors are negotiated to ensure product flow. The process also covers sustainable waste management, water recycling systems, and community engagement initiatives. Quality control protocols and crop cycle optimization are continuously refined to maximize yield and minimize resource consumption. Finally, a phased product launch is executed alongside ongoing data analytics to adapt operations dynamically.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site = Transition(label='Site Survey')
impact = Transition(label='Impact Study')
permit = Transition(label='Permit Filing')
design = Transition(label='Unit Design')
equip = Transition(label='Equip Sourcing')
system = Transition(label='System Setup')
lighting = Transition(label='Lighting Install')
hire = Transition(label='Staff Hiring')
train = Transition(label='Training Session')
market = Transition(label='Market Outreach')
waste = Transition(label='Waste Setup')
water = Transition(label='Water Recycle')
community = Transition(label='Community Meet')
quality = Transition(label='Quality Check')
cycle = Transition(label='Cycle Review')
launch = Transition(label='Launch Phase')
data = Transition(label='Data Monitor')

# Define the continuous refinement loop: Quality Check then optionally Cycle Review then back
loop = OperatorPOWL(operator=Operator.LOOP, children=[quality, cycle])

# Build the partial order model
root = StrictPartialOrder(nodes=[
    site, impact, permit, design,
    equip, system, lighting,
    hire, train, market,
    waste, water, community,
    loop, launch, data
])

# Sequence: Site Survey -> Impact Study
root.order.add_edge(site, impact)

# After Impact Study: Permit Filing and Unit Design in parallel
root.order.add_edge(impact, permit)
root.order.add_edge(impact, design)

# Permit and Design both precede Equipment Sourcing
root.order.add_edge(permit, equip)
root.order.add_edge(design, equip)

# Equipment Sourcing -> System Setup -> Lighting Install
root.order.add_edge(equip, system)
root.order.add_edge(system, lighting)

# After lighting, start Staff Hiring and Market Outreach in parallel
root.order.add_edge(lighting, hire)
root.order.add_edge(lighting, market)

# Staff Hiring -> Training Session
root.order.add_edge(hire, train)

# After lighting, also set up Waste, Water recycling, and Community engagement in parallel
root.order.add_edge(lighting, waste)
root.order.add_edge(lighting, water)
root.order.add_edge(lighting, community)

# All of training, waste, water, community feed into the continuous refinement loop
root.order.add_edge(train, loop)
root.order.add_edge(waste, loop)
root.order.add_edge(water, loop)
root.order.add_edge(community, loop)

# After the loop, execute Launch Phase and Data Monitor in parallel
root.order.add_edge(loop, launch)
root.order.add_edge(loop, data)