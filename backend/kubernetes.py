import subprocess


def run_kubectl_command(command):
    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )
    return result.stdout


def get_pods():
    return run_kubectl_command(["kubectl", "get", "pods"])


def get_failed_pod():
    output = run_kubectl_command(["kubectl", "get", "pods"])

    lines = output.splitlines()

    for line in lines[1:]:
        if "ImagePullBackOff" in line or "CrashLoopBackOff" in line or "ErrImagePull" in line:
            return line.split()[0]

    return None


def describe_pod(pod_name):
    return run_kubectl_command(
        ["kubectl", "describe", "pod", pod_name]
    )
