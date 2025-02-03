import os
import logging
import json
import re
import sys
import typing
import datetime as dt
from zoneinfo import ZoneInfo

from deye_events import DeyeEvent, DeyeEventProcessor, DeyeObservationEvent, DeyeLoggerStatusEvent
from deye_config import DeyeConfig
from deye_observation import Observation
from deye_plugin_loader import DeyePluginContext


DEYE_JSON_FILEPATH="./data"

def datetime_converter(o: dt.datetime) -> str:
    """Helper function to convert datetime objects to strings. Default precision is seconds"""
    return o.isoformat(timespec='seconds')


class DeyeJsonPublishError(Exception):
    def __init__(self, message: str):
        self.message = message


class DeyeStdoutPublisher(DeyeEventProcessor):
    """
    Publishes events on STDOUT
    """

    __mqtt_topic_suffix_splitter = r"/|_"
    __source_joiner = "/"

    def __init__(self, config: DeyeConfig, dest: typing.IO = sys.stdout):
        self.__log = logging.getLogger(DeyeStdoutPublisher.__name__)
        self.__config = config
        self.__dest = dest

    def initialize(self):
        pass

    def get_id(self):
        return "stdout_publisher"

    def process(self, events: list[DeyeEvent]):
        data = []

        for event in events:
            if isinstance(event, DeyeObservationEvent):
                data.append(DeyeStdoutPublisher.__handle_observation(event.observation))
                # data.append(event.observation.to_dict())  # msa version
            elif isinstance(event, DeyeLoggerStatusEvent):
                pass
            #     data.append({
            #         "name": "logger_status", 
            #         "value": True, # event
            #         "unit": "bool",
            #         "timestamp": dt.datetime.now(),
            #         "category": "data_logger",
            #         "groups": "logger",
            #     })
            else:
                self.__log.warn(f"Unsupported event type {event.__class__}")
                raise DeyeJsonPublishError(f"Unsupported event type encountered: {event.__class__.__name__}")
        
        # data ETL
        # data.insert(0, {"timestamp": dt.datetime.now()})

        # print(
        #     json.dumps(
        #         {
        #             "serial": str(self.__config.logger.serial_number),
        #             "address": self.__config.logger.ip_address,
        #             "port": self.__config.logger.port,
        #             "data": data,
        #         }
        #     ),
        #     flush=True,
        #     file=self.__dest,
        # )
        self.write_to_file(data)
        return data

    @staticmethod
    def __handle_observation(observation: Observation) -> dict[str, str | float | int]:
        data = {
            "name": observation.sensor.name,
            "value": observation.value,
            "unit": observation.sensor.unit,
            "groups": ",".join(observation.sensor.groups),
            "timestamp": observation.timestamp,
            "category": observation.sensor.mqtt_topic_suffix,
            # "sensor": observation.sensor.__class__.__name__,
        }

        return data

    @staticmethod
    def write_to_file(data: list[dict]):
        
        now_local: dt.datetime  = dt.datetime.now(ZoneInfo('Europe/Athens'))
        now_loc_isoform: str = datetime_converter( now_local ).replace(':', '_')
        year, month, day = now_local.year, now_local.month, now_local.day
        
        file_path: str = f"{DEYE_JSON_FILEPATH}/{year}/{month:02}/{day:02}/{now_loc_isoform}.json"
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
        with open(file_path, "w", encoding='utf-8') as file:
            json.dump(data, file, default=datetime_converter, ensure_ascii=False, indent=2)

    @classmethod
    def __mqtt_topic_to_identity(cls, topic_suffix: str) -> tuple[str, str | None]:
        # topic_suffix can be something like 'dc/pv2/total_power'
        # and will be split into "power" and "dc/pv2/total"
        parts = re.split(cls.__mqtt_topic_suffix_splitter, topic_suffix)

        name = parts[-1]
        source = cls.__source_joiner.join(parts[:-1])

        return name, None if source == "" else source


class DeyePlugin:
    def __init__(self, plugin_context: DeyePluginContext):
        self.publisher = DeyeStdoutPublisher(config=plugin_context.config)

    def get_event_processors(self) -> [DeyeEventProcessor]:
        return [self.publisher]
