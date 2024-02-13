# Test_Divar_Web_Select_Vehicle

This repository demonstrates a process for selecting a special vehicle from the Divar Website by applying Selenium in **python3.10**.
this Code consists of multiple actions alluded to below:
1) select vehicle category
2) select a special vehicle such as a car
3) select the intended use of the vehicle
4) apply three filters for instance color, Maximum price, and minimum kilometrage
5) apply the cheapest filter after all of them
6) ultimately, choose a random advertising car shown
7) selenium will take screenshots from the result of this process for the correctness of executing code. This image is available as result.png.

## requirement
    webdriver-manager
    selenium 
    pytest
    
## Steps to run the tests by using the terminal 
1) install in env of python
- `python3 -m venv .venv`
- `source .venv/bin/activate`
2) Install the requirements
- `cd /snap_food_project`
- `pip install -r requirements.txt`
3) Run the tests
- `python -m pytest test_Divar_Web_search_Vehicle.py`
4) View the test results as an image in /snap_food_project
- `result.png`
-    ![Image Alt Text](result.png)

## Steps to run the tests in Docker

**Prerequisites**:

- Docker

**Steps**:

1) Build the Docker image
- `docker build -t "test" -f Dockerfile .`
2) Create a container instance of that image (which will run the entrypoint)
- `docker run test`

## Convenience scripts (for Docker approach)

1) Build the Docker image
- `./build.sh`
2) Run the Docker image and extract the test results
- `./run.sh`
