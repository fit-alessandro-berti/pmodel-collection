# Generated from: 4ec9e802-c9c5-4e16-88bf-ce88d8e7199a.json
# Description: This process outlines a highly adaptive urban farming cycle designed to optimize crop yields in micro-environments within cityscapes. It begins with microclimate scanning to assess localized conditions, followed by dynamic soil profiling to tailor nutrient delivery. The system employs modular planting strategies which adapt based on real-time sensor data, enabling selective germination and staggered growth phases. Automated pest detection and biological control deployment ensure sustainable protection without chemicals. Concurrently, vertical irrigation management adjusts water flow based on evapotranspiration rates. Harvesting is synchronized with market demand analytics to minimize waste and maximize freshness. Post-harvest sorting integrates AI-driven quality assessment, while urban composting loops recycle organic waste into nutrient-rich substrates. Finally, community feedback and data-driven analytics refine future cycles, creating a continuous improvement loop tailored for dense urban agricultural ecosystems.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Microclimate_Scan = Transition(label='Microclimate Scan')
Soil_Profiling = Transition(label='Soil Profiling')
Nutrient_Mapping = Transition(label='Nutrient Mapping')
Modular_Planting = Transition(label='Modular Planting')
Sensor_Calibration = Transition(label='Sensor Calibration')
Germination_Check = Transition(label='Germination Check')
Growth_Staggering = Transition(label='Growth Staggering')
Pest_Detection = Transition(label='Pest Detection')
Biocontrol_Deploy = Transition(label='Biocontrol Deploy')
Irrigation_Adjust = Transition(label='Irrigation Adjust')
Market_Sync = Transition(label='Market Sync')
Harvest_Timing = Transition(label='Harvest Timing')
Quality_Sorting = Transition(label='Quality Sorting')
Compost_Processing = Transition(label='Compost Processing')
Feedback_Analyze = Transition(label='Feedback Analyze')
Cycle_Refinement = Transition(label='Cycle Refinement')

# Modular Planting sub-process partial order for selective germination and staggered growth
ModularPlanting_PO = StrictPartialOrder(
    nodes=[Modular_Planting, Sensor_Calibration, Germination_Check, Growth_Staggering]
)
ModularPlanting_PO.order.add_edge(Modular_Planting, Sensor_Calibration)
ModularPlanting_PO.order.add_edge(Sensor_Calibration, Germination_Check)
ModularPlanting_PO.order.add_edge(Germination_Check, Growth_Staggering)

# Pest control partial order: Pest Detection then Biocontrol Deploy
PestControl_PO = StrictPartialOrder(
    nodes=[Pest_Detection, Biocontrol_Deploy]
)
PestControl_PO.order.add_edge(Pest_Detection, Biocontrol_Deploy)

# Harvesting partial order: Market Sync then Harvest Timing
Harvest_PO = StrictPartialOrder(
    nodes=[Market_Sync, Harvest_Timing]
)
Harvest_PO.order.add_edge(Market_Sync, Harvest_Timing)

# Post-harvest partial order: Quality Sorting then Compost Processing
PostHarvest_PO = StrictPartialOrder(
    nodes=[Quality_Sorting, Compost_Processing]
)
PostHarvest_PO.order.add_edge(Quality_Sorting, Compost_Processing)

# Feedback loop partial order: Feedback Analyze then Cycle Refinement
Feedback_PO = StrictPartialOrder(
    nodes=[Feedback_Analyze, Cycle_Refinement]
)
Feedback_PO.order.add_edge(Feedback_Analyze, Cycle_Refinement)

# Compost loop: Compost Processing and Cycle Refinement form a loop (recycle organic waste into substrates, then refine cycle)
# Define loop: first Compost Processing, then either exit or do Feedback_PO then Compost Processing again
# The loop children: body activity Compost Processing and loop body Feedback_PO
Compost_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Compost_Processing, Feedback_PO]
)

# Combine Pest control and irrigation concurrently
Pest_Irrigation_PO = StrictPartialOrder(
    nodes=[PestControl_PO, Irrigation_Adjust]
)
# The PestControl_PO happens before Irrigation_Adjust, or concurrently?
# Description says concurrently pest detection & biocontrol and irrigation management happen concurrently.
# So no order edges between PestControl_PO and Irrigation_Adjust
# Therefore no edges between PestControl_PO and Irrigation_Adjust, so concurrency assumed
# Since PestControl_PO is itself a PO, it's better to add them both as nodes in the main PO directly.

# Top-level partial order
root = StrictPartialOrder(
    nodes=[
        Microclimate_Scan,
        Soil_Profiling,
        Nutrient_Mapping,
        ModularPlanting_PO,
        PestControl_PO,
        Irrigation_Adjust,
        Harvest_PO,
        PostHarvest_PO,
        Compost_loop,
        Feedback_PO,
        Cycle_Refinement,
    ]
)

# Define order
root.order.add_edge(Microclimate_Scan, Soil_Profiling)  # microclimate scan -> soil profiling
root.order.add_edge(Soil_Profiling, Nutrient_Mapping)  # soil profiling -> nutrient mapping

# Nutrient mapping then modular planting strategies
root.order.add_edge(Nutrient_Mapping, ModularPlanting_PO)

# Modular planting includes several steps internally
# After ModularPlanting, pest control and irrigation execute concurrently (no order edges)
root.order.add_edge(ModularPlanting_PO, PestControl_PO)
root.order.add_edge(ModularPlanting_PO, Irrigation_Adjust)

# Pest control partial order already defined internally

# After pest control and irrigation, harvesting happens
root.order.add_edge(PestControl_PO, Harvest_PO)
root.order.add_edge(Irrigation_Adjust, Harvest_PO)

# After harvesting, post-harvest sorting and compost processing
root.order.add_edge(Harvest_PO, PostHarvest_PO)

# Compost processing node is part of Compost_loop, which includes feedback and cycle refinement in a loop
# So link PostHarvest_PO to compost loop
root.order.add_edge(PostHarvest_PO, Compost_loop)

# Compost_loop ends include Cycle_Refinement, which is also part of Feedback_PO
# We do not add extra edges, the loop structure handles cycling Compost Processing and Feedback Analyze/Cycle Refinement

# The Feedback_PO is included as child of the loop, so no need to add additional edges outside loop

# End definition