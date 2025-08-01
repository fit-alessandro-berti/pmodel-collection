# Generated from: 0bb6a448-b0d1-489f-aff5-1c6992335e25.json
# Description: This process outlines the intricate steps involved in launching an urban vertical farm, integrating advanced hydroponics, renewable energy, and IoT monitoring systems. It begins with site analysis and regulatory approval, followed by system design, vendor selection, and infrastructure setup. Subsequent phases include seed sourcing, climate calibration, and automation programming. Quality control and pest management run concurrently with staff training and community outreach to ensure sustainability and local engagement. The final stages focus on trial harvests, data analysis, and iterative optimization before full commercial production begins, ensuring a resilient urban agriculture ecosystem.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Site_Analysis = Transition(label='Site Analysis')
Permit_Filing = Transition(label='Permit Filing')
System_Design = Transition(label='System Design')
Vendor_Selection = Transition(label='Vendor Selection')
Infrastructure_Setup = Transition(label='Infrastructure Setup')
Seed_Sourcing = Transition(label='Seed Sourcing')
Climate_Setup = Transition(label='Climate Setup')
Automation_Code = Transition(label='Automation Code')
Quality_Control = Transition(label='Quality Control')
Pest_Monitoring = Transition(label='Pest Monitoring')
Staff_Training = Transition(label='Staff Training')
Community_Outreach = Transition(label='Community Outreach')
Trial_Harvest = Transition(label='Trial Harvest')
Data_Review = Transition(label='Data Review')
Process_Optimize = Transition(label='Process Optimize')
Launch_Prep = Transition(label='Launch Prep')
Commercial_Start = Transition(label='Commercial Start')

# Quality control and pest management run concurrently with staff training and community outreach
QC_PM = StrictPartialOrder(nodes=[Quality_Control, Pest_Monitoring])  # concurrent
ST_CO = StrictPartialOrder(nodes=[Staff_Training, Community_Outreach])  # concurrent

# Join these two concurrency groups into one node set with no order (fully concurrent)
QC_PM_ST_CO = StrictPartialOrder(nodes=[Quality_Control, Pest_Monitoring, Staff_Training, Community_Outreach])

# First part: site analysis -> permit filing -> system design -> vendor selection -> infrastructure setup
first_seq = StrictPartialOrder(nodes=[Site_Analysis, Permit_Filing, System_Design, Vendor_Selection, Infrastructure_Setup])
first_seq.order.add_edge(Site_Analysis, Permit_Filing)
first_seq.order.add_edge(Permit_Filing, System_Design)
first_seq.order.add_edge(System_Design, Vendor_Selection)
first_seq.order.add_edge(Vendor_Selection, Infrastructure_Setup)

# Second part: seed sourcing -> climate setup -> automation code
second_seq = StrictPartialOrder(nodes=[Seed_Sourcing, Climate_Setup, Automation_Code])
second_seq.order.add_edge(Seed_Sourcing, Climate_Setup)
second_seq.order.add_edge(Climate_Setup, Automation_Code)

# Combine second_seq with QC_PM_ST_CO (the four concurrent activities)
middle_part = StrictPartialOrder(nodes=[Seed_Sourcing, Climate_Setup, Automation_Code,
                                        Quality_Control, Pest_Monitoring,
                                        Staff_Training, Community_Outreach])
# Add order in middle_part
middle_part.order.add_edge(Seed_Sourcing, Climate_Setup)
middle_part.order.add_edge(Climate_Setup, Automation_Code)
# QC, Pest, Staff, Community concurrent => no order edges among them

# Third part: trial harvest -> data review -> process optimize
third_seq = StrictPartialOrder(nodes=[Trial_Harvest, Data_Review, Process_Optimize])
third_seq.order.add_edge(Trial_Harvest, Data_Review)
third_seq.order.add_edge(Data_Review, Process_Optimize)

# Final steps: launch prep -> commercial start
final_seq = StrictPartialOrder(nodes=[Launch_Prep, Commercial_Start])
final_seq.order.add_edge(Launch_Prep, Commercial_Start)

# Combine all parts into root PO with the appropriate ordering:
# first_seq -> second_seq (which includes the four concurrent)
# second_seq -> third_seq
# third_seq -> final_seq
root = StrictPartialOrder(nodes=[
    Site_Analysis, Permit_Filing, System_Design, Vendor_Selection, Infrastructure_Setup,
    Seed_Sourcing, Climate_Setup, Automation_Code,
    Quality_Control, Pest_Monitoring, Staff_Training, Community_Outreach,
    Trial_Harvest, Data_Review, Process_Optimize,
    Launch_Prep, Commercial_Start
])

# Add first_seq order edges
root.order.add_edge(Site_Analysis, Permit_Filing)
root.order.add_edge(Permit_Filing, System_Design)
root.order.add_edge(System_Design, Vendor_Selection)
root.order.add_edge(Vendor_Selection, Infrastructure_Setup)

# Link first_seq to second_seq: Infrastructure Setup -> Seed Sourcing
root.order.add_edge(Infrastructure_Setup, Seed_Sourcing)

# Add second_seq internal edges
root.order.add_edge(Seed_Sourcing, Climate_Setup)
root.order.add_edge(Climate_Setup, Automation_Code)

# No order edges among QC, Pest, Staff, Community (concurrent)
# They all start after Automation_Code
root.order.add_edge(Automation_Code, Quality_Control)
root.order.add_edge(Automation_Code, Pest_Monitoring)
root.order.add_edge(Automation_Code, Staff_Training)
root.order.add_edge(Automation_Code, Community_Outreach)

# Link second_seq to third_seq: finish of QC/Pest/Staff/Community -> trial harvest
# Since those 4 are concurrent and independent, assume Trial Harvest must wait all 4 to finish
# In PO, this means edges:
root.order.add_edge(Quality_Control, Trial_Harvest)
root.order.add_edge(Pest_Monitoring, Trial_Harvest)
root.order.add_edge(Staff_Training, Trial_Harvest)
root.order.add_edge(Community_Outreach, Trial_Harvest)

# Add third_seq internal edges
root.order.add_edge(Trial_Harvest, Data_Review)
root.order.add_edge(Data_Review, Process_Optimize)

# Link third_seq to final_seq: Process Optimize -> Launch Prep
root.order.add_edge(Process_Optimize, Launch_Prep)

# Add final_seq internal edges
root.order.add_edge(Launch_Prep, Commercial_Start)