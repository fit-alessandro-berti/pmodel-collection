# Generated from: bf8a9023-17b1-4b9b-9213-5a25c293b869.json
# Description: This process involves the systematic verification and authentication of historical artifacts acquired by museums or private collectors. It begins with initial assessment and cataloging, followed by material analysis using non-invasive technology. Experts from multiple disciplines collaborate to compare findings with historical records. The workflow includes provenance verification, condition evaluation, and risk assessment for potential forgery or damage. Upon successful authentication, secure packaging and insurance appraisal are conducted before final archival registration. Continuous monitoring and periodic re-evaluation ensure long-term preservation and authenticity validation over time.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Initial_Assessment = Transition(label='Initial Assessment')
Catalog_Entry = Transition(label='Catalog Entry')
Material_Scan = Transition(label='Material Scan')

# Expert collaboration includes Expert Review, Provenance Check, Condition Eval, Forgery Risk, Cross Reference, Report Draft
Expert_Review = Transition(label='Expert Review')
Provenance_Check = Transition(label='Provenance Check')
Condition_Eval = Transition(label='Condition Eval')
Forgery_Risk = Transition(label='Forgery Risk')
Cross_Reference = Transition(label='Cross Reference')
Report_Draft = Transition(label='Report Draft')

Secure_Packaging = Transition(label='Secure Packaging')
Insurance_Appraisal = Transition(label='Insurance Appraisal')
Archival_Entry = Transition(label='Archival Entry')
Stakeholder_Brief = Transition(label='Stakeholder Brief')

Periodic_Audit = Transition(label='Periodic Audit')
Preservation_Plan = Transition(label='Preservation Plan')
Reevaluation_Set = Transition(label='Reevaluation Set')

# Expert collaboration partial order: these 6 activities are concurrent (no order imposed)
expert_nodes = [Expert_Review, Provenance_Check, Condition_Eval, Forgery_Risk, Cross_Reference, Report_Draft]
Expert_Collab = StrictPartialOrder(nodes=expert_nodes)
# no order edges - fully concurrent expert activities

# After expert collaboration complete, proceed to Secure Packaging and Insurance Appraisal in parallel
Packaging_Insurance = StrictPartialOrder(nodes=[Secure_Packaging, Insurance_Appraisal])
# no order edges between these two activities - concurrent

# Then Archival Entry and Stakeholder Brief in parallel
Archival_Stakeholder = StrictPartialOrder(nodes=[Archival_Entry, Stakeholder_Brief])
# no order edges between these two - concurrent

# Build the main partial order for the first part:
# Initial Assessment --> Catalog Entry --> Material Scan --> Expert Collaboration --> (Packaging & Insurance) --> (Archival Entry & Stakeholder Brief)
first_part = StrictPartialOrder(nodes=[
    Initial_Assessment, Catalog_Entry, Material_Scan, Expert_Collab, Packaging_Insurance, Archival_Stakeholder
])
first_part.order.add_edge(Initial_Assessment, Catalog_Entry)
first_part.order.add_edge(Catalog_Entry, Material_Scan)
first_part.order.add_edge(Material_Scan, Expert_Collab)
first_part.order.add_edge(Expert_Collab, Packaging_Insurance)
first_part.order.add_edge(Packaging_Insurance, Archival_Stakeholder)

# Define the loop: periodic monitoring and re-evaluation
# LOOP(
#   Body: Periodic_Audit --> Preservation_Plan --> Reevaluation_Set
#   Exit: Silent transition (exit)
# )
Periodic_Body = StrictPartialOrder(nodes=[Periodic_Audit, Preservation_Plan, Reevaluation_Set])
Periodic_Body.order.add_edge(Periodic_Audit, Preservation_Plan)
Periodic_Body.order.add_edge(Preservation_Plan, Reevaluation_Set)

from pm4py.objects.powl.obj import SilentTransition
skip = SilentTransition()
Periodic_Loop = OperatorPOWL(operator=Operator.LOOP, children=[Periodic_Body, skip])

# Final model: first_part --> periodic_loop
root = StrictPartialOrder(nodes=[first_part, Periodic_Loop])
root.order.add_edge(first_part, Periodic_Loop)