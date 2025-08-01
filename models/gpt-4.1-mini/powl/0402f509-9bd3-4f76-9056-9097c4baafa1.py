# Generated from: 0402f509-9bd3-4f76-9056-9097c4baafa1.json
# Description: This process outlines the detailed workflow for authenticating historical artifacts prior to acquisition by a museum or private collector. It involves multidisciplinary examination phases including provenance verification, material composition analysis, stylistic comparison, and digital forensics. Each step requires collaboration among historians, chemists, and data scientists. The workflow also incorporates risk assessment, legal compliance checks, and final documentation preparation. The aim is to minimize forgery risk while ensuring cultural and legal integrity, involving iterative feedback loops between experts and external databases before final acquisition approval.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Initial_Review = Transition(label='Initial Review')
Provenance_Check = Transition(label='Provenance Check')
Material_Testing = Transition(label='Material Testing')
Style_Analysis = Transition(label='Style Analysis')
Digital_Scan = Transition(label='Digital Scan')
Forensic_Audit = Transition(label='Forensic Audit')
Expert_Panel = Transition(label='Expert Panel')
Data_Crossref = Transition(label='Data Crossref')
Risk_Assess = Transition(label='Risk Assess')
Legal_Verify = Transition(label='Legal Verify')
Ethics_Review = Transition(label='Ethics Review')
Ownership_Trace = Transition(label='Ownership Trace')
Condition_Report = Transition(label='Condition Report')
Auth_Certify = Transition(label='Auth Certify')
Final_Approval = Transition(label='Final Approval')
Archive_Entry = Transition(label='Archive Entry')

skip = SilentTransition()

# Loop for interdisciplinary iterative feedback:
# loop on (Expert_Panel + Data_Crossref) between testing/analysis and risk/legal
# We'll model this loop as: execute the "body" (Test+Analysis), then the loop body (Expert_Panel, Data_Crossref),
# then choose to exit or repeat the loop.

# Partial order for testing and analyses (provenance, material, style, digital, forensic)
Testing_Analysis = StrictPartialOrder(nodes=[
    Provenance_Check,
    Material_Testing,
    Style_Analysis,
    Digital_Scan,
    Forensic_Audit
])
# These testing activities are concurrent (no order edges)

# After testing & analysis, there's the loop where Experts panel and Data Crossref interact iteratively:
# The loop body is Expert_Panel then Data_Crossref.
Expert_Data_PO = StrictPartialOrder(nodes=[Expert_Panel, Data_Crossref])
Expert_Data_PO.order.add_edge(Expert_Panel, Data_Crossref)

# The loop is: after Testing_Analysis, run Expert_Data_PO, then either exit or repeat Expert_Data_PO again
# so * (Expert_Data_PO, skip) would be inverted; as per POWL definition, * (A,B):
# execute A, then choose either exit or (execute B then A again)
# Here, take A=Expert_Data_PO and B=skip? 
# But skip is empty, so that means no iteration. Instead, to model "loop executing Expert_Data_PO repeatedly":
# We can set the loop as * (Expert_Data_PO, skip)
loop_expert_data = OperatorPOWL(operator=Operator.LOOP, children=[Expert_Data_PO, skip])

# After the loop, proceed to final compliance checks: Risk, Legal, Ethics, Ownership trace, Condition Report
Compliance_Checks = StrictPartialOrder(nodes=[
    Risk_Assess,
    Legal_Verify,
    Ethics_Review,
    Ownership_Trace,
    Condition_Report
])
# All compliance checks concurrent

# Then Auth Certify, Final Approval, Archive Entry in sequence
Final_Seq = StrictPartialOrder(nodes=[Auth_Certify, Final_Approval, Archive_Entry])
Final_Seq.order.add_edge(Auth_Certify, Final_Approval)
Final_Seq.order.add_edge(Final_Approval, Archive_Entry)

# The overall sequence:
# Initial Review -> Testing_Analysis -> loop_expert_data -> Compliance_Checks -> Final_Seq

nodes = [
    Initial_Review,
    Testing_Analysis,
    loop_expert_data,
    Compliance_Checks,
    Final_Seq
]

root = StrictPartialOrder(nodes=nodes)

# Define edges to form the sequence

root.order.add_edge(Initial_Review, Testing_Analysis)

root.order.add_edge(Testing_Analysis, loop_expert_data)

root.order.add_edge(loop_expert_data, Compliance_Checks)

root.order.add_edge(Compliance_Checks, Final_Seq)