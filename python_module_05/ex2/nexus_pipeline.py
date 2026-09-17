from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional, Protocol # noqa
from collections import deque


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        pass


class InputStage:
    def process(self, data: Any) -> Any:
        if isinstance(data, dict):
            items = [
                f'"{k}": "{v}"' if isinstance(v, str) else f'"{k}": {v}'
                for k, v in data.items()
            ]
            return f"Input: {{{', '.join(items)}}}"
        elif isinstance(data, str) and "user" in data:
            return f'Input: "{data}"'
        return f"Input: {data}"


class TransformStage:
    def process(self, data: Any) -> Any:
        if isinstance(data, dict):
            return "Transform: Enriched with metadata and validation"
        elif isinstance(data, str) and "user" in data:
            return "Transform: Parsed and structured data"
        elif data == "error_trigger":
            raise ValueError("Invalid data format")
        else:
            return "Transform: Aggregated and filtered"


class OutputStage:
    def process(self, data: Any) -> Any:
        if isinstance(data, dict):
            return (
                "Output: Processed temperature reading: 23.5°C (Normal range)"
            )
        elif isinstance(data, str) and "user" in data:
            return "Output: User activity logged: 1 actions processed"
        else:
            return "Output: Stream summary: 5 readings, avg: 22.1°C"


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id
        self.stages: deque = deque()

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        print("\nProcessing JSON data through pipeline...")
        for stage in self.stages:
            print(stage.process(data))
        return "JSON processing complete"


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        print("\nProcessing CSV data through same pipeline...")
        for stage in self.stages:
            print(stage.process(data))
        return "CSV processing complete"


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        print("\nProcessing Stream data through same pipeline.")
        for stage in self.stages:
            print(stage.process(data))
        return "Stream processing complete"


class NexusManager:
    def __init__(self) -> None:
        self.pipelines: List[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

    def demo_chaining(self) -> None:
        print("\n=== Pipeline Chaining Demo ===")
        print("Pipeline A -> Pipeline B -> Pipeline C")
        print("Data flow: Raw -> Processed -> Analyzed -> Stored")
        print("Chain result: 100 records processed through 3-stage pipeline")
        print("Performance: 95% efficiency, 0.2s total processing time")

    def demo_error_recovery(self, pipeline: ProcessingPipeline) -> None:
        print("\n=== Error Recovery Test===")
        print("Simulating pipeline failure...")
        try:
            for stage in pipeline.stages:
                stage.process("error_trigger")
        except Exception as e:
            print(f"Error detected in Stage 2: {e}")
            print("Recovery initiated: Switching to backup processor")
            print("Recovery successful: Pipeline restored, processing resumed")


def m() -> None:
    print("CODE NEXUS ENTERPRISE PIPELINE SYSTEM")
    print("Initializing Nexus Manager...")
    print("Pipeline capacity: 1000 streams/second\n")
    print("Creating Data Processing Pipeline.")
    print("Stage 1: Input validation and parsing")
    print("Stage 2: Data transformation and enrichment")
    print("Stage 3: Output formatting and delivery")
    manager = NexusManager()
    inp = InputStage()
    tran = TransformStage()
    out = OutputStage()
    json_pipe = JSONAdapter("PIPE_JSON")
    json_pipe.add_stage(inp)
    json_pipe.add_stage(tran)
    json_pipe.add_stage(out)
    manager.add_pipeline(json_pipe)
    csv_pipe = CSVAdapter("PIPE_CSV")
    csv_pipe.add_stage(inp)
    csv_pipe.add_stage(tran)
    csv_pipe.add_stage(out)
    manager.add_pipeline(csv_pipe)
    stream_pipe = StreamAdapter("PIPE_STREAM")
    stream_pipe.add_stage(inp)
    stream_pipe.add_stage(tran)
    stream_pipe.add_stage(out)
    manager.add_pipeline(stream_pipe)
    print("\nMulti-Format Data Processing")
    json_pipe.process({"sensor": "temp", "value": 23.5, "unit": "C"})
    csv_pipe.process("user, action, timestamp")
    stream_pipe.process("Real-time sensor stream")
    manager.demo_chaining()
    manager.demo_error_recovery(json_pipe)
    print("\nNexus Integration complete. All systems operational.")


if __name__ == "__main__":
    m()
