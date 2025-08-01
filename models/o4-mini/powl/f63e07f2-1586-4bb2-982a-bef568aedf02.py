# Generated from: f63e07f2-1586-4bb2-982a-bef568aedf02.json
# Description: This process outlines the intricate steps involved in authenticating rare historical artifacts for a private museum collection. It begins with initial artifact intake, followed by provenance verification through archival research and expert interviews. Subsequently, advanced material analysis using spectroscopy and radiocarbon dating is conducted to determine the artifact's age and composition. Concurrently, digital imaging and 3D modeling capture detailed visual data. A collaborative review meeting with historians, scientists, and curators evaluates all collected data to reach a consensus on authenticity. If authenticated, the artifact undergoes conservation assessment and customized preservation planning. Finally, detailed documentation is archived and a public exhibition strategy is developed, ensuring the artifact's historical integrity is maintained while maximizing educational impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# define transitions
intake = Transition(label='Artifact Intake')
prov = Transition(label='Provenance Check')
archive = Transition(label='Archive Research')
expert = Transition(label='Expert Interview')
material = Transition(label='Material Analysis')
spectro = Transition(label='Spectroscopy Test')
carbon = Transition(label='Carbon Dating')
digi = Transition(label='Digital Imaging')
model3d = Transition(label='3D Modeling')
data_rev = Transition(label='Data Review')
consensus = Transition(label='Consensus Meeting')
cons_plan = Transition(label='Conservation Plan')
preserv = Transition(label='Preservation Setup')
doc = Transition(label='Documentation')
expo = Transition(label='Exhibition Prep')

# assemble the partial order
root = StrictPartialOrder(nodes=[
    intake, prov, archive, expert,
    material, spectro, carbon,
    digi, model3d, data_rev,
    consensus, cons_plan, preserv,
    doc, expo
])

# define the control-flow dependencies
root.order.add_edge(intake, prov)

# provenance tasks
root.order.add_edge(prov, archive)
root.order.add_edge(prov, expert)

# material analysis starts after provenance
root.order.add_edge(archive, material)
root.order.add_edge(expert, material)

# material analysis subtasks
root.order.add_edge(material, spectro)
root.order.add_edge(material, carbon)

# digital capture runs concurrently after provenance
root.order.add_edge(prov, digi)
root.order.add_edge(prov, model3d)

# data review after all analyses and imaging
root.order.add_edge(spectro, data_rev)
root.order.add_edge(carbon, data_rev)
root.order.add_edge(digi, data_rev)
root.order.add_edge(model3d, data_rev)

# consensus meeting after data review
root.order.add_edge(data_rev, consensus)

# conservation planning sequence
root.order.add_edge(consensus, cons_plan)
root.order.add_edge(cons_plan, preserv)

# final documentation and exhibition prep in parallel
root.order.add_edge(preserv, doc)
root.order.add_edge(preserv, expo)