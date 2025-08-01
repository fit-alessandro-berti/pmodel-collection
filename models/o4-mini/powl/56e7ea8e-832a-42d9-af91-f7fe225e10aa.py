# Generated from: 56e7ea8e-832a-42d9-af91-f7fe225e10aa.json
# Description: This process involves the complex and meticulous evaluation of antique artifacts to verify their authenticity and provenance. It includes initial visual inspection, material analysis using advanced spectroscopy, historical research through archival records, expert consultations, and multi-layered documentation. The process must navigate legal restrictions, cultural sensitivities, and potential forgeries. Each artifact undergoes condition assessment, digital imaging, and comparison against known databases. Finally, results are compiled into a comprehensive report that supports insurance, sale, or museum acquisition decisions. The process requires interdisciplinary collaboration and can take several months to complete due to the depth of analysis and verification steps involved.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
inspect = Transition(label='Initial Inspection')
material = Transition(label='Material Analysis')
research = Transition(label='Historical Research')
expert = Transition(label='Expert Consult')
legal = Transition(label='Legal Review')
cond = Transition(label='Condition Check')
digital = Transition(label='Digital Imaging')
db = Transition(label='Database Compare')
forgery = Transition(label='Forgery Detection')
prov = Transition(label='Provenance Trace')
cultural = Transition(label='Cultural Assessment')
documentation = Transition(label='Documentation')
insurance = Transition(label='Insurance Review')
report = Transition(label='Report Compilation')
final = Transition(label='Final Approval')
skip = SilentTransition()

# Loop: do historical research then expert consult until legal review approves
A = StrictPartialOrder(nodes=[research, expert])
A.order.add_edge(research, expert)
B = StrictPartialOrder(nodes=[legal, expert])
B.order.add_edge(legal, expert)
loop = OperatorPOWL(operator=Operator.LOOP, children=[A, B])

# Concurrent provenance trace and cultural assessment
concurrent = StrictPartialOrder(nodes=[prov, cultural])
# no edge => they are concurrent

# Choice: insurance review or skip (e.g., museum acquisition path)
insurance_xor = OperatorPOWL(operator=Operator.XOR, children=[insurance, skip])

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    inspect,
    material,
    loop,
    cond,
    digital,
    db,
    forgery,
    concurrent,
    documentation,
    insurance_xor,
    report,
    final
])

# Define the control‐flow relations
root.order.add_edge(inspect, material)
root.order.add_edge(material, loop)
root.order.add_edge(loop, cond)
root.order.add_edge(cond, digital)
root.order.add_edge(digital, db)
root.order.add_edge(db, forgery)
root.order.add_edge(forgery, concurrent)
root.order.add_edge(concurrent, documentation)
root.order.add_edge(documentation, insurance_xor)
root.order.add_edge(insurance_xor, report)
root.order.add_edge(report, final)