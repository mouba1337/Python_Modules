from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional # noqa


class DataProcessor(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        try:
            if type(data) is not list:
                return False
            for i in data:
                if type(i) is not int and type(i) is not float:
                    return False
            return True
        except Exception:
            return False

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Invalid numeric data"
        try:
            tot = sum(data)
            avg = tot / len(data) if len(data) > 0 else 0
            return (
                f"Processed {len(data)} numeric values, "
                f"sum={tot}, avg={avg}"
            )
        except Exception:
            return "Invalid numeric data"


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if type(data) is str:
            return True
        return False

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Invalid text data"
        try:
            c = len(data)
            w = len(data.split())
            return f"Processed text: {c} characters, {w} words"
        except Exception:
            return "Invalid text data"


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if type(data) is str and ":" in data:
            return True
        else:
            return False

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Invalid log data"
        try:
            parts = data.split(":", 1)
            level = parts[0].strip()
            msg = parts[1].strip()
            pre = "[ALERT]" if level == "ERROR" else f"[{level}]"
            return f"{pre} {level} level detected: {msg}"
        except Exception:
            return "Invalid log data"


def m() -> None:
    ndata = [1, 2, 3, 4, 5]
    nu = NumericProcessor()
    tdata = "Hello Nexus World"
    te = TextProcessor()
    ldata = "ERROR: Connection timeout"
    lo = LogProcessor()
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    print("Initializing Numeric Processor...")
    print(f"Processing data: {ndata}")
    if nu.validate(ndata):
        print("Validation: Numeric data verified")
    print(nu.format_output(nu.process(ndata)))
    print()
    print("Initializing Text Processor...")
    print(f"Processing data: {tdata}")
    if te.validate(tdata):
        print("Validation: Text data verified")
    print(te.format_output(te.process(tdata)))
    print()
    print("Initializing Log Processor...")
    print(f"Processing data: {ldata}")
    if lo.validate(ldata):
        print("Validation: Log entry verified")
    print(lo.format_output(lo.process(ldata)))
    print()
    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    streams = [
        (nu, [1, 2, 3]), (te, "1 2 3 soleil"), (lo, "INFO: System ready")]
    for i, (c, da) in enumerate(streams, 1):
        print(f"Result {i}: {c.process(da)}")
    print()
    print("Foundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    m()
