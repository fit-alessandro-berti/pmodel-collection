# Generated from: 65bf2b4e-3aad-4546-8e2a-83796b25a5d8.json
# Description: This process outlines the end-to-end supply chain for artisan cheese production, emphasizing small-batch quality and traceability. It begins with raw milk sourcing from local farms, followed by milk quality testing and fermentation control. The cheese is then manually curdled, molded, and aged under specific conditions. Each batch undergoes sensory evaluation and packaging with detailed provenance labels. Distribution involves coordinating with niche retailers and specialty food markets. The process includes customer feedback loops to adjust recipes and maintain artisanal standards while ensuring regulatory compliance and seasonal ingredient management.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
seasonal            = Transition(label='Seasonal Sourcing')
milk                = Transition(label='Milk Sourcing')
quality             = Transition(label='Quality Testing')
fermentation        = Transition(label='Fermentation Check')
curd                = Transition(label='Curd Formation')
molding             = Transition(label='Molding Cheese')
aging               = Transition(label='Aging Control')
sensory             = Transition(label='Sensory Eval')
label_printing      = Transition(label='Label Printing')
batch_packaging     = Transition(label='Batch Packaging')
inventory           = Transition(label='Inventory Logging')
retail              = Transition(label='Retail Coordination')
transport           = Transition(label='Transport Scheduling')
compliance          = Transition(label='Compliance Audit')
customer_survey     = Transition(label='Customer Survey')
recipe_adjust       = Transition(label='Recipe Adjust')

# Define the customer‐feedback loop: Survey then optionally Adjust, repeating
feedback_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[customer_survey, recipe_adjust]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    seasonal, milk, quality, fermentation, curd, molding, aging,
    sensory, label_printing, batch_packaging, inventory, retail,
    transport, compliance, feedback_loop
])

# Add the control‐flow edges to impose the intended ordering
root.order.add_edge(seasonal,        milk)
root.order.add_edge(milk,            quality)
root.order.add_edge(quality,         fermentation)
root.order.add_edge(fermentation,    curd)
root.order.add_edge(curd,            molding)
root.order.add_edge(molding,         aging)
root.order.add_edge(aging,           sensory)
root.order.add_edge(sensory,         label_printing)
root.order.add_edge(label_printing,  batch_packaging)
root.order.add_edge(batch_packaging, inventory)
root.order.add_edge(inventory,       retail)
root.order.add_edge(retail,          transport)
root.order.add_edge(transport,       compliance)
root.order.add_edge(compliance,      feedback_loop)