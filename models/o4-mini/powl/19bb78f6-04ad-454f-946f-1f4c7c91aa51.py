# Generated from: 19bb78f6-04ad-454f-946f-1f4c7c91aa51.json
# Description: This process outlines the unique and intricate supply chain for artisanal cheese production, involving sourcing rare milk types, carefully timed fermentation, handcrafted molding, aging under controlled humidity, and specialized packaging. The process requires coordination between small-scale farmers, fermentation experts, quality inspectors, and boutique distributors to ensure the final product maintains its distinct flavor profile and meets niche market demands while complying with strict food safety regulations and seasonal variations in milk availability.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as POWL transitions
milk_sourcing    = Transition(label='Milk Sourcing')
quality_testing  = Transition(label='Quality Testing')
milk_pasteurize  = Transition(label='Milk Pasteurize')
starter_culture  = Transition(label='Starter Culture')
fermentation_ck  = Transition(label='Fermentation Check')
curd_cutting     = Transition(label='Curd Cutting')
whey_draining    = Transition(label='Whey Draining')
mold_pressing    = Transition(label='Mold Pressing')
salt_brining     = Transition(label='Salt Brining')
humidity_aging   = Transition(label='Humidity Aging')
flavor_infuse    = Transition(label='Flavor Infuse')
rind_treatment   = Transition(label='Rind Treatment')
quality_inspect  = Transition(label='Quality Inspect')
packaging_design = Transition(label='Packaging Design')
boutique_ship    = Transition(label='Boutique Shipping')
market_feedback  = Transition(label='Market Feedback')

# Build the partial order
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    quality_testing,
    milk_pasteurize,
    starter_culture,
    fermentation_ck,
    curd_cutting,
    whey_draining,
    mold_pressing,
    salt_brining,
    humidity_aging,
    flavor_infuse,
    rind_treatment,
    quality_inspect,
    packaging_design,
    boutique_ship,
    market_feedback
])

# Define the control‐flow dependencies
o = root.order
o.add_edge(milk_sourcing,   quality_testing)
o.add_edge(quality_testing, milk_pasteurize)
o.add_edge(milk_pasteurize, starter_culture)
o.add_edge(starter_culture, fermentation_ck)
o.add_edge(fermentation_ck, curd_cutting)
o.add_edge(curd_cutting,    whey_draining)
o.add_edge(whey_draining,   mold_pressing)
o.add_edge(mold_pressing,   salt_brining)

# After brining, two threads:
#  1) cheese production continues
o.add_edge(salt_brining,    humidity_aging)
o.add_edge(humidity_aging,  flavor_infuse)
o.add_edge(flavor_infuse,   rind_treatment)
o.add_edge(rind_treatment,  quality_inspect)

#  2) packaging design can start once brining is done
o.add_edge(salt_brining,    packaging_design)

# Join before shipping: both quality inspection and packaging design must complete
o.add_edge(quality_inspect, boutique_ship)
o.add_edge(packaging_design, boutique_ship)

# Final step: get market feedback
o.add_edge(boutique_ship, market_feedback)