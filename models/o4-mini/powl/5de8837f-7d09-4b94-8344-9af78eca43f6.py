# Generated from: 5de8837f-7d09-4b94-8344-9af78eca43f6.json
# Description: This process involves the end-to-end management of artisan cheese production and distribution, starting from sourcing rare milk varieties from niche farms, monitoring fermentation stages with microbial analysis, and custom aging in controlled environments. It includes quality inspections, bespoke packaging design tailored for each cheese type, coordinating limited batch shipments to specialty retailers, and managing customer feedback loops for continuous product refinement. The process also integrates seasonal variations in milk supply, compliance with food safety regulations, and marketing efforts highlighting artisanal craftsmanship and provenance stories to attract connoisseurs and maintain brand exclusivity.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
t_source      = Transition(label='Milk Sourcing')
t_test        = Transition(label='Microbial Test')
t_regcheck    = Transition(label='Regulation Check')
t_pasteurize  = Transition(label='Milk Pasteurize')
t_curd        = Transition(label='Curd Formation')
t_drain       = Transition(label='Whey Drain')
t_inoculate   = Transition(label='Mold Inoculate')
t_press       = Transition(label='Press Cheese')
t_age         = Transition(label='Custom Aging')
t_quality     = Transition(label='Quality Inspect')
t_flavor      = Transition(label='Flavor Profiling')
t_design      = Transition(label='Package Design')
t_label       = Transition(label='Batch Labeling')
t_shipplan    = Transition(label='Shipment Plan')
t_retail      = Transition(label='Retail Notify')
t_feedback    = Transition(label='Feedback Review')
t_marketing   = Transition(label='Marketing Draft')
t_inventory   = Transition(label='Inventory Audit')

# Core production & distribution as a partial order
production = StrictPartialOrder(nodes=[
    t_source,
    t_test,
    t_regcheck,
    t_pasteurize,
    t_curd,
    t_drain,
    t_inoculate,
    t_press,
    t_age,
    t_quality,
    t_flavor,
    t_design,
    t_label,
    t_shipplan,
    t_retail,
    t_marketing,
    t_inventory
])

# Define the control-flow dependencies
production.order.add_edge(t_source,     t_test)
production.order.add_edge(t_source,     t_regcheck)
production.order.add_edge(t_test,       t_regcheck)
production.order.add_edge(t_regcheck,   t_pasteurize)
production.order.add_edge(t_pasteurize, t_curd)
production.order.add_edge(t_curd,       t_drain)
production.order.add_edge(t_drain,      t_inoculate)
production.order.add_edge(t_inoculate,  t_press)
production.order.add_edge(t_press,      t_age)
production.order.add_edge(t_age,        t_quality)
production.order.add_edge(t_quality,    t_flavor)
production.order.add_edge(t_flavor,     t_design)
production.order.add_edge(t_design,     t_label)
production.order.add_edge(t_label,      t_shipplan)
production.order.add_edge(t_shipplan,   t_retail)
# Marketing and inventory audit follow labeling and notification
production.order.add_edge(t_label,      t_marketing)
production.order.add_edge(t_retail,     t_inventory)

# Wrap the entire production & distribution in a feedback loop:
# Execute production, then either exit or do a feedback review and repeat
root = OperatorPOWL(operator=Operator.LOOP, children=[production, t_feedback])