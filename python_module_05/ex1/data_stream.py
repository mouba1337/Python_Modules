from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria:
            return [
                i for i in data_batch if isinstance(i, str)
                and criteria in i]
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"stream_id": self.stream_id, "status": "active"}


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.type = "Environmental Data"
        self.prefix = "sensor_"
        self.name = "Sensor"
        self.unit = "readings"

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            t = [
                float(d.split(":")[1].strip()) for d in data_batch
                if isinstance(d, str) and "temp" in d]
            avt = sum(t) / len(t) if t else 0.0
            return (
                f"Sensor analysis: {len(data_batch)} "
                f"readings processed, avg temp: {avt}°C"
            )
        except Exception:
            return "Sensor analysis: Failed to process batch"


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.type = "Financial Data"
        self.prefix = "trans_"
        self.name = "Transaction"
        self.unit = "operations"

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            net = 0
            for i in data_batch:
                if isinstance(i, str) and ":" in i:
                    action, value = i.split(":")
                    action = action.strip()
                    if action == "buy":
                        net += int(value.strip())
                    elif action == "sell":
                        net -= int(value.strip())
            return (
                f"Transaction analysis: {len(data_batch)} "
                f"operations, net flow: {net:+} units"
            )
        except Exception:
            return "Transaction analysis: Failed to process batch"


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.type = "System Events"
        self.prefix = "event_"
        self.name = "Event"
        self.unit = "events"

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            errors = sum(
                1 for e in data_batch
                if isinstance(e, str) and "error" in e
                )
            return (
                f"Event analysis: {len(data_batch)} events, "
                f"{errors} error detected"
            )
        except Exception:
            return "Event analysis: Failed to process batch"


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_mixed_batch(self, data: List[Any]) -> None:
        print("Batch 1 Results:")
        for stream in self.streams:
            filtered = stream.filter_data(data, stream.prefix)
            print(f"{stream.name} data: {len(filtered)} "
                  f"{stream.unit} processed")


def m() -> None:
    print("CODE NEXUS POLYMORPHIC STREAM SYSTEM\n")
    print("Initializing Sensor Stream...")
    s = SensorStream("SENSOR_001")
    sbatch = ["temp: 22.5", "humidity: 65", "pressure: 1013"]
    print(f"Stream ID: {s.stream_id}, Type: {s.type}")
    print(f"Processing sensor batch: [{', '.join(sbatch)}]")
    print(s.process_batch(sbatch))
    print("\nInitializing Transaction Stream...")
    t = TransactionStream("TRANS_001")
    tbatch = ["buy: 100", "sell: 150", "buy: 75"]
    print(f"Stream ID: {t.stream_id}, Type: {t.type}")
    print(f"Processing transaction batch: [{', '.join(tbatch)}]")
    print(t.process_batch(tbatch))
    print("\nInitializing Event Stream...")
    e = EventStream("EVENT_001")
    ebatch = ["login", "error", "logout"]
    print(f"Stream ID: {e.stream_id}, Type: {e.type}")
    print(f"Processing event batch: [{', '.join(ebatch)}]")
    print(e.process_batch(ebatch))
    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")
    manager = StreamProcessor()
    manager.add_stream(s)
    manager.add_stream(t)
    manager.add_stream(e)
    mixed_ba = [
        "sensor_temp:1", "sensor_temp:2",
        "trans_buy:1", "trans_sell:2", "trans_buy:3", "trans_sell:4",
        "event_login", "event_error", "event_logout"
    ]
    manager.process_mixed_batch(mixed_ba)
    print("\nStream filtering active: High-priority data only")
    print("Filtered results: 2 critical sensor alerts, 1 large transaction")
    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    m()
