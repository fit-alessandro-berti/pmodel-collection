# Generated from: 5aff6ae7-ff82-4e43-9ac2-d84e8e8aa349.json
# Description: This process involves sourcing rare milk varieties from remote farms, followed by a detailed fermentation and aging procedure under controlled environmental conditions. Quality inspectors assess texture and flavor profiles periodically. Packaging requires specialized breathable materials to maintain cheese integrity during long overseas transit. Customs documentation and international compliance checks are handled before shipment. Upon arrival, distribution partners coordinate cold storage and retail placement, ensuring freshness and optimal shelf life. Customer feedback loops influence future batch adjustments, integrating artisanal craft with global supply chain complexities.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Milk_Sourcing = Transition(label='Milk Sourcing')
Quality_Testing = Transition(label='Quality Testing')
Fermentation_Start = Transition(label='Fermentation Start')
Age_Monitoring = Transition(label='Age Monitoring')
Texture_Check = Transition(label='Texture Check')
Flavor_Profiling = Transition(label='Flavor Profiling')
Packaging_Prep = Transition(label='Packaging Prep')
Breathable_Wrap = Transition(label='Breathable Wrap')
Customs_Filing = Transition(label='Customs Filing')
Compliance_Audit = Transition(label='Compliance Audit')
Export_Scheduling = Transition(label='Export Scheduling')
Cold_Storage = Transition(label='Cold Storage')
Retail_Placement = Transition(label='Retail Placement')
Feedback_Review = Transition(label='Feedback Review')
Batch_Adjust = Transition(label='Batch Adjust')

# Quality testing involves both Texture and Flavor checks, partially ordered (can be concurrent)
quality_checks = StrictPartialOrder(nodes=[Texture_Check, Flavor_Profiling])
# no order edge between them -> concurrent

# Group quality inspection phase (Quality Testing followed by both checks)
quality_phase = StrictPartialOrder(nodes=[Quality_Testing, quality_checks])
quality_phase.order.add_edge(Quality_Testing, quality_checks)

# Fermentation phase loop: Fermentation Start followed by repeated Age Monitoring
# but periodically Quality Checks (Texture and Flavor) must happen during aging

# We'll model aging with a loop that includes Age Monitoring and choice of doing or skipping quality phase
# Using a loop: 
# A = Age Monitoring
# B = X(Quality inspection phase, skip)
# In each iteration: Age Monitoring then optionally do quality inspection

skip = SilentTransition()

quality_choice = OperatorPOWL(operator=Operator.XOR, children=[quality_phase, skip])
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[Age_Monitoring, quality_choice])

# Packaging phase partial order: Packaging Prep then Breathable Wrap
packaging_phase = StrictPartialOrder(nodes=[Packaging_Prep, Breathable_Wrap])
packaging_phase.order.add_edge(Packaging_Prep, Breathable_Wrap)

# Export compliance checks partial order: Customs Filing then Compliance Audit then Export Scheduling
export_compliance = StrictPartialOrder(nodes=[Customs_Filing, Compliance_Audit, Export_Scheduling])
export_compliance.order.add_edge(Customs_Filing, Compliance_Audit)
export_compliance.order.add_edge(Compliance_Audit, Export_Scheduling)

# Distribution phase partial order: Cold Storage then Retail Placement
distribution_phase = StrictPartialOrder(nodes=[Cold_Storage, Retail_Placement])
distribution_phase.order.add_edge(Cold_Storage, Retail_Placement)

# Feedback loop modeled as loop:
# Loop over Feedback Review followed by Batch Adjust
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[Feedback_Review, Batch_Adjust])

# Construct main process partial order:
# Order:
# Milk Sourcing --> Fermentation Start --> aging_loop
# aging_loop --> packaging_phase --> export_compliance --> distribution_phase --> feedback_loop

main_nodes = [
    Milk_Sourcing,
    Fermentation_Start,
    aging_loop,
    packaging_phase,
    export_compliance,
    distribution_phase,
    feedback_loop
]

root = StrictPartialOrder(nodes=main_nodes)
root.order.add_edge(Milk_Sourcing, Fermentation_Start)
root.order.add_edge(Fermentation_Start, aging_loop)
root.order.add_edge(aging_loop, packaging_phase)
root.order.add_edge(packaging_phase, export_compliance)
root.order.add_edge(export_compliance, distribution_phase)
root.order.add_edge(distribution_phase, feedback_loop)