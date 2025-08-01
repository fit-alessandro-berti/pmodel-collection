# Generated from: 78227013-41dd-4239-9e95-b11a0ccca3fb.json
# Description: This process details the complex setup of an urban vertical farm within a repurposed warehouse space. It involves site analysis, environmental control installation, hydroponic system integration, nutrient solution calibration, lighting optimization, and automation programming. Coordination with local authorities for zoning and safety compliance is required, alongside workforce training for specialized agricultural and technical tasks. Ongoing monitoring and iterative adjustment ensure optimal crop yield and resource efficiency, while data analytics support predictive maintenance and supply chain synchronization. The process culminates in establishing a sustainable, scalable urban farming operation that minimizes ecological impact while maximizing productivity in a confined urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Site_Survey = Transition(label='Site Survey')
Zoning_Check = Transition(label='Zoning Check')
Layout_Plan = Transition(label='Layout Plan')
Env_Control = Transition(label='Env Control')
Hydro_Setup = Transition(label='Hydro Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')
Light_Config = Transition(label='Light Config')
Automation_Dev = Transition(label='Automation Dev')
Safety_Audit = Transition(label='Safety Audit')
Staff_Training = Transition(label='Staff Training')
System_Test = Transition(label='System Test')
Crop_Seeding = Transition(label='Crop Seeding')
Data_Monitor = Transition(label='Data Monitor')
Yield_Optimize = Transition(label='Yield Optimize')
Supply_Align = Transition(label='Supply Align')
Maintenance_Plan = Transition(label='Maintenance Plan')

# Coordination with local authorities branch (Zoning Check, Safety Audit)
Coord_Authorities = StrictPartialOrder(nodes=[Zoning_Check, Safety_Audit])
# They can be concurrent (no order defined)

# Workforce training depends on Safety Audit
Training_PO = StrictPartialOrder(nodes=[Safety_Audit, Staff_Training])
Training_PO.order.add_edge(Safety_Audit, Staff_Training)

# Environmental control and hydroponics setup partial order
Env_Hydro_PO = StrictPartialOrder(
    nodes=[Env_Control, Hydro_Setup, Nutrient_Mix, Light_Config, Automation_Dev]
)
Env_Hydro_PO.order.add_edge(Env_Control, Hydro_Setup)
Env_Hydro_PO.order.add_edge(Hydro_Setup, Nutrient_Mix)
Env_Hydro_PO.order.add_edge(Nutrient_Mix, Light_Config)
Env_Hydro_PO.order.add_edge(Light_Config, Automation_Dev)

# System Test depends on automation dev and staff training complete
SystemTest_PO = StrictPartialOrder(nodes=[Automation_Dev, Staff_Training, System_Test])
SystemTest_PO.order.add_edge(Automation_Dev, System_Test)
SystemTest_PO.order.add_edge(Staff_Training, System_Test)

# Crop Seeding after successful system test
# Data monitoring and yield optimization can be concurrent after Crop seeding
PostSeed_PO = StrictPartialOrder(nodes=[Crop_Seeding, Data_Monitor, Yield_Optimize])
PostSeed_PO.order.add_edge(Crop_Seeding, Data_Monitor)
PostSeed_PO.order.add_edge(Crop_Seeding, Yield_Optimize)
# No order between Data Monitor and Yield Optimize => concurrent

# Supply alignment depends on Data Monitor and Yield Optimize (both)
Supply_PO = StrictPartialOrder(nodes=[Data_Monitor, Yield_Optimize, Supply_Align])
Supply_PO.order.add_edge(Data_Monitor, Supply_Align)
Supply_PO.order.add_edge(Yield_Optimize, Supply_Align)

# Maintenance plan depends on Supply Align
Maint_PO = StrictPartialOrder(nodes=[Supply_Align, Maintenance_Plan])
Maint_PO.order.add_edge(Supply_Align, Maintenance_Plan)

# Initial planning phase: Site survey then Layout plan
Initial_PO = StrictPartialOrder(nodes=[Site_Survey, Layout_Plan])
Initial_PO.order.add_edge(Site_Survey, Layout_Plan)

# Assemble first phase: Initial plan -> Coordination & Training
Phase1_PO = StrictPartialOrder(
    nodes=[Initial_PO, Coord_Authorities, Training_PO]
)
Phase1_PO.order.add_edge(Initial_PO, Coord_Authorities)
Phase1_PO.order.add_edge(Coord_Authorities, Training_PO)

# Assemble setup phase: Environmental/hydro -> System test
Phase2_PO = StrictPartialOrder(nodes=[Env_Hydro_PO, SystemTest_PO])
Phase2_PO.order.add_edge(Env_Hydro_PO, SystemTest_PO)

# Assemble monitoring & optimization phase: Post seed -> Supply -> Maintenance
Phase3_PO = StrictPartialOrder(nodes=[PostSeed_PO, Supply_PO, Maint_PO])
Phase3_PO.order.add_edge(PostSeed_PO, Supply_PO)
Phase3_PO.order.add_edge(Supply_PO, Maint_PO)

# Compose main flow:
# Phase1 -> Phase2 -> Phase3
root = StrictPartialOrder(nodes=[Phase1_PO, Phase2_PO, Phase3_PO])
root.order.add_edge(Phase1_PO, Phase2_PO)
root.order.add_edge(Phase2_PO, Phase3_PO)