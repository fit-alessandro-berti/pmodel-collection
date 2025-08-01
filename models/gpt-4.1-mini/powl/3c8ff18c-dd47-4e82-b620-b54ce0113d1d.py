# Generated from: 3c8ff18c-dd47-4e82-b620-b54ce0113d1d.json
# Description: This process outlines the establishment of an urban vertical farming system within a repurposed industrial building. It involves site analysis, modular rack installation, climate system calibration, nutrient solution preparation, seed selection, automated planting, lighting optimization, pest monitoring, data analytics integration, crop harvesting, waste recycling, packaging, and distribution logistics. The process ensures sustainable, high-yield crop production with minimal environmental impact, leveraging IoT sensors and AI-driven adjustments to maximize efficiency in a dense urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

SiteSurvey = Transition(label='Site Survey')
RackSetup = Transition(label='Rack Setup')
ClimateAdjust = Transition(label='Climate Adjust')
NutrientMix = Transition(label='Nutrient Mix')
SeedSelect = Transition(label='Seed Select')
AutoPlant = Transition(label='Auto Plant')
LightTune = Transition(label='Light Tune')
PestCheck = Transition(label='Pest Check')
SensorSync = Transition(label='Sensor Sync')
DataReview = Transition(label='Data Review')
GrowthScan = Transition(label='Growth Scan')
HarvestCrop = Transition(label='Harvest Crop')
WasteSort = Transition(label='Waste Sort')
PackGoods = Transition(label='Pack Goods')
Distribute = Transition(label='Distribute')

root = StrictPartialOrder(
    nodes=[
        SiteSurvey,
        RackSetup,
        ClimateAdjust,
        NutrientMix,
        SeedSelect,
        AutoPlant,
        LightTune,
        PestCheck,
        SensorSync,
        DataReview,
        GrowthScan,
        HarvestCrop,
        WasteSort,
        PackGoods,
        Distribute,
    ]
)

root.order.add_edge(SiteSurvey, RackSetup)
root.order.add_edge(RackSetup, ClimateAdjust)

root.order.add_edge(ClimateAdjust, NutrientMix)
root.order.add_edge(ClimateAdjust, SeedSelect)

root.order.add_edge(NutrientMix, AutoPlant)
root.order.add_edge(SeedSelect, AutoPlant)

root.order.add_edge(AutoPlant, LightTune)
root.order.add_edge(LightTune, PestCheck)

root.order.add_edge(PestCheck, SensorSync)
root.order.add_edge(SensorSync, DataReview)
root.order.add_edge(DataReview, GrowthScan)

root.order.add_edge(GrowthScan, HarvestCrop)

root.order.add_edge(HarvestCrop, WasteSort)
root.order.add_edge(HarvestCrop, PackGoods)

root.order.add_edge(WasteSort, Distribute)
root.order.add_edge(PackGoods, Distribute)