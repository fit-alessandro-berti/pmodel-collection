# Generated from: dd7bc2cb-e945-49b7-bdff-008a99bba3ed.json
# Description: This process outlines the intricate steps involved in sourcing, aging, and distributing artisan cheeses from small-scale farms to gourmet retailers. It begins with farm selection, ensuring ethical animal treatment and unique milk qualities, followed by milk testing, curdling, and controlled aging in specialized environments. Quality inspections occur at multiple stages, including texture and flavor profiling. Packaging is customized for each cheese type to maintain freshness and brand identity. The distribution involves cold chain logistics with real-time monitoring and retailer training on product handling. Finally, customer feedback is collected to refine future batches and maintain artisanal standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activity transitions
farm_select      = Transition(label='Farm Select')
milk_test        = Transition(label='Milk Test')
milk_pasteurize  = Transition(label='Milk Pasteurize')
curd_form        = Transition(label='Curd Form')
whey_drain       = Transition(label='Whey Drain')
cheese_press     = Transition(label='Cheese Press')
salt_rub         = Transition(label='Salt Rub')
aging_set        = Transition(label='Aging Set')
flavor_check     = Transition(label='Flavor Check')
texture_scan     = Transition(label='Texture Scan')
quality_approve  = Transition(label='Quality Approve')
custom_pack      = Transition(label='Custom Pack')
cold_ship        = Transition(label='Cold Ship')
retail_train     = Transition(label='Retail Train')
feedback_log     = Transition(label='Feedback Log')
batch_adjust     = Transition(label='Batch Adjust')

# Main production sequence up to retailer training
main = StrictPartialOrder(nodes=[
    farm_select, milk_test, milk_pasteurize, curd_form, whey_drain,
    cheese_press, salt_rub, aging_set,
    flavor_check, texture_scan,
    quality_approve, custom_pack, cold_ship, retail_train
])

# Add the ordering constraints for the main sequence
m = main.order
m.add_edge(farm_select,      milk_test)
m.add_edge(milk_test,        milk_pasteurize)
m.add_edge(milk_pasteurize,  curd_form)
m.add_edge(curd_form,        whey_drain)
m.add_edge(whey_drain,       cheese_press)
m.add_edge(cheese_press,     salt_rub)
m.add_edge(salt_rub,         aging_set)
# After aging, flavor and texture checks happen in parallel
m.add_edge(aging_set,        flavor_check)
m.add_edge(aging_set,        texture_scan)
# Both checks must complete before quality approval
m.add_edge(flavor_check,     quality_approve)
m.add_edge(texture_scan,     quality_approve)
m.add_edge(quality_approve,  custom_pack)
m.add_edge(custom_pack,      cold_ship)
m.add_edge(cold_ship,        retail_train)

# Feedback-and-adjustment subprocess
feedback_seq = StrictPartialOrder(nodes=[feedback_log, batch_adjust])
fb = feedback_seq.order
fb.add_edge(feedback_log, batch_adjust)

# Loop: do main once, then optionally perform feedback+adjust and repeat
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[main, feedback_seq]
)