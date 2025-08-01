# Generated from: f3df672d-f64b-487b-b503-9bf0de9f6aa0.json
# Description: This process involves verifying the authenticity of rare and custom-made artifacts through multi-layered analysis combining historical research, material science tests, provenance validation, and expert consensus. It integrates unconventional data sources such as oral histories and blockchain records, followed by secure certification and archival. The process ensures artifacts are properly cataloged, insured, and prepared for exhibition or sale, while maintaining strict confidentiality and compliance with international cultural property laws. Final steps include continuous monitoring through IoT sensors and periodic re-validation to prevent fraud and degradation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Data_Collection = Transition(label='Data Collection')

Provenance_Check = Transition(label='Provenance Check')
Material_Scan = Transition(label='Material Scan')
Historical_Review = Transition(label='Historical Review')

Expert_Panel = Transition(label='Expert Panel')

Blockchain_Verify = Transition(label='Blockchain Verify')
Oral_History = Transition(label='Oral History')

Condition_Report = Transition(label='Condition Report')
Legal_Review = Transition(label='Legal Review')

Certification = Transition(label='Certification')
Archival_Update = Transition(label='Archival Update')

Insurance_Setup = Transition(label='Insurance Setup')
Exhibition_Prep = Transition(label='Exhibition Prep')

IoT_Monitoring = Transition(label='IoT Monitoring')
Revalidation = Transition(label='Re-validation')

# Step 1: Data Collection starts
# Step 2: Parallel analysis: Provenance, Material Scan, Historical Review
# Historical Review includes Expert Panel (sequential: Historical_Review -> Expert_Panel)

# Step 3: unconventional data sources: Blockchain Verify and Oral History run in parallel
# Step 4: Next Condition Report and Legal Review in parallel

# Step 5: Certification and Archival Update sequential

# Step 6: Insure and Exhibition prep sequential

# Step 7: Loop for continuous monitoring (IoT Monitoring) and Revalidation
# loop body: IoT Monitoring -> choice(exit or Re-validation then IoT Monitoring again)

# Build partial orders and operators according to steps:

# Historical review sequence
hist_seq = StrictPartialOrder(nodes=[Historical_Review, Expert_Panel])
hist_seq.order.add_edge(Historical_Review, Expert_Panel)

# Step 2 parallel analyses
analysis_PO = StrictPartialOrder(
    nodes=[Provenance_Check, Material_Scan, hist_seq]
)
# no order edges = concurrent

# Step 3 unconventional data sources in parallel
unconventional_PO = StrictPartialOrder(nodes=[Blockchain_Verify, Oral_History])
# no order edges = concurrent

# Step 4 condition and legal parallel
condition_legal_PO = StrictPartialOrder(nodes=[Condition_Report, Legal_Review])

# Step 5 certification then archival update sequence
cert_arch_seq = StrictPartialOrder(nodes=[Certification, Archival_Update])
cert_arch_seq.order.add_edge(Certification, Archival_Update)

# Step 6 insurance setup then exhibition prep sequence
insure_exhibit_seq = StrictPartialOrder(nodes=[Insurance_Setup, Exhibition_Prep])
insure_exhibit_seq.order.add_edge(Insurance_Setup, Exhibition_Prep)

# Step 7: LOOP of IoT Monitoring and Re-validation
# LOOP(A, B): execute A, then choose (exit or B then A again)
loop_monitor = OperatorPOWL(operator=Operator.LOOP, children=[IoT_Monitoring, Revalidation])

# Construct the overall PO combining all steps with edges showing the flow

# nodes:
# Data Collection -> Analysis -> Unconventional -> Condition/Legal -> Cert/Arch -> Insure/Exhibit -> Loop monitor

root = StrictPartialOrder(
    nodes=[
        Data_Collection,
        analysis_PO,
        unconventional_PO,
        condition_legal_PO,
        cert_arch_seq,
        insure_exhibit_seq,
        loop_monitor
    ]
)

# Add control-flow edges:
root.order.add_edge(Data_Collection, analysis_PO)
root.order.add_edge(analysis_PO, unconventional_PO)
root.order.add_edge(unconventional_PO, condition_legal_PO)
root.order.add_edge(condition_legal_PO, cert_arch_seq)
root.order.add_edge(cert_arch_seq, insure_exhibit_seq)
root.order.add_edge(insure_exhibit_seq, loop_monitor)