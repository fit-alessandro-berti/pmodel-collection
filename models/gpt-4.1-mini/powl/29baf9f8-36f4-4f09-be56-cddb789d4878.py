# Generated from: 29baf9f8-36f4-4f09-be56-cddb789d4878.json
# Description: This process outlines the complex steps involved in establishing a sustainable urban rooftop farm in a densely populated city. It includes site assessment for structural integrity and sunlight exposure, regulatory compliance checks, soil and water testing, modular bed construction, seed selection for microclimates, installation of automated irrigation and nutrient delivery systems, pest management using integrated biological controls, community engagement for local participation, ongoing data monitoring through IoT sensors, yield forecasting, and seasonal crop rotation planning. The process also integrates waste composting from urban sources and renewable energy usage to minimize environmental footprint, ensuring economic viability and social impact in an unconventional agricultural setting.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transition instances
Site_Survey = Transition(label='Site Survey')
Risk_Assess = Transition(label='Risk Assess')
Permit_Check = Transition(label='Permit Check')
Soil_Sample = Transition(label='Soil Sample')
Water_Test = Transition(label='Water Test')
Bed_Build = Transition(label='Bed Build')
Seed_Select = Transition(label='Seed Select')
Irrigation_Install = Transition(label='Irrigation Install')
Nutrient_Setup = Transition(label='Nutrient Setup')
Pest_Control = Transition(label='Pest Control')
Community_Engage = Transition(label='Community Engage')
Sensor_Deploy = Transition(label='Sensor Deploy')
Data_Monitor = Transition(label='Data Monitor')
Yield_Forecast = Transition(label='Yield Forecast')
Waste_Compost = Transition(label='Waste Compost')
Energy_Integrate = Transition(label='Energy Integrate')
Crop_Rotate = Transition(label='Crop Rotate')

# Step 1 & 2: Site Survey -> Risk Assess -> Permit Check
site_assessment = StrictPartialOrder(nodes=[Site_Survey, Risk_Assess, Permit_Check])
site_assessment.order.add_edge(Site_Survey, Risk_Assess)
site_assessment.order.add_edge(Risk_Assess, Permit_Check)

# Step 3 & 4: Soil Sample and Water Test concurrent after Permit Check
soil_water = StrictPartialOrder(nodes=[Soil_Sample, Water_Test])
# They are concurrent (no order edges)

# Combine Assessment + Soil/Water tests
assess_and_tests = StrictPartialOrder(nodes=[site_assessment, soil_water])
assess_and_tests.order.add_edge(site_assessment, soil_water)

# Step 5: Bed Build after Soil and Water tests
bed_build = Bed_Build

# Step 6: Seed Select after Bed Build
seed_select = Seed_Select

# Step 7: Irrigation Install and Nutrient Setup can be done in parallel after Seed Select
irrigation_nutrient = StrictPartialOrder(nodes=[Irrigation_Install, Nutrient_Setup])

# Step 8: Pest Control after irrigation and nutrient setup
# So order edges connect irrigation and nutrient setup to pest control
pest_control = Pest_Control
# Pest Control depends on both irrigation and nutrient setup
irrigation_nutrient_pest = StrictPartialOrder(nodes=[irrigation_nutrient, pest_control])
irrigation_nutrient_pest.order.add_edge(irrigation_nutrient, pest_control)

# Step 9: Community Engage can be done in parallel with pest control or after
# For realistic sequencing, let’s say community engage starts after Pest Control
community_engage = Community_Engage

# Step 10 & 11: Sensor Deploy then Data Monitor after community engage
sensor_and_monitor = StrictPartialOrder(nodes=[Sensor_Deploy, Data_Monitor])
sensor_and_monitor.order.add_edge(Sensor_Deploy, Data_Monitor)

# The sensor_and_monitor depends on community_engage
community_and_sensor = StrictPartialOrder(nodes=[community_engage, sensor_and_monitor])
community_and_sensor.order.add_edge(community_engage, sensor_and_monitor)

# Step 12: Yield Forecast depends on Data Monitor
yield_forecast = Yield_Forecast

# Step 13: Waste Compost and Energy Integrate can be done concurrently at any time after initial setup
waste_energy = StrictPartialOrder(nodes=[Waste_Compost, Energy_Integrate])

# Step 14: Crop Rotate is a seasonal loop repeating the cycle of Seed Select onwards
# Loop(A=Seed_Select->...->Crop_Rotate; B=Crop_Rotate->Seed_Select to represent repeating crop rotations)

# Model the loop body: Seed Select -> Irrigation/Nutrient -> Pest Control -> Community Engage -> Sensor Deploy -> Data Monitor -> Yield Forecast -> Crop Rotate
loop_body_nodes = [
    Seed_Select,
    Irrigation_Install,
    Nutrient_Setup,
    Pest_Control,
    Community_Engage,
    Sensor_Deploy,
    Data_Monitor,
    Yield_Forecast,
    Crop_Rotate
]

loop_body = StrictPartialOrder(nodes=loop_body_nodes)
loop_body.order.add_edge(Seed_Select, Irrigation_Install)
loop_body.order.add_edge(Seed_Select, Nutrient_Setup)
loop_body.order.add_edge(Irrigation_Install, Pest_Control)
loop_body.order.add_edge(Nutrient_Setup, Pest_Control)
loop_body.order.add_edge(Pest_Control, Community_Engage)
loop_body.order.add_edge(Community_Engage, Sensor_Deploy)
loop_body.order.add_edge(Sensor_Deploy, Data_Monitor)
loop_body.order.add_edge(Data_Monitor, Yield_Forecast)
loop_body.order.add_edge(Yield_Forecast, Crop_Rotate)

# Loop structure: * (loop_body, silent exit)
silent_exit = SilentTransition()
crop_rotation_loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, silent_exit])

# Full initial setup before entering loop: Site assessment + soil/water tests + bed build
initial_setup = StrictPartialOrder(
    nodes=[assess_and_tests, Bed_Build]
)
initial_setup.order.add_edge(assess_and_tests, Bed_Build)

# Add waste compost and energy integrate concurrently to initial setup (can run in parallel)
setup_and_misc = StrictPartialOrder(
    nodes=[initial_setup, waste_energy]
)
setup_and_misc.order.add_edge(initial_setup, waste_energy)

# Combine initial setup, bed, and then loop
first_phase = StrictPartialOrder(
    nodes=[setup_and_misc, crop_rotation_loop]
)
first_phase.order.add_edge(setup_and_misc, crop_rotation_loop)

root = StrictPartialOrder(
    nodes=[Site_Survey, Risk_Assess, Permit_Check,
           Soil_Sample, Water_Test,
           Bed_Build,
           Waste_Compost, Energy_Integrate,
           crop_rotation_loop]
)

# add order edges reflecting dependencies as in first_phase
root.order.add_edge(Site_Survey, Risk_Assess)
root.order.add_edge(Risk_Assess, Permit_Check)
root.order.add_edge(Permit_Check, Soil_Sample)
root.order.add_edge(Permit_Check, Water_Test)
root.order.add_edge(Soil_Sample, Bed_Build)
root.order.add_edge(Water_Test, Bed_Build)
root.order.add_edge(Bed_Build, Waste_Compost)
root.order.add_edge(Bed_Build, Energy_Integrate)
root.order.add_edge(Waste_Compost, crop_rotation_loop)
root.order.add_edge(Energy_Integrate, crop_rotation_loop)

# Note: The loop structure defines internal order of crop rotation and related steps.

# The final root represents the full process.