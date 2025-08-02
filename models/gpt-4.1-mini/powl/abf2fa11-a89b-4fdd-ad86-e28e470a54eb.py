# Generated from: abf2fa11-a89b-4fdd-ad86-e28e470a54eb.json
# Description: This process involves verifying the authenticity of ancient artifacts through a series of interdisciplinary activities combining scientific analysis, provenance research, and expert validation. The workflow starts with artifact intake and initial physical assessment, followed by multi-modal imaging techniques to detect hidden markings and material composition. Next, chemical dating and isotopic analysis help establish temporal origins. Concurrently, archival research cross-references historical records to confirm provenance chains. Expert panels review combined findings and assess cultural significance. Digital replication and blockchain registration ensure traceability. Finally, the artifact is either certified authentic or flagged for further investigation, with detailed reports generated for stakeholders and regulatory compliance.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
ArtifactIntake = Transition(label='Artifact Intake')
PhysicalCheck = Transition(label='Physical Check')
ImagingScan = Transition(label='Imaging Scan')
MaterialTest = Transition(label='Material Test')
ChemicalDating = Transition(label='Chemical Dating')
IsotopicAnalysis = Transition(label='Isotopic Analysis')
ArchiveReview = Transition(label='Archive Review')
ProvenanceCheck = Transition(label='Provenance Check')
ExpertPanel = Transition(label='Expert Panel')
CulturalAssess = Transition(label='Cultural Assess')
DigitalReplica = Transition(label='Digital Replica')
BlockchainReg = Transition(label='Blockchain Reg')
ReportDraft = Transition(label='Report Draft')
ComplianceReview = Transition(label='Compliance Review')
FinalCertification = Transition(label='Final Certification')

# Define partial orders and choices based on process description

# Step 1: Artifact Intake and Physical Check sequentially
step1 = StrictPartialOrder(nodes=[ArtifactIntake, PhysicalCheck])
step1.order.add_edge(ArtifactIntake, PhysicalCheck)

# Step 2: Multi-modal imaging and material tests concurrent
imaging_and_material = StrictPartialOrder(nodes=[ImagingScan, MaterialTest])
# no edges => concurrent

# Step 3: Chemical Dating and Isotopic Analysis concurrent
chemical_and_isotopic = StrictPartialOrder(nodes=[ChemicalDating, IsotopicAnalysis])
# no edges => concurrent

# Step 2 & 3 combined sequentially after step1
step2_and_3 = StrictPartialOrder(nodes=[imaging_and_material, chemical_and_isotopic])
step2_and_3.order.add_edge(imaging_and_material, chemical_and_isotopic)

# Step 4: Archival research and Provenance Check concurrent
archival_and_provenance = StrictPartialOrder(nodes=[ArchiveReview, ProvenanceCheck])
# no edges => concurrent

# Step 5 & 6: Expert Panel and Cultural Assess sequential
expert_and_cultural = StrictPartialOrder(nodes=[ExpertPanel, CulturalAssess])
expert_and_cultural.order.add_edge(ExpertPanel, CulturalAssess)

# Step 4 (archival_and_provenance) feeds into Step 5&6 (expert_and_cultural)
step4_and_5 = StrictPartialOrder(nodes=[archival_and_provenance, expert_and_cultural])
# All archival and provenance precede expert panel start
step4_and_5.order.add_edge(archival_and_provenance, expert_and_cultural)

# After step 3 finishes, steps 4&5 run concurrently to step 3 (To capture concurrency between scientific analysis and archival-expert)
# But description states archival concurrent with chemical dating and isotopic analysis but step 4 starts concurrently to those
# Refine concurrency between (step2_and_3) and (step4_and_5):
# Actually the description says archival research is concurrent with chemical dating/isotopic
# So split step2_and_3 into two parts:
# (ImagingScan & MaterialTest)
# (ChemicalDating & IsotopicAnalysis & ArchiveReview & ProvenanceCheck)

# Let's reorganize Step 3 and 4 for concurrency:

# imaging_and_material (Step 2)
# second group: chemical_and_isotopic + archival_and_provenance concurrent

chem_iso_and_archprov = StrictPartialOrder(
    nodes=[chemical_and_isotopic, archival_and_provenance]
)
# no edge => concurrent

# Now step1 --> imaging_and_material and step1 --> chem_iso_and_archprov concurrently
after_step1 = StrictPartialOrder(
    nodes=[imaging_and_material, chem_iso_and_archprov]
)
after_step1.order.add_edge(imaging_and_material, chem_iso_and_archprov)  # from description: "Next" (suggests imaging precedes chemical/archival?)

# The description is ambiguous here: "Next, chemical dating and isotopic analysis... Concurrently, archival research..."
# This means chemical dating & isotopic analysis run, and at the same time archival research & provenance check run.
# So chemical_and_isotopic concurrent with archival_and_provenance, after imaging_and_material

# So after physical check:
# imaging_and_material first
# then chemical_and_isotopic concurrent with archival_and_provenance

# So step1 --> imaging_and_material --> (chemical_and_isotopic || archival_and_provenance)

step_after_physical = StrictPartialOrder(
    nodes=[imaging_and_material, chem_iso_and_archprov]
)
step_after_physical.order.add_edge(imaging_and_material, chem_iso_and_archprov)

# expert_and_cultural follows chemical_and_isotopic + archival_and_provenance
# So expert_and_cultural depends on chem_iso_and_archprov

after_expert = StrictPartialOrder(
    nodes=[chem_iso_and_archprov, expert_and_cultural]
)
after_expert.order.add_edge(chem_iso_and_archprov, expert_and_cultural)

# Digital replication and blockchain registration concurrent after expert assessment

digital_and_blockchain = StrictPartialOrder(nodes=[DigitalReplica, BlockchainReg])
# no edges => concurrent

# Digital & Blockchain after expert_and_cultural
after_digital = StrictPartialOrder(
    nodes=[expert_and_cultural, digital_and_blockchain]
)
after_digital.order.add_edge(expert_and_cultural, digital_and_blockchain)

# Reporting and compliance sequential after digital_and_blockchain
report_and_compliance = StrictPartialOrder(nodes=[ReportDraft, ComplianceReview])
report_and_compliance.order.add_edge(ReportDraft, ComplianceReview)

# After digital_and_blockchain comes report_and_compliance
after_report = StrictPartialOrder(
    nodes=[digital_and_blockchain, report_and_compliance]
)
after_report.order.add_edge(digital_and_blockchain, report_and_compliance)

# Final certification either certifies or flags for further investigation
# The description says "Finally, the artifact is either certified authentic or flagged for further investigation"
# We do not have explicit activity for flagging; only "Final Certification"
# We'll model Final Certification as last step (since no flagging activity given),
# assuming flagging is implicit in possible non-completion.

# Final Certification after compliance review
final_step = StrictPartialOrder(
    nodes=[ComplianceReview, FinalCertification]
)
final_step.order.add_edge(ComplianceReview, FinalCertification)

# Assemble the full workflow

# Step1 node: step1 (Artifact Intake -> Physical Check)
# Step2 node: step_after_physical (imaging_and_material -> (chemical_and_isotopic || archival_and_provenance))
# Step3 node: after_expert (chem_iso_and_archprov -> expert_and_cultural)
# Step4 node: after_digital (expert_and_cultural -> digital_and_blockchain)
# Step5 node: after_report (digital_and_blockchain -> report_and_compliance)
# Step6 node: final_step (ComplianceReview -> FinalCertification)

# Chain all with edges
root = StrictPartialOrder(
    nodes=[
        step1,
        step_after_physical,
        after_expert,
        after_digital,
        after_report,
        final_step,
    ]
)
root.order.add_edge(step1, step_after_physical)
root.order.add_edge(step_after_physical, after_expert)
root.order.add_edge(after_expert, after_digital)
root.order.add_edge(after_digital, after_report)
root.order.add_edge(after_report, final_step)