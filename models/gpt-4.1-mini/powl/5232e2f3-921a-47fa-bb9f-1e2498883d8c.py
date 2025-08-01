# Generated from: 5232e2f3-921a-47fa-bb9f-1e2498883d8c.json
# Description: This process involves establishing a sustainable urban vertical farm from concept to operational status. It begins with site selection based on environmental impact and zoning laws, followed by architectural design tailored for optimal light and water use. Next, hydroponic system installation and integration of IoT sensors ensure precise resource management. Crop selection and genetic optimization prepare the farm for diverse yield. Staff recruitment focuses on agritech expertise, while partnerships with local markets and distribution channels are established. Regulatory compliance and organic certification are secured before trial cultivation cycles start. Continuous monitoring and data analysis refine growth parameters, leading to full-scale production and community engagement initiatives to promote urban agriculture awareness.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all the transitions labeled by activity names
Site_Selection = Transition(label='Site Selection')
Zoning_Review = Transition(label='Zoning Review')
Design_Planning = Transition(label='Design Planning')
Hydroponic_Setup = Transition(label='Hydroponic Setup')
Sensor_Install = Transition(label='Sensor Install')
Crop_Selection = Transition(label='Crop Selection')
Genetic_Tuning = Transition(label='Genetic Tuning')
Staff_Hiring = Transition(label='Staff Hiring')
Market_Partner = Transition(label='Market Partner')
Compliance_Check = Transition(label='Compliance Check')
Certification = Transition(label='Certification')
Trial_Cultivation = Transition(label='Trial Cultivation')
Data_Analysis = Transition(label='Data Analysis')
Scale_Launch = Transition(label='Scale Launch')
Community_Outreach = Transition(label='Community Outreach')

# Model the process structure as partial orders and sequences
# Site Selection and Zoning Review happen in parallel (both needed before Design Planning)
site_and_zoning = StrictPartialOrder(nodes=[Site_Selection, Zoning_Review])
# No order edge -> concurrent activities

# After site selection and zoning review, Design Planning happens
phase1 = StrictPartialOrder(nodes=[site_and_zoning, Design_Planning])
phase1.order.add_edge(site_and_zoning, Design_Planning)

# Hydroponic Setup and Sensor Install can be done concurrently after Design Planning
hydro_sensor = StrictPartialOrder(nodes=[Hydroponic_Setup, Sensor_Install])
# Again no edges -> concurrent

# So phase2 is after Design Planning
phase2 = StrictPartialOrder(nodes=[Design_Planning, hydro_sensor])
phase2.order.add_edge(Design_Planning, hydro_sensor)

# Crop Selection and Genetic Tuning are done in sequence after phase2
crop_seq = StrictPartialOrder(nodes=[Crop_Selection, Genetic_Tuning])
crop_seq.order.add_edge(Crop_Selection, Genetic_Tuning)

phase3 = StrictPartialOrder(nodes=[phase2, crop_seq])
phase3.order.add_edge(phase2, crop_seq)

# Staff Hiring and Market Partner can happen concurrently after crop_seq
staff_market = StrictPartialOrder(nodes=[Staff_Hiring, Market_Partner])

# Compliance Check and Certification are sequential after staff and marketing
compliance_cert = StrictPartialOrder(nodes=[Compliance_Check, Certification])
compliance_cert.order.add_edge(Compliance_Check, Certification)

# Phase4 collects these in sequence: staff_market -> compliance_cert
phase4 = StrictPartialOrder(nodes=[staff_market, compliance_cert])
phase4.order.add_edge(staff_market, compliance_cert)

# Trial Cultivation after certifications
phase5 = StrictPartialOrder(nodes=[phase4, Trial_Cultivation])
phase5.order.add_edge(phase4, Trial_Cultivation)

# Data Analysis after Trial Cultivation
phase6 = StrictPartialOrder(nodes=[Trial_Cultivation, Data_Analysis])
phase6.order.add_edge(Trial_Cultivation, Data_Analysis)

# Scale Launch after Data Analysis
phase7 = StrictPartialOrder(nodes=[Data_Analysis, Scale_Launch])
phase7.order.add_edge(Data_Analysis, Scale_Launch)

# Community Outreach after Scale Launch
phase8 = StrictPartialOrder(nodes=[Scale_Launch, Community_Outreach])
phase8.order.add_edge(Scale_Launch, Community_Outreach)

# Now build the full process as a chain of partial orders by connecting phase after phase
process_1to3 = StrictPartialOrder(nodes=[phase1, phase3])
process_1to3.order.add_edge(phase1, phase3)

process_1to4 = StrictPartialOrder(nodes=[process_1to3, phase4])
process_1to4.order.add_edge(process_1to3, phase4)

process_1to5 = StrictPartialOrder(nodes=[process_1to4, phase5])
process_1to5.order.add_edge(process_1to4, phase5)

process_1to6 = StrictPartialOrder(nodes=[process_1to5, phase6])
process_1to6.order.add_edge(process_1to5, phase6)

process_1to7 = StrictPartialOrder(nodes=[process_1to6, phase7])
process_1to7.order.add_edge(process_1to6, phase7)

root = StrictPartialOrder(nodes=[process_1to7, phase8])
root.order.add_edge(process_1to7, phase8)