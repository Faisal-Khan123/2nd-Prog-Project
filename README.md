# Community Event Planer
An application that is focused on APIs, the Community Event Planner helps with the planning and administration of community events. This platform offers tools for organising, managing participation, and advertising a range of events, including workshops, cultural festivals, sporting events, and educational seminars. It provides adaptable APIs that may be incorporated into various platforms to satisfy certain requirements. With the help of this platform, community organisers may plan and carry out events with ease while actively involving the community. It also facilitates simplified participant registration, and thorough feedback collecting.
## Installation

1. After cloning, move to the `2nd-Prog-Project` folder on `cmd` and create the virtual environment.
   ```sh
   python -m venv venv
   ```   
3. In `2nd-Prog-Project/`, activate the virtual environment using:
    ```sh
    scripts\activate
    ```
4. Then install all dependencies using (It might take some time):
    ```sh
    pip install -r requirements.txt
    ```
5. Move to the `eventplanner` folder:
    ```sh
    cd eventplanner
    ```
6. In `eventplanner/app/instance/`:
    - Right click the `eventplanner.sqlite3` file and copy the path.
      
7. Replace it with the path in `app/init.py` where the path of my database is mentioned. Replace it after `sqlite:///` and invert the slashes like convert `\` to `/` in the path.
   
8. Move back to `cmd` and inside `eventplanner/` run the following:
    ```sh
    python run.py
    ```
9. Open your web browser and navigate to:
    ```
    http://127.0.0.1:5000/
    ```
