# Bachelor

Repository containing the report, application and resources concerning my bachelor project

## Installation

1. Make sure a Gurobi license file is present in the root folder.
2. Download the assignment program from https://github.com/belzebuu/ProjectAssignment
	* Place it in ./resources, or change the path on line 7 in the Dockerfile.
3. Make sure all the variables in the _.env_ file has been set.
	* Use _env.template_ as a guide.
4. Run `docker compose build web`
	* Or `docker compose build` to include NGINX and Jenkins
5. Run `docker compose up --no-deps -d web`
	* Or `docker compose up -d` to include NGINX and Jenkins
6. When the Docker container(s) have started, Adsigno will be available at http://127.0.0.1:8000