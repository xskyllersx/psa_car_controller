# coding: utf-8

# flake8: noqa

"""
    Groupe PSA Connected Car - WEB API B2C

    *PSA B2C Connected Car API*  # Introduction This is the description of the *Groupe PSA Connected Car V2 API*. The speccification is  is based on **OpenAPI Specification version 3** and can be displayed via [ReDoc](https://github.com/Rebilly/ReDoc)a or [Swagger](http://swagger.io).   This API allows applications to fetch data from the connected Vehicles data platform. # Authentication PSA Connected Car APIs uses the [OAuth 2.0](https://tools.ietf.org/html/rfc6749) protocol for authentication and Authorization. any application require a valid [Access Token](https://tools.ietf.org/html/rfc6749#section-1.4) to access to user data. # Errors   Error codes returned by all REST APIs comply with the standard. Nevertheless, PSA Services (callers) need to have more complete data structures (even when the answer is not Http-OK) to better detail the type of error by providing application code, message and a debugging code(for investigation purposes). The http code of the response is managed by the protocol itself (in the header).      **Errors are  returned as a generic error response:**    * ```xError``` object model.       # noqa: E501

    OpenAPI spec version: 4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


# import apis into sdk package
from psa_car_controller.psa.connected_car_api.api.trips_api import TripsApi
from psa_car_controller.psa.connected_car_api.api.user_api import UserApi
from psa_car_controller.psa.connected_car_api.api.vehicles_api import VehiclesApi

# import ApiClient
from psa_car_controller.psa.connected_car_api.api_client import ApiClient
from psa_car_controller.psa.connected_car_api.configuration import Configuration
# import models into sdk package
from psa_car_controller.psa.connected_car_api.models.adas import Adas
from psa_car_controller.psa.connected_car_api.models.adas_park_assist import AdasParkAssist
from psa_car_controller.psa.connected_car_api.models.alert import Alert
from psa_car_controller.psa.connected_car_api.models.alert_end_position import AlertEndPosition
from psa_car_controller.psa.connected_car_api.models.alert_links import AlertLinks
from psa_car_controller.psa.connected_car_api.models.alert_msg_enum import AlertMsgEnum
from psa_car_controller.psa.connected_car_api.models.alerts import Alerts
from psa_car_controller.psa.connected_car_api.models.alerts_embedded import AlertsEmbedded
from psa_car_controller.psa.connected_car_api.models.battery import Battery
from psa_car_controller.psa.connected_car_api.models.bounded_program import BoundedProgram
from psa_car_controller.psa.connected_car_api.models.charging_status_enum import ChargingStatusEnum
from psa_car_controller.psa.connected_car_api.models.circle_zone import CircleZone
from psa_car_controller.psa.connected_car_api.models.circle_zone_coordinates import CircleZoneCoordinates
from psa_car_controller.psa.connected_car_api.models.collection_result import CollectionResult
from psa_car_controller.psa.connected_car_api.models.collision import Collision
from psa_car_controller.psa.connected_car_api.models.collision_links import CollisionLinks
from psa_car_controller.psa.connected_car_api.models.collision_obj import CollisionObj
from psa_car_controller.psa.connected_car_api.models.collision_obj_front import CollisionObjFront
from psa_car_controller.psa.connected_car_api.models.collisions import Collisions
from psa_car_controller.psa.connected_car_api.models.collisions_embedded import CollisionsEmbedded
from psa_car_controller.psa.connected_car_api.models.created_at_field import CreatedAtField
from psa_car_controller.psa.connected_car_api.models.data_monitor_trigger import DataMonitorTrigger
from psa_car_controller.psa.connected_car_api.models.data_trigger import DataTrigger
from psa_car_controller.psa.connected_car_api.models.default_alert_push import DefaultAlertPush
from psa_car_controller.psa.connected_car_api.models.default_alert_push_attributes import DefaultAlertPushAttributes
from psa_car_controller.psa.connected_car_api.models.doors_state import DoorsState
from psa_car_controller.psa.connected_car_api.models.doors_state_opening import DoorsStateOpening
from psa_car_controller.psa.connected_car_api.models.e_coaching import ECoaching
from psa_car_controller.psa.connected_car_api.models.e_coaching_links import ECoachingLinks
from psa_car_controller.psa.connected_car_api.models.e_coaching_scores import ECoachingScores
from psa_car_controller.psa.connected_car_api.models.energy import Energy
from psa_car_controller.psa.connected_car_api.models.energy_battery import EnergyBattery
from psa_car_controller.psa.connected_car_api.models.energy_battery_health import EnergyBatteryHealth
from psa_car_controller.psa.connected_car_api.models.energy_charging import EnergyCharging
from psa_car_controller.psa.connected_car_api.models.engine import Engine
from psa_car_controller.psa.connected_car_api.models.engine_oil import EngineOil
from psa_car_controller.psa.connected_car_api.models.environment import Environment
from psa_car_controller.psa.connected_car_api.models.environment_luminosity import EnvironmentLuminosity
from psa_car_controller.psa.connected_car_api.models.event import Event
from psa_car_controller.psa.connected_car_api.models.event_links import EventLinks
from psa_car_controller.psa.connected_car_api.models.extension import Extension
from psa_car_controller.psa.connected_car_api.models.extension_type import ExtensionType
from psa_car_controller.psa.connected_car_api.models.geometry import Geometry
from psa_car_controller.psa.connected_car_api.models.ignition import Ignition
from psa_car_controller.psa.connected_car_api.models.index_range import IndexRange
from psa_car_controller.psa.connected_car_api.models.kinetic import Kinetic
from psa_car_controller.psa.connected_car_api.models.lighting import Lighting
from psa_car_controller.psa.connected_car_api.models.link import Link
from psa_car_controller.psa.connected_car_api.models.maintenance import Maintenance
from psa_car_controller.psa.connected_car_api.models.maintenance_links import MaintenanceLinks
from psa_car_controller.psa.connected_car_api.models.maintenance_obj import MaintenanceObj
from psa_car_controller.psa.connected_car_api.models.monitor import Monitor
from psa_car_controller.psa.connected_car_api.models.monitor_id import MonitorId
from psa_car_controller.psa.connected_car_api.models.monitor_links import MonitorLinks
from psa_car_controller.psa.connected_car_api.models.monitor_parameter import MonitorParameter
from psa_car_controller.psa.connected_car_api.models.monitor_parameter_trigger_param import MonitorParameterTriggerParam
from psa_car_controller.psa.connected_car_api.models.monitor_ref import MonitorRef
from psa_car_controller.psa.connected_car_api.models.monitor_ref_links import MonitorRefLinks
from psa_car_controller.psa.connected_car_api.models.monitor_status import MonitorStatus
from psa_car_controller.psa.connected_car_api.models.monitor_status_setter import MonitorStatusSetter
from psa_car_controller.psa.connected_car_api.models.monitor_subscribe import MonitorSubscribe
from psa_car_controller.psa.connected_car_api.models.monitor_subscribe_batch_notify import MonitorSubscribeBatchNotify
from psa_car_controller.psa.connected_car_api.models.monitor_subscribe_retry_policy import MonitorSubscribeRetryPolicy
from psa_car_controller.psa.connected_car_api.models.monitor_trigger import MonitorTrigger
from psa_car_controller.psa.connected_car_api.models.monitor_webhook import MonitorWebhook
from psa_car_controller.psa.connected_car_api.models.monitor_webhook_attributes import MonitorWebhookAttributes
from psa_car_controller.psa.connected_car_api.models.monitors import Monitors
from psa_car_controller.psa.connected_car_api.models.monitors_embedded import MonitorsEmbedded
from psa_car_controller.psa.connected_car_api.models.overall_autonomy import OverallAutonomy
from psa_car_controller.psa.connected_car_api.models.point import Point
from psa_car_controller.psa.connected_car_api.models.polygon_zone import PolygonZone
from psa_car_controller.psa.connected_car_api.models.position import Position
from psa_car_controller.psa.connected_car_api.models.position_properties import PositionProperties
from psa_car_controller.psa.connected_car_api.models.preconditioning import Preconditioning
from psa_car_controller.psa.connected_car_api.models.preconditioning_air_conditioning import PreconditioningAirConditioning
from psa_car_controller.psa.connected_car_api.models.preconditioning_program import PreconditioningProgram
from psa_car_controller.psa.connected_car_api.models.privacy import Privacy
from psa_car_controller.psa.connected_car_api.models.program import Program
from psa_car_controller.psa.connected_car_api.models.program_occurence import ProgramOccurence
from psa_car_controller.psa.connected_car_api.models.safety import Safety
from psa_car_controller.psa.connected_car_api.models.service_type import ServiceType
from psa_car_controller.psa.connected_car_api.models.status import Status
from psa_car_controller.psa.connected_car_api.models.status_embedded import StatusEmbedded
from psa_car_controller.psa.connected_car_api.models.status_extension_type import StatusExtensionType
from psa_car_controller.psa.connected_car_api.models.status_links import StatusLinks
from psa_car_controller.psa.connected_car_api.models.tab_links import TabLinks
from psa_car_controller.psa.connected_car_api.models.telemetry import Telemetry
from psa_car_controller.psa.connected_car_api.models.telemetry_embedded import TelemetryEmbedded
from psa_car_controller.psa.connected_car_api.models.telemetry_enum import TelemetryEnum
from psa_car_controller.psa.connected_car_api.models.telemetry_extension import TelemetryExtension
from psa_car_controller.psa.connected_car_api.models.telemetry_extension_type import TelemetryExtensionType
from psa_car_controller.psa.connected_car_api.models.telemetry_message import TelemetryMessage
from psa_car_controller.psa.connected_car_api.models.telemetry_message_embedded import TelemetryMessageEmbedded
from psa_car_controller.psa.connected_car_api.models.telemetry_message_vehicle import TelemetryMessageVehicle
from psa_car_controller.psa.connected_car_api.models.telemetry_message_vehicle_braking_system import TelemetryMessageVehicleBrakingSystem
from psa_car_controller.psa.connected_car_api.models.telemetry_message_vehicle_transmission import TelemetryMessageVehicleTransmission
from psa_car_controller.psa.connected_car_api.models.telemetry_message_vehicle_transmission_gearbox import TelemetryMessageVehicleTransmissionGearbox
from psa_car_controller.psa.connected_car_api.models.telemetry_message_vehicle_transmission_gearbox_gear import TelemetryMessageVehicleTransmissionGearboxGear
from psa_car_controller.psa.connected_car_api.models.telemetry_message_vehicle_transmission_gearbox_mode import TelemetryMessageVehicleTransmissionGearboxMode
from psa_car_controller.psa.connected_car_api.models.time_monitor_trigger import TimeMonitorTrigger
from psa_car_controller.psa.connected_car_api.models.time_range import TimeRange
from psa_car_controller.psa.connected_car_api.models.time_stamped import TimeStamped
from psa_car_controller.psa.connected_car_api.models.time_trigger import TimeTrigger
from psa_car_controller.psa.connected_car_api.models.time_zone_monitor_trigger import TimeZoneMonitorTrigger
from psa_car_controller.psa.connected_car_api.models.time_zone_trigger import TimeZoneTrigger
from psa_car_controller.psa.connected_car_api.models.trip import Trip
from psa_car_controller.psa.connected_car_api.models.trip_avg_consumption import TripAvgConsumption
from psa_car_controller.psa.connected_car_api.models.trip_links import TripLinks
from psa_car_controller.psa.connected_car_api.models.trips import Trips
from psa_car_controller.psa.connected_car_api.models.trips_embedded import TripsEmbedded
from psa_car_controller.psa.connected_car_api.models.updated_field import UpdatedField
from psa_car_controller.psa.connected_car_api.models.url import Url
from psa_car_controller.psa.connected_car_api.models.user import User
from psa_car_controller.psa.connected_car_api.models.user_embedded import UserEmbedded
from psa_car_controller.psa.connected_car_api.models.user_links import UserLinks
from psa_car_controller.psa.connected_car_api.models.vect2_d import Vect2D
from psa_car_controller.psa.connected_car_api.models.vehicle import Vehicle
from psa_car_controller.psa.connected_car_api.models.vehicle_engine import VehicleEngine
from psa_car_controller.psa.connected_car_api.models.vehicle_links import VehicleLinks
from psa_car_controller.psa.connected_car_api.models.vehicle_odometer import VehicleOdometer
from psa_car_controller.psa.connected_car_api.models.vehicles import Vehicles
from psa_car_controller.psa.connected_car_api.models.vehicles_embedded import VehiclesEmbedded
from psa_car_controller.psa.connected_car_api.models.way_points import WayPoints
from psa_car_controller.psa.connected_car_api.models.way_points_embedded import WayPointsEmbedded
from psa_car_controller.psa.connected_car_api.models.x_error import XError
from psa_car_controller.psa.connected_car_api.models.zone_monitor_trigger import ZoneMonitorTrigger
from psa_car_controller.psa.connected_car_api.models.zone_trigger import ZoneTrigger
from psa_car_controller.psa.connected_car_api.models.zone_trigger_place import ZoneTriggerPlace
from psa_car_controller.psa.connected_car_api.models.zone_trigger_place_center import ZoneTriggerPlaceCenter
