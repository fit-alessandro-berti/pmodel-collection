# Generated from: 81441f5c-7e18-4939-834d-751c794fbc65.json
# Description: This process outlines the creation of a large-scale collaborative art installation involving multiple artists, engineers, and community stakeholders. It begins with concept ideation and stakeholder alignment, followed by material sourcing and prototype development. Parallel activities include regulatory compliance checks and community feedback sessions. After iterative design refinements, technical integration and structural testing are conducted to ensure safety and functionality. The installation phase involves coordinated logistics, on-site assembly, and real-time troubleshooting. Post-installation, the process includes interactive programming, public engagement events, and maintenance scheduling to sustain the artwork’s impact over time. Documentation and archival of the project complete the workflow, ensuring knowledge transfer and future reference.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
c_ideation = Transition(label='Concept Ideation')
stakeholder = Transition(label='Stakeholder Meet')
material = Transition(label='Material Sourcing')
prototype = Transition(label='Prototype Build')
compliance = Transition(label='Compliance Check')
community = Transition(label='Community Review')
design_refine = Transition(label='Design Refinement')
tech_int = Transition(label='Tech Integration')
struct_test = Transition(label='Structural Test')
logistics = Transition(label='Logistics Plan')
onsite = Transition(label='Onsite Setup')
troubleshoot = Transition(label='Troubleshoot Fix')
program = Transition(label='Program Install')
engagement = Transition(label='Engagement Event')
maintenance = Transition(label='Maintenance Plan')
archive = Transition(label='Project Archive')

# Parallel checks and reviews
checks = StrictPartialOrder(nodes=[compliance, community])
# (no order edges: concurrent)

# Loop for iterative design: perform checks/review then optionally refine and repeat
iter_loop = OperatorPOWL(operator=Operator.LOOP, children=[checks, design_refine])

# Installation phase sequence
install_seq = StrictPartialOrder(nodes=[logistics, onsite, troubleshoot])
install_seq.order.add_edge(logistics, onsite)
install_seq.order.add_edge(onsite, troubleshoot)

# Post-installation sequence including archival
post_seq = StrictPartialOrder(nodes=[program, engagement, maintenance, archive])
post_seq.order.add_edge(program, engagement)
post_seq.order.add_edge(engagement, maintenance)
post_seq.order.add_edge(maintenance, archive)

# Root workflow: full sequence
root = StrictPartialOrder(nodes=[
    c_ideation, stakeholder, material, prototype,
    iter_loop, tech_int, struct_test,
    install_seq, post_seq
])
root.order.add_edge(c_ideation, stakeholder)
root.order.add_edge(stakeholder, material)
root.order.add_edge(material, prototype)
root.order.add_edge(prototype, iter_loop)
root.order.add_edge(iter_loop, tech_int)
root.order.add_edge(tech_int, struct_test)
root.order.add_edge(struct_test, install_seq)
root.order.add_edge(install_seq, post_seq)