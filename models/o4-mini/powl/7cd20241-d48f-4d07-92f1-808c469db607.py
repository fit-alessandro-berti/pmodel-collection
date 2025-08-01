# Generated from: 7cd20241-d48f-4d07-92f1-808c469db607.json
# Description: This process outlines the steps for reclaiming and repurposing remote or stranded physical assets, such as equipment or vehicles, located in inaccessible or hazardous environments. It involves remote assessment, coordination with local authorities, specialized transport logistics, environmental compliance checks, and final reintegration into the operational inventory. The process ensures minimal downtime, cost efficiency, and adherence to safety regulations while handling assets that require unconventional retrieval methods due to geographic, legal, or operational constraints.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define the activities
audit = Transition(label='Asset Audit')
risk = Transition(label='Risk Survey')
remote = Transition(label='Remote Inspect')
local = Transition(label='Local Liaison')
permit = Transition(label='Permit Request')
notify = Transition(label='Stakeholder Notify')
transport = Transition(label='Transport Plan')
safety = Transition(label='Safety Brief')
prep = Transition(label='Equipment Prep')
extract = Transition(label='Extraction Execute')
env_check = Transition(label='Environmental Check')
damage = Transition(label='Damage Assess')
recondition = Transition(label='Reconditioning')
inventory = Transition(label='Inventory Update')
report = Transition(label='Report Submit')

# Build the partial‐order model
root = StrictPartialOrder(nodes=[
    audit, risk,
    remote, local,
    permit, notify,
    transport, safety, prep, extract,
    env_check, damage,
    recondition, inventory, report
])

# Remote assessment phase
root.order.add_edge(audit, risk)
root.order.add_edge(risk, remote)
root.order.add_edge(risk, local)

# Permit & stakeholder coordination (can proceed in parallel after liaison)
root.order.add_edge(local, permit)
root.order.add_edge(local, notify)

# Logistics planning
root.order.add_edge(permit, transport)
root.order.add_edge(notify, transport)
root.order.add_edge(transport, safety)
root.order.add_edge(safety, prep)

# Extraction execution
root.order.add_edge(prep, extract)

# Post‐extraction checks in parallel
root.order.add_edge(extract, env_check)
root.order.add_edge(extract, damage)

# Reintegration steps
root.order.add_edge(env_check, recondition)
root.order.add_edge(damage, recondition)
root.order.add_edge(recondition, inventory)
root.order.add_edge(inventory, report)