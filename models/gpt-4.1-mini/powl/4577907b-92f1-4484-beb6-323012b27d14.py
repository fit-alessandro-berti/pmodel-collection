# Generated from: 4577907b-92f1-4484-beb6-323012b27d14.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farming operation within a metropolitan building. It includes site assessment for structural capacity and sunlight optimization, integration of automated hydroponic systems, IoT sensor deployment for real-time monitoring, nutrient solution calibration, and climate control setup. The workflow further involves workforce training on system maintenance, scheduling crop cycles for maximum yield, implementing pest management protocols without pesticides, and coordinating logistics for local distribution. Continuous data analysis and iterative adjustment of environmental parameters ensure sustainable growth and energy efficiency. The process culminates in certification compliance and marketing launch to promote locally grown produce in urban communities, providing a scalable model for future expansion.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Site_Survey = Transition(label='Site Survey')
Load_Test = Transition(label='Load Test')
Light_Mapping = Transition(label='Light Mapping')
System_Design = Transition(label='System Design')
Hydro_Setup = Transition(label='Hydro Setup')
Sensor_Install = Transition(label='Sensor Install')
Nutrient_Mix = Transition(label='Nutrient Mix')
Climate_Control = Transition(label='Climate Control')
Staff_Training = Transition(label='Staff Training')
Crop_Planning = Transition(label='Crop Planning')
Pest_Control = Transition(label='Pest Control')
Data_Monitoring = Transition(label='Data Monitoring')
Yield_Analysis = Transition(label='Yield Analysis')
Compliance_Check = Transition(label='Compliance Check')
Market_Launch = Transition(label='Market Launch')

# Site assessment partial order: Site Survey --> {Load Test, Light Mapping} concurrently
site_assessment = StrictPartialOrder(nodes=[Site_Survey, Load_Test, Light_Mapping])
site_assessment.order.add_edge(Site_Survey, Load_Test)
site_assessment.order.add_edge(Site_Survey, Light_Mapping)

# System integration partial order: System Design --> Hydro Setup --> Sensor Install
system_integration = StrictPartialOrder(nodes=[System_Design, Hydro_Setup, Sensor_Install])
system_integration.order.add_edge(System_Design, Hydro_Setup)
system_integration.order.add_edge(Hydro_Setup, Sensor_Install)

# Nutrient and climate partial order: Nutrient Mix --> Climate Control
nutrient_climate = StrictPartialOrder(nodes=[Nutrient_Mix, Climate_Control])
nutrient_climate.order.add_edge(Nutrient_Mix, Climate_Control)

# Training and planning partial order: Staff Training --> Crop Planning --> Pest Control (pesticide-free)
training_planning = StrictPartialOrder(nodes=[Staff_Training, Crop_Planning, Pest_Control])
training_planning.order.add_edge(Staff_Training, Crop_Planning)
training_planning.order.add_edge(Crop_Planning, Pest_Control)

# Data analysis loop: Data Monitoring and Yield Analysis repeatedly to adjust parameters
data_monitoring = Data_Monitoring
yield_analysis = Yield_Analysis
# Loop node: execute Data Monitoring, then choose exit or (Yield Analysis then again Data Monitoring)
monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_monitoring, yield_analysis])

# Logistics and final steps partial order: Compliance Check --> Market Launch
final_steps = StrictPartialOrder(nodes=[Compliance_Check, Market_Launch])
final_steps.order.add_edge(Compliance_Check, Market_Launch)

# Combine: site_assessment --> system_integration --> nutrient_climate --> training_planning --> monitoring_loop --> final_steps
root = StrictPartialOrder(
    nodes=[
        site_assessment,
        system_integration,
        nutrient_climate,
        training_planning,
        monitoring_loop,
        final_steps
    ]
)
root.order.add_edge(site_assessment, system_integration)
root.order.add_edge(system_integration, nutrient_climate)
root.order.add_edge(nutrient_climate, training_planning)
root.order.add_edge(training_planning, monitoring_loop)
root.order.add_edge(monitoring_loop, final_steps)