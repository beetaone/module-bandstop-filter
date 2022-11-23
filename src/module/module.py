"""
This file implements module's main logic.
Data processing should happen here.

Edit this file to implement your module.
"""

from os import getenv
from logging import getLogger

log = getLogger("module")


def module_main(received_data: any) -> [any, str]:
    """
    Process received data by implementing module's main logic.
    Function description should not be modified.

    Args:
        received_data (any): Data received by module and validated.

    Returns:
        any: Processed data that are ready to be sent to the next module or None if error occurs.
        str: Error message if error occurred, otherwise None.

    """

    log.debug("Processing ...")

    try:
        freq_ranges_str = [freq_range.strip() for freq_range in getenv("FREQUENCY_RANGES").split(";")]

        freq_ranges = []
        for freq_range_str in freq_ranges_str:
            freq_range = [float(freq.strip()) for freq in freq_range_str.split("-")]
            freq_ranges.append(freq_range)

        processed_data = []
        for entry in received_data:
            in_range = False
            for freq_range in freq_ranges:
                if entry["frequency"] > freq_range[0] and entry["frequency"] < freq_range[1]:
                    in_range = True
                    break

            if not in_range:
                processed_data.append(entry)

        return processed_data, None

    except Exception as e:
        return None, f"Exception in the module business logic: {e}"
