# Generated from: 87f5134d-65ef-4faa-8ca0-fdbe6e4ef8f6.json
# Description: This process outlines the complex setup of an urban vertical farming system within a repurposed industrial building. It involves site analysis, modular farm design, equipment procurement, and installation of hydroponic and aeroponic systems. The process includes environmental control calibration, integration of IoT sensors for real-time monitoring, and development of automated nutrient delivery schedules. Staff training on system operation and safety protocols is conducted, followed by initial trial planting and iterative optimization of growth parameters. The final steps focus on establishing supply chain logistics, marketing strategies for local produce, and ongoing maintenance scheduling to ensure sustainability and productivity in an urban context.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

Site_Survey = Transition(label='Site Survey')
Design_Plan = Transition(label='Design Plan')
Procure_Equipment = Transition(label='Procure Equipment')
Install_Modules = Transition(label='Install Modules')
Setup_Hydroponics = Transition(label='Setup Hydroponics')
Calibrate_Sensors = Transition(label='Calibrate Sensors')
Integrate_IoT = Transition(label='Integrate IoT')
Program_Automation = Transition(label='Program Automation')
Train_Staff = Transition(label='Train Staff')
Trial_Planting = Transition(label='Trial Planting')
Optimize_Growth = Transition(label='Optimize Growth')
Logistics_Setup = Transition(label='Logistics Setup')
Marketing_Plan = Transition(label='Marketing Plan')
Maintenance_Plan = Transition(label='Maintenance Plan')
Launch_Operations = Transition(label='Launch Operations')

# Loop for iterative optimization: Optimize Growth after Trial Planting repeatedly until done
opt_loop = OperatorPOWL(operator=Operator.LOOP, children=[Trial_Planting, Optimize_Growth])

# Partial order for environmental control calibration steps (calibration and integration and programming) in sequence
calibration_seq = StrictPartialOrder(nodes=[Calibrate_Sensors, Integrate_IoT, Program_Automation])
calibration_seq.order.add_edge(Calibrate_Sensors, Integrate_IoT)
calibration_seq.order.add_edge(Integrate_IoT, Program_Automation)

# Partial order for installation-related activities
installation_seq = StrictPartialOrder(nodes=[Install_Modules, Setup_Hydroponics])
installation_seq.order.add_edge(Install_Modules, Setup_Hydroponics)

# Partial order for logistics and marketing steps in parallel to maintenance and launch
logistics_marketing = StrictPartialOrder(nodes=[Logistics_Setup, Marketing_Plan])
maintenance_launch = StrictPartialOrder(nodes=[Maintenance_Plan, Launch_Operations])
maintenance_launch.order.add_edge(Maintenance_Plan, Launch_Operations)

# Partial order for staff training and after installation and calibration etc.
train = Train_Staff

# Partial order for main development steps after design
develop_seq = StrictPartialOrder(nodes=[
    Procure_Equipment,
    installation_seq,
    calibration_seq,
    train,
    opt_loop
])
develop_seq.order.add_edge(Procure_Equipment, installation_seq)
develop_seq.order.add_edge(installation_seq, calibration_seq)
develop_seq.order.add_edge(calibration_seq, train)
develop_seq.order.add_edge(train, opt_loop)

# Overall process order: Site Survey -> Design Plan -> Develop -> parallel logistics/marketing and maintenance/launch
root = StrictPartialOrder(nodes=[
    Site_Survey,
    Design_Plan,
    develop_seq,
    logistics_marketing,
    maintenance_launch
])
root.order.add_edge(Site_Survey, Design_Plan)
root.order.add_edge(Design_Plan, develop_seq)
root.order.add_edge(develop_seq, logistics_marketing)
root.order.add_edge(develop_seq, maintenance_launch)