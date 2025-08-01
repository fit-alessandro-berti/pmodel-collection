# Generated from: f809f07d-752b-4d60-862e-6c114c2857a8.json
# Description: This process involves the intricate authentication of rare cultural artifacts obtained through unconventional channels. The workflow begins with provenance verification, followed by material composition analysis using advanced spectroscopy. Parallelly, historical context validation is performed via archival research and expert consultations. Once initial checks pass, the artifact undergoes digital 3D scanning and microscopic wear pattern analysis. Subsequent steps include cross-referencing with stolen artifact databases and coordinating with international law enforcement. Final stages involve certification issuance, secure documentation, and client briefing. This atypical process ensures high confidence in artifact legitimacy, balancing scientific rigor with legal compliance and ethical considerations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

t_prov = Transition(label='Provenance Check')
t_mat = Transition(label='Material Test')
t_arch = Transition(label='Archive Search')
t_exp = Transition(label='Expert Review')
t_scan = Transition(label='3D Scanning')
t_wear = Transition(label='Wear Analysis')
t_db = Transition(label='Database Cross')
t_law = Transition(label='Law Consult')
t_forg = Transition(label='Forgery Detect')
t_risk = Transition(label='Risk Assessment')
t_cert = Transition(label='Certification')
t_doc = Transition(label='Document Prep')
t_brief = Transition(label='Client Brief')
t_store = Transition(label='Secure Storage')
t_final = Transition(label='Final Approval')

root = StrictPartialOrder(nodes=[
    t_prov, t_mat, t_arch, t_exp, t_scan, t_wear,
    t_db, t_law, t_forg, t_risk, t_cert, t_doc,
    t_brief, t_store, t_final
])

root.order.add_edge(t_prov, t_mat)
root.order.add_edge(t_mat, t_arch)
root.order.add_edge(t_mat, t_exp)

root.order.add_edge(t_arch, t_scan)
root.order.add_edge(t_exp, t_scan)
root.order.add_edge(t_arch, t_wear)
root.order.add_edge(t_exp, t_wear)

root.order.add_edge(t_scan, t_db)
root.order.add_edge(t_wear, t_db)
root.order.add_edge(t_scan, t_law)
root.order.add_edge(t_wear, t_law)

root.order.add_edge(t_db, t_forg)
root.order.add_edge(t_law, t_forg)

root.order.add_edge(t_forg, t_risk)
root.order.add_edge(t_risk, t_cert)
root.order.add_edge(t_cert, t_doc)
root.order.add_edge(t_doc, t_brief)
root.order.add_edge(t_brief, t_store)
root.order.add_edge(t_store, t_final)