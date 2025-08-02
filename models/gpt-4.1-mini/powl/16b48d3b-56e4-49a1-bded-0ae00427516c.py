# Generated from: 16b48d3b-56e4-49a1-bded-0ae00427516c.json
# Description: This process outlines the establishment of an urban vertical farming facility designed to maximize crop yield in limited city spaces using hydroponic and aeroponic systems. It integrates site analysis, modular infrastructure assembly, environmental control calibration, nutrient delivery optimization, and continuous monitoring. The workflow includes coordination with local authorities for permits, sourcing sustainable materials, implementing energy-efficient lighting, and setting up automated harvesting and packaging systems. The process also emphasizes adaptive crop rotation planning, employee training on advanced agricultural technologies, and integration of data analytics for yield prediction and resource management, ensuring a scalable and eco-friendly urban agriculture model.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
Site_Survey = Transition(label='Site Survey')
Permit_Request = Transition(label='Permit Request')
Material_Sourcing = Transition(label='Material Sourcing')
Modular_Build = Transition(label='Modular Build')
System_Wiring = Transition(label='System Wiring')
Enviro_Setup = Transition(label='Enviro Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')
Lighting_Install = Transition(label='Lighting Install')
Sensor_Deploy = Transition(label='Sensor Deploy')
Calibration_Run = Transition(label='Calibration Run')
Crop_Seeding = Transition(label='Crop Seeding')
Irrigation_Test = Transition(label='Irrigation Test')
Growth_Monitor = Transition(label='Growth Monitor')
Data_Analysis = Transition(label='Data Analysis')
Harvest_Prep = Transition(label='Harvest Prep')
Packaging_Line = Transition(label='Packaging Line')
Waste_Manage = Transition(label='Waste Manage')
Staff_Training = Transition(label='Staff Training')

###############################################
# Structure interpretation:

# 1) Site Survey --> Permit Request (coordination with local authorities)
po1 = StrictPartialOrder(nodes=[Site_Survey, Permit_Request])
po1.order.add_edge(Site_Survey, Permit_Request)

# 2) Material Sourcing (sourcing sustainable materials)
# Can run concurrently with Permit Request
# So partial order with nodes = Permit_Request, Material_Sourcing with no edges (concurrent)
po2 = StrictPartialOrder(nodes=[Permit_Request, Material_Sourcing])  # concurrent

# 3) After both Permit Request and Material Sourcing done, Modular Build and System Wiring start
# Modular Build depends on Material Sourcing (need materials)
# System Wiring depends on Modular Build (wiring the modules)
po3 = StrictPartialOrder(nodes=[Modular_Build, System_Wiring])
po3.order.add_edge(Modular_Build, System_Wiring)

# Combine po2 and po3 in a partial order; Modular Build depends on Material Sourcing,
# Material Sourcing concurrent with Permit Request,
# but Modular Build cannot start before Material Sourcing,
# also Permit Request completes independently but Modular Build & wiring after Materials
po_build = StrictPartialOrder(nodes=[Permit_Request, Material_Sourcing, Modular_Build, System_Wiring])
po_build.order.add_edge(Modular_Build, System_Wiring)
po_build.order.add_edge(Material_Sourcing, Modular_Build)

# 4) Environmental control calibration:
# Enviro Setup, Lighting Install, Sensor Deploy can be done concurrently after wiring done
enviro_setup_group = StrictPartialOrder(nodes=[Enviro_Setup, Lighting_Install, Sensor_Deploy])

# Calibration Run depends on Enviro Setup, Lighting Install, Sensor Deploy
calibration_run_group = StrictPartialOrder(nodes=[Enviro_Setup, Lighting_Install, Sensor_Deploy, Calibration_Run])
calibration_run_group.order.add_edge(Enviro_Setup, Calibration_Run)
calibration_run_group.order.add_edge(Lighting_Install, Calibration_Run)
calibration_run_group.order.add_edge(Sensor_Deploy, Calibration_Run)

# 5) Nutrient Mix and Irrigation Test come after Calibration Run
# Nutrient Mix and Irrigation Test can be parallel
nutrient_irrigation = StrictPartialOrder(nodes=[Nutrient_Mix, Irrigation_Test])

# Calibration_Run --> Nutrient Mix and Irrigation Test
nutrient_irr_after_calib = StrictPartialOrder(nodes=[Calibration_Run, Nutrient_Mix, Irrigation_Test])
nutrient_irr_after_calib.order.add_edge(Calibration_Run, Nutrient_Mix)
nutrient_irr_after_calib.order.add_edge(Calibration_Run, Irrigation_Test)

# 6) Crop Seeding after Nutrient Mix and Irrigation Test
crop_seeding_after = StrictPartialOrder(nodes=[Nutrient_Mix, Irrigation_Test, Crop_Seeding])
crop_seeding_after.order.add_edge(Nutrient_Mix, Crop_Seeding)
crop_seeding_after.order.add_edge(Irrigation_Test, Crop_Seeding)

# 7) Growth Monitor runs after Crop Seeding
growth_monitor_after = StrictPartialOrder(nodes=[Crop_Seeding, Growth_Monitor])
growth_monitor_after.order.add_edge(Crop_Seeding, Growth_Monitor)

# 8) Data Analysis runs concurrent with Growth Monitor (monitor produces data analyzed in parallel)
growth_data_analysis = StrictPartialOrder(nodes=[Growth_Monitor, Data_Analysis])
# no edge means concurrent

# 9) Harvest Prep after Growth Monitor and Data Analysis both done
harvest_prep_order = StrictPartialOrder(nodes=[Growth_Monitor, Data_Analysis, Harvest_Prep])
harvest_prep_order.order.add_edge(Growth_Monitor, Harvest_Prep)
harvest_prep_order.order.add_edge(Data_Analysis, Harvest_Prep)

# 10) Packaging Line after Harvest Prep
packaging_after = StrictPartialOrder(nodes=[Harvest_Prep, Packaging_Line])
packaging_after.order.add_edge(Harvest_Prep, Packaging_Line)

# 11) Waste Manage concurrent or after Packaging Line?
# Manage waste after packaging to handle residues
waste_after_pack = StrictPartialOrder(nodes=[Packaging_Line, Waste_Manage])
waste_after_pack.order.add_edge(Packaging_Line, Waste_Manage)

# 12) Staff Training can occur any time after Site Survey is done (early training, adaptive crop rotation planning)
# We'll make Staff Training start after Site Survey and concurrent with ongoing tasks (like Build etc)
# So Staff Training depends on Site Survey
staff_train_after = StrictPartialOrder(nodes=[Site_Survey, Staff_Training])
staff_train_after.order.add_edge(Site_Survey, Staff_Training)

#########################################
# Combine all parts via partial order respecting dependencies

# Root nodes:
# Start: Site_Survey

# Site Survey --> Permit Request
# Permit Request concurrent with Material Sourcing
# Material Sourcing --> Modular Build --> System Wiring
# System Wiring --> (Enviro Setup, Lighting Install, Sensor Deploy) (concurrent)
# (Enviro Setup, Lighting Install, Sensor Deploy) --> Calibration Run
# Calibration Run --> (Nutrient Mix, Irrigation Test) (concurrent)
# Both --> Crop Seeding --> Growth Monitor --> Data Analysis (parallel) --> Harvest Prep --> Packaging Line --> Waste Manage

# Staff Training depends on Site Survey and can be concurrent with everything after Site Survey

# Build one big partial order with all nodes and edges

all_nodes = [
    Site_Survey,
    Permit_Request,
    Material_Sourcing,
    Modular_Build,
    System_Wiring,
    Enviro_Setup,
    Lighting_Install,
    Sensor_Deploy,
    Calibration_Run,
    Nutrient_Mix,
    Irrigation_Test,
    Crop_Seeding,
    Growth_Monitor,
    Data_Analysis,
    Harvest_Prep,
    Packaging_Line,
    Waste_Manage,
    Staff_Training,
]

root = StrictPartialOrder(nodes=all_nodes)

# Add edges per above logic
root.order.add_edge(Site_Survey, Permit_Request)
root.order.add_edge(Site_Survey, Staff_Training)

# Permit Request and Material Sourcing concurrent (no edge)

root.order.add_edge(Material_Sourcing, Modular_Build)
root.order.add_edge(Modular_Build, System_Wiring)

root.order.add_edge(System_Wiring, Enviro_Setup)
root.order.add_edge(System_Wiring, Lighting_Install)
root.order.add_edge(System_Wiring, Sensor_Deploy)

root.order.add_edge(Enviro_Setup, Calibration_Run)
root.order.add_edge(Lighting_Install, Calibration_Run)
root.order.add_edge(Sensor_Deploy, Calibration_Run)

root.order.add_edge(Calibration_Run, Nutrient_Mix)
root.order.add_edge(Calibration_Run, Irrigation_Test)

root.order.add_edge(Nutrient_Mix, Crop_Seeding)
root.order.add_edge(Irrigation_Test, Crop_Seeding)

root.order.add_edge(Crop_Seeding, Growth_Monitor)

# Growth Monitor and Data Analysis concurrent but Data Analysis presumably depends on Growth Monitor data to start,
# interpretation: start Data Analysis after Growth Monitor begins (we model with Growth Monitor --> Data Analysis)
# Or just concurrency (no edge). To be conservative, add edge.
root.order.add_edge(Growth_Monitor, Data_Analysis)

root.order.add_edge(Growth_Monitor, Harvest_Prep)
root.order.add_edge(Data_Analysis, Harvest_Prep)

root.order.add_edge(Harvest_Prep, Packaging_Line)
root.order.add_edge(Packaging_Line, Waste_Manage)