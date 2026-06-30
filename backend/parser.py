import re


def parse_describe_output(output: str):

    data = {
        "pod_status": None,
        "container_image": None,
        "reason": None,
        "events": []
    }

    lines = output.splitlines()

    for line in lines:

        line = line.strip()

        if line.startswith("Status:"):
            data["pod_status"] = line.replace("Status:", "").strip()

        elif line.startswith("Image:"):
            data["container_image"] = line.replace("Image:", "").strip()

        elif line.startswith("Reason:"):
            data["reason"] = line.replace("Reason:", "").strip()

    if "Events:" in output:

        events = output.split("Events:")[1]

        data["events"] = [
            event.strip()
            for event in events.splitlines()
            if event.strip()
        ]

    return data
