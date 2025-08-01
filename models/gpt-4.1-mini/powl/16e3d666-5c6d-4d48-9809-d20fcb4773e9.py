# Generated from: 16e3d666-5c6d-4d48-9809-d20fcb4773e9.json
# Description: This process involves verifying the authenticity and provenance of rare artifacts through multidisciplinary examination methods. It includes initial discovery reporting, detailed physical and chemical analysis, historical provenance research, expert consultations, and final certification. The process integrates advanced imaging, isotopic testing, and digital archiving to ensure comprehensive validation. Each step requires collaboration among archaeologists, chemists, historians, and legal experts to mitigate forgery risks and establish legitimate ownership. The final output is a verified artifact dossier for collectors or museums, including risk assessment and insurance recommendations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
Discovery_Report = Transition(label='Discovery Report')
Preliminary_Scan = Transition(label='Preliminary Scan')
Material_Sampling = Transition(label='Material Sampling')
Isotope_Test = Transition(label='Isotope Test')
Imaging_Capture = Transition(label='Imaging Capture')
Provenance_Check = Transition(label='Provenance Check')
Expert_Review = Transition(label='Expert Review')
Forgery_Analysis = Transition(label='Forgery Analysis')
Legal_Verify = Transition(label='Legal Verify')
Risk_Assess = Transition(label='Risk Assess')
Ownership_Trace = Transition(label='Ownership Trace')
Digital_Archive = Transition(label='Digital Archive')
Certification_Issue = Transition(label='Certification Issue')
Insurance_Advise = Transition(label='Insurance Advise')
Final_Dossier = Transition(label='Final Dossier')

# Physical and chemical analysis partial order
# - Preliminary Scan
# - Material Sampling --> Isotope Test & Imaging Capture concurrent
physical_chemical_analysis = StrictPartialOrder(nodes=[
    Preliminary_Scan, 
    Material_Sampling, Isotope_Test, Imaging_Capture
])
physical_chemical_analysis.order.add_edge(Preliminary_Scan, Material_Sampling)
physical_chemical_analysis.order.add_edge(Material_Sampling, Isotope_Test)
physical_chemical_analysis.order.add_edge(Material_Sampling, Imaging_Capture)

# Historical provenance research partial order
# - Provenance Check --> Ownership Trace
historical_provenance = StrictPartialOrder(nodes=[Provenance_Check, Ownership_Trace])
historical_provenance.order.add_edge(Provenance_Check, Ownership_Trace)

# Expert consultations partial order:
# Expert Review and Forgery Analysis concurrent
# Then Legal Verify
expert_consultations = StrictPartialOrder(nodes=[Expert_Review, Forgery_Analysis, Legal_Verify])
expert_consultations.order.add_edge(Expert_Review, Legal_Verify)
expert_consultations.order.add_edge(Forgery_Analysis, Legal_Verify)

# Risk assessment and insurance advice concurrent
risk_and_insurance = StrictPartialOrder(nodes=[Risk_Assess, Insurance_Advise])

# Digital archiving after physical/chemical, historical provenance, and expert consultations
# Final dossier after Certification Issue and Digital Archive
certification_and_final = StrictPartialOrder(nodes=[Certification_Issue, Digital_Archive, Final_Dossier])
certification_and_final.order.add_edge(Certification_Issue, Final_Dossier)
certification_and_final.order.add_edge(Digital_Archive, Final_Dossier)

# Root partial order combining all the subprocesses
root = StrictPartialOrder(nodes=[
    Discovery_Report,
    physical_chemical_analysis,
    historical_provenance,
    expert_consultations,
    risk_and_insurance,
    certification_and_final
])

# Ordering dependencies
# Start with Discovery Report
root.order.add_edge(Discovery_Report, physical_chemical_analysis)
root.order.add_edge(Discovery_Report, historical_provenance)
root.order.add_edge(Discovery_Report, expert_consultations)

# Physical chemical, historical provenance, and expert consultations must complete before risk_and_insurance and certification_and_final
root.order.add_edge(physical_chemical_analysis, risk_and_insurance)
root.order.add_edge(historical_provenance, risk_and_insurance)
root.order.add_edge(expert_consultations, risk_and_insurance)

root.order.add_edge(physical_chemical_analysis, certification_and_final)
root.order.add_edge(historical_provenance, certification_and_final)
root.order.add_edge(expert_consultations, certification_and_final)

# Risk and insurance precedes certification and final dossier (to reflect risk assessment informing certification)
root.order.add_edge(risk_and_insurance, certification_and_final)