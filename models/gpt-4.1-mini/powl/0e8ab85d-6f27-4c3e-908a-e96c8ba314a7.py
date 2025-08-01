# Generated from: 0e8ab85d-6f27-4c3e-908a-e96c8ba314a7.json
# Description: This process outlines the comprehensive steps required to establish an urban vertical farming facility in a repurposed warehouse. It includes site analysis, environmental control calibration, modular system installation, nutrient cycling optimization, and continuous crop monitoring. The process integrates IoT sensor deployment for real-time data, automated irrigation scheduling, and adaptive lighting adjustments based on crop growth phases. Additionally, it involves waste recycling protocols, staff training on precision agriculture technologies, and market readiness assessments to ensure sustainable production and profitable yield cycles within a compact urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
SiteSurvey = Transition(label='Site Survey')
DesignLayout = Transition(label='Design Layout')
StructureRetrofit = Transition(label='Structure Retrofit')
SystemInstall = Transition(label='System Install')
SensorSetup = Transition(label='Sensor Setup')
EnviroCalibrate = Transition(label='Enviro Calibrate')
NutrientMix = Transition(label='Nutrient Mix')
IrrigationPlan = Transition(label='Irrigation Plan')
LightingAdjust = Transition(label='Lighting Adjust')
CropPlanting = Transition(label='Crop Planting')
GrowthMonitor = Transition(label='Growth Monitor')
WasteRecycle = Transition(label='Waste Recycle')
DataAnalysis = Transition(label='Data Analysis')
StaffTraining = Transition(label='Staff Training')
MarketReview = Transition(label='Market Review')
YieldForecast = Transition(label='Yield Forecast')

# Create sub partial orders to reflect the process and concurrency

# Phase 1: Setup and preparation (site survey, design, retrofit, install)
preparation = StrictPartialOrder(
    nodes=[SiteSurvey, DesignLayout, StructureRetrofit, SystemInstall]
)
preparation.order.add_edge(SiteSurvey, DesignLayout)
preparation.order.add_edge(DesignLayout, StructureRetrofit)
preparation.order.add_edge(StructureRetrofit, SystemInstall)

# Phase 2: Sensor deployment and environmental calibration can run concurrently with staff training and waste recycling preparation
sensors_calibration = StrictPartialOrder(
    nodes=[SensorSetup, EnviroCalibrate]
)
sensors_calibration.order.add_edge(SensorSetup, EnviroCalibrate)

support_activities = StrictPartialOrder(
    nodes=[WasteRecycle, StaffTraining]
)
# Staff training and waste recycling are concurrent, no order edge

# Phase 3: System operation planning (nutrient mix, irrigation, lighting)
operation_planning = StrictPartialOrder(
    nodes=[NutrientMix, IrrigationPlan, LightingAdjust]
)
# All three can be concurrent
# No edges

# Phase 4: Planting and growth monitoring
planting_monitoring = StrictPartialOrder(
    nodes=[CropPlanting, GrowthMonitor]
)
planting_monitoring.order.add_edge(CropPlanting, GrowthMonitor)

# Phase 5: Data analysis, market review, and yield forecast can be concurrent but all after growth monitoring and sensors/calibration done
analysis_review_forecast = StrictPartialOrder(
    nodes=[DataAnalysis, MarketReview, YieldForecast]
)
# Concurrent (no edges)

# Combine Phase 2 and Phase 3 concurrency
second_phase = StrictPartialOrder(
    nodes=[sensors_calibration, support_activities, operation_planning]
)
second_phase.order.add_edge(sensors_calibration, operation_planning)
# Support activities can run concurrently, no edges needed

# Combine Phase 4 after operation planning
third_phase = StrictPartialOrder(
    nodes=[operation_planning, planting_monitoring]
)
third_phase.order.add_edge(operation_planning, planting_monitoring)

# Combine all phases with overall order:

# preparation -> Phase2 + Phase3 (represented by second_phase)
# second_phase (sensor calibration, support_activities (waste recycle + staff training), operation_planning)
# planting_monitoring after operation_planning is embedded in third_phase, so we keep that

# We can link preparation to second_phase, second_phase to planting_monitoring, planting_monitoring to analysis_review_forecast

# Because composition is a bit complex, let's flatten logically as follows:

# root nodes: preparation, second_phase, planting_monitoring, analysis_review_forecast

root = StrictPartialOrder(
    nodes=[preparation, sensors_calibration, support_activities, operation_planning, planting_monitoring, analysis_review_forecast]
)

# preparation before sensors_calibration and support_activities and operation_planning
root.order.add_edge(preparation, sensors_calibration)
root.order.add_edge(preparation, support_activities)
root.order.add_edge(preparation, operation_planning)

# operation_planning before planting_monitoring
root.order.add_edge(operation_planning, planting_monitoring)

# planting_monitoring before analysis_review_forecast
root.order.add_edge(planting_monitoring, analysis_review_forecast)