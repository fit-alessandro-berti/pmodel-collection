# Generated from: 16aa67b5-b524-4e8a-b148-d0462ec0663d.json
# Description: This process describes the end-to-end supply chain of artisanal cheese production and distribution involving unique steps such as milk sourcing from rare breeds, precise aging conditions monitoring, custom flavor profiling, and direct-to-consumer sales through curated events. It includes managing small batch fermentation, quality control using sensory panels, packaging with sustainable materials, and coordinating with niche retailers globally. The complexity arises from balancing traditional craftsmanship with modern logistics and traceability requirements, ensuring each cheese wheel maintains its distinctive character while meeting regulatory standards and consumer expectations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
breed_sel     = Transition(label='Breed Selection')
milk_harvest  = Transition(label='Milk Harvest')
quality_check = Transition(label='Quality Check')
starter_prep  = Transition(label='Starter Prep')
curd_cutting  = Transition(label='Curd Cutting')
molding_press = Transition(label='Molding Press')
salt_brining  = Transition(label='Salt Brining')
aging_setup   = Transition(label='Aging Setup')
humidity_ctrl = Transition(label='Humidity Control')
flavor_test   = Transition(label='Flavor Test')
batch_label   = Transition(label='Batch Labeling')
eco_packaging = Transition(label='Eco Packaging')
event_planning= Transition(label='Event Planning')
retail_out    = Transition(label='Retail Outreach')
order_fulfill = Transition(label='Order Fulfill')
feedback_loop = Transition(label='Feedback Loop')
inventory_aud = Transition(label='Inventory Audit')

# Composite for aging: setup then in parallel humidity & flavor testing
agingPO = StrictPartialOrder(
    nodes=[aging_setup, humidity_ctrl, flavor_test]
)
agingPO.order.add_edge(aging_setup, humidity_ctrl)
agingPO.order.add_edge(aging_setup, flavor_test)

# Loop for ongoing feedback & inventory audit
feedback_loop_cycle = OperatorPOWL(
    operator=Operator.LOOP,
    children=[feedback_loop, inventory_aud]
)

# Root partial order of the entire process
root = StrictPartialOrder(
    nodes=[
        breed_sel,
        milk_harvest,
        quality_check,
        starter_prep,
        curd_cutting,
        molding_press,
        salt_brining,
        agingPO,
        batch_label,
        eco_packaging,
        event_planning,
        retail_out,
        order_fulfill,
        feedback_loop_cycle
    ]
)

# Define the sequential and concurrent dependencies
root.order.add_edge(breed_sel,     milk_harvest)
root.order.add_edge(milk_harvest,  quality_check)
root.order.add_edge(quality_check, starter_prep)
root.order.add_edge(starter_prep,  curd_cutting)
root.order.add_edge(curd_cutting,  molding_press)
root.order.add_edge(molding_press, salt_brining)
root.order.add_edge(salt_brining,  agingPO)
root.order.add_edge(agingPO,       batch_label)
root.order.add_edge(batch_label,   eco_packaging)
# After eco-packaging both event planning and retail outreach proceed concurrently
root.order.add_edge(eco_packaging, event_planning)
root.order.add_edge(eco_packaging, retail_out)
# Both feed into order fulfillment
root.order.add_edge(event_planning, order_fulfill)
root.order.add_edge(retail_out,     order_fulfill)
# Finally enter the feedback/inventory loop
root.order.add_edge(order_fulfill,  feedback_loop_cycle)