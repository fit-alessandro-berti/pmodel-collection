# Generated from: 3767b692-ca02-470c-a161-24638cc50de4.json
# Description: This process involves the complex authentication and provenance verification of historical artifacts sourced from multiple regions worldwide. The process begins with initial artifact receipt and condition logging, followed by multi-expert physical inspection, advanced material composition analysis, and cross-referencing with global artifact databases. Subsequent activities include digital 3D modeling, provenance chain reconstruction through archival research, and authentication report drafting. Additionally, the process integrates blockchain registration for provenance transparency, stakeholder consultation for disputed origins, and final certification issuance. Parallel steps encompass conservation recommendations, replication authorization, and secure artifact storage planning. The entire workflow demands coordination between historians, scientists, legal experts, and technology specialists to ensure authenticity, legal compliance, and preservation of cultural heritage assets.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Artifact_Receipt = Transition(label='Artifact Receipt')
Condition_Log = Transition(label='Condition Log')
Expert_Inspection = Transition(label='Expert Inspection')
Material_Analysis = Transition(label='Material Analysis')
Database_Check = Transition(label='Database Check')
_3D_Modeling = Transition(label='3D Modeling')
Provenance_Research = Transition(label='Provenance Research')
Report_Draft = Transition(label='Report Draft')
Blockchain_Register = Transition(label='Blockchain Register')
Stakeholder_Consult = Transition(label='Stakeholder Consult')
Certification_Issue = Transition(label='Certification Issue')
Conservation_Plan = Transition(label='Conservation Plan')
Replication_Review = Transition(label='Replication Review')
Storage_Design = Transition(label='Storage Design')
Legal_Compliance = Transition(label='Legal Compliance')

# Sequential initial part:
# Artifact Receipt --> Condition Log
# --> Expert Inspection --> Material Analysis --> Database Check
order_init = set()
order_init.add((Artifact_Receipt, Condition_Log))
order_init.add((Condition_Log, Expert_Inspection))
order_init.add((Expert_Inspection, Material_Analysis))
order_init.add((Material_Analysis, Database_Check))

# Next sequence:
# Database Check --> 3D Modeling --> Provenance Research --> Report Draft
order_mid = set()
order_mid.add((Database_Check, _3D_Modeling))
order_mid.add((_3D_Modeling, Provenance_Research))
order_mid.add((Provenance_Research, Report_Draft))

# Report Draft --> Blockchain Register
# Blockchain Register --> Stakeholder Consult
# Stakeholder Consult --> Certification Issue
order_end = set()
order_end.add((Report_Draft, Blockchain_Register))
order_end.add((Blockchain_Register, Stakeholder_Consult))
order_end.add((Stakeholder_Consult, Certification_Issue))

# Parallel steps after or during (parallel with the latter part of the process):
# Conservation Plan, Replication Review, Storage Design, Legal Compliance
# These are concurrent, but must start after Condition Log (i.e. after initial logging)
# Let's branch them parallel after Condition Log.
# To model that, we connect Condition_Log to each parallel activity, and from each parallel
# we connect to Stakeholder Consult or Certification Issue to synchronize ending.

# Define the parallel activities as a partial order with no internal order (fully concurrent)
parallel_nodes = [Conservation_Plan, Replication_Review, Storage_Design, Legal_Compliance]

parallel_PO = StrictPartialOrder(nodes=parallel_nodes)
# no order edges inside, fully concurrent

# full PO nodes all activities + parallel PO + the sequential flow in order
# We want to create a root PO with these nodes:
# nodes = { all seq nodes } union { parallel_PO }

# We'll embed the parallel_PO as a node in the top-level PO to keep it modular,
# then create edges from Condition_Log to parallel_PO, and from parallel_PO to Stakeholder_Consult (before Certification Issue).

# Create top level nodes list
top_nodes = [
    Artifact_Receipt, Condition_Log, Expert_Inspection, Material_Analysis, Database_Check,
    _3D_Modeling, Provenance_Research, Report_Draft, Blockchain_Register,
    Stakeholder_Consult, Certification_Issue,
    parallel_PO
]

root = StrictPartialOrder(nodes=top_nodes)

# Add all sequential edges
for src, tgt in order_init:
    root.order.add_edge(src, tgt)
for src, tgt in order_mid:
    root.order.add_edge(src, tgt)
for src, tgt in order_end:
    root.order.add_edge(src, tgt)

# Connect Condition_Log to parallel_PO (parallel subtree starts after logging)
root.order.add_edge(Condition_Log, parallel_PO)
# Connect parallel_PO to Stakeholder Consult to synchronize before final cert issuance
root.order.add_edge(parallel_PO, Stakeholder_Consult)