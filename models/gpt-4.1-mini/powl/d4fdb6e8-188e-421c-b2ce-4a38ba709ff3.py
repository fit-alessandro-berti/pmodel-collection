# Generated from: d4fdb6e8-188e-421c-b2ce-4a38ba709ff3.json
# Description: This process involves the detailed authentication of rare historical artifacts before acquisition by museums or private collectors. It combines scientific analysis, provenance research, expert consultations, and legal verifications. The workflow includes physical examination, chemical testing, archival research, digital imaging, cross-referencing databases, expert panel review, and final certification. Additional steps ensure cultural sensitivity and compliance with international heritage laws, followed by secure transport arrangements and insurance validation. The process concludes with archival documentation and publication of findings to maintain transparency and historical integrity.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Artifact_Receipt = Transition(label='Artifact Receipt')
Initial_Inspection = Transition(label='Initial Inspection')

# Scientific analysis branch: Material Testing, Digital Imaging
Material_Testing = Transition(label='Material Testing')
Digital_Imaging = Transition(label='Digital Imaging')

# Provenance research branch: Provenance Check, Database Search
Provenance_Check = Transition(label='Provenance Check')
Database_Search = Transition(label='Database Search')

# Expert consultations: Expert Consult, Legal Review, Cultural Audit
Expert_Consult = Transition(label='Expert Consult')
Legal_Review = Transition(label='Legal Review')
Cultural_Audit = Transition(label='Cultural Audit')

# Condition report and risk assessment (concurrent)
Condition_Report = Transition(label='Condition Report')
Risk_Assessment = Transition(label='Risk Assessment')

# Logistics and insurance: Insurance Setup and Transport Plan
Insurance_Setup = Transition(label='Insurance Setup')
Transport_Plan = Transition(label='Transport Plan')

# Final certification and archival/publication
Final_Certification = Transition(label='Final Certification')
Archive_Entry = Transition(label='Archive Entry')
Publication_Prep = Transition(label='Publication Prep')

# Build branches as partial orders

# Scientific analysis simple PO (Material Testing --> Digital Imaging)
scientific_analysis = StrictPartialOrder(nodes=[Material_Testing, Digital_Imaging])
scientific_analysis.order.add_edge(Material_Testing, Digital_Imaging)

# Provenance research simple PO (Provenance Check --> Database Search)
provenance_research = StrictPartialOrder(nodes=[Provenance_Check, Database_Search])
provenance_research.order.add_edge(Provenance_Check, Database_Search)

# Expert consultations PO: Expert Consult --> Legal Review --> Cultural Audit
expert_consultations = StrictPartialOrder(nodes=[Expert_Consult, Legal_Review, Cultural_Audit])
expert_consultations.order.add_edge(Expert_Consult, Legal_Review)
expert_consultations.order.add_edge(Legal_Review, Cultural_Audit)

# Condition report and risk assessment concurrent
condition_and_risk = StrictPartialOrder(nodes=[Condition_Report, Risk_Assessment])
# No edges, so concurrent

# Insurance and transport concurrent (logical concurrent)
insurance_transport = StrictPartialOrder(nodes=[Insurance_Setup, Transport_Plan])
# No edges, concurrent

# Archival and publication sequential
archive_publication = StrictPartialOrder(nodes=[Archive_Entry, Publication_Prep])
archive_publication.order.add_edge(Archive_Entry, Publication_Prep)

# Now combine: scientific_analysis, provenance_research, expert_consultations run concurrently after Initial Inspection
# Then condition_and_risk concurrent after expert_consultations
# Then insurance_transport after condition_and_risk
# Then Final Certification after insurance_transport
# Then archive_publication after Final Certification

# Combine scientific_analysis, provenance_research, expert_consultations concurrently
# We use a StrictPartialOrder with nodes including these three POWL models, no edges to keep concurrency
analysis_research_expert = StrictPartialOrder(
    nodes=[scientific_analysis, provenance_research, expert_consultations]
)

# After initial inspection, these three concurrent branches
post_initial = StrictPartialOrder(
    nodes=[Initial_Inspection, analysis_research_expert]
)
post_initial.order.add_edge(Initial_Inspection, analysis_research_expert)

# After expert_consultations finishes, condition_and_risk start
# Hence condition_and_risk depends on expert_consultations' completion.
# Since expert_consultations is one node within analysis_research_expert,
# add order edges from analysis_research_expert to condition_and_risk so condition_and_risk waits for expert_consultations.
# But we only want condition_and_risk after expert_consultations finishes, not after scientific_analysis or provenance_research.
# We can handle this by separating the three branches as nodes, not grouped.

# So, refine analysis_research_expert to be PO with nodes:
analysis_research_expert_refined = StrictPartialOrder(
    nodes=[scientific_analysis, provenance_research, expert_consultations]
)
# initial inspection leads to all three branches concurrently
post_initial_refined = StrictPartialOrder(
    nodes=[Initial_Inspection, scientific_analysis, provenance_research, expert_consultations]
)
post_initial_refined.order.add_edge(Initial_Inspection, scientific_analysis)
post_initial_refined.order.add_edge(Initial_Inspection, provenance_research)
post_initial_refined.order.add_edge(Initial_Inspection, expert_consultations)

# condition_and_risk depend only on expert_consultations
post_condition_risk = StrictPartialOrder(
    nodes=[expert_consultations, condition_and_risk]
)
post_condition_risk.order.add_edge(expert_consultations, condition_and_risk)

# insurance_transport depends on condition_and_risk
post_insurance_transport = StrictPartialOrder(
    nodes=[condition_and_risk, insurance_transport]
)
post_insurance_transport.order.add_edge(condition_and_risk, insurance_transport)

# Final Certification after insurance_transport
post_final_certification = StrictPartialOrder(
    nodes=[insurance_transport, Final_Certification]
)
post_final_certification.order.add_edge(insurance_transport, Final_Certification)

# Archive and publication depend on final certification
post_archive_publication = StrictPartialOrder(
    nodes=[Final_Certification, archive_publication]
)
post_archive_publication.order.add_edge(Final_Certification, archive_publication)

# Now chain all partial orders from Artifact Receipt start

root = StrictPartialOrder(
    nodes=[Artifact_Receipt,
           post_initial_refined,
           post_condition_risk,
           post_insurance_transport,
           post_final_certification,
           post_archive_publication]
)

root.order.add_edge(Artifact_Receipt, post_initial_refined)
root.order.add_edge(post_initial_refined, post_condition_risk)
root.order.add_edge(post_condition_risk, post_insurance_transport)
root.order.add_edge(post_insurance_transport, post_final_certification)
root.order.add_edge(post_final_certification, post_archive_publication)