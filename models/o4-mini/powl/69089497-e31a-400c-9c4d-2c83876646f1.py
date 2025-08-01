# Generated from: 69089497-e31a-400c-9c4d-2c83876646f1.json
# Description: This process involves the intricate steps required to produce, age, and distribute artisan cheese from small-scale farms to niche markets. It begins with selecting rare milk varieties, followed by specialized fermentation and aging techniques under strict environmental controls. Quality control includes microbial analysis and texture testing. Packaging involves eco-friendly materials and personalized labeling. Finally, distribution leverages boutique logistics partners to maintain freshness and unique branding, targeting gourmet retailers and exclusive restaurants. This atypical supply chain emphasizes craftsmanship, traceability, and sustainability throughout every stage of production and delivery, ensuring the final product meets artisanal standards and consumer expectations for rare cheeses.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
milk_sel     = Transition(label='Milk Selection')
milk_test    = Transition(label='Milk Testing')
starter      = Transition(label='Starter Culture')
curd         = Transition(label='Curd Formation')
whey         = Transition(label='Whey Separation')
molding      = Transition(label='Molding Cheese')
press        = Transition(label='Pressing Cheese')
salting      = Transition(label='Salting Process')
aging_ctrl   = Transition(label='Aging Control')
humidity_chk = Transition(label='Humidity Check')
microbial    = Transition(label='Microbial Test')
texture      = Transition(label='Texture Check')
pack_prep    = Transition(label='Packaging Prep')
label_print  = Transition(label='Label Printing')
eco_pack     = Transition(label='Eco Packing')
cold_store   = Transition(label='Cold Storage')
shipping     = Transition(label='Boutique Shipping')

# Loop for aging under environmental control: do Aging Control, then optionally
# repeat after a Humidity Check
loop_aging = OperatorPOWL(
    operator=Operator.LOOP,
    children=[aging_ctrl, humidity_chk]
)

# Build the root partial order
root = StrictPartialOrder(nodes=[
    milk_sel, milk_test, starter, curd, whey, molding, press, salting,
    loop_aging,
    microbial, texture,
    pack_prep, label_print, eco_pack,
    cold_store, shipping
])

# Sequencing edges
root.order.add_edge(milk_sel, milk_test)
root.order.add_edge(milk_test, starter)
root.order.add_edge(starter, curd)
root.order.add_edge(curd, whey)
root.order.add_edge(whey, molding)
root.order.add_edge(molding, press)
root.order.add_edge(press, salting)

# After salting, enter the aging loop
root.order.add_edge(salting, loop_aging)

# After completing the aging loop, perform quality control tasks in parallel
root.order.add_edge(loop_aging, microbial)
root.order.add_edge(loop_aging, texture)

# Both QC tasks must finish before packaging prep
root.order.add_edge(microbial, pack_prep)
root.order.add_edge(texture, pack_prep)

# Packaging prep leads to labeling and eco-packing in parallel
root.order.add_edge(pack_prep, label_print)
root.order.add_edge(pack_prep, eco_pack)

# After both packaging steps, move to cold storage and then shipping
root.order.add_edge(label_print, cold_store)
root.order.add_edge(eco_pack, cold_store)
root.order.add_edge(cold_store, shipping)