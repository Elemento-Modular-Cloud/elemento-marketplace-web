from flask import Flask, jsonify
import requests, yaml, re, os
from constants import icons, titles

homepage_path = os.getenv("HOMEPAGE_PATH")
traefik_path = os.getenv("TRAEFIK_ROUTE")
user = os.getenv("USER")
password = os.getenv("PASSWORD")
pattern = r"Host\([^)]*\)"
app = Flask(__name__)

if homepage_path is not None or not traefik_path is not None:
    app.logger.info("HOMEPAGE_PATH and TRAEFIK_ROUTE must be set!")

def is_custom_service(rule):
    return re.search(pattern, rule) is not None


##* APIs *##
@app.route("/api/v1/status", methods=["GET"])
def check_server():
    return jsonify({"message": "Traefik discovery is running"})

@app.route("/api/v1/homepage/update", methods=["POST"])
def homepage_update():
    try:

        # Open the YAML file for reading
        with open(str(homepage_path), "r") as yaml_file:
            data = yaml.safe_load(yaml_file)

        if user is not None and password is not None:
            response = requests.get(str(traefik_path), auth=(user, password))
        else:
            app.logger.info(f"No authentication provided, using unauthenticated request.")
            response = requests.get(str(traefik_path))

        routers = response.json()
        if data[0]["Services"] == None:
            data[0]["Services"] = []

        keys = [list(service.keys())[0] for service in data[0]["Services"]]
        for router in routers:
            name = router["name"].split("@")[0]
            if (
                is_custom_service(router["rule"])
                and name.capitalize() not in keys
                and name != "homepage" and name != "dashboard"
            ):
                icon = icons[name] if name in icons else ""
                title = titles[name] if name in titles else name
                data[0]["Services"].append(
                    {
                        title.capitalize(): {
                            "icon": icon,
                            "href": "https://" + router["rule"].split("`")[1],
                        }
                    }
                )

        with open(str(homepage_path), "w") as yaml_file:
            yaml.dump(data, yaml_file)

        return jsonify(data[0]["Services"])

    except requests.exceptions.RequestException as e:
        app.logger.info(f"Failed to update services, status code: 500 \n error: {e}")
        return jsonify({"error": f"Update services failed: {e}"}), 500


@app.route("/api/v1/homepage/refresh", methods=["POST"])
def homepage_refresh():
    try:

        # Open the YAML file for reading
        with open(str(homepage_path), "r") as yaml_file:
            data = yaml.safe_load(yaml_file)

        if user is not None and password is not None:
            response = requests.get(str(traefik_path), auth=(user, password))
        else:
            app.logger.info(f"No authentication provided, using unauthenticated request.")
            response = requests.get(str(traefik_path))

        routers = response.json()
        data[0]["Services"] = []

        for router in routers:
            name = router["name"].split("@")[0]
            if (
                is_custom_service(router["rule"])
                and name != "homepage" and name != "dashboard"
            ):
                icon = icons[name] if name in icons else ""
                title = titles[name] if name in titles else name
                data[0]["Services"].append(
                    {
                        title.capitalize(): {
                            "icon": icon,
                            "href": "https://" + router["rule"].split("`")[1],
                        }
                    }
                )

        with open(str(homepage_path), "w") as yaml_file:
            yaml.dump(data, yaml_file)

        return jsonify(data[0]["Services"])

    except requests.exceptions.RequestException as e:
        app.logger.info(f"Failed to update services, status code: 500 \n error: {e}")
        return jsonify({"error": f"Update services failed: {e}"}), 500


##* APP (just for testing purpose - use flask run instead) *##
#if __name__ == "__main__":
#     # app.run(port=5001, debug=True)
      #homepage_refresh()
