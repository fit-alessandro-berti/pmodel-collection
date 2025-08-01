# Generated from: 27c1e2ba-f7cb-443e-9afa-a57e143b78a4.json
# Description: This process outlines the comprehensive steps involved in authenticating antique artifacts for auction purposes. It begins with initial artifact intake and provenance verification, followed by detailed material composition analysis using advanced spectroscopy. Next, stylistic and historical context assessments are performed by experts, complemented by digital imaging and 3D scanning to detect restoration or forgery. The process involves cross-referencing with global artifact databases and consultation with external historians. A risk evaluation is then conducted to estimate potential market value and legal considerations. Finally, a certification report is generated and archived, with recommendations for preservation or restoration. The process ensures thorough validation to maintain auction integrity and client trust.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
ai = Transition(label='Artifact Intake')
pc = Transition(label='Provenance Check')
ms = Transition(label='Material Scan')
sa = Transition(label='Spectral Analysis')
sr = Transition(label='Stylistic Review')
hc = Transition(label='Historical Context')
ti = Transition(label='3D Imaging')
fd = Transition(label='Forgery Detection')
dc = Transition(label='Database Crossref')
ec = Transition(label='Expert Consult')
ra = Transition(label='Risk Assessment')
ve = Transition(label='Value Estimation')
lr = Transition(label='Legal Review')
rg = Transition(label='Report Generation')
ast = Transition(label='Archive Storage')
pp = Transition(label='Preservation Plan')

# Build the partial order
root = StrictPartialOrder(nodes=[ai, pc, ms, sa, sr, hc, ti, fd, dc, ec, ra, ve, lr, rg, ast, pp])

# Sequential flow from intake through provenance and material analysis
root.order.add_edge(ai, pc)
root.order.add_edge(pc, ms)
root.order.add_edge(ms, sa)

# After spectral analysis, run stylistic & historical reviews in parallel
root.order.add_edge(sa, sr)
root.order.add_edge(sa, hc)

# After spectral analysis, run 3D imaging → forgery detection
root.order.add_edge(sa, ti)
root.order.add_edge(ti, fd)

# Cross-reference and expert consultation wait for review and detection branches
for pre in [sr, hc, fd]:
    root.order.add_edge(pre, dc)
    root.order.add_edge(pre, ec)

# Risk assessment after cross-ref and consult
root.order.add_edge(dc, ra)
root.order.add_edge(ec, ra)

# Value estimation and legal review in parallel after risk assessment
root.order.add_edge(ra, ve)
root.order.add_edge(ra, lr)

# Report generation after both estimation and legal review
root.order.add_edge(ve, rg)
root.order.add_edge(lr, rg)

# Final archiving and preservation planning in parallel
root.order.add_edge(rg, ast)
root.order.add_edge(rg, pp)