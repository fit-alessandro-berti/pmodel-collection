# Generated from: 00ccd9bd-06f0-4add-bc93-4cfe53db383b.json
# Description: This process involves integrating quantum computing algorithms into traditional supply chain management to optimize inventory, forecasting, and logistics dynamically in real-time. The workflow incorporates quantum data encryption, probabilistic demand modeling, and adaptive routing that reacts to environmental changes and market volatility instantly. It also includes cross-border regulatory compliance checks using AI-driven legal scanners and blockchain verification, ensuring secure and transparent transactions across multiple stakeholders. The process ends with continuous feedback loops from IoT sensors and predictive maintenance schedules, enabling proactive risk mitigation and sustainable resource allocation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
t_di = Transition(label='Data Ingestion')
t_qe = Transition(label='Quantum Encrypt')
t_dm = Transition(label='Demand Model')
t_ia = Transition(label='Inventory Audit')
t_ro = Transition(label='Route Optimize')
t_cs = Transition(label='Compliance Scan')
t_bv = Transition(label='Blockchain Verify')
t_ra = Transition(label='Risk Assess')
t_ss = Transition(label='Stakeholder Sync')
t_fa = Transition(label='Forecast Adjust')
t_oc = Transition(label='Order Confirm')
t_st = Transition(label='Shipment Track')
t_im = Transition(label='IoT Monitor')
t_mp = Transition(label='Maintenance Plan')
t_ra2 = Transition(label='Resource Allocate')
t_fl = Transition(label='Feedback Loop')

# Define the maintenance/feedback sub-process for the loop
po_maintenance = StrictPartialOrder(nodes=[t_mp, t_ra2, t_fl])
po_maintenance.order.add_edge(t_mp, t_ra2)
po_maintenance.order.add_edge(t_ra2, t_fl)

# Loop: monitor, then either exit or run maintenance+feedback and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[t_im, po_maintenance])

# Build the top-level partial order
root = StrictPartialOrder(
    nodes=[
        t_di, t_qe, t_dm,
        t_ia, t_ro,
        t_cs, t_bv,
        t_ra, t_ss, t_fa,
        t_oc, t_st,
        loop
    ]
)

# Sequence: Data Ingestion -> Quantum Encrypt -> Demand Model
root.order.add_edge(t_di, t_qe)
root.order.add_edge(t_qe, t_dm)

# After Demand Model, run Inventory Audit and Route Optimize in parallel
root.order.add_edge(t_dm, t_ia)
root.order.add_edge(t_dm, t_ro)

# After inventory & routing, do compliance scan & blockchain verify (both depend on both)
root.order.add_edge(t_ia, t_cs)
root.order.add_edge(t_ia, t_bv)
root.order.add_edge(t_ro, t_cs)
root.order.add_edge(t_ro, t_bv)

# After compliance checks, do risk assessment
root.order.add_edge(t_cs, t_ra)
root.order.add_edge(t_bv, t_ra)

# After risk assess: forecast adjust and stakeholder sync in parallel
root.order.add_edge(t_ra, t_fa)
root.order.add_edge(t_ra, t_ss)

# Both forecasts and stakeholder sync must complete before order confirm
root.order.add_edge(t_fa, t_oc)
root.order.add_edge(t_ss, t_oc)

# Then shipment track
root.order.add_edge(t_oc, t_st)

# Finally enter the continuous monitoring & maintenance loop
root.order.add_edge(t_st, loop)