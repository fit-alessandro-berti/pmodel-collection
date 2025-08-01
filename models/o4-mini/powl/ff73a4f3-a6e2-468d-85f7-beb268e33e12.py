# Generated from: ff73a4f3-a6e2-468d-85f7-beb268e33e12.json
# Description: This process involves the strategic identification, retrieval, and reintegration of lost or archived corporate artifacts such as legacy software, deprecated hardware, or obsolete documentation. The process begins with artifact discovery through audits and employee interviews, followed by risk assessment to determine value and potential hazards. Next, retrieval plans are developed considering legal, technical, and security constraints. After recovery, artifacts undergo validation and restoration to ensure usability. Finally, reintegration involves updating current systems or archives, training relevant staff, and documenting lessons learned to prevent future losses. This atypical process ensures valuable corporate knowledge and assets are preserved and leveraged despite their age or initial obsolescence.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
audit = Transition(label='Audit Artifacts')
interview = Transition(label='Interview Staff')
assess = Transition(label='Assess Risks')
plan = Transition(label='Plan Retrieval')
legal = Transition(label='Legal Review')
security = Transition(label='Security Check')
execute = Transition(label='Execute Recovery')
validate = Transition(label='Validate Items')
restore = Transition(label='Restore Function')
update = Transition(label='Update Systems')
archive = Transition(label='Archive Records')
train = Transition(label='Train Users')
document = Transition(label='Document Findings')
review = Transition(label='Review Lessons')
close = Transition(label='Close Process')

# Choice between updating systems or archiving records
reintegr_choice = OperatorPOWL(operator=Operator.XOR, children=[update, archive])

# Build the partial order
root = StrictPartialOrder(nodes=[
    audit, interview, assess, plan, legal, security,
    execute, validate, restore, reintegr_choice,
    train, document, review, close
])

# Discovery phase: audit and interview precede assessment
root.order.add_edge(audit, assess)
root.order.add_edge(interview, assess)

# Planning phase
root.order.add_edge(assess, plan)
root.order.add_edge(plan, legal)
root.order.add_edge(plan, security)

# Retrieval execution
root.order.add_edge(legal, execute)
root.order.add_edge(security, execute)
root.order.add_edge(execute, validate)
root.order.add_edge(validate, restore)

# Reintegration choice
root.order.add_edge(restore, reintegr_choice)

# Post‐reintegration activities
root.order.add_edge(reintegr_choice, train)
root.order.add_edge(reintegr_choice, document)
root.order.add_edge(train, document)

# Lessons review and closure
root.order.add_edge(document, review)
root.order.add_edge(review, close)