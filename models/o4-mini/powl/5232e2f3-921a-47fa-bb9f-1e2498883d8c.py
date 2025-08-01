# Generated from: 5232e2f3-921a-47fa-bb9f-1e2498883d8c.json
# Description: This process involves establishing a sustainable urban vertical farm from concept to operational status. It begins with site selection based on environmental impact and zoning laws, followed by architectural design tailored for optimal light and water use. Next, hydroponic system installation and integration of IoT sensors ensure precise resource management. Crop selection and genetic optimization prepare the farm for diverse yield. Staff recruitment focuses on agritech expertise, while partnerships with local markets and distribution channels are established. Regulatory compliance and organic certification are secured before trial cultivation cycles start. Continuous monitoring and data analysis refine growth parameters, leading to full-scale production and community engagement initiatives to promote urban agriculture awareness.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
Site_Selection    = Transition(label='Site Selection')
Zoning_Review     = Transition(label='Zoning Review')
Design_Planning   = Transition(label='Design Planning')
Hydroponic_Setup  = Transition(label='Hydroponic Setup')
Sensor_Install    = Transition(label='Sensor Install')
Crop_Selection    = Transition(label='Crop Selection')
Genetic_Tuning    = Transition(label='Genetic Tuning')
Staff_Hiring      = Transition(label='Staff Hiring')
Market_Partner    = Transition(label='Market Partner')
Compliance_Check  = Transition(label='Compliance Check')
Certification     = Transition(label='Certification')
Trial_Cultivation = Transition(label='Trial Cultivation')
Data_Analysis     = Transition(label='Data Analysis')
Scale_Launch      = Transition(label='Scale Launch')
Community_Outreach= Transition(label='Community Outreach')

# Build the partial order
root = StrictPartialOrder(nodes=[
    Site_Selection, Zoning_Review, Design_Planning,
    Hydroponic_Setup, Sensor_Install,
    Crop_Selection, Genetic_Tuning,
    Staff_Hiring, Market_Partner,
    Compliance_Check, Certification,
    Trial_Cultivation, Data_Analysis,
    Scale_Launch, Community_Outreach
])

# Sequence of core design and installation
root.order.add_edge(Site_Selection, Zoning_Review)
root.order.add_edge(Zoning_Review, Design_Planning)
root.order.add_edge(Design_Planning, Hydroponic_Setup)
root.order.add_edge(Hydroponic_Setup, Sensor_Install)

# Crop preparation
root.order.add_edge(Sensor_Install, Crop_Selection)
root.order.add_edge(Crop_Selection, Genetic_Tuning)

# Parallel staffing and market setup, then compliance
root.order.add_edge(Genetic_Tuning, Staff_Hiring)
root.order.add_edge(Genetic_Tuning, Market_Partner)
root.order.add_edge(Staff_Hiring, Compliance_Check)
root.order.add_edge(Market_Partner, Compliance_Check)

# Certification and trial cultivation
root.order.add_edge(Compliance_Check, Certification)
root.order.add_edge(Certification, Trial_Cultivation)

# Monitoring and scale-up
root.order.add_edge(Trial_Cultivation, Data_Analysis)
root.order.add_edge(Data_Analysis, Scale_Launch)
root.order.add_edge(Data_Analysis, Community_Outreach)