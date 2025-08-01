# Generated from: 0dddba58-ee44-4fb2-bd74-d1f00dbc87fc.json
# Description: This process outlines the multi-step procedure for authenticating rare historical artifacts before acquisition by a museum. It involves initial appraisal, scientific testing including spectroscopy and radiocarbon dating, provenance verification through archival research, consultation with external experts, risk assessment for forgery, legal ownership checks, and final approval by the curatorial board. The process ensures comprehensive validation to prevent acquisition of counterfeit or illegally acquired items, balancing scholarly integrity with institutional acquisition goals. Documentation and digital archiving of each step are mandatory for transparency and future reference.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

Initial_Appraisal = Transition(label='Initial Appraisal')

# Scientific testing partial order: Visual Inspection --> Material Sampling --> choice(XOR) between Spectroscopy Test and Radiocarbon Date
Visual_Inspection = Transition(label='Visual Inspection')
Material_Sampling = Transition(label='Material Sampling')
Spectroscopy_Test = Transition(label='Spectroscopy Test')
Radiocarbon_Date = Transition(label='Radiocarbon Date')

scientific_test_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[Spectroscopy_Test, Radiocarbon_Date]
)
scientific_test = StrictPartialOrder(
    nodes=[Visual_Inspection, Material_Sampling, scientific_test_choice]
)
scientific_test.order.add_edge(Visual_Inspection, Material_Sampling)
scientific_test.order.add_edge(Material_Sampling, scientific_test_choice)

# Provenance check partial order: Provenance Check --> Archive Search
Provenance_Check = Transition(label='Provenance Check')
Archive_Search = Transition(label='Archive Search')
provenance_check_po = StrictPartialOrder(
    nodes=[Provenance_Check, Archive_Search]
)
provenance_check_po.order.add_edge(Provenance_Check, Archive_Search)

# Expert Consult
Expert_Consult = Transition(label='Expert Consult')

# Risk Assessment partial order: Forgery Analysis --> Legal Review --> Ownership Verify --> Risk Assessment
Forgery_Analysis = Transition(label='Forgery Analysis')
Legal_Review = Transition(label='Legal Review')
Ownership_Verify = Transition(label='Ownership Verify')
Risk_Assessment = Transition(label='Risk Assessment')

risk_assessment_po = StrictPartialOrder(
    nodes=[Forgery_Analysis, Legal_Review, Ownership_Verify, Risk_Assessment]
)
risk_assessment_po.order.add_edge(Forgery_Analysis, Legal_Review)
risk_assessment_po.order.add_edge(Legal_Review, Ownership_Verify)
risk_assessment_po.order.add_edge(Ownership_Verify, Risk_Assessment)

# Curator Meeting --> Final Approval
Curator_Meeting = Transition(label='Curator Meeting')
Final_Approval = Transition(label='Final Approval')
curator_po = StrictPartialOrder(
    nodes=[Curator_Meeting, Final_Approval]
)
curator_po.order.add_edge(Curator_Meeting, Final_Approval)

# Documentation partial order: Record Archive --> Digital Upload
Record_Archive = Transition(label='Record Archive')
Digital_Upload = Transition(label='Digital Upload')
documentation_po = StrictPartialOrder(
    nodes=[Record_Archive, Digital_Upload]
)
documentation_po.order.add_edge(Record_Archive, Digital_Upload)

# Now set up the full process partial order
# Initial Appraisal first
# Then scientific_test, provenance_check, expert_consult, risk_assessment concurrently after initial appraisal
# Then curator_po after the above concurrent group
# Documentation concurrent with curator_po and final_approval (documentation can happen in parallel with final approval process)
root = StrictPartialOrder(
    nodes=[
        Initial_Appraisal,
        scientific_test,
        provenance_check_po,
        Expert_Consult,
        risk_assessment_po,
        curator_po,
        documentation_po
    ]
)
# Initial appraisal precedes all concurrent: scientific_test, provenance_check, expert_consult, risk_assessment
root.order.add_edge(Initial_Appraisal, scientific_test)
root.order.add_edge(Initial_Appraisal, provenance_check_po)
root.order.add_edge(Initial_Appraisal, Expert_Consult)
root.order.add_edge(Initial_Appraisal, risk_assessment_po)

# scientific_test, provenance_check, expert_consult, risk_assessment all precede curator_po
root.order.add_edge(scientific_test, curator_po)
root.order.add_edge(provenance_check_po, curator_po)
root.order.add_edge(Expert_Consult, curator_po)
root.order.add_edge(risk_assessment_po, curator_po)

# Documentation can start after Initial Appraisal and proceed concurrently with curator_po
root.order.add_edge(Initial_Appraisal, documentation_po)

# No dependency between documentation_po and curator_po to keep parallelism
