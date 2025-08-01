# Generated from: 6e51aa90-f787-4e68-9955-a5fb0939a6ce.json
# Description: This process outlines the establishment of an urban rooftop farm integrating advanced hydroponic systems and renewable energy sources. It begins with site evaluation for structural integrity and sunlight exposure, followed by design planning incorporating modular growing units and water recycling mechanisms. Procurement of specialized materials such as nutrient solutions, grow lights, and sensors is coordinated with local vendors. Installation involves structural reinforcement, system assembly, and sensor calibration. Crop selection is optimized for urban climates and market demands. Continuous monitoring ensures optimal growth through data analysis and automated adjustments. Community engagement activities include workshops and local produce distribution. The process concludes with performance review and scalability assessment for other rooftops in the city.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Activities as transitions
Site_Survey = Transition(label='Site Survey')

# Site Survey splits into two concurrent activities: Structural Test and Sunlight Map
Structural_Test = Transition(label='Structural Test')
Sunlight_Map = Transition(label='Sunlight Map')

# After both tests complete, Design Plan
Design_Plan = Transition(label='Design Plan')

# Procurement phase: Material Order and Vendor Coordination in parallel
Material_Order = Transition(label='Material Order')
Vendor_Coordination = Transition(label='Vendor Coordination')

# Installation phase: Reinforce Roof --> Install Systems --> Calibrate Sensors (sequential)
Reinforce_Roof = Transition(label='Reinforce Roof')
Install_Systems = Transition(label='Install Systems')
Calibrate_Sensors = Transition(label='Calibrate Sensors')

# Crop selection
Select_Crops = Transition(label='Select Crops')

# Setup Hydroponics, Configure Lighting and Water Recycling are related to design plan 
# and installation, they can be done in partial order along with Install Systems
# But logically they belong to setup phase, after Reinforce Roof
Setup_Hydroponics = Transition(label='Setup Hydroponics')
Configure_Lighting = Transition(label='Configure Lighting')
Water_Recycling = Transition(label='Water Recycling')

# Monitoring phase: Monitor Growth, Data Analysis, Automate Controls in partial order
Monitor_Growth = Transition(label='Monitor Growth')
Data_Analysis = Transition(label='Data Analysis')
Automate_Controls = Transition(label='Automate Controls')

# Community Engagement: Community Workshop and Local Distribution in parallel
Community_Workshop = Transition(label='Community Workshop')
Local_Distribution = Transition(label='Local Distribution')

# Final phase: Performance Review and Scale Assessment sequential
Performance_Review = Transition(label='Performance Review')
Scale_Assessment = Transition(label='Scale Assessment')

# Define site survey partial order with concurrency of Structural Test and Sunlight Map
site_survey_po = StrictPartialOrder(
    nodes=[Site_Survey, Structural_Test, Sunlight_Map]
)
site_survey_po.order.add_edge(Site_Survey, Structural_Test)
site_survey_po.order.add_edge(Site_Survey, Sunlight_Map)

# After site survey (including tests) completes, Design Plan
site_and_design_po = StrictPartialOrder(
    nodes=[site_survey_po, Design_Plan]
)
site_and_design_po.order.add_edge(site_survey_po, Design_Plan)

# Procurement partial order - parallel Material Order and Vendor Coordination
procurement_po = StrictPartialOrder(
    nodes=[Material_Order, Vendor_Coordination]
)
# No order edges: concurrent

# Installation partial order - Reinforce Roof precedes others
installation_po = StrictPartialOrder(
    nodes=[Reinforce_Roof, Install_Systems, Calibrate_Sensors, Setup_Hydroponics, Configure_Lighting, Water_Recycling]
)
installation_po.order.add_edge(Reinforce_Roof, Install_Systems)
installation_po.order.add_edge(Install_Systems, Calibrate_Sensors)

# Setup Hydroponics, Configure Lighting, Water Recycling can be done concurrently after Reinforce Roof
installation_po.order.add_edge(Reinforce_Roof, Setup_Hydroponics)
installation_po.order.add_edge(Reinforce_Roof, Configure_Lighting)
installation_po.order.add_edge(Reinforce_Roof, Water_Recycling)

# Crop Selection after Installation 
crop_selection_po = StrictPartialOrder(
    nodes=[installation_po, Select_Crops]
)
crop_selection_po.order.add_edge(installation_po, Select_Crops)

# Monitoring phase partial order - partial for Monitor Growth then Data Analysis then Automate Controls
monitoring_po = StrictPartialOrder(
    nodes=[Monitor_Growth, Data_Analysis, Automate_Controls]
)
monitoring_po.order.add_edge(Monitor_Growth, Data_Analysis)
monitoring_po.order.add_edge(Data_Analysis, Automate_Controls)

# Community Engagement parallel activities
community_engagement_po = StrictPartialOrder(
    nodes=[Community_Workshop, Local_Distribution]
)
# No edges: concurrent

# Final review sequential
final_review_po = StrictPartialOrder(
    nodes=[Performance_Review, Scale_Assessment]
)
final_review_po.order.add_edge(Performance_Review, Scale_Assessment)

# Build the whole process partial order
root = StrictPartialOrder(
    nodes=[
        site_and_design_po,
        procurement_po,
        crop_selection_po,
        monitoring_po,
        community_engagement_po,
        final_review_po
    ]
)

# Add edges to define partial order between major phases

# Procurement after Design Plan
root.order.add_edge(site_and_design_po, procurement_po)

# Installation and Crop Selection after Procurement
root.order.add_edge(procurement_po, crop_selection_po)

# Monitoring after Crop Selection
root.order.add_edge(crop_selection_po, monitoring_po)

# Community Engagement can start after Monitoring (or concurrent? but text suggests continuous monitoring *before* engagement)
root.order.add_edge(monitoring_po, community_engagement_po)

# Final Review after Community Engagement
root.order.add_edge(community_engagement_po, final_review_po)