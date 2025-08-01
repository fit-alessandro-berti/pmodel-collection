# Generated from: 3c12d807-03e3-49d5-b201-99870fa08b46.json
# Description: This process outlines the complex steps involved in establishing a vertical farming operation within an urban environment. It includes site analysis for structural suitability, environmental impact assessment, resource logistics coordination, specialized equipment procurement, modular farm assembly, hydroponic system calibration, nutrient solution formulation, integrated pest management planning, real-time monitoring setup using IoT sensors, staff training in crop management, regulatory compliance verification, community engagement initiatives, yield forecasting, and continuous optimization based on data analytics to ensure sustainable production and profitability in constrained urban spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activity nodes
Site_Survey = Transition(label='Site Survey')
Impact_Study = Transition(label='Impact Study')
Resource_Plan = Transition(label='Resource Plan')
Vendor_Select = Transition(label='Vendor Select')
Equipment_Order = Transition(label='Equipment Order')
Module_Build = Transition(label='Module Build')
Hydroponic_Setup = Transition(label='Hydroponic Setup')
Solution_Mix = Transition(label='Solution Mix')
Pest_Control = Transition(label='Pest Control')
Sensor_Setup = Transition(label='Sensor Setup')
Staff_Train = Transition(label='Staff Train')
Compliance_Check = Transition(label='Compliance Check')
Community_Meet = Transition(label='Community Meet')
Yield_Forecast = Transition(label='Yield Forecast')
Data_Review = Transition(label='Data Review')

# Construct partial orders to capture plausible concurrency and ordering based on the description.

# Initial site and impact assessment happen sequentially
initial_PO = StrictPartialOrder(nodes=[Site_Survey, Impact_Study])
initial_PO.order.add_edge(Site_Survey, Impact_Study)

# In parallel: resource planning and vendor select (both likely can be concurrent after impact study)
resource_PO = StrictPartialOrder(nodes=[Resource_Plan, Vendor_Select])
# No order edges, concurrent

# Equipment order depends on vendor select
equipment_PO = StrictPartialOrder(nodes=[Vendor_Select, Equipment_Order])
equipment_PO.order.add_edge(Vendor_Select, Equipment_Order)

# Module build and hydroponic setup happen after equipment order
module_hydro_PO = StrictPartialOrder(nodes=[Equipment_Order, Module_Build, Hydroponic_Setup])
module_hydro_PO.order.add_edge(Equipment_Order, Module_Build)
module_hydro_PO.order.add_edge(Equipment_Order, Hydroponic_Setup)

# Nutrient solution mix and pest control after hydroponic setup (both can be concurrent)
nutrients_pest_PO = StrictPartialOrder(nodes=[Hydroponic_Setup, Solution_Mix, Pest_Control])
nutrients_pest_PO.order.add_edge(Hydroponic_Setup, Solution_Mix)
nutrients_pest_PO.order.add_edge(Hydroponic_Setup, Pest_Control)

# Sensor setup and staff training depend on module build and nutrient/pest activities
sensor_staff_PO = StrictPartialOrder(
    nodes=[Module_Build, Solution_Mix, Pest_Control, Sensor_Setup, Staff_Train]
)
sensor_staff_PO.order.add_edge(Module_Build, Sensor_Setup)
sensor_staff_PO.order.add_edge(Module_Build, Staff_Train)
sensor_staff_PO.order.add_edge(Solution_Mix, Sensor_Setup)
sensor_staff_PO.order.add_edge(Solution_Mix, Staff_Train)
sensor_staff_PO.order.add_edge(Pest_Control, Sensor_Setup)
sensor_staff_PO.order.add_edge(Pest_Control, Staff_Train)

# Compliance check can be done concurrently with sensor setup / staff training
compliance_PO = StrictPartialOrder(nodes=[Sensor_Setup, Staff_Train, Compliance_Check])
# Compliance_Check after or concurrent with sensor setup and staff training? Assume after both.
compliance_PO.order.add_edge(Sensor_Setup, Compliance_Check)
compliance_PO.order.add_edge(Staff_Train, Compliance_Check)

# Community meeting can be parallel or after compliance check
community_PO = StrictPartialOrder(nodes=[Compliance_Check, Community_Meet])
community_PO.order.add_edge(Compliance_Check, Community_Meet)

# Yield forecast after community meet
yield_PO = StrictPartialOrder(nodes=[Community_Meet, Yield_Forecast])
yield_PO.order.add_edge(Community_Meet, Yield_Forecast)

# Data review after yield forecast, loop back for continuous optimization:
# Form a loop: run Yield Forecast, then Data Review and back to Yield Forecast or exit.
loop = OperatorPOWL(operator=Operator.LOOP, children=[Yield_Forecast, Data_Review])

# Now compose the big partial order:
# Chain initial_PO -> resource_PO -> equipment_PO -> module_hydro_PO -> nutrients_pest_PO -> sensor_staff_PO -> compliance_PO -> community_PO -> loop

root = StrictPartialOrder(nodes=[
    initial_PO,
    resource_PO,
    equipment_PO,
    module_hydro_PO,
    nutrients_pest_PO,
    sensor_staff_PO,
    compliance_PO,
    community_PO,
    loop
])
root.order.add_edge(initial_PO, resource_PO)
root.order.add_edge(resource_PO, equipment_PO)
root.order.add_edge(equipment_PO, module_hydro_PO)
root.order.add_edge(module_hydro_PO, nutrients_pest_PO)
root.order.add_edge(nutrients_pest_PO, sensor_staff_PO)
root.order.add_edge(sensor_staff_PO, compliance_PO)
root.order.add_edge(compliance_PO, community_PO)
root.order.add_edge(community_PO, loop)