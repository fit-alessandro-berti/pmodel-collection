# Generated from: abceea7b-1c75-4ab9-981f-b52daaf9e24a.json
# Description: This process outlines the setup of an urban vertical farming system integrating advanced hydroponics, IoT environmental controls, and renewable energy sources in a compact city environment. It involves site analysis, modular structure assembly, nutrient solution preparation, sensor calibration, automated planting, growth monitoring, pest management through biological agents, and yield forecasting using AI models. The process also includes waste recycling, community engagement for local distribution, and continuous system optimization based on real-time data analytics to maximize crop yield and sustainability within limited urban space.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
structure_build = Transition(label='Structure Build')
install_sensors = Transition(label='Install Sensors')
mix_nutrients = Transition(label='Mix Nutrients')
calibrate_controls = Transition(label='Calibrate Controls')
seed_planting = Transition(label='Seed Planting')
set_irrigation = Transition(label='Set Irrigation')
monitor_growth = Transition(label='Monitor Growth')
pest_control = Transition(label='Pest Control')
data_analysis = Transition(label='Data Analysis')
waste_recycle = Transition(label='Waste Recycle')
energy_optimize = Transition(label='Energy Optimize')
community_meet = Transition(label='Community Meet')
forecast_yield = Transition(label='Forecast Yield')
system_update = Transition(label='System Update')

# Build partial orders for main sequences

# Initial setup: Site Survey -> Design Layout -> Structure Build
initial_setup = StrictPartialOrder(nodes=[site_survey, design_layout, structure_build])
initial_setup.order.add_edge(site_survey, design_layout)
initial_setup.order.add_edge(design_layout, structure_build)

# Sensor and nutrient preparation: Install Sensors -> Calibrate Controls, Mix Nutrients (parallel)
sensor_prep = StrictPartialOrder(nodes=[install_sensors, calibrate_controls])
sensor_prep.order.add_edge(install_sensors, calibrate_controls)

nutrient_prep = mix_nutrients  # single node

# Combine sensor calibration and nutrient mixing in parallel (they are both after Structure Build)
sensors_and_nutrients = StrictPartialOrder(nodes=[sensor_prep, nutrient_prep])

# Automated planting and irrigation settings in sequence
plant_irrigate = StrictPartialOrder(nodes=[seed_planting, set_irrigation])
plant_irrigate.order.add_edge(seed_planting, set_irrigation)

# Growth monitoring with pest control (parallel)
monitor_pest = StrictPartialOrder(nodes=[monitor_growth, pest_control])

# Data analysis and forecast yield (sequential) and then system update
analysis_yield_update = StrictPartialOrder(nodes=[data_analysis, forecast_yield, system_update])
analysis_yield_update.order.add_edge(data_analysis, forecast_yield)
analysis_yield_update.order.add_edge(forecast_yield, system_update)

# Waste recycle and energy optimize and community meet - all concurrent parallel tasks after main growth process
waste_energy_community = StrictPartialOrder(
    nodes=[waste_recycle, energy_optimize, community_meet]
)
# No order edges, fully parallel

# Build the full workflow as partial order with edges connecting the main parts

# First level: initial_setup
# Then sensors_and_nutrients and plant_irrigate after initial_setup and sensor/nutrient prep
# Then monitor_pest after plant_irrigate
# Then analysis_yield_update after monitor_pest
# Then waste_energy_community last (concurrent, after analysis)

root = StrictPartialOrder(
    nodes=[
        initial_setup,
        sensors_and_nutrients,
        plant_irrigate,
        monitor_pest,
        analysis_yield_update,
        waste_energy_community,
    ]
)

# Define ordering between these major workflow parts
root.order.add_edge(initial_setup, sensors_and_nutrients)
root.order.add_edge(sensors_and_nutrients, plant_irrigate)
root.order.add_edge(plant_irrigate, monitor_pest)
root.order.add_edge(monitor_pest, analysis_yield_update)
root.order.add_edge(analysis_yield_update, waste_energy_community)