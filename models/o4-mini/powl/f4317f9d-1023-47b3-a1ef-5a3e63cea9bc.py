# Generated from: f4317f9d-1023-47b3-a1ef-5a3e63cea9bc.json
# Description: This process governs the intricate steps involved in authenticating rare antiques for auction houses. Starting with initial provenance research, experts conduct material analysis and stylistic comparison using both manual examination and AI-enhanced imaging. Following this, chemical tests verify aging patterns, while historical records are cross-checked with global databases. The item then undergoes expert panel review and market valuation, where risk assessments for forgery are performed. Finally, a detailed authentication report is generated and certified, after which the item is prepared for secure transport to auction. Throughout, multi-level approval and documentation ensure transparency and legal compliance in this atypical yet critical authentication process.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define the atomic activities
prov     = Transition(label='Provenance Check')
ms       = Transition(label='Material Scan')
sc       = Transition(label='Style Compare')
ai       = Transition(label='AI Imaging')
ct       = Transition(label='Chemical Test')
av       = Transition(label='Aging Verify')
rm       = Transition(label='Record Match')
dq       = Transition(label='Database Query')
pr       = Transition(label='Panel Review')
mv       = Transition(label='Market Value')
fr       = Transition(label='Forgery Risk')
rd       = Transition(label='Report Draft')
cert     = Transition(label='Certification')
app      = Transition(label='Approval Stage')
sp       = Transition(label='Secure Packing')
tp       = Transition(label='Transport Prep')

# Build the partial‐order model
root = StrictPartialOrder(
    nodes=[
        prov, ms, sc, ai,
        ct, av, rm, dq,
        pr, mv, fr, rd,
        cert, app, sp, tp
    ]
)

# Provenance Check precedes all analysis tasks
root.order.add_edge(prov, ms)
root.order.add_edge(prov, sc)
root.order.add_edge(prov, ai)

# Analysis tasks synchronize into Chemical Test
root.order.add_edge(ms, ct)
root.order.add_edge(sc, ct)
root.order.add_edge(ai, ct)
root.order.add_edge(ct, av)

# Historical record checking after the same analysis tasks
root.order.add_edge(ms, rm)
root.order.add_edge(sc, rm)
root.order.add_edge(ai, rm)
# Then cross‐check records with the global database
root.order.add_edge(rm, dq)

# After verification branches join into review and valuation
root.order.add_edge(av, pr)
root.order.add_edge(dq, pr)
root.order.add_edge(av, mv)
root.order.add_edge(dq, mv)

# Risk assessment is part of market valuation
root.order.add_edge(mv, fr)

# Drafting and certification of the report
root.order.add_edge(pr, rd)
root.order.add_edge(fr, rd)
root.order.add_edge(rd, cert)

# Final approval and secure transport preparation
root.order.add_edge(cert, app)
root.order.add_edge(app, sp)
root.order.add_edge(sp, tp)