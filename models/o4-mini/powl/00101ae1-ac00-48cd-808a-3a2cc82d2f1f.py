# Generated from: 00101ae1-ac00-48cd-808a-3a2cc82d2f1f.json
# Description: This process involves the comprehensive examination, verification, and certification of historical artifacts to ensure their authenticity and provenance. It starts with initial intake and cataloging, followed by multi-disciplinary scientific analysis including radiocarbon dating, material composition, and stylistic comparison. Experts then conduct provenance research through archival investigation. Subsequent steps involve digital 3D scanning and condition assessment before final authentication certification. The process concludes with secure storage recommendations and preparation for public exhibition or private sale, ensuring the artifact's integrity is maintained throughout.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
intake = Transition(label='Artifact Intake')
catalog = Transition(label='Initial Catalog')
material_analysis = Transition(label='Material Analysis')
radiocarbon_test = Transition(label='Radiocarbon Test')
stylistic_review = Transition(label='Stylistic Review')
historical_research = Transition(label='Historical Research')
provenance_check = Transition(label='Provenance Check')
scanning = Transition(label='3D Scanning')
condition_survey = Transition(label='Condition Survey')
expert_panel = Transition(label='Expert Panel')
report_draft = Transition(label='Report Draft')
authentication_cert = Transition(label='Authentication Cert')
storage_planning = Transition(label='Storage Planning')
exhibit_prep = Transition(label='Exhibit Prep')
sale_coordination = Transition(label='Sale Coordination')

# Final choice: public exhibition or private sale
final_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[exhibit_prep, sale_coordination]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    intake, catalog,
    material_analysis, radiocarbon_test, stylistic_review,
    historical_research, provenance_check,
    scanning, condition_survey,
    expert_panel, report_draft, authentication_cert,
    storage_planning, final_choice
])

# Add ordering edges
# 1. Intake -> Catalog
root.order.add_edge(intake, catalog)

# 2. After catalog, parallel analyses
root.order.add_edge(catalog, material_analysis)
root.order.add_edge(catalog, radiocarbon_test)
root.order.add_edge(catalog, stylistic_review)

# 3. All analyses must complete before Historical Research
root.order.add_edge(material_analysis, historical_research)
root.order.add_edge(radiocarbon_test, historical_research)
root.order.add_edge(stylistic_review, historical_research)

# 4. Historical Research -> Provenance Check
root.order.add_edge(historical_research, provenance_check)

# 5. Provenance Check -> (3D Scanning & Condition Survey) in parallel
root.order.add_edge(provenance_check, scanning)
root.order.add_edge(provenance_check, condition_survey)

# 6. Scanning & Condition Survey -> Expert Panel
root.order.add_edge(scanning, expert_panel)
root.order.add_edge(condition_survey, expert_panel)

# 7. Expert Panel -> Report Draft -> Authentication Cert -> Storage Planning
root.order.add_edge(expert_panel, report_draft)
root.order.add_edge(report_draft, authentication_cert)
root.order.add_edge(authentication_cert, storage_planning)

# 8. Storage Planning -> final choice (Exhibit Prep or Sale Coordination)
root.order.add_edge(storage_planning, final_choice)