# Generated from: 33d03a3d-34b4-466e-ac80-9231cb9f5671.json
# Description: This process outlines the comprehensive operational cycle of an urban vertical farming system integrating automated hydroponics, environmental control, and crop yield optimization. Beginning with seed selection adapted for vertical growth, it moves through nutrient solution calibration, climate modulation, and multi-layer planting schedules. Continuous sensor data analysis enables adaptive lighting and irrigation adjustments while pest monitoring employs AI-driven detection. Harvesting is staggered to maximize space utilization, followed by post-harvest sorting and packaging within onsite clean rooms. Waste biomass is processed into bio-compost, closing the sustainability loop. This atypical but realistic process blends agriculture, IoT technology, and urban sustainability initiatives to meet local food demand efficiently within constrained city spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
seed_selection   = Transition(label='Seed Selection')
nutrient_mix     = Transition(label='Nutrient Mix')
climate_setup    = Transition(label='Climate Setup')
layer_planting   = Transition(label='Layer Planting')
sensor_install   = Transition(label='Sensor Install')
data_monitor     = Transition(label='Data Monitoring')
lighting_adjust  = Transition(label='Lighting Adjust')
irrigation_tune  = Transition(label='Irrigation Tune')
pest_detect      = Transition(label='Pest Detect')
harvest_plan     = Transition(label='Harvest Plan')
crop_harvest     = Transition(label='Crop Harvest')
sorting_pack     = Transition(label='Sorting Pack')
waste_collect    = Transition(label='Waste Collect')
bio_compost      = Transition(label='Bio-Compost')
yield_review     = Transition(label='Yield Review')
system_clean     = Transition(label='System Clean')

# Define the intra-cycle sensor loop:
#   A = Data Monitoring
#   B = concurrent adjustments: Lighting, Irrigation, Pest
sensor_adjustments = StrictPartialOrder(
    nodes=[lighting_adjust, irrigation_tune, pest_detect]
)
sensor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[data_monitor, sensor_adjustments]
)

# Build the top‐level partial order of the vertical farming cycle
root = StrictPartialOrder(
    nodes=[
        seed_selection,
        nutrient_mix,
        climate_setup,
        layer_planting,
        sensor_install,
        sensor_loop,
        harvest_plan,
        crop_harvest,
        sorting_pack,
        waste_collect,
        bio_compost,
        yield_review,
        system_clean
    ]
)

# Define the control‐flow ordering
root.order.add_edge(seed_selection, nutrient_mix)
root.order.add_edge(nutrient_mix, climate_setup)
root.order.add_edge(climate_setup, layer_planting)
root.order.add_edge(layer_planting, sensor_install)
root.order.add_edge(sensor_install, sensor_loop)
root.order.add_edge(sensor_loop, harvest_plan)
root.order.add_edge(harvest_plan, crop_harvest)
root.order.add_edge(crop_harvest, sorting_pack)
root.order.add_edge(sorting_pack, waste_collect)
root.order.add_edge(waste_collect, bio_compost)
root.order.add_edge(bio_compost, yield_review)
root.order.add_edge(yield_review, system_clean)