# Generated from: bc11e1c9-f5e8-4173-8635-9a467d2a3d47.json
# Description: This process outlines the intricate supply chain for artisan cheese production, starting from sourcing rare milk varieties from remote farms, through specialized fermentation monitoring, hand craftsmanship in curd cutting, aging under precise humidity controls, and finally bespoke packaging tailored for niche markets. The workflow involves quality assurance at multiple stages, logistics coordination with temperature-controlled transport, compliance with local food safety regulations, and dynamic inventory adjustments based on seasonal demand fluctuations. Collaboration with local farmers, artisan cheesemakers, and boutique retailers is essential to maintain product uniqueness and customer satisfaction in a highly competitive gourmet segment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Milk_Sourcing = Transition(label='Milk Sourcing')
Quality_Testing = Transition(label='Quality Testing')
Curd_Cutting = Transition(label='Curd Cutting')
Whey_Draining = Transition(label='Whey Draining')
Salt_Application = Transition(label='Salt Application')
Fermentation_Check = Transition(label='Fermentation Check')
Humidity_Control = Transition(label='Humidity Control')
Aging_Monitoring = Transition(label='Aging Monitoring')
Texture_Testing = Transition(label='Texture Testing')
Flavor_Profiling = Transition(label='Flavor Profiling')
Packaging_Design = Transition(label='Packaging Design')
Label_Printing = Transition(label='Label Printing')
Compliance_Audit = Transition(label='Compliance Audit')
Cold_Storage = Transition(label='Cold Storage')
Transport_Scheduling = Transition(label='Transport Scheduling')
Retail_Coordination = Transition(label='Retail Coordination')
Inventory_Review = Transition(label='Inventory Review')

# Build fermentation and aging sub-process with QA checks interleaved
# Fermentation monitoring loop: Fermentation_Check then either exit or Humidity_Control -> loop again
fermentation_loop = OperatorPOWL(operator=Operator.LOOP, children=[Fermentation_Check, Humidity_Control])
# Add Aging monitoring sequence after fermentation loop
aging_seq = StrictPartialOrder(nodes=[fermentation_loop, Aging_Monitoring])
aging_seq.order.add_edge(fermentation_loop, Aging_Monitoring)

# Quality Testing after Milk Sourcing, then parallel to (Curd Cutting + Whey Draining + Salt Application)
preparing_cheese = StrictPartialOrder(
    nodes=[Milk_Sourcing, Quality_Testing, Curd_Cutting, Whey_Draining, Salt_Application]
)
preparing_cheese.order.add_edge(Milk_Sourcing, Quality_Testing)
# After Quality Testing, Curd Cutting, Whey Draining and Salt Application are concurrent
preparing_cheese.order.add_edge(Quality_Testing, Curd_Cutting)
preparing_cheese.order.add_edge(Quality_Testing, Whey_Draining)
preparing_cheese.order.add_edge(Quality_Testing, Salt_Application)

# Texture Testing and Flavor Profiling follow Aging Monitoring
quality_profile = StrictPartialOrder(nodes=[aging_seq, Texture_Testing, Flavor_Profiling])
quality_profile.order.add_edge(aging_seq, Texture_Testing)
quality_profile.order.add_edge(aging_seq, Flavor_Profiling)

# Packaging steps: Packaging Design then Label Printing
packaging = StrictPartialOrder(nodes=[Packaging_Design, Label_Printing])
packaging.order.add_edge(Packaging_Design, Label_Printing)

# Compliance Audit, Cold Storage, Transport Scheduling, Retail Coordination, and Inventory Review form logistics / compliance branch
logistics = StrictPartialOrder(nodes=[
    Compliance_Audit,
    Cold_Storage,
    Transport_Scheduling,
    Retail_Coordination,
    Inventory_Review
])
logistics.order.add_edge(Compliance_Audit, Cold_Storage)
logistics.order.add_edge(Cold_Storage, Transport_Scheduling)
logistics.order.add_edge(Transport_Scheduling, Retail_Coordination)
logistics.order.add_edge(Retail_Coordination, Inventory_Review)

# Whey Draining leads to Fermentation Check loop after salt application and preparation
prep_followup = StrictPartialOrder(nodes=[Salt_Application, fermentation_loop])
prep_followup.order.add_edge(Salt_Application, fermentation_loop)

# Merge partial orders: preparing_cheese with prep_followup integrated by edges
preparing_and_fermentation = StrictPartialOrder(
    nodes=[Milk_Sourcing, Quality_Testing, Curd_Cutting, Whey_Draining, Salt_Application, fermentation_loop]
)
preparing_and_fermentation.order.add_edge(Milk_Sourcing, Quality_Testing)
preparing_and_fermentation.order.add_edge(Quality_Testing, Curd_Cutting)
preparing_and_fermentation.order.add_edge(Quality_Testing, Whey_Draining)
preparing_and_fermentation.order.add_edge(Quality_Testing, Salt_Application)
preparing_and_fermentation.order.add_edge(Salt_Application, fermentation_loop)

# Now complete process order:
# After prep_and_fermentation, aging monitoring etc. (integrated into quality_profile)
# After quality_profile, packaging
# After packaging, logistics

root = StrictPartialOrder(
    nodes=[preparing_and_fermentation, aging_seq, Texture_Testing, Flavor_Profiling,
           Packaging_Design, Label_Printing,
           Compliance_Audit, Cold_Storage, Transport_Scheduling, Retail_Coordination, Inventory_Review]
)

# Add edges to connect partial orders as per process flows:

# 1) prep_and_fermentation -> aging_seq (fermentation_loop is inside both)
root.order.add_edge(preparing_and_fermentation, aging_seq)

# 2) aging_seq to texture testing and flavor profiling
root.order.add_edge(aging_seq, Texture_Testing)
root.order.add_edge(aging_seq, Flavor_Profiling)

# 3) texture & flavor profiling to packaging design
root.order.add_edge(Texture_Testing, Packaging_Design)
root.order.add_edge(Flavor_Profiling, Packaging_Design)

# 4) packaging steps order
root.order.add_edge(Packaging_Design, Label_Printing)

# 5) label printing leads to compliance audit
root.order.add_edge(Label_Printing, Compliance_Audit)

# 6) compliance and logistics order
root.order.add_edge(Compliance_Audit, Cold_Storage)
root.order.add_edge(Cold_Storage, Transport_Scheduling)
root.order.add_edge(Transport_Scheduling, Retail_Coordination)
root.order.add_edge(Retail_Coordination, Inventory_Review)