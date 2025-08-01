# Generated from: ba91bee8-533c-4a35-95b7-2ac1060cfbce.json
# Description: This complex process involves the verification and authentication of ancient artifacts for museums and private collectors. It begins with initial artifact intake and condition assessment, followed by material analysis using spectroscopy and radiocarbon dating. Next, provenance research is conducted through archival exploration and expert consultations. If discrepancies arise, forensic imaging and chemical residue testing are employed to validate authenticity. Concurrently, legal clearance and cultural heritage compliance checks are performed. Once verified, detailed documentation and digital archiving occur, alongside stakeholder reporting and insurance valuation. The final steps include secure packaging and coordinated shipment logistics to the client, ensuring preservation and chain of custody integrity throughout the process.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
t1 = Transition(label="Artifact Intake")
t2 = Transition(label="Condition Check")
t3 = Transition(label="Material Analysis")
t4 = Transition(label="Spectroscopy Test")
t5 = Transition(label="Radiocarbon Date")
t6 = Transition(label="Provenance Research")
t7 = Transition(label="Archive Search")
t8 = Transition(label="Expert Consult")
t9 = Transition(label="Forensic Imaging")
t10 = Transition(label="Residue Testing")
t11 = Transition(label="Legal Clearance")
t12 = Transition(label="Compliance Check")
t13 = Transition(label="Documentation")
t14 = Transition(label="Digital Archive")
t15 = Transition(label="Stakeholder Report")
t16 = Transition(label="Insurance Valuation")
t17 = Transition(label="Secure Packaging")
t18 = Transition(label="Shipment Logistics")

# Silent skip for the discrepancy branch
skip = SilentTransition()

# 1. Material analysis branch: spectroscopy and radiocarbon in parallel
materialPO = StrictPartialOrder(nodes=[t4, t5])
# no order edges => t4 and t5 concurrent

# 2. Provenance research branch: archive search and expert consult in parallel
provPO = StrictPartialOrder(nodes=[t7, t8])
# no order edges => t7 and t8 concurrent

# 3. Discrepancy check choice: either perform forensic steps in order or skip
forensicPO = StrictPartialOrder(nodes=[t9, t10])
forensicPO.order.add_edge(t9, t10)  # imaging before residue testing
discrepancyXor = OperatorPOWL(operator=Operator.XOR, children=[forensicPO, skip])

# 4. Documentation branch: all four in parallel
docPO = StrictPartialOrder(nodes=[t13, t14, t15, t16])
# no order edges => all concurrent

# 5. Build the root partial order
root = StrictPartialOrder(
    nodes=[
        t1,
        t2,
        t3,
        materialPO,
        t6,
        provPO,
        discrepancyXor,
        t11,
        t12,
        docPO,
        t17,
        t18,
    ]
)

# Define the control-flow/order dependencies
root.order.add_edge(t1, t2)
root.order.add_edge(t2, t3)

# After material analysis, provenance research
root.order.add_edge(t3, materialPO)
root.order.add_edge(materialPO, t6)

# After provenance, do discrepancy choice
root.order.add_edge(t6, provPO)
root.order.add_edge(provPO, discrepancyXor)

# After discrepancy branch completes, start legal & compliance in parallel
root.order.add_edge(discrepancyXor, t11)
root.order.add_edge(discrepancyXor, t12)

# After both legal & compliance, documentation
root.order.add_edge(t11, docPO)
root.order.add_edge(t12, docPO)

# After documentation, packaging then shipment
root.order.add_edge(docPO, t17)
root.order.add_edge(t17, t18)