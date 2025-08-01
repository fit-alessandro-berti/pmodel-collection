# Generated from: 83701a0c-9c83-4db6-9381-7e2721291820.json
# Description: This process outlines the steps involved in authenticating rare historical artifacts for museum acquisition. It begins with initial appraisal and provenance research, followed by material analysis and expert consultations. The workflow incorporates unconventional activities such as multispectral imaging and isotope testing to verify origin. Legal compliance checks and ethical sourcing evaluations are included before final authentication. Documentation and digital archiving ensure traceability. The process concludes with a presentation to the acquisition committee and secure transport arrangements, ensuring the artifact's integrity is maintained throughout the workflow.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Initial_Appraisal = Transition(label='Initial Appraisal')
Provenance_Check = Transition(label='Provenance Check')
Material_Sampling = Transition(label='Material Sampling')
Isotope_Testing = Transition(label='Isotope Testing')
Imaging_Scan = Transition(label='Imaging Scan')
Expert_Review = Transition(label='Expert Review')
Ethics_Audit = Transition(label='Ethics Audit')
Legal_Verify = Transition(label='Legal Verify')
Condition_Report = Transition(label='Condition Report')
Historical_Context = Transition(label='Historical Context')
Digital_Archive = Transition(label='Digital Archive')
Acquisition_Pitch = Transition(label='Acquisition Pitch')
Security_Clearance = Transition(label='Security Clearance')
Transport_Prep = Transition(label='Transport Prep')
Final_Approval = Transition(label='Final Approval')

# The process is partially ordered as described:

# Step 1: Initial Appraisal --> Provenance Check
# Step 2: Material Sampling after Provenance Check
# Steps 3 & 4: Isotope Testing and Imaging Scan occur concurrently after Material Sampling
# Step 5: Expert Review after both Isotope Testing and Imaging Scan
# Step 6 & 7: Ethics Audit and Legal Verify in any order after Expert Review (concurrent)
# Step 8: Condition Report & Historical Context concurrent after Ethics Audit + Legal Verify done
# Step 9: Digital Archive after Condition Report and Historical Context
# Step 10: Acquisition Pitch after Digital Archive
# Step 11 & 12: Security Clearance and Transport Prep concurrent after Acquisition Pitch
# Step 13: Final Approval after Security Clearance and Transport Prep

# Build the partial order accordingly

root = StrictPartialOrder(
    nodes=[
        Initial_Appraisal, Provenance_Check, Material_Sampling,
        Isotope_Testing, Imaging_Scan,
        Expert_Review,
        Ethics_Audit, Legal_Verify,
        Condition_Report, Historical_Context,
        Digital_Archive,
        Acquisition_Pitch,
        Security_Clearance, Transport_Prep,
        Final_Approval
    ]
)

# Define edges (dependencies)

root.order.add_edge(Initial_Appraisal, Provenance_Check)
root.order.add_edge(Provenance_Check, Material_Sampling)

# Isotope Testing and Imaging Scan concurrent after Material Sampling
root.order.add_edge(Material_Sampling, Isotope_Testing)
root.order.add_edge(Material_Sampling, Imaging_Scan)

# Both must complete before Expert Review
root.order.add_edge(Isotope_Testing, Expert_Review)
root.order.add_edge(Imaging_Scan, Expert_Review)

# Ethics Audit and Legal Verify concurrent after Expert Review
root.order.add_edge(Expert_Review, Ethics_Audit)
root.order.add_edge(Expert_Review, Legal_Verify)

# Condition Report and Historical Context concurrent after Ethics Audit and Legal Verify
root.order.add_edge(Ethics_Audit, Condition_Report)
root.order.add_edge(Ethics_Audit, Historical_Context)
root.order.add_edge(Legal_Verify, Condition_Report)
root.order.add_edge(Legal_Verify, Historical_Context)

# Digital Archive after Condition Report and Historical Context
root.order.add_edge(Condition_Report, Digital_Archive)
root.order.add_edge(Historical_Context, Digital_Archive)

# Acquisition Pitch after Digital Archive
root.order.add_edge(Digital_Archive, Acquisition_Pitch)

# Security Clearance and Transport Prep concurrent after Acquisition Pitch
root.order.add_edge(Acquisition_Pitch, Security_Clearance)
root.order.add_edge(Acquisition_Pitch, Transport_Prep)

# Final Approval after Security Clearance and Transport Prep
root.order.add_edge(Security_Clearance, Final_Approval)
root.order.add_edge(Transport_Prep, Final_Approval)