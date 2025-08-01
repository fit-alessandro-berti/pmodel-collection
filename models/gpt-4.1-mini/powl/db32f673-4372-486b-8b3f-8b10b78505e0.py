# Generated from: db32f673-4372-486b-8b3f-8b10b78505e0.json
# Description: This process involves the intricate verification and certification of historical artifacts for museums and private collectors. It starts with initial artifact receipt and condition logging, followed by multi-modal scientific analysis including radiocarbon dating and spectroscopy. Expert consultations are scheduled to assess provenance, involving cross-referencing archival records and past ownership documentation. A risk assessment is performed to evaluate potential forgery or damage, then a digital 3D scan is created for virtual archiving. Legal compliance checks ensure cultural heritage laws are respected. The artifact is then insured, and an official certificate of authenticity is drafted and approved. Finally, the artifact is packaged under climate-controlled conditions for either display or secure storage, with ongoing monitoring scheduled for conservation purposes.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Defined activities as transitions with given labels
Receive_Artifact = Transition(label='Receive Artifact')
Condition_Log = Transition(label='Condition Log')
Radiocarbon_Test = Transition(label='Radiocarbon Test')
Spectroscopy_Scan = Transition(label='Spectroscopy Scan')
Expert_Consult = Transition(label='Expert Consult')
Provenance_Check = Transition(label='Provenance Check')
Archive_Search = Transition(label='Archive Search')
Risk_Assess = Transition(label='Risk Assess')
Scan_3D = Transition(label='3D Scan')
Legal_Review = Transition(label='Legal Review')
Insurance_Setup = Transition(label='Insurance Setup')
Certificate_Draft = Transition(label='Certificate Draft')
Certificate_Approve = Transition(label='Certificate Approve')
Climate_Pack = Transition(label='Climate Pack')
Conservation_Plan = Transition(label='Conservation Plan')
Monitoring_Schedule = Transition(label='Monitoring Schedule')

# Create a partial order model

# Scientific analysis includes Radiocarbon Test and Spectroscopy Scan, seem concurrent
scientific_analysis = StrictPartialOrder(nodes=[Radiocarbon_Test, Spectroscopy_Scan])

# Expert Consult involves Provenance Check and Archive Search, done concurrectly before Expert Consult
provenance_checks = StrictPartialOrder(nodes=[Provenance_Check, Archive_Search])
provenance_and_expert = StrictPartialOrder(nodes=[provenance_checks, Expert_Consult])
provenance_and_expert.order.add_edge(provenance_checks, Expert_Consult)

# Certificate Draft then Certificate Approve sequentially
certificate_seq = StrictPartialOrder(nodes=[Certificate_Draft, Certificate_Approve])
certificate_seq.order.add_edge(Certificate_Draft, Certificate_Approve)

# Climate Pack before Conservation Plan and Monitoring Schedule concurrently
conservation_and_monitoring = StrictPartialOrder(nodes=[Conservation_Plan, Monitoring_Schedule])
climate_and_monitor = StrictPartialOrder(nodes=[Climate_Pack, conservation_and_monitoring])
climate_and_monitor.order.add_edge(Climate_Pack, conservation_and_monitoring)

# Build full partial order adhering to the described order:
# Receive Artifact --> Condition Log --> scientific_analysis (Radiocarbon + Spectroscopy)
# scientific_analysis --> provenance_and_expert (Provenance Check + Archive Search concurrent, then Expert Consult)
# provenance_and_expert --> Risk Assess --> 3D Scan --> Legal Review --> Insurance Setup --> certificate_seq --> climate_and_monitor

root = StrictPartialOrder(nodes=[
    Receive_Artifact,
    Condition_Log,
    scientific_analysis,
    provenance_and_expert,
    Risk_Assess,
    Scan_3D,
    Legal_Review,
    Insurance_Setup,
    certificate_seq,
    climate_and_monitor
])

# Adding edges to define dependencies
root.order.add_edge(Receive_Artifact, Condition_Log)
root.order.add_edge(Condition_Log, scientific_analysis)
root.order.add_edge(scientific_analysis, provenance_and_expert)
root.order.add_edge(provenance_and_expert, Risk_Assess)
root.order.add_edge(Risk_Assess, Scan_3D)
root.order.add_edge(Scan_3D, Legal_Review)
root.order.add_edge(Legal_Review, Insurance_Setup)
root.order.add_edge(Insurance_Setup, certificate_seq)
root.order.add_edge(certificate_seq, climate_and_monitor)