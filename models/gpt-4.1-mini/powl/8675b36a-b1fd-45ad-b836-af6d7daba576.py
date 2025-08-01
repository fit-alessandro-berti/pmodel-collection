# Generated from: 8675b36a-b1fd-45ad-b836-af6d7daba576.json
# Description: This process describes the complex integration of vertical farming systems within urban environments to optimize limited space and resources. It involves site assessment, modular system design, environmental calibration, crop selection based on microclimate, automated nutrient delivery, pest monitoring through AI sensors, energy consumption optimization, waste recycling, yield forecasting using predictive analytics, community engagement for local distribution, regulatory compliance checks, continuous system maintenance, data-driven growth adjustments, and final harvest logistics. The process aims to create a sustainable, scalable urban agriculture model that maximizes efficiency while minimizing environmental impact and fostering community participation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Site_Survey = Transition(label='Site Survey')
Design_Module = Transition(label='Design Module')
Calibrate_Sensors = Transition(label='Calibrate Sensors')
Select_Crops = Transition(label='Select Crops')
Setup_Irrigation = Transition(label='Setup Irrigation')
Install_AI = Transition(label='Install AI')
Monitor_Pests = Transition(label='Monitor Pests')
Optimize_Energy = Transition(label='Optimize Energy')
Recycle_Waste = Transition(label='Recycle Waste')
Forecast_Yield = Transition(label='Forecast Yield')
Engage_Community = Transition(label='Engage Community')
Check_Compliance = Transition(label='Check Compliance')
Maintain_Systems = Transition(label='Maintain Systems')
Adjust_Growth = Transition(label='Adjust Growth')
Plan_Harvest = Transition(label='Plan Harvest')

# Model partial orders according to the typical sequence and concurrency implied by the process description

# 1) Initial site assessment and module design must precede sensor calibration
initial_PO = StrictPartialOrder(nodes=[Site_Survey, Design_Module, Calibrate_Sensors])
initial_PO.order.add_edge(Site_Survey, Calibrate_Sensors)
initial_PO.order.add_edge(Design_Module, Calibrate_Sensors)

# 2) Crop selection depends on sensor calibration
crop_selection_PO = StrictPartialOrder(nodes=[Calibrate_Sensors, Select_Crops])
crop_selection_PO.order.add_edge(Calibrate_Sensors, Select_Crops)

# 3) Setup irrigation, install AI sensors and pest monitoring form next steps
# Setup irrigation and install AI can be concurrent, pest monitoring depends on install AI
irrigation_install_PO = StrictPartialOrder(nodes=[Setup_Irrigation, Install_AI, Monitor_Pests])
irrigation_install_PO.order.add_edge(Install_AI, Monitor_Pests)

# 4) Optimize energy and recycle waste can be done concurrently but after irrigation, AI install, and pest monitoring
energy_recycle_PO = StrictPartialOrder(nodes=[Setup_Irrigation, Install_AI, Monitor_Pests, Optimize_Energy, Recycle_Waste])
energy_recycle_PO.order.add_edge(Setup_Irrigation, Optimize_Energy)
energy_recycle_PO.order.add_edge(Install_AI, Optimize_Energy)
energy_recycle_PO.order.add_edge(Monitor_Pests, Optimize_Energy)
energy_recycle_PO.order.add_edge(Setup_Irrigation, Recycle_Waste)
energy_recycle_PO.order.add_edge(Install_AI, Recycle_Waste)
energy_recycle_PO.order.add_edge(Monitor_Pests, Recycle_Waste)

# 5) Forecast Yield depends on Optimize Energy and Recycle Waste
forecast_PO = StrictPartialOrder(nodes=[Optimize_Energy, Recycle_Waste, Forecast_Yield])
forecast_PO.order.add_edge(Optimize_Energy, Forecast_Yield)
forecast_PO.order.add_edge(Recycle_Waste, Forecast_Yield)

# 6) Engage Community and Check Compliance can be done after Forecast Yield in parallel
community_compliance_PO = StrictPartialOrder(nodes=[Forecast_Yield, Engage_Community, Check_Compliance])
community_compliance_PO.order.add_edge(Forecast_Yield, Engage_Community)
community_compliance_PO.order.add_edge(Forecast_Yield, Check_Compliance)

# 7) Maintain Systems and Adjust Growth can run concurrently after community engagement and compliance check
maintain_adjust_PO = StrictPartialOrder(nodes=[Engage_Community, Check_Compliance, Maintain_Systems, Adjust_Growth])
maintain_adjust_PO.order.add_edge(Engage_Community, Maintain_Systems)
maintain_adjust_PO.order.add_edge(Check_Compliance, Maintain_Systems)
maintain_adjust_PO.order.add_edge(Engage_Community, Adjust_Growth)
maintain_adjust_PO.order.add_edge(Check_Compliance, Adjust_Growth)

# 8) Plan Harvest after maintain and adjust
harvest_PO = StrictPartialOrder(nodes=[Maintain_Systems, Adjust_Growth, Plan_Harvest])
harvest_PO.order.add_edge(Maintain_Systems, Plan_Harvest)
harvest_PO.order.add_edge(Adjust_Growth, Plan_Harvest)

# Compose all partial orders in a global PO by ordering them sequentially
# initial_PO -> crop_selection_PO -> irrigation_install_PO -> energy_recycle_PO -> forecast_PO -> community_compliance_PO -> maintain_adjust_PO -> harvest_PO

root = StrictPartialOrder(nodes=[
    initial_PO,
    crop_selection_PO,
    irrigation_install_PO,
    energy_recycle_PO,
    forecast_PO,
    community_compliance_PO,
    maintain_adjust_PO,
    harvest_PO,
])

root.order.add_edge(initial_PO, crop_selection_PO)
root.order.add_edge(crop_selection_PO, irrigation_install_PO)
root.order.add_edge(irrigation_install_PO, energy_recycle_PO)
root.order.add_edge(energy_recycle_PO, forecast_PO)
root.order.add_edge(forecast_PO, community_compliance_PO)
root.order.add_edge(community_compliance_PO, maintain_adjust_PO)
root.order.add_edge(maintain_adjust_PO, harvest_PO)