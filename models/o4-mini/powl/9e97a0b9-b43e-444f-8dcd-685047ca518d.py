# Generated from: 9e97a0b9-b43e-444f-8dcd-685047ca518d.json
# Description: This process involves the detailed authentication of rare historical artifacts, integrating multidisciplinary expertise from provenance research to scientific analysis. Each artifact undergoes initial visual inspection, documentation review, and material composition testing using advanced spectroscopy. Provenance data is cross-checked with global registries and auction records. Anomaly detection algorithms flag inconsistencies for expert panel review. Conservation status assessment ensures proper handling protocols. Finally, a comprehensive certification report is generated, including high-resolution imaging and 3D scans, before secure archival and client delivery. The process demands coordination across historians, chemists, data scientists, and legal advisors to maintain authenticity standards and legal compliance.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# define atomic activities
vi = Transition(label='Visual Inspect')
dr = Transition(label='Document Review')
mt = Transition(label='Material Test')
sr = Transition(label='Spectroscopy Run')
rc = Transition(label='Registry Check')
av = Transition(label='Auction Verify')
af = Transition(label='Anomaly Flag')
ep = Transition(label='Expert Panel')
ca = Transition(label='Conservation Assess')
hp = Transition(label='Handle Protocol')
ic = Transition(label='Image Capture')
sc3 = Transition(label='3D Scan')
rcp = Transition(label='Report Compile')
lr = Transition(label='Legal Review')
dsync = Transition(label='Data Sync')
ast = Transition(label='Archive Store')
cd = Transition(label='Client Deliver')

# build the partial order
root = StrictPartialOrder(nodes=[
    vi, dr, mt, sr,
    rc, av, af, ep,
    ca, hp, ic, sc3,
    rcp, lr, dsync, ast, cd
])

# initial inspection and tests
root.order.add_edge(vi, dr)
root.order.add_edge(dr, mt)
root.order.add_edge(mt, sr)

# parallel provenance checks
root.order.add_edge(sr, rc)
root.order.add_edge(sr, av)

# anomaly detection and expert review
root.order.add_edge(rc, af)
root.order.add_edge(av, af)
root.order.add_edge(af, ep)

# conservation and handling
root.order.add_edge(ep, ca)
root.order.add_edge(ca, hp)

# imaging and report
root.order.add_edge(hp, ic)
root.order.add_edge(hp, sc3)
root.order.add_edge(ic, rcp)
root.order.add_edge(sc3, rcp)

# legal review and data synchronization
root.order.add_edge(rcp, lr)
root.order.add_edge(rcp, dsync)
root.order.add_edge(lr, ast)
root.order.add_edge(dsync, ast)

# archival and delivery
root.order.add_edge(ast, cd)