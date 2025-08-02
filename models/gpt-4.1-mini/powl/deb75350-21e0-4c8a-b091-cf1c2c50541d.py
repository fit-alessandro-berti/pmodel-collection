# Generated from: deb75350-21e0-4c8a-b091-cf1c2c50541d.json
# Description: This process outlines the detailed steps involved in authenticating historical artifacts for museum acquisition. It includes initial artifact intake, physical and chemical analysis, provenance verification through archival research, expert consultation, digital imaging, and condition reporting. The workflow ensures that each artifact undergoes rigorous scrutiny to confirm authenticity and historical significance before final acquisition decisions are made. Additionally, it integrates risk assessment related to forgery detection and coordinates with legal teams for compliance with cultural property laws. The process concludes with cataloging and secure storage preparation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Intake_Review = Transition(label='Intake Review')
Visual_Inspect = Transition(label='Visual Inspect')
Material_Test = Transition(label='Material Test')
Provenance_Check = Transition(label='Provenance Check')
Archival_Search = Transition(label='Archival Search')
Expert_Consult = Transition(label='Expert Consult')
Digital_Scan = Transition(label='Digital Scan')
Condition_Report = Transition(label='Condition Report')
Forgery_Assess = Transition(label='Forgery Assess')
Legal_Review = Transition(label='Legal Review')
Risk_Analysis = Transition(label='Risk Analysis')
Acquisition_Vote = Transition(label='Acquisition Vote')
Catalog_Entry = Transition(label='Catalog Entry')
Storage_Prep = Transition(label='Storage Prep')
Final_Approval = Transition(label='Final Approval')

# Build provenance verification subtree: X(Archival Search, Expert Consult)
Prov_Verif = OperatorPOWL(operator=Operator.XOR, children=[Archival_Search, Expert_Consult])

# Partial order for provenance check followed by provenance verification
Prov_Check_PO = StrictPartialOrder(nodes=[Provenance_Check, Prov_Verif])
Prov_Check_PO.order.add_edge(Provenance_Check, Prov_Verif)

# Risk assessment subtree: X(Forgery Assess, Risk Analysis)
Risk_Assess = OperatorPOWL(operator=Operator.XOR, children=[Forgery_Assess, Risk_Analysis])

# Loop for Physical and Chemical analysis:
# A = Material Test
# B = Visual Inspect
# Loop(A,B): do Material Test, then either exit or do Visual Inspect and then Material Test again
Physical_Chem_Analysis = OperatorPOWL(operator=Operator.LOOP, children=[Material_Test, Visual_Inspect])

# Partial order representing the core analysis sequence before acquisition vote:
# (Physical_Chem_Analysis then Prov_Check_PO then Digital Scan then Condition Report then Risk Assessment then Legal Review)
Core_Analysis = StrictPartialOrder(
    nodes=[
        Physical_Chem_Analysis,
        Prov_Check_PO,
        Digital_Scan,
        Condition_Report,
        Risk_Assess,
        Legal_Review,
    ]
)

# Define edges for core analysis linear order
Core_Analysis.order.add_edge(Physical_Chem_Analysis, Prov_Check_PO)
Core_Analysis.order.add_edge(Prov_Check_PO, Digital_Scan)
Core_Analysis.order.add_edge(Digital_Scan, Condition_Report)
Core_Analysis.order.add_edge(Condition_Report, Risk_Assess)
Core_Analysis.order.add_edge(Risk_Assess, Legal_Review)

# Partial order from Intake Review to Core Analysis
Initial_Phase = StrictPartialOrder(nodes=[Intake_Review, Core_Analysis])
Initial_Phase.order.add_edge(Intake_Review, Core_Analysis)

# Final acquisition decisions sequence: Acquisition Vote, Catalog Entry, Storage Prep, Final Approval
Final_Seq = StrictPartialOrder(
    nodes=[Acquisition_Vote, Catalog_Entry, Storage_Prep, Final_Approval]
)
Final_Seq.order.add_edge(Acquisition_Vote, Catalog_Entry)
Final_Seq.order.add_edge(Catalog_Entry, Storage_Prep)
Final_Seq.order.add_edge(Storage_Prep, Final_Approval)

# Root partial order for entire process: Initial_Phase then Final_Seq
root = StrictPartialOrder(nodes=[Initial_Phase, Final_Seq])
root.order.add_edge(Initial_Phase, Final_Seq)