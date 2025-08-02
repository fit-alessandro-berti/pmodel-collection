# Generated from: 88251bbf-2034-4e8e-86a7-6cfc141060ae.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farm within a metropolitan area. It includes site analysis, modular structure design, hydroponic system installation, sensor calibration, crop cycle planning, and integration of renewable energy sources. The process also covers regulatory compliance, community engagement, waste recycling, and real-time data monitoring to optimize yield and sustainability in a constrained urban environment, ensuring both economic viability and environmental responsibility.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Permits_Obtain = Transition(label='Permits Obtain')
Structure_Build = Transition(label='Structure Build')
Hydroponic_Setup = Transition(label='Hydroponic Setup')
Sensor_Install = Transition(label='Sensor Install')
Calibrate_Sensors = Transition(label='Calibrate Sensors')
Energy_Integrate = Transition(label='Energy Integrate')
Crop_Plan = Transition(label='Crop Plan')
Seed_Selection = Transition(label='Seed Selection')
Planting_Stage = Transition(label='Planting Stage')
Growth_Monitor = Transition(label='Growth Monitor')
Waste_Process = Transition(label='Waste Process')
Data_Analyze = Transition(label='Data Analyze')
Community_Meet = Transition(label='Community Meet')
Yield_Harvest = Transition(label='Yield Harvest')
Market_Launch = Transition(label='Market Launch')

# Site survey and design layout in sequence
site_and_design = StrictPartialOrder(nodes=[Site_Survey, Design_Layout])
site_and_design.order.add_edge(Site_Survey, Design_Layout)

# Permits obtain occurs after design layout
permits = StrictPartialOrder(nodes=[Permits_Obtain])
site_design_permits = StrictPartialOrder(nodes=[site_and_design, permits])
site_design_permits.order.add_edge(site_and_design, permits)

# Structure build follows permits
structure_build = StrictPartialOrder(nodes=[Structure_Build])
permits_structure = StrictPartialOrder(nodes=[permits, structure_build])
permits_structure.order.add_edge(permits, structure_build)

# Hydroponic Setup and Sensor Install can be concurrent after Structure Build
# So model partial order with Structure Build first, then both Hydroponic Setup and Sensor Install concurrent
# and Calibrate Sensors after Sensor Install
# Energy Integrate can run concurrently with Sensor Calibration
# After Hydroponic Setup and Sensor Calibration (+Energy Integrate), proceed to Crop Plan

# Partial order for Sensor Install -> Calibrate Sensors
sensor_seq = StrictPartialOrder(nodes=[Sensor_Install, Calibrate_Sensors])
sensor_seq.order.add_edge(Sensor_Install, Calibrate_Sensors)

# Energy Integrate runs in parallel with Calibrate Sensors
sensor_energy_po = StrictPartialOrder(nodes=[sensor_seq, Energy_Integrate])

# Hydroponic Setup is concurrent with sensor_energy_po
hydro_sensor_energy_po = StrictPartialOrder(nodes=[Hydroponic_Setup, sensor_energy_po])

# Structure Build precedes hydro_sensor_energy_po
structure_hydro_sensor = StrictPartialOrder(nodes=[structure_build, hydro_sensor_energy_po])
structure_hydro_sensor.order.add_edge(structure_build, hydro_sensor_energy_po)

# Crop Plan follows completion of Hydroponic Setup and sensor calibration/energy integration
crop_plan = Crop_Plan

# Crop Plan and Seed Selection in sequence
crop_seed = StrictPartialOrder(nodes=[crop_plan, Seed_Selection])
crop_seed.order.add_edge(crop_plan, Seed_Selection)

# Planting Stage follows Seed Selection
planting = Planting_Stage
seed_planting = StrictPartialOrder(nodes=[Seed_Selection, planting])
seed_planting.order.add_edge(Seed_Selection, planting)

# Growth Monitor after Planting
growth = Growth_Monitor
planting_growth = StrictPartialOrder(nodes=[planting, growth])
planting_growth.order.add_edge(planting, growth)

# Waste Process and Community Meet can be concurrent with Growth Monitor (environment and engagement)
growth_concurrent = StrictPartialOrder(nodes=[growth, Waste_Process, Community_Meet])

# Data Analyze after Growth Monitor
data_analyze = Data_Analyze
data_after_growth = StrictPartialOrder(nodes=[growth, data_analyze])
data_after_growth.order.add_edge(growth, data_analyze)

# Yield Harvest after Data Analyze
yield_harvest = Yield_Harvest
data_yield = StrictPartialOrder(nodes=[data_analyze, yield_harvest])
data_yield.order.add_edge(data_analyze, yield_harvest)

# Market Launch after Yield Harvest
market_launch = Market_Launch
yield_market = StrictPartialOrder(nodes=[yield_harvest, market_launch])
yield_market.order.add_edge(yield_harvest, market_launch)

# Combine all final steps in partial order respecting dependencies:
# Crop and planting through Market Launch linearized
crop_to_market = StrictPartialOrder(
    nodes=[crop_plan, Seed_Selection, planting, growth, data_analyze, yield_harvest, market_launch,
           Waste_Process, Community_Meet]
)
crop_to_market.order.add_edge(crop_plan, Seed_Selection)
crop_to_market.order.add_edge(Seed_Selection, planting)
crop_to_market.order.add_edge(planting, growth)
crop_to_market.order.add_edge(growth, data_analyze)
crop_to_market.order.add_edge(data_analyze, yield_harvest)
crop_to_market.order.add_edge(yield_harvest, market_launch)
# Waste_Process and Community_Meet concurrent with Growth_Monitor
crop_to_market.order.add_edge(growth, Waste_Process)
crop_to_market.order.add_edge(growth, Community_Meet)

# Now combine all main blocks
root = StrictPartialOrder(
    nodes=[site_and_design, permits, structure_build, hydro_sensor_energy_po, crop_to_market]
)
root.order.add_edge(site_and_design, permits)
root.order.add_edge(permits, structure_build)
root.order.add_edge(structure_build, hydro_sensor_energy_po)
root.order.add_edge(hydro_sensor_energy_po, crop_to_market)