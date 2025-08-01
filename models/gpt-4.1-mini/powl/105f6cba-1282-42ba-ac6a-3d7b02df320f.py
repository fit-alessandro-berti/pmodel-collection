# Generated from: 105f6cba-1282-42ba-ac6a-3d7b02df320f.json
# Description: This process outlines the establishment of an urban vertical farming system designed to optimize limited city space for sustainable food production. It integrates advanced hydroponic techniques, IoT sensor deployment, and automated nutrient delivery to ensure optimal plant growth. The process involves site analysis, modular infrastructure assembly, climate control calibration, and continuous data monitoring to maximize yield and reduce resource consumption. Additionally, it incorporates waste recycling from urban sources and energy-efficient lighting installation. The process aims to create a scalable, eco-friendly farming solution that minimizes environmental impact while addressing urban food security challenges through innovative technology and precise operational workflows.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities as transitions
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Procure_Modules = Transition(label='Procure Modules')
Install_Frames = Transition(label='Install Frames')
Setup_Hydroponics = Transition(label='Setup Hydroponics')
Deploy_Sensors = Transition(label='Deploy Sensors')
Configure_Climate = Transition(label='Configure Climate')
Calibrate_Lighting = Transition(label='Calibrate Lighting')
Install_Automation = Transition(label='Install Automation')
Implement_Recycling = Transition(label='Implement Recycling')
Test_Systems = Transition(label='Test Systems')
Plant_Seeding = Transition(label='Plant Seeding')
Monitor_Growth = Transition(label='Monitor Growth')
Adjust_Nutrients = Transition(label='Adjust Nutrients')
Harvest_Crop = Transition(label='Harvest Crop')
Analyze_Data = Transition(label='Analyze Data')
Report_Metrics = Transition(label='Report Metrics')

# Construct partial orders for logical grouping

# Phase 1: Site analysis and design
phase1 = StrictPartialOrder(nodes=[Site_Survey, Design_Layout, Procure_Modules])
phase1.order.add_edge(Site_Survey, Design_Layout)
phase1.order.add_edge(Design_Layout, Procure_Modules)

# Phase 2: Infrastructure assembly - frames and modules
phase2 = StrictPartialOrder(nodes=[Install_Frames, Setup_Hydroponics, Deploy_Sensors])
phase2.order.add_edge(Install_Frames, Setup_Hydroponics)
phase2.order.add_edge(Install_Frames, Deploy_Sensors)

# Phase 3: Climate and lighting calibration
phase3 = StrictPartialOrder(nodes=[Configure_Climate, Calibrate_Lighting, Install_Automation])
phase3.order.add_edge(Configure_Climate, Calibrate_Lighting)
phase3.order.add_edge(Calibrate_Lighting, Install_Automation)

# Phase 4: Waste recycling and testing
phase4 = StrictPartialOrder(nodes=[Implement_Recycling, Test_Systems])
phase4.order.add_edge(Implement_Recycling, Test_Systems)

# Phase 5: Planting, growth monitoring and nutrient adjustment loop
# Loop: after Monitor Growth, choose to exit or Adjust Nutrients then Monitor Growth again
growth_monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[Monitor_Growth, Adjust_Nutrients])

planting_and_monitor = StrictPartialOrder(nodes=[Plant_Seeding, growth_monitoring_loop])
planting_and_monitor.order.add_edge(Plant_Seeding, growth_monitoring_loop)

# Phase 6: Harvest and data analysis/report
phase6 = StrictPartialOrder(nodes=[Harvest_Crop, Analyze_Data, Report_Metrics])
phase6.order.add_edge(Harvest_Crop, Analyze_Data)
phase6.order.add_edge(Analyze_Data, Report_Metrics)

# Combine phases in order
root = StrictPartialOrder(nodes=[phase1, phase2, phase3, phase4, planting_and_monitor, phase6])

root.order.add_edge(phase1, phase2)
root.order.add_edge(phase2, phase3)
root.order.add_edge(phase3, phase4)
root.order.add_edge(phase4, planting_and_monitor)
root.order.add_edge(planting_and_monitor, phase6)