# Generated from: 853ec268-38ac-4cd2-9a41-6d8e1093e7a1.json
# Description: This process outlines the comprehensive steps involved in establishing an urban rooftop farm in a densely populated city environment. It begins with site analysis to evaluate structural integrity and sunlight exposure, followed by soil and water quality testing. Then, permits and zoning approvals are secured from local authorities. Afterward, the design phase includes selecting appropriate plant varieties adapted to urban climates and creating an efficient irrigation system. Installation involves assembling modular planters, setting up rainwater harvesting, and integrating renewable energy sources like solar panels for sustainable operations. The process continues with training staff on urban farming techniques, implementing pest management strategies suitable for rooftop ecosystems, and establishing a supply chain for distributing fresh produce to local markets. Finally, ongoing monitoring and adjustments ensure optimal crop yields while maintaining environmental compliance and community engagement.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Site_Analysis = Transition(label='Site Analysis')
Structure_Check = Transition(label='Structure Check')
Sunlight_Mapping = Transition(label='Sunlight Mapping')
Soil_Testing = Transition(label='Soil Testing')
Water_Testing = Transition(label='Water Testing')
Permit_Filing = Transition(label='Permit Filing')
Zoning_Approval = Transition(label='Zoning Approval')
Crop_Selection = Transition(label='Crop Selection')
Irrigation_Setup = Transition(label='Irrigation Setup')
Planter_Assembly = Transition(label='Planter Assembly')
Rainwater_Install = Transition(label='Rainwater Install')
Solar_Paneling = Transition(label='Solar Paneling')
Staff_Training = Transition(label='Staff Training')
Pest_Control = Transition(label='Pest Control')
Supply_Chain = Transition(label='Supply Chain')
Yield_Monitoring = Transition(label='Yield Monitoring')
Compliance_Review = Transition(label='Compliance Review')
Community_Outreach = Transition(label='Community Outreach')

# Step 1: Site analysis: Structure Check and Sunlight Mapping concurrently after Site Analysis
site_analysis_po = StrictPartialOrder(
    nodes=[Site_Analysis, Structure_Check, Sunlight_Mapping],
)
site_analysis_po.order.add_edge(Site_Analysis, Structure_Check)
site_analysis_po.order.add_edge(Site_Analysis, Sunlight_Mapping)

# Step 2: Soil and Water quality testing concurrently
soil_water_po = StrictPartialOrder(
    nodes=[Soil_Testing, Water_Testing],
)

# Step 3: Permits and zoning approvals sequential (Permit Filing then Zoning Approval)
permits_po = StrictPartialOrder(
    nodes=[Permit_Filing, Zoning_Approval],
)
permits_po.order.add_edge(Permit_Filing, Zoning_Approval)

# Step 4: Design phase: Crop Selection then Irrigation Setup sequential
design_po = StrictPartialOrder(
    nodes=[Crop_Selection, Irrigation_Setup],
)
design_po.order.add_edge(Crop_Selection, Irrigation_Setup)

# Step 5: Installation concurrently: Planter Assembly, Rainwater Install, Solar Paneling
installation_po = StrictPartialOrder(
    nodes=[Planter_Assembly, Rainwater_Install, Solar_Paneling],
)

# Step 6: Training and pest control concurrently: Staff Training and Pest Control
training_pest_po = StrictPartialOrder(
    nodes=[Staff_Training, Pest_Control],
)

# Step 7: Supply chain (single activity)
supply_chain = Supply_Chain = Supply_Chain  # Typo avoided by direct use below
Supply_Chain = Transition(label='Supply Chain')

# Step 8: Monitoring and adjustments concurrently: Yield Monitoring, Compliance Review, Community Outreach
monitoring_po = StrictPartialOrder(
    nodes=[Yield_Monitoring, Compliance_Review, Community_Outreach],
)

# Now build the main workflow combining the steps in sequence except for concurrent steps internally

nodes = [
    site_analysis_po,
    soil_water_po,
    permits_po,
    design_po,
    installation_po,
    training_pest_po,
    Supply_Chain,
    monitoring_po,
]

root = StrictPartialOrder(nodes=nodes)

# Add edges to enforce the sequence between the steps:
# site_analysis_po -> soil_water_po -> permits_po -> design_po -> installation_po -> training_pest_po -> Supply_Chain -> monitoring_po

root.order.add_edge(site_analysis_po, soil_water_po)
root.order.add_edge(soil_water_po, permits_po)
root.order.add_edge(permits_po, design_po)
root.order.add_edge(design_po, installation_po)
root.order.add_edge(installation_po, training_pest_po)
root.order.add_edge(training_pest_po, Supply_Chain)
root.order.add_edge(Supply_Chain, monitoring_po)