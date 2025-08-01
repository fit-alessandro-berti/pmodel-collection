# Generated from: 00101ae1-ac00-48cd-808a-3a2cc82d2f1f.json
# Description: This process involves the comprehensive examination, verification, and certification of historical artifacts to ensure their authenticity and provenance. It starts with initial intake and cataloging, followed by multi-disciplinary scientific analysis including radiocarbon dating, material composition, and stylistic comparison. Experts then conduct provenance research through archival investigation. Subsequent steps involve digital 3D scanning and condition assessment before final authentication certification. The process concludes with secure storage recommendations and preparation for public exhibition or private sale, ensuring the artifact's integrity is maintained throughout.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
artifact_intake = Transition(label='Artifact Intake')
initial_catalog = Transition(label='Initial Catalog')

# Multidisciplinary scientific analysis: Radiocarbon Test, Material Analysis, Stylistic Review (concurrent)
radiocarbon_test = Transition(label='Radiocarbon Test')
material_analysis = Transition(label='Material Analysis')
stylistic_review = Transition(label='Stylistic Review')
scientific_analysis = StrictPartialOrder(nodes=[radiocarbon_test, material_analysis, stylistic_review])
# no order edges among these 3, they are concurrent

historical_research = Transition(label='Historical Research')
provenance_check = Transition(label='Provenance Check')

# provenance research sequence
provenance_research = StrictPartialOrder(nodes=[historical_research, provenance_check])
provenance_research.order.add_edge(historical_research, provenance_check)

# Next steps concurrent: 3D Scanning and Condition Survey
scanning = Transition(label='3D Scanning')
condition_survey = Transition(label='Condition Survey')
pre_auth = StrictPartialOrder(nodes=[scanning, condition_survey])
# no order edges = concurrent

expert_panel = Transition(label='Expert Panel')
authentication_cert = Transition(label='Authentication Cert')

report_draft = Transition(label='Report Draft')

storage_planning = Transition(label='Storage Planning')

# choice at end: Exhibit Prep or Sale Coordination
exhibit_prep = Transition(label='Exhibit Prep')
sale_coordination = Transition(label='Sale Coordination')
final_choice = OperatorPOWL(operator=Operator.XOR, children=[exhibit_prep, sale_coordination])

# Construct sequence:

# 1) artifact_intake --> initial_catalog
start_seq = StrictPartialOrder(nodes=[artifact_intake, initial_catalog])
start_seq.order.add_edge(artifact_intake, initial_catalog)

# 2) initial_catalog --> scientific_analysis
after_catalog = StrictPartialOrder(nodes=[start_seq, scientific_analysis])
after_catalog.order.add_edge(start_seq, scientific_analysis)

# 3) scientific_analysis --> provenance_research
after_science = StrictPartialOrder(nodes=[after_catalog, provenance_research])
after_science.order.add_edge(after_catalog, provenance_research)

# 4) provenance_research --> pre_auth (3D scanning + condition)
after_prov = StrictPartialOrder(nodes=[after_science, pre_auth])
after_prov.order.add_edge(after_science, pre_auth)

# 5) pre_auth --> expert_panel --> authentication_cert
panel_and_cert = StrictPartialOrder(nodes=[expert_panel, authentication_cert])
panel_and_cert.order.add_edge(expert_panel, authentication_cert)

after_pan_cert = StrictPartialOrder(nodes=[after_prov, panel_and_cert])
after_pan_cert.order.add_edge(after_prov, panel_and_cert)

# 6) authentication_cert --> report draft --> storage planning
report_and_storage = StrictPartialOrder(nodes=[report_draft, storage_planning])
report_and_storage.order.add_edge(report_draft, storage_planning)

after_storage = StrictPartialOrder(nodes=[after_pan_cert, report_and_storage])
after_storage.order.add_edge(after_pan_cert, report_and_storage)

# 7) storage planning --> final choice (exhibit or sale)
final_seq = StrictPartialOrder(nodes=[after_storage, final_choice])
final_seq.order.add_edge(after_storage, final_choice)

root = final_seq