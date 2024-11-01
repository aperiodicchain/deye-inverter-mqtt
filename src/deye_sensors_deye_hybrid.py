# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# This file is autogenerated

# flake8: noqa

from deye_sensor import (
    SingleRegisterSensor,
    ComputedPowerSensor,
    DoubleRegisterSensor,
    ComputedSumSensor,
    SensorRegisterRange,
)

deye_hybrid_solar_186 = SingleRegisterSensor(
    "PV1 Power", 186, 1, mqtt_topic_suffix="dc/pv1/power", unit="W", signed=False, groups=["deye_hybrid"]
)

deye_hybrid_solar_187 = SingleRegisterSensor(
    "PV2 Power", 187, 1, mqtt_topic_suffix="dc/pv2/power", unit="W", signed=False, groups=["deye_hybrid"]
)

deye_hybrid_solar_109 = SingleRegisterSensor(
    "PV1 Voltage", 109, 0.1, mqtt_topic_suffix="dc/pv1/voltage", unit="V", signed=False, groups=["deye_hybrid"]
)

deye_hybrid_solar_111 = SingleRegisterSensor(
    "PV2 Voltage", 111, 0.1, mqtt_topic_suffix="dc/pv2/voltage", unit="V", signed=False, groups=["deye_hybrid"]
)

deye_hybrid_solar_110 = SingleRegisterSensor(
    "PV1 Current", 110, 0.1, mqtt_topic_suffix="dc/pv1/current", unit="A", signed=False, groups=["deye_hybrid"]
)

deye_hybrid_solar_112 = SingleRegisterSensor(
    "PV2 Current", 112, 0.1, mqtt_topic_suffix="dc/pv2/current", unit="A", signed=False, groups=["deye_hybrid"]
)

deye_hybrid_solar_108 = SingleRegisterSensor(
    "Daily Production", 108, 0.1, mqtt_topic_suffix="day_energy", unit="kWh", signed=False, groups=["deye_hybrid"]
)

deye_hybrid_solar_96 = DoubleRegisterSensor(
    "Total Production", 96, 0.1, mqtt_topic_suffix="total_energy", unit="kWh", signed=False, groups=["deye_hybrid"]
)

deye_hybrid_solar_166 = SingleRegisterSensor(
    "Micro-inverter Power",
    166,
    1,
    mqtt_topic_suffix="micro_inverter_power",
    unit="W",
    signed=False,
    groups=["deye_hybrid"],
)

deye_hybrid_battery_72 = DoubleRegisterSensor(
    "Total Battery Charge",
    72,
    0.1,
    mqtt_topic_suffix="battery/total_charge",
    unit="kWh",
    signed=False,
    groups=["deye_hybrid_battery"],
)

deye_hybrid_battery_74 = DoubleRegisterSensor(
    "Total Battery Discharge",
    74,
    0.1,
    mqtt_topic_suffix="battery/total_discharge",
    unit="kWh",
    signed=False,
    groups=["deye_hybrid_battery"],
)

deye_hybrid_battery_70 = SingleRegisterSensor(
    "Daily Battery Charge",
    70,
    0.1,
    mqtt_topic_suffix="battery/daily_charge",
    unit="kWh",
    signed=False,
    groups=["deye_hybrid_battery"],
)

deye_hybrid_battery_71 = SingleRegisterSensor(
    "Daily Battery Discharge",
    71,
    0.1,
    mqtt_topic_suffix="battery/daily_discharge",
    unit="kWh",
    signed=False,
    groups=["deye_hybrid_battery"],
)

deye_hybrid_battery_189 = SingleRegisterSensor(
    "Battery Status", 189, 1, mqtt_topic_suffix="battery/status", unit="", signed=False, groups=["deye_hybrid_battery"]
)

deye_hybrid_battery_190 = SingleRegisterSensor(
    "Battery Power", 190, 1, mqtt_topic_suffix="battery/power", unit="W", signed=True, groups=["deye_hybrid_battery"]
)

deye_hybrid_battery_183 = SingleRegisterSensor(
    "Battery Voltage",
    183,
    0.01,
    mqtt_topic_suffix="battery/voltage",
    unit="V",
    signed=False,
    groups=["deye_hybrid_battery"],
)

deye_hybrid_battery_184 = SingleRegisterSensor(
    "Battery SOC", 184, 1, mqtt_topic_suffix="battery/soc", unit="%", signed=False, groups=["deye_hybrid_battery"]
)

deye_hybrid_battery_191 = SingleRegisterSensor(
    "Battery Current",
    191,
    0.01,
    mqtt_topic_suffix="battery/current",
    unit="A",
    signed=True,
    groups=["deye_hybrid_battery"],
)

deye_hybrid_battery_182 = SingleRegisterSensor(
    "Battery Temperature",
    182,
    0.1,
    offset=-100.0,
    mqtt_topic_suffix="battery/temperature",
    unit="°C",
    signed=False,
    groups=["deye_hybrid_battery"],
)

deye_hybrid_grid_169 = SingleRegisterSensor(
    "Total Grid Power", 169, 1, mqtt_topic_suffix="ac/total_grid_power", unit="W", signed=True, groups=["deye_hybrid"]
)

deye_hybrid_grid_150 = SingleRegisterSensor(
    "Grid Voltage L1", 150, 0.1, mqtt_topic_suffix="ac/l1/voltage", unit="V", signed=False, groups=["deye_hybrid"]
)

deye_hybrid_grid_151 = SingleRegisterSensor(
    "Grid Voltage L2", 151, 0.1, mqtt_topic_suffix="ac/l2/voltage", unit="V", signed=False, groups=["deye_hybrid"]
)

deye_hybrid_grid_167 = SingleRegisterSensor(
    "Internal CT L1 Power", 167, 1, mqtt_topic_suffix="ac/l1/ct/internal", unit="W", signed=True, groups=["deye_hybrid"]
)

deye_hybrid_grid_168 = SingleRegisterSensor(
    "Internal CT L2 Power", 168, 1, mqtt_topic_suffix="ac/l2/ct/internal", unit="W", signed=True, groups=["deye_hybrid"]
)

deye_hybrid_grid_170 = SingleRegisterSensor(
    "External CT L1 Power", 170, 1, mqtt_topic_suffix="ac/l1/ct/external", unit="W", signed=True, groups=["deye_hybrid"]
)

deye_hybrid_grid_171 = SingleRegisterSensor(
    "External CT L2 Power", 171, 1, mqtt_topic_suffix="ac/l2/ct/external", unit="W", signed=True, groups=["deye_hybrid"]
)

deye_hybrid_grid_76 = SingleRegisterSensor(
    "Daily Energy Bought",
    76,
    0.1,
    mqtt_topic_suffix="ac/daily_energy_bought",
    unit="kWh",
    signed=False,
    groups=["deye_hybrid"],
)

deye_hybrid_grid_78 = DoubleRegisterSensor(
    "Total Energy Bought",
    78,
    0.1,
    mqtt_topic_suffix="ac/total_energy_bought",
    unit="kWh",
    signed=False,
    groups=["deye_hybrid"],
)

deye_hybrid_grid_77 = SingleRegisterSensor(
    "Daily Energy Sold",
    77,
    0.1,
    mqtt_topic_suffix="ac/daily_energy_sold",
    unit="kWh",
    signed=False,
    groups=["deye_hybrid"],
)

deye_hybrid_grid_81 = DoubleRegisterSensor(
    "Total Energy Sold",
    81,
    0.1,
    mqtt_topic_suffix="ac/total_energy_sold",
    unit="kWh",
    signed=False,
    groups=["deye_hybrid"],
)

deye_hybrid_inverter_175 = SingleRegisterSensor(
    "Total Power", 175, 1, mqtt_topic_suffix="ac/total_power", unit="W", signed=True, groups=["deye_hybrid"]
)

deye_hybrid_inverter_164 = SingleRegisterSensor(
    "Current L1", 164, 0.01, mqtt_topic_suffix="ac/l1/current", unit="A", signed=True, groups=["deye_hybrid"]
)

deye_hybrid_inverter_165 = SingleRegisterSensor(
    "Current L2", 165, 0.01, mqtt_topic_suffix="ac/l2/current", unit="A", signed=True, groups=["deye_hybrid"]
)

deye_hybrid_inverter_173 = SingleRegisterSensor(
    "Inverter L1 Power", 173, 1, mqtt_topic_suffix="ac/l1/power", unit="W", signed=True, groups=["deye_hybrid"]
)

deye_hybrid_inverter_174 = SingleRegisterSensor(
    "Inverter L2 Power", 174, 1, mqtt_topic_suffix="ac/l2/power", unit="W", signed=True, groups=["deye_hybrid"]
)

deye_hybrid_inverter_192 = SingleRegisterSensor(
    "Load Frequency", 192, 0.01, mqtt_topic_suffix="ac/frequency", unit="Hz", signed=False, groups=["deye_hybrid"]
)

deye_hybrid_inverter_90 = SingleRegisterSensor(
    "DC Temperature",
    90,
    0.1,
    offset=-100.0,
    mqtt_topic_suffix="radiator_temp",
    unit="°C",
    signed=True,
    groups=["deye_hybrid"],
)

deye_hybrid_inverter_91 = SingleRegisterSensor(
    "AC Temperature",
    91,
    0.1,
    offset=-100.0,
    mqtt_topic_suffix="ac/temperature",
    unit="°C",
    signed=True,
    groups=["deye_hybrid"],
)

deye_hybrid_time_of_use_250 = SingleRegisterSensor(
    "Time of use Time 1",
    250,
    1,
    mqtt_topic_suffix="timeofuse/time/1",
    unit="",
    signed=False,
    groups=["deye_hybrid_timeofuse"],
)

deye_hybrid_time_of_use_251 = SingleRegisterSensor(
    "Time of use Time 2",
    251,
    1,
    mqtt_topic_suffix="timeofuse/time/2",
    unit="",
    signed=False,
    groups=["deye_hybrid_timeofuse"],
)

deye_hybrid_time_of_use_252 = SingleRegisterSensor(
    "Time of Use Time 3",
    252,
    1,
    mqtt_topic_suffix="timeofuse/time/3",
    unit="",
    signed=False,
    groups=["deye_hybrid_timeofuse"],
)

deye_hybrid_time_of_use_253 = SingleRegisterSensor(
    "Time of Use Time 4",
    253,
    1,
    mqtt_topic_suffix="timeofuse/time/4",
    unit="",
    signed=False,
    groups=["deye_hybrid_timeofuse"],
)

deye_hybrid_time_of_use_254 = SingleRegisterSensor(
    "Time of Use Time 5",
    254,
    1,
    mqtt_topic_suffix="timeofuse/time/5",
    unit="",
    signed=False,
    groups=["deye_hybrid_timeofuse"],
)

deye_hybrid_time_of_use_255 = SingleRegisterSensor(
    "Time of Use Time 6",
    255,
    1,
    mqtt_topic_suffix="timeofuse/time/6",
    unit="",
    signed=False,
    groups=["deye_hybrid_timeofuse"],
)

deye_hybrid_time_of_use_256 = SingleRegisterSensor(
    "Time of Use Power 1",
    256,
    1,
    mqtt_topic_suffix="timeofuse/power/1",
    unit="",
    signed=False,
    groups=["deye_hybrid_timeofuse"],
)

deye_hybrid_time_of_use_257 = SingleRegisterSensor(
    "Time of Use Power 2",
    257,
    1,
    mqtt_topic_suffix="timeofuse/power/2",
    unit="",
    signed=False,
    groups=["deye_hybrid_timeofuse"],
)

deye_hybrid_time_of_use_258 = SingleRegisterSensor(
    "Time of Use Power 3",
    258,
    1,
    mqtt_topic_suffix="timeofuse/power/3",
    unit="",
    signed=False,
    groups=["deye_hybrid_timeofuse"],
)

deye_hybrid_time_of_use_259 = SingleRegisterSensor(
    "Time of Use Power 4",
    259,
    1,
    mqtt_topic_suffix="timeofuse/power/4",
    unit="",
    signed=False,
    groups=["deye_hybrid_timeofuse"],
)

deye_hybrid_time_of_use_260 = SingleRegisterSensor(
    "Time of Use Power 5",
    260,
    1,
    mqtt_topic_suffix="timeofuse/power/5",
    unit="",
    signed=False,
    groups=["deye_hybrid_timeofuse"],
)

deye_hybrid_time_of_use_261 = SingleRegisterSensor(
    "Time of Use Power 6",
    261,
    1,
    mqtt_topic_suffix="timeofuse/power/6",
    unit="",
    signed=False,
    groups=["deye_hybrid_timeofuse"],
)

deye_hybrid_time_of_use_268 = SingleRegisterSensor(
    "Time of Use SOC 1",
    268,
    1,
    mqtt_topic_suffix="timeofuse/soc/1",
    unit="",
    signed=False,
    groups=["deye_hybrid_timeofuse"],
)

deye_hybrid_time_of_use_269 = SingleRegisterSensor(
    "Time of Use SOC 2",
    269,
    1,
    mqtt_topic_suffix="timeofuse/soc/2",
    unit="",
    signed=False,
    groups=["deye_hybrid_timeofuse"],
)

deye_hybrid_time_of_use_270 = SingleRegisterSensor(
    "Time of Use SOC 3",
    270,
    1,
    mqtt_topic_suffix="timeofuse/soc/3",
    unit="",
    signed=False,
    groups=["deye_hybrid_timeofuse"],
)

deye_hybrid_time_of_use_271 = SingleRegisterSensor(
    "Time of Use SOC 4",
    271,
    1,
    mqtt_topic_suffix="timeofuse/soc/4",
    unit="",
    signed=False,
    groups=["deye_hybrid_timeofuse"],
)

deye_hybrid_time_of_use_272 = SingleRegisterSensor(
    "Time of Use SOC 5",
    272,
    1,
    mqtt_topic_suffix="timeofuse/soc/5",
    unit="",
    signed=False,
    groups=["deye_hybrid_timeofuse"],
)

deye_hybrid_time_of_use_273 = SingleRegisterSensor(
    "Time of Use SOC 6",
    273,
    1,
    mqtt_topic_suffix="timeofuse/soc/6",
    unit="",
    signed=False,
    groups=["deye_hybrid_timeofuse"],
)

deye_hybrid_time_of_use_274 = SingleRegisterSensor(
    "Time of Use Enable 1",
    274,
    1,
    mqtt_topic_suffix="timeofuse/enabled/1",
    unit="",
    signed=False,
    groups=["deye_hybrid_timeofuse"],
)

deye_hybrid_time_of_use_275 = SingleRegisterSensor(
    "Time of Use Enable 2",
    275,
    1,
    mqtt_topic_suffix="timeofuse/enabled/2",
    unit="",
    signed=False,
    groups=["deye_hybrid_timeofuse"],
)

deye_hybrid_time_of_use_276 = SingleRegisterSensor(
    "Time of Use Enable 3",
    276,
    1,
    mqtt_topic_suffix="timeofuse/enabled/3",
    unit="",
    signed=False,
    groups=["deye_hybrid_timeofuse"],
)

deye_hybrid_time_of_use_277 = SingleRegisterSensor(
    "Time of Use Enable 4",
    277,
    1,
    mqtt_topic_suffix="timeofuse/enabled/4",
    unit="",
    signed=False,
    groups=["deye_hybrid_timeofuse"],
)

deye_hybrid_time_of_use_278 = SingleRegisterSensor(
    "Time of Use Enable 5",
    278,
    1,
    mqtt_topic_suffix="timeofuse/enabled/5",
    unit="",
    signed=False,
    groups=["deye_hybrid_timeofuse"],
)

deye_hybrid_time_of_use_279 = SingleRegisterSensor(
    "Time of Use Enable 6",
    279,
    1,
    mqtt_topic_suffix="timeofuse/enabled/6",
    unit="",
    signed=False,
    groups=["deye_hybrid_timeofuse"],
)

deye_hybrid_time_of_use_248 = SingleRegisterSensor(
    "Time of use",
    248,
    1,
    mqtt_topic_suffix="timeofuse/enabled",
    unit="",
    signed=False,
    groups=["deye_hybrid_timeofuse"],
)

deye_hybrid_time_of_use_262 = SingleRegisterSensor(
    "Time of Use Voltage 1",
    262,
    0.01,
    mqtt_topic_suffix="timeofuse/voltage/1",
    unit="V",
    signed=False,
    groups=["deye_hybrid_timeofuse"],
)

deye_hybrid_time_of_use_263 = SingleRegisterSensor(
    "Time of Use Voltage 2",
    263,
    0.01,
    mqtt_topic_suffix="timeofuse/voltage/2",
    unit="V",
    signed=False,
    groups=["deye_hybrid_timeofuse"],
)

deye_hybrid_time_of_use_264 = SingleRegisterSensor(
    "Time of Use Voltage 3",
    264,
    0.01,
    mqtt_topic_suffix="timeofuse/voltage/3",
    unit="V",
    signed=False,
    groups=["deye_hybrid_timeofuse"],
)

deye_hybrid_time_of_use_265 = SingleRegisterSensor(
    "Time of Use Voltage 4",
    265,
    0.01,
    mqtt_topic_suffix="timeofuse/voltage/4",
    unit="V",
    signed=False,
    groups=["deye_hybrid_timeofuse"],
)

deye_hybrid_time_of_use_266 = SingleRegisterSensor(
    "Time of Use Voltage 5",
    266,
    0.01,
    mqtt_topic_suffix="timeofuse/voltage/5",
    unit="V",
    signed=False,
    groups=["deye_hybrid_timeofuse"],
)

deye_hybrid_time_of_use_267 = SingleRegisterSensor(
    "Time of Use Voltage 6",
    267,
    0.01,
    mqtt_topic_suffix="timeofuse/voltage/6",
    unit="V",
    signed=False,
    groups=["deye_hybrid_timeofuse"],
)

deye_hybrid_bms_312 = SingleRegisterSensor(
    "BMS1 Charging Voltage",
    312,
    0.01,
    mqtt_topic_suffix="bms/1/charging_voltage",
    unit="V",
    signed=False,
    groups=["deye_hybrid_bms"],
)

deye_hybrid_bms_313 = SingleRegisterSensor(
    "BMS1 Discharge Voltage",
    313,
    0.01,
    mqtt_topic_suffix="bms/1/discharge_voltage",
    unit="V",
    signed=False,
    groups=["deye_hybrid_bms"],
)

deye_hybrid_bms_314 = SingleRegisterSensor(
    "BMS1 Charge Current Limit",
    314,
    1,
    mqtt_topic_suffix="bms/1/charge_current_limit",
    unit="A",
    signed=False,
    groups=["deye_hybrid_bms"],
)

deye_hybrid_bms_315 = SingleRegisterSensor(
    "BMS1 Discharge Current Limit",
    315,
    1,
    mqtt_topic_suffix="bms/1/discharge_current_limit",
    unit="A",
    signed=False,
    groups=["deye_hybrid_bms"],
)

deye_hybrid_bms_316 = SingleRegisterSensor(
    "BMS1 SOC", 316, 1, mqtt_topic_suffix="bms/1/soc", unit="%", signed=False, groups=["deye_hybrid_bms"]
)

deye_hybrid_bms_317 = SingleRegisterSensor(
    "BMS1 Voltage", 317, 0.01, mqtt_topic_suffix="bms/1/voltage", unit="V", signed=False, groups=["deye_hybrid_bms"]
)

deye_hybrid_bms_318 = SingleRegisterSensor(
    "BMS1 Current", 318, 1, mqtt_topic_suffix="bms/1/current", unit="A", signed=True, groups=["deye_hybrid_bms"]
)

deye_hybrid_bms_319 = SingleRegisterSensor(
    "BMS1 Temp", 319, 0.1, mqtt_topic_suffix="bms/1/temp", unit="°C", signed=False, groups=["deye_hybrid_bms"]
)

deye_hybrid_sensors = [
    deye_hybrid_solar_186,
    deye_hybrid_solar_187,
    deye_hybrid_solar_109,
    deye_hybrid_solar_111,
    deye_hybrid_solar_110,
    deye_hybrid_solar_112,
    deye_hybrid_solar_108,
    deye_hybrid_solar_96,
    deye_hybrid_solar_166,
    deye_hybrid_battery_72,
    deye_hybrid_battery_74,
    deye_hybrid_battery_70,
    deye_hybrid_battery_71,
    deye_hybrid_battery_189,
    deye_hybrid_battery_190,
    deye_hybrid_battery_183,
    deye_hybrid_battery_184,
    deye_hybrid_battery_191,
    deye_hybrid_battery_182,
    deye_hybrid_grid_169,
    deye_hybrid_grid_150,
    deye_hybrid_grid_151,
    deye_hybrid_grid_167,
    deye_hybrid_grid_168,
    deye_hybrid_grid_170,
    deye_hybrid_grid_171,
    deye_hybrid_grid_76,
    deye_hybrid_grid_78,
    deye_hybrid_grid_77,
    deye_hybrid_grid_81,
    deye_hybrid_inverter_175,
    deye_hybrid_inverter_164,
    deye_hybrid_inverter_165,
    deye_hybrid_inverter_173,
    deye_hybrid_inverter_174,
    deye_hybrid_inverter_192,
    deye_hybrid_inverter_90,
    deye_hybrid_inverter_91,
    deye_hybrid_time_of_use_250,
    deye_hybrid_time_of_use_251,
    deye_hybrid_time_of_use_252,
    deye_hybrid_time_of_use_253,
    deye_hybrid_time_of_use_254,
    deye_hybrid_time_of_use_255,
    deye_hybrid_time_of_use_256,
    deye_hybrid_time_of_use_257,
    deye_hybrid_time_of_use_258,
    deye_hybrid_time_of_use_259,
    deye_hybrid_time_of_use_260,
    deye_hybrid_time_of_use_261,
    deye_hybrid_time_of_use_268,
    deye_hybrid_time_of_use_269,
    deye_hybrid_time_of_use_270,
    deye_hybrid_time_of_use_271,
    deye_hybrid_time_of_use_272,
    deye_hybrid_time_of_use_273,
    deye_hybrid_time_of_use_274,
    deye_hybrid_time_of_use_275,
    deye_hybrid_time_of_use_276,
    deye_hybrid_time_of_use_277,
    deye_hybrid_time_of_use_278,
    deye_hybrid_time_of_use_279,
    deye_hybrid_time_of_use_248,
    deye_hybrid_time_of_use_262,
    deye_hybrid_time_of_use_263,
    deye_hybrid_time_of_use_264,
    deye_hybrid_time_of_use_265,
    deye_hybrid_time_of_use_266,
    deye_hybrid_time_of_use_267,
    deye_hybrid_bms_312,
    deye_hybrid_bms_313,
    deye_hybrid_bms_314,
    deye_hybrid_bms_315,
    deye_hybrid_bms_316,
    deye_hybrid_bms_317,
    deye_hybrid_bms_318,
    deye_hybrid_bms_319,
]

deye_hybrid_register_ranges = [
    SensorRegisterRange(group="deye_hybrid_battery", first_reg_address=3, last_reg_address=112),
    SensorRegisterRange(group="deye_hybrid", first_reg_address=3, last_reg_address=112),
    SensorRegisterRange(group="deye_hybrid_timeofuse", first_reg_address=150, last_reg_address=249),
    SensorRegisterRange(group="deye_hybrid_battery", first_reg_address=150, last_reg_address=249),
    SensorRegisterRange(group="deye_hybrid", first_reg_address=150, last_reg_address=249),
    SensorRegisterRange(group="deye_hybrid_timeofuse", first_reg_address=250, last_reg_address=279),
    SensorRegisterRange(group="deye_hybrid_bms", first_reg_address=312, last_reg_address=319),
]
