import subprocess, sys

version = sys.argv[1] if len(sys.argv) > 1 else "latest"
port = 5000
container_name = "devops-container"
image_name = f"devops-app:{version}"

try:
    subprocess.run(f"docker stop {container_name} || true", shell=True)
    subprocess.run(f"docker rm {container_name} || true", shell=True)
    subprocess.run(f"docker run -d -p {port}:5000 --name {container_name} {image_name}", shell=True)
    print(f"App déployée sur localhost:{port} (version {version})")
except Exception as e:
    print(f"Erreur déploiement: {e}")
