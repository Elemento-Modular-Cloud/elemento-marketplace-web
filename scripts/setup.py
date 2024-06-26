import subprocess, sys, re, string, os


######## UTILS FUNCTIONS ########


def flags_setup(args):
    flags = {"deploy": False, "stack": "production", "path": False, "network": False}
    for i in range(len(args)):
        if args[i] in ["-d", "--deploy"]:
            flags["deploy"] = True
            try:
                if not args[i + 1].startswith("-"):
                    flags["stack"] = args[i + 1]
            except IndexError:
                print("WARNING: No stack name provided. Using default.")
            continue
        if args[i] in ["-p", "--path"]:
            try:
                if not args[i + 1].startswith("-"):
                    flags["path"] = args[i + 1]
                    if not os.path.isdir(flags["path"]):
                        print("ERROR: Path not found.")
                        exit(1)
            except IndexError:
                print("ERROR: No path provided.")
                exit(1)
            continue
        if args[i] in ["-n", "--network"]:
            flags["network"] = True
            continue
        if args[i] in ["-h", "--help"]:
            print("python3 setup.py <customer> <traefik_password>")
            print("For more info check the README.md file.")
            exit(0)
    return flags


def check_command(command, result):
    if result.returncode != 0:
        print(f"\nError executing command: {command}")
        print(f"Error message: {result.stderr.strip()}")
        exit(1)
    return 0


def check_position():
    command = "ls | grep docker-compose.yml"
    content = subprocess.run(command, shell=True, capture_output=True, text=True)
    if content.returncode != 0:
        os.chdir("..")
        content = subprocess.run(command, shell=True, capture_output=True, text=True)
        if content.returncode != 0:
            print("ERROR: docker-compose.yml not found.")
            print("Please run this script from the root directory of the project.")
            exit(1)
    return 0


######## SETUP FUNCTIONS ########


def traefik_ba_setup(customer, traefik_password):
    command = f"htpasswd -nb {customer} {traefik_password}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    check_command(command, result)
    result = result.stdout.strip().replace("$", "$$")
    print("Password generated successfully.")
    return result


def compose_setup(customer, result):
    url_regex = r"(\w+)\.(web)\.(elemento)\.(cloud)"
    traefik_regex = r"(traefik.http.middlewares.mid-auth.basicauth.users=)[^ ]+"
    url_replace = r"\1." + customer + r".\3.\4"
    traefik_replace = r"\1" + result + '"\n'

    with open("docker-compose.yml", "r") as f:
        compose = f.readlines()
    with open("docker-compose-custom.yml", "w") as f:
        for line in compose:
            modified_line = re.sub(url_regex, url_replace, line)
            modified_line = re.sub(traefik_regex, traefik_replace, modified_line)
            f.write(modified_line)
    print("Compose file updated successfully.")


def env_setup():
    result = subprocess.run(
        "ls -a | grep .env", shell=True, capture_output=True, text=True
    )
    files = list(result.stdout.strip().split("\n"))
    if result.returncode != 0 or ".env" not in files:
        print("WARNING: .env file not found, using default values.")
        result = subprocess.run(
            "cp .env.template .env", shell=True, capture_output=True, text=True
        )
        check_command("mv .env.template .env", result)


def permission_setup():
    command = (
        "sudo chmod 600 traefik/acme.json; sudo chmod 600 homepage/config/services.yaml; sudo chmod -R 755 php"
    )
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    check_command(command, result)
    print("Permissions updated successfully.")


def network_setup():
    command = "sudo docker network create --driver overlay net"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    check_command(command, result)
    print("Network created successfully.")


#################################


def setup():
    if len(sys.argv) < 3:
        print("ERROR: python3 setup.py <customer> <traefik_password>")
        return 1

    customer = (sys.argv[1]).strip().lower()
    traefik_password = (sys.argv[2]).strip()
    flags = sys.argv[3:]

    if any(char in string.punctuation for char in customer):
        print("ERROR: Punctuation is not allowed for the customer's name.")
        return 1

    flags = flags_setup(flags)
    if type(flags["path"]) is str:
        os.chdir(flags["path"])
    else:
        check_position()

    # Setup
    result = traefik_ba_setup(customer, traefik_password)
    compose_setup(customer, result)
    env_setup()
    permission_setup()
    if flags["network"]:
        network_setup()

    # Deploy?
    if flags["deploy"]:
        stack_name = (flags["stack"]).strip().lower()
        command = (
            "sudo docker stack deploy --compose-file docker-compose-custom.yml "
            + stack_name
        )
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        check_command(command, result)
        print(result.stdout.strip())


if __name__ == "__main__":
    setup()
