import subprocess
import sys

port = sys.argv[1] if len(sys.argv) > 1 else "5000"
image_name = "devops-app"
container_name = "devops-container"

with open("deploy.log", "a") as log_file:
    log_file.write("Début du déploiement...\n")

subprocess.run(f"docker stop {container_name} || true", shell=True)
subprocess.run(f"docker rm {container_name} || true", shell=True)

result = subprocess.run(f"docker build -t {image_name} .", shell=True)
if result.returncode != 0:
    with open("deploy.log", "a") as log_file:
        log_file.write("Erreur lors du build, rollback...\n")
    print("Erreur build ! Rollback effectué")
    sys.exit(1)

subprocess.run(f"docker run -d -p {port}:5000 --name {container_name} {image_name}", shell=True)

with open("deploy.log", "a") as log_file:
    log_file.write(f"App déployée sur localhost:{port}\n")

print(f"App déployée sur localhost:{port}")
print("Déploiement terminé")
