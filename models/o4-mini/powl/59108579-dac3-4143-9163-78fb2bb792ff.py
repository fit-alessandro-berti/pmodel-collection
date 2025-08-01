# Generated from: 59108579-dac3-4143-9163-78fb2bb792ff.json
# Description: This process outlines the end-to-end operations involved in producing and distributing artisan cheese from small dairy farms to niche retail shops. It includes raw milk sourcing, quality checks under varying seasonal conditions, traditional cheese culturing, aging in controlled environments, custom packaging, and logistics coordination with temperature-sensitive transport. It also incorporates periodic artisan workshops for skill improvement, market trend analysis for new cheese varieties, and direct customer feedback loops to adjust production. The process balances artisanal craftsmanship with traceability and regulatory compliance across multiple regions, ensuring product authenticity and superior taste consistency in a competitive specialty food market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
milk = Transition(label='Milk Sourcing')
qc = Transition(label='Quality Check')
culture = Transition(label='Culture Prep')
curd = Transition(label='Curd Formation')
cut = Transition(label='Cutting Curd')
mold = Transition(label='Molding Cheese')
press = Transition(label='Pressing Cheese')
salt = Transition(label='Salting Stage')
aging = Transition(label='Aging Control')
pack = Transition(label='Packaging Art')
label = Transition(label='Label Design')
survey = Transition(label='Market Survey')
audit = Transition(label='Storage Audit')
workshop = Transition(label='Workshop Host')
order = Transition(label='Order Processing')
logistics = Transition(label='Temp Logistics')
customer = Transition(label='Customer Review')

# Silent transition for loop constructs
skip = SilentTransition()

# Loop: periodic artisan workshops
workshop_loop = OperatorPOWL(operator=Operator.LOOP, children=[workshop, skip])
# Loop: customer feedback cycles
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[customer, skip])

# Build the partial order
root = StrictPartialOrder(nodes=[
    milk, qc, culture, curd, cut, mold, press, salt, aging,
    pack, label, survey, audit, order, logistics,
    workshop_loop, feedback_loop
])

# Production sequence
root.order.add_edge(milk, qc)
root.order.add_edge(qc, culture)
root.order.add_edge(culture, curd)
root.order.add_edge(curd, cut)
root.order.add_edge(cut, mold)
root.order.add_edge(mold, press)
root.order.add_edge(press, salt)
root.order.add_edge(salt, aging)

# Workshops run periodically after quality check (concurrent with production)
root.order.add_edge(qc, workshop_loop)

# After aging, run packaging, labeling, market survey, and storage audit in parallel
root.order.add_edge(aging, pack)
root.order.add_edge(aging, label)
root.order.add_edge(aging, survey)
root.order.add_edge(aging, audit)

# All four converge into order processing
root.order.add_edge(pack, order)
root.order.add_edge(label, order)
root.order.add_edge(survey, order)
root.order.add_edge(audit, order)

# Then logistics and customer feedback loop
root.order.add_edge(order, logistics)
root.order.add_edge(logistics, feedback_loop)