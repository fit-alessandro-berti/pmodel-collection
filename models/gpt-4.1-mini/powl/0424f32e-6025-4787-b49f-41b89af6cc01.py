# Generated from: 0424f32e-6025-4787-b49f-41b89af6cc01.json
# Description: This process involves the intricate steps required to authenticate rare and ancient artifacts before acquisition or exhibition. It includes multidisciplinary activities such as provenance research, material analysis, expert consultation, digital imaging, and legal clearance. The workflow ensures the artifact's legitimacy through scientific testing, historical verification, and ethical sourcing checks. Complex coordination between historians, scientists, legal advisors, and curators is essential. The process culminates in certification, secure cataloging, and preparation for transport or display, minimizing risks of fraud and preserving cultural heritage integrity.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
Preliminary_Review = Transition(label='Preliminary Review')
Provenance_Check = Transition(label='Provenance Check')
Material_Testing = Transition(label='Material Testing')
XRay_Imaging = Transition(label='XRay Imaging')
Carbon_Dating = Transition(label='Carbon Dating')
Expert_Panel = Transition(label='Expert Panel')
Historical_Analysis = Transition(label='Historical Analysis')
Legal_Clearance = Transition(label='Legal Clearance')
Ethics_Approval = Transition(label='Ethics Approval')
Condition_Report = Transition(label='Condition Report')
Digital_Scan = Transition(label='Digital Scan')
Risk_Assessment = Transition(label='Risk Assessment')
Authentication_Cert = Transition(label='Authentication Cert')
Secure_Cataloging = Transition(label='Secure Cataloging')
Transport_Prep = Transition(label='Transport Prep')
Exhibit_Setup = Transition(label='Exhibit Setup')

# Scientific testing parallel: Material Testing, XRay Imaging, Carbon Dating
scientific_tests = StrictPartialOrder(nodes=[Material_Testing, XRay_Imaging, Carbon_Dating])
# No order edges: all concurrent

# Historical verification parallel: Provenance Check, Historical Analysis, Expert Panel
historical_verification = StrictPartialOrder(nodes=[Provenance_Check, Historical_Analysis, Expert_Panel])
# No order edges: all concurrent

# Ethical and legal clearance parallel: Legal Clearance, Ethics Approval
legal_ethics = StrictPartialOrder(nodes=[Legal_Clearance, Ethics_Approval])

# Digital imaging and condition report parallel step (may happen after scientific tests or parallel)
imaging_condition = StrictPartialOrder(nodes=[Digital_Scan, Condition_Report])
# No edges; concurrent

# Risk assessment step is standalone before certification
# Define partial order of phases simulating the process:
# Preliminary Review --> (scientific_tests || historical_verification) --> legal_ethics --> imaging_condition --> Risk_Assessment --> Certification and after

# Combine scientific and historical as parallel nodes in PO
science_hist = StrictPartialOrder(nodes=[scientific_tests, historical_verification])
# No order edges, concurrent

# Combine legal_ethics and imaging_condition as parallel nodes (legal and ethics must happen before imaging and condition report? Usually legal clearance before cataloging)
# But description says complex coordination, let's put legal_ethics before imaging_condition

# Construct the overall PO:

root = StrictPartialOrder(nodes=[
    Preliminary_Review,
    science_hist,
    legal_ethics,
    imaging_condition,
    Risk_Assessment,
    Authentication_Cert,
    Secure_Cataloging,
    Transport_Prep,
    Exhibit_Setup
])

# Add order edges according to the workflow

# Preliminary Review before scientific and historical verification
root.order.add_edge(Preliminary_Review, science_hist)

# scientific_hist before legal_ethics
root.order.add_edge(science_hist, legal_ethics)

# legal_ethics before imaging_condition
root.order.add_edge(legal_ethics, imaging_condition)

# imaging_condition before Risk_Assessment
root.order.add_edge(imaging_condition, Risk_Assessment)

# Risk_Assessment before certification
root.order.add_edge(Risk_Assessment, Authentication_Cert)

# Certification before Cataloging
root.order.add_edge(Authentication_Cert, Secure_Cataloging)

# Cataloging before Transport Prep
root.order.add_edge(Secure_Cataloging, Transport_Prep)

# Transport Prep before Exhibit Setup
root.order.add_edge(Transport_Prep, Exhibit_Setup)