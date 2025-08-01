# Generated from: ff73a4f3-a6e2-468d-85f7-beb268e33e12.json
# Description: This process involves the strategic identification, retrieval, and reintegration of lost or archived corporate artifacts such as legacy software, deprecated hardware, or obsolete documentation. The process begins with artifact discovery through audits and employee interviews, followed by risk assessment to determine value and potential hazards. Next, retrieval plans are developed considering legal, technical, and security constraints. After recovery, artifacts undergo validation and restoration to ensure usability. Finally, reintegration involves updating current systems or archives, training relevant staff, and documenting lessons learned to prevent future losses. This atypical process ensures valuable corporate knowledge and assets are preserved and leveraged despite their age or initial obsolescence.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities
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
train = Transition(label='Train Users')
document = Transition(label='Document Findings')
archive = Transition(label='Archive Records')
review = Transition(label='Review Lessons')
close = Transition(label='Close Process')

# Concurrent audit and interview (artifact discovery)
discovery = StrictPartialOrder(nodes=[audit, interview])
# no order edges, concurrent

# After discovery, assess risks
order1 = StrictPartialOrder(nodes=[discovery, assess])
order1.order.add_edge(discovery, assess)

# Planning retrieval includes legal review and security check after planning
# The legal review and security check can be concurrent after plan retrieval

plan_section = StrictPartialOrder(nodes=[plan, legal, security])
plan_section.order.add_edge(plan, legal)
plan_section.order.add_edge(plan, security)

# After planning, execute recovery
order2 = StrictPartialOrder(nodes=[order1, plan_section, execute])
order2.order.add_edge(order1, plan_section)
order2.order.add_edge(plan_section, execute)

# After execute, validate and restore - validate then restore (restore depends on validate)
validate_restore = StrictPartialOrder(nodes=[validate, restore])
validate_restore.order.add_edge(validate, restore)

# Reintegration: update systems, train users, document findings, archive records, review lessons
# Updating, training, documenting, archiving, reviewing can be concurrent except reviewing depends on documenting

reintegration = StrictPartialOrder(nodes=[update, train, document, archive, review, close])
# Dependencies:
# document --> review (review depends on documenting lessons learned)
reintegration.order.add_edge(document, review)
# after reintegration comes close process depends on all others:
# close depends on update, train, review, archive at least
reintegration.order.add_edge(update, close)
reintegration.order.add_edge(train, close)
reintegration.order.add_edge(review, close)
reintegration.order.add_edge(archive, close)

# Full model PO: discovery --> assess --> plan/ (legal and security) --> execute --> validate/restore --> reintegration
# Build full partial order combining all

root = StrictPartialOrder(
    nodes=[discovery, assess, plan_section, execute, validate_restore, reintegration]
)
root.order.add_edge(discovery, assess)
root.order.add_edge(assess, plan_section)
root.order.add_edge(plan_section, execute)
root.order.add_edge(execute, validate_restore)
root.order.add_edge(validate_restore, reintegration)