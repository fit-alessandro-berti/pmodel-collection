# Generated from: 01f1e244-889e-4ecc-919e-c9df5ffc9edd.json
# Description: This process outlines the intricate journey of artisan cheese production and distribution, starting from raw milk sourcing on small farms, through traditional curdling and aging methods, quality assurance by expert tasters, custom packaging, and finally niche market delivery. The chain integrates seasonal milk variations, manual aging adjustments, artisan branding, compliance with food safety standards, and direct customer feedback loops to maintain product uniqueness and authenticity across diverse regional markets. Each step requires expert craftsmanship combined with logistical coordination to preserve the delicate flavor profiles and cultural heritage of the cheese varieties produced.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
milk           = Transition(label='Milk Sourcing')
curd           = Transition(label='Curd Preparation')
whey           = Transition(label='Whey Separation')
press          = Transition(label='Press Molding')
salt           = Transition(label='Salting Process')
aging_control  = Transition(label='Aging Control')
flavor         = Transition(label='Flavor Infusion')
texture        = Transition(label='Texture Assessment')
quality        = Transition(label='Quality Testing')
pkg_design     = Transition(label='Packaging Design')
label_print    = Transition(label='Label Printing')
batch_track    = Transition(label='Batch Tracking')
reg_check      = Transition(label='Regulatory Check')
delivery       = Transition(label='Market Delivery')
review         = Transition(label='Customer Review')

# Build the packaging‐and‐delivery loop:
# Body of the loop: Packaging Design -> Label Printing -> Batch Tracking -> Regulatory Check -> Market Delivery
body = StrictPartialOrder(
    nodes=[pkg_design, label_print, batch_track, reg_check, delivery]
)
body.order.add_edge(pkg_design, label_print)
body.order.add_edge(label_print, batch_track)
body.order.add_edge(batch_track, reg_check)
body.order.add_edge(reg_check, delivery)

# Loop operator: after the body, Customer Review may trigger another cycle
packaging_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[body, review]
)

# Build the main process Partial Order
root = StrictPartialOrder(
    nodes=[
        milk, curd, whey, press, salt,
        aging_control, flavor, texture,
        quality, packaging_loop
    ]
)

# Define the control‐flow dependencies
root.order.add_edge(milk, curd)
root.order.add_edge(milk, whey)
root.order.add_edge(curd, press)
root.order.add_edge(whey, press)
root.order.add_edge(press, salt)
root.order.add_edge(salt, aging_control)
root.order.add_edge(salt, flavor)
root.order.add_edge(aging_control, texture)
root.order.add_edge(flavor, texture)
root.order.add_edge(texture, quality)
root.order.add_edge(quality, packaging_loop)