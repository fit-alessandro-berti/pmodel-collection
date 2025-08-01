# Generated from: d7737c35-e58b-4ba8-96bc-af94e425f158.json
# Description: This process ensures comprehensive traceability of artisan cheese production from raw milk sourcing through aging and packaging to final distribution. It involves meticulous documentation of milk origin, microbial cultures used, fermentation conditions, aging environments, and sensory evaluations. Quality checkpoints include microbial testing, texture analysis, and flavor profiling. The process integrates supplier audits, batch tracking, and regulatory compliance reviews. It also incorporates consumer feedback loops and sustainability assessments to optimize both product quality and environmental impact. Data is collected digitally at each stage to enable real-time analytics and to support recall procedures if necessary.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
milk_sourcing       = Transition(label='Milk Sourcing')
supplier_audit      = Transition(label='Supplier Audit')
culture_prep        = Transition(label='Culture Prep')
milk_testing        = Transition(label='Milk Testing')
fermentation_start  = Transition(label='Fermentation Start')
ph_monitoring       = Transition(label='pH Monitoring')
curd_cutting        = Transition(label='Curd Cutting')
mold_inoculation    = Transition(label='Mold Inoculation')
aging_setup         = Transition(label='Aging Setup')
humidity_control    = Transition(label='Humidity Control')
texture_check       = Transition(label='Texture Check')
flavor_profiling    = Transition(label='Flavor Profiling')
batch_labeling      = Transition(label='Batch Labeling')
packaging           = Transition(label='Packaging')
distribution        = Transition(label='Distribution')
feedback_review     = Transition(label='Feedback Review')
sustainability_audit= Transition(label='Sustainability Audit')

# Core production partial order
production = StrictPartialOrder(nodes=[
    milk_sourcing, supplier_audit, culture_prep, milk_testing,
    fermentation_start, ph_monitoring, curd_cutting, mold_inoculation,
    aging_setup, humidity_control, texture_check, flavor_profiling,
    batch_labeling, packaging, distribution
])
production.order.add_edge(milk_sourcing,      supplier_audit)
production.order.add_edge(supplier_audit,     culture_prep)
production.order.add_edge(culture_prep,       milk_testing)
production.order.add_edge(milk_testing,       fermentation_start)
production.order.add_edge(fermentation_start, ph_monitoring)
production.order.add_edge(ph_monitoring,      curd_cutting)
production.order.add_edge(curd_cutting,       mold_inoculation)
production.order.add_edge(mold_inoculation,   aging_setup)
production.order.add_edge(aging_setup,        humidity_control)
production.order.add_edge(humidity_control,   texture_check)
production.order.add_edge(texture_check,      flavor_profiling)
production.order.add_edge(flavor_profiling,   batch_labeling)
production.order.add_edge(batch_labeling,     packaging)
production.order.add_edge(packaging,          distribution)

# Feedback & sustainability inspection partial order
feedback_loop = StrictPartialOrder(nodes=[
    feedback_review, sustainability_audit
])
feedback_loop.order.add_edge(feedback_review, sustainability_audit)

# Combine into a LOOP: do production, then either exit or do feedback & sustainability and repeat
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[production, feedback_loop]
)