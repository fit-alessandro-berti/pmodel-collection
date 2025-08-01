# Generated from: 3fa3435c-0f0e-4f99-8f5b-8ceca61852b3.json
# Description: This process describes the detailed steps involved in producing and distributing artisanal cheese from farm to consumer. It begins with sourcing rare milk varieties from select farms, followed by specialized fermentation and aging techniques in controlled environments. Quality inspections occur at multiple stages to ensure flavor consistency and safety. Packaging is done using eco-friendly materials with custom labeling. The process also includes coordinating niche marketing campaigns targeting gourmet retailers and direct consumer subscriptions. Logistics are managed with temperature-controlled transport and real-time tracking to preserve product integrity, culminating in customer feedback analysis to refine future batches and supply strategies.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
milk_pasteurize = Transition(label='Milk Pasteurize')
starter_culture = Transition(label='Starter Culture')
curd_cutting = Transition(label='Curd Cutting')
whey_drain = Transition(label='Whey Drain')
mold_inoculate = Transition(label='Mold Inoculate')
press_cheese = Transition(label='Press Cheese')
aging_control = Transition(label='Aging Control')
humidity_check = Transition(label='Humidity Check')
flavor_tasting = Transition(label='Flavor Tasting')
eco_packaging = Transition(label='Eco Packaging')
label_design = Transition(label='Label Design')
market_targeting = Transition(label='Market Targeting')
transport_setup = Transition(label='Transport Setup')
temp_monitor = Transition(label='Temp Monitor')
retail_delivery = Transition(label='Retail Delivery')
customer_survey = Transition(label='Customer Survey')

# Define fermentation and aging steps including quality steps as a loop:
# Loop body B includes the repeated steps of aging control, humidity check, flavor tasting, quality testing
# Loop entry A includes mold inoculate, pressing cheese and first aging control
# Construct loop: A = mold_inoculate->press_cheese->aging_control
# B = humidity_check->flavor_tasting->quality_testing

aging_loop_body = StrictPartialOrder(nodes=[humidity_check, flavor_tasting, quality_testing])
aging_loop_body.order.add_edge(humidity_check, flavor_tasting)
aging_loop_body.order.add_edge(flavor_tasting, quality_testing)

aging_loop_entry = StrictPartialOrder(nodes=[mold_inoculate, press_cheese, aging_control])
aging_loop_entry.order.add_edge(mold_inoculate, press_cheese)
aging_loop_entry.order.add_edge(press_cheese, aging_control)

aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_loop_entry, aging_loop_body])

# Cheese production sequence before aging loop:
# milk_sourcing -> milk_pasteurize -> starter_culture -> curd_cutting -> whey_drain -> quality_testing

production_seq = StrictPartialOrder(nodes=[
    milk_sourcing,
    milk_pasteurize,
    starter_culture,
    curd_cutting,
    whey_drain,
    quality_testing
])
production_seq.order.add_edge(milk_sourcing, milk_pasteurize)
production_seq.order.add_edge(milk_pasteurize, starter_culture)
production_seq.order.add_edge(starter_culture, curd_cutting)
production_seq.order.add_edge(curd_cutting, whey_drain)
production_seq.order.add_edge(whey_drain, quality_testing)

# Packaging sequence (after aging loop)
# eco_packaging -> label_design -> market_targeting

packaging_seq = StrictPartialOrder(nodes=[eco_packaging, label_design, market_targeting])
packaging_seq.order.add_edge(eco_packaging, label_design)
packaging_seq.order.add_edge(label_design, market_targeting)

# Logistics sequence after marketing
# transport_setup -> temp_monitor -> retail_delivery -> customer_survey

logistics_seq = StrictPartialOrder(nodes=[transport_setup, temp_monitor, retail_delivery, customer_survey])
logistics_seq.order.add_edge(transport_setup, temp_monitor)
logistics_seq.order.add_edge(temp_monitor, retail_delivery)
logistics_seq.order.add_edge(retail_delivery, customer_survey)

# Combine all main parts in a PO with proper ordering

# Overall order:
# production_seq -> aging_loop -> packaging_seq -> logistics_seq
root = StrictPartialOrder(
    nodes=[production_seq, aging_loop, packaging_seq, logistics_seq]
)
root.order.add_edge(production_seq, aging_loop)
root.order.add_edge(aging_loop, packaging_seq)
root.order.add_edge(packaging_seq, logistics_seq)