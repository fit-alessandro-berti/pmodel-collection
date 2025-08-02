# Generated from: f23f42e0-cf33-4472-9f50-92811cfbd4e6.json
# Description: This process encompasses the end-to-end supply chain of artisan cheese production, involving niche activities such as microbial culture selection, milk sourcing from specific regional farms, controlled aging in microclimates, quality tasting panels, and coordinated distribution to specialty retailers and exclusive gastronomic events. The process requires precise timing, temperature control, and regulatory compliance checks to maintain product uniqueness and safety. It integrates traditional craftsmanship with modern traceability technology, ensuring provenance and enhancing brand value in a competitive, small-batch market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

Milk_Sourcing = Transition(label='Milk Sourcing')
Culture_Selection = Transition(label='Culture Selection')
Milk_Testing = Transition(label='Milk Testing')
Curd_Cutting = Transition(label='Curd Cutting')
Whey_Draining = Transition(label='Whey Draining')
Mold_Inoculation = Transition(label='Mold Inoculation')
Forming_Cheese = Transition(label='Forming Cheese')
Salting_Stage = Transition(label='Salting Stage')
Aging_Setup = Transition(label='Aging Setup')
Climate_Control = Transition(label='Climate Control')
Quality_Tasting = Transition(label='Quality Tasting')
Packaging_Prep = Transition(label='Packaging Prep')
Label_Printing = Transition(label='Label Printing')
Distribution_Plan = Transition(label='Distribution Plan')
Retail_Delivery = Transition(label='Retail Delivery')
Event_Coordination = Transition(label='Event Coordination')
Regulatory_Audit = Transition(label='Regulatory Audit')

# Partial order setup for preparation steps
preparation = StrictPartialOrder(
    nodes=[Milk_Sourcing, Culture_Selection, Milk_Testing, Curd_Cutting, Whey_Draining,
           Mold_Inoculation, Forming_Cheese, Salting_Stage]
)
preparation.order.add_edge(Milk_Sourcing, Culture_Selection)
preparation.order.add_edge(Culture_Selection, Milk_Testing)
preparation.order.add_edge(Milk_Testing, Curd_Cutting)
preparation.order.add_edge(Curd_Cutting, Whey_Draining)
preparation.order.add_edge(Whey_Draining, Mold_Inoculation)
preparation.order.add_edge(Mold_Inoculation, Forming_Cheese)
preparation.order.add_edge(Forming_Cheese, Salting_Stage)

# Partial order for aging and quality steps, which can overlap / be partially concurrent
aging_quality = StrictPartialOrder(
    nodes=[Aging_Setup, Climate_Control, Quality_Tasting]
)
aging_quality.order.add_edge(Aging_Setup, Climate_Control)
aging_quality.order.add_edge(Climate_Control, Quality_Tasting)

# Partial order for packaging and distribution
packaging_distribution = StrictPartialOrder(
    nodes=[Packaging_Prep, Label_Printing, Distribution_Plan]
)
packaging_distribution.order.add_edge(Packaging_Prep, Label_Printing)
packaging_distribution.order.add_edge(Label_Printing, Distribution_Plan)

# Partial order for delivery options: Retail Delivery and Event Coordination can happen concurrently
delivery = StrictPartialOrder(
    nodes=[Retail_Delivery, Event_Coordination],
    # no order edges between them; concurrent
)

# After delivery, Regulatory Audit occurs
final_audit = Regulatory_Audit

# Combine packaging_distribution and delivery in partial order (packaging_distribution --> delivery)
packaging_delivery = StrictPartialOrder(
    nodes=[packaging_distribution, delivery]
)
packaging_delivery.order.add_edge(packaging_distribution, delivery)

# Compose all parts into final partial order:
# preparation --> aging_quality --> packaging_distribution --> delivery --> regulatory audit

root = StrictPartialOrder(
    nodes=[preparation, aging_quality, packaging_distribution, delivery, final_audit]
)
root.order.add_edge(preparation, aging_quality)
root.order.add_edge(aging_quality, packaging_distribution)
root.order.add_edge(packaging_distribution, delivery)
root.order.add_edge(delivery, final_audit)