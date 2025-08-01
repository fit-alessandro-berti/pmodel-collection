# Generated from: bf8a9023-17b1-4b9b-9213-5a25c293b869.json
# Description: This process involves the systematic verification and authentication of historical artifacts acquired by museums or private collectors. It begins with initial assessment and cataloging, followed by material analysis using non-invasive technology. Experts from multiple disciplines collaborate to compare findings with historical records. The workflow includes provenance verification, condition evaluation, and risk assessment for potential forgery or damage. Upon successful authentication, secure packaging and insurance appraisal are conducted before final archival registration. Continuous monitoring and periodic re-evaluation ensure long-term preservation and authenticity validation over time.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
t1 = Transition(label='Initial Assessment')
t2 = Transition(label='Catalog Entry')
t3 = Transition(label='Material Scan')
t4 = Transition(label='Expert Review')
t5 = Transition(label='Cross Reference')
t6 = Transition(label='Provenance Check')
t7 = Transition(label='Condition Eval')
t8 = Transition(label='Forgery Risk')
t9 = Transition(label='Report Draft')
t10 = Transition(label='Secure Packaging')
t11 = Transition(label='Insurance Appraisal')
t12 = Transition(label='Archival Entry')
t13 = Transition(label='Stakeholder Brief')
t14 = Transition(label='Periodic Audit')
t15 = Transition(label='Preservation Plan')
t16 = Transition(label='Reevaluation Set')

# Parallel provenance/condition/risk checks
P_checks = StrictPartialOrder(nodes=[t6, t7, t8])
# Parallel packaging and insurance appraisal
P_post = StrictPartialOrder(nodes=[t10, t11])
# Redo part of the monitoring loop: preservation plan and reevaluation set
redo_monitor = StrictPartialOrder(nodes=[t15, t16])

# Loop for continuous monitoring and periodic re-evaluation
loop_monitor = OperatorPOWL(operator=Operator.LOOP, children=[t14, redo_monitor])

# Build the main process as a partial order
root = StrictPartialOrder(nodes=[t1, t2, t3, t4, t5, P_checks, t9, P_post, t12, t13, loop_monitor])

# Add sequencing edges
root.order.add_edge(t1, t2)
root.order.add_edge(t2, t3)
root.order.add_edge(t3, t4)
root.order.add_edge(t4, t5)
root.order.add_edge(t5, P_checks)
root.order.add_edge(P_checks, t9)
root.order.add_edge(t9, P_post)
root.order.add_edge(P_post, t12)
root.order.add_edge(t12, t13)
root.order.add_edge(t13, loop_monitor)