# Generated from: 5eb2e3f6-4b85-44be-9267-5e2d2f64bf64.json
# Description: This process involves the end-to-end deployment of an urban vertical farming system in dense metropolitan areas. It begins with site analysis and regulatory compliance checks, followed by modular farm design tailored to the building structure. Procurement of specialized hydroponic equipment and nutrient solutions is critical, alongside the integration of IoT sensors for climate control. Installation includes assembling grow racks, lighting, and irrigation systems. Post-installation, calibration of environmental controls ensures optimal plant growth. Staff training on maintenance and data monitoring is conducted before initiating the crop seeding phase. Continuous monitoring, pest management, and yield optimization are performed throughout the growth cycle. Finally, harvested produce is packaged and distributed locally, completing the sustainable urban agriculture supply chain.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Activities
Site_Analysis = Transition(label='Site Analysis')
Permits_Check = Transition(label='Permits Check')
Farm_Design = Transition(label='Farm Design')
Equipment_Buy = Transition(label='Equipment Buy')
Nutrient_Prep = Transition(label='Nutrient Prep')
Sensor_Setup = Transition(label='Sensor Setup')
Rack_Install = Transition(label='Rack Install')
Light_Config = Transition(label='Light Config')
Irrigation_Fit = Transition(label='Irrigation Fit')
Enviro_Calibrate = Transition(label='Enviro Calibrate')
Staff_Training = Transition(label='Staff Training')
Crop_Seeding = Transition(label='Crop Seeding')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Control = Transition(label='Pest Control')
Yield_Optimize = Transition(label='Yield Optimize')
Harvest_Pack = Transition(label='Harvest Pack')
Local_Deliver = Transition(label='Local Deliver')

# Partial order for Procurement (Equipment Buy and Nutrient Prep and Sensor Setup can be concurrent but must be after Farm Design)
procurement = StrictPartialOrder(nodes=[Equipment_Buy, Nutrient_Prep, Sensor_Setup])

# Partial order for Installation (Rack Install, Light Config, Irrigation Fit - concurrent but after procurement)
installation = StrictPartialOrder(nodes=[Rack_Install, Light_Config, Irrigation_Fit])

# Partial order for growth cycle monitoring loop (Growth Monitor, Pest Control, Yield Optimize concurrent)
growth_cycle = StrictPartialOrder(nodes=[Growth_Monitor, Pest_Control, Yield_Optimize])

# Loop for continuous monitoring, pest management, and yield optimization:
# loop body: growth_cycle, then choice to continue monitoring or exit
loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_cycle, growth_cycle])

# Partial order for Finalization (Harvest Pack and Local Deliver sequential)
finalization = StrictPartialOrder(nodes=[Harvest_Pack, Local_Deliver])
finalization.order.add_edge(Harvest_Pack, Local_Deliver)

# Build the overall process partial order
root = StrictPartialOrder(nodes=[
    Site_Analysis,
    Permits_Check,
    Farm_Design,
    procurement,
    installation,
    Enviro_Calibrate,
    Staff_Training,
    Crop_Seeding,
    loop,
    finalization
])

# Add order edges for the phases:
root.order.add_edge(Site_Analysis, Permits_Check)
root.order.add_edge(Permits_Check, Farm_Design)
root.order.add_edge(Farm_Design, procurement)
root.order.add_edge(procurement, installation)
root.order.add_edge(installation, Enviro_Calibrate)
root.order.add_edge(Enviro_Calibrate, Staff_Training)
root.order.add_edge(Staff_Training, Crop_Seeding)
root.order.add_edge(Crop_Seeding, loop)
root.order.add_edge(loop, finalization)