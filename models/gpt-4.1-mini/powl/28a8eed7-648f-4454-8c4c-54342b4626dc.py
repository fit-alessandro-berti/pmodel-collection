# Generated from: 28a8eed7-648f-4454-8c4c-54342b4626dc.json
# Description: This process details the complex steps involved in importing artisan cheeses from remote European farms to boutique stores in North America. It involves sourcing rare cheese varieties, verifying organic certifications, coordinating with local customs agents, managing temperature-controlled logistics, handling quarantine inspections, and ensuring compliance with strict FDA regulations. The process also includes quality sampling, labeling adjustments for different markets, marketing coordination for product launch, and final distribution to specialty retailers, all while maintaining traceability and minimizing spoilage risks throughout the supply chain.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Farm_Sourcing = Transition(label='Farm Sourcing')
Certify_Organic = Transition(label='Certify Organic')
Contract_Signing = Transition(label='Contract Signing')
Customs_Liaison = Transition(label='Customs Liaison')
Logistics_Planning = Transition(label='Logistics Planning')
Temp_Monitoring = Transition(label='Temp Monitoring')
Quarantine_Check = Transition(label='Quarantine Check')
FDA_Compliance = Transition(label='FDA Compliance')
Sample_Testing = Transition(label='Sample Testing')
Label_Revision = Transition(label='Label Revision')
Marketing_Prep = Transition(label='Marketing Prep')
Import_Clearance = Transition(label='Import Clearance')
Quality_Audit = Transition(label='Quality Audit')
Retail_Scheduling = Transition(label='Retail Scheduling')
Traceability_Setup = Transition(label='Traceability Setup')
Spoilage_Control = Transition(label='Spoilage Control')
Distribution_Setup = Transition(label='Distribution Setup')

# Construct partial orders and operators reflecting the described process

# Initial sourcing and certification phase
source_and_certify = StrictPartialOrder(
    nodes=[Farm_Sourcing, Certify_Organic, Contract_Signing]
)
source_and_certify.order.add_edge(Farm_Sourcing, Certify_Organic)
source_and_certify.order.add_edge(Certify_Organic, Contract_Signing)

# Customs-related activities: liaison and import clearance
customs = StrictPartialOrder(
    nodes=[Customs_Liaison, Import_Clearance]
)
customs.order.add_edge(Customs_Liaison, Import_Clearance)

# Quality assurance branch:
# sample testing and quality audit can be done in parallel with label revision and marketing prep
quality_sampling = StrictPartialOrder(
    nodes=[Sample_Testing, Quality_Audit]
)
quality_sampling.order.add_edge(Sample_Testing, Quality_Audit)

label_and_marketing = StrictPartialOrder(
    nodes=[Label_Revision, Marketing_Prep]
)
# Label and marketing prep can be done in parallel (no edges)

quality_and_label = StrictPartialOrder(
    nodes=[quality_sampling, label_and_marketing]
)
# concurrency between these two suborders (no edges between their roots)

# Logistics branch:
# planning, temp monitoring, quarantine check, spoilage control
logistics_plan = StrictPartialOrder(
    nodes=[Logistics_Planning, Temp_Monitoring, Quarantine_Check, Spoilage_Control]
)
logistics_plan.order.add_edge(Logistics_Planning, Temp_Monitoring)
logistics_plan.order.add_edge(Temp_Monitoring, Quarantine_Check)
logistics_plan.order.add_edge(Quarantine_Check, Spoilage_Control)

# Compliance and traceability branch:
compliance_trace = StrictPartialOrder(
    nodes=[FDA_Compliance, Traceability_Setup]
)
compliance_trace.order.add_edge(FDA_Compliance, Traceability_Setup)

# Final distribution phase after all above branches finish:
final_distribution = StrictPartialOrder(
    nodes=[Retail_Scheduling, Distribution_Setup]
)
final_distribution.order.add_edge(Retail_Scheduling, Distribution_Setup)

# Combine multiple parallel branches that must all complete before final distribution
pre_final_parallel = StrictPartialOrder(
    nodes=[customs, quality_and_label, logistics_plan, compliance_trace]
)
# No order edges among these four, they are concurrent

# Compose the whole process flow partial order
root = StrictPartialOrder(
    nodes=[source_and_certify, pre_final_parallel, final_distribution]
)

# Add ordering edges connecting phases:
root.order.add_edge(source_and_certify, pre_final_parallel)
root.order.add_edge(pre_final_parallel, final_distribution)