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
4. Then install all dependencies using (It might take some time. Some of the versions may be different on your device so just install the appropriate version):
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
## Target Audience

- Companies
- NGOs
- Businesses
- Government departments

## Summary of Key Elements

1. **Organizing and managing events:**
   - Add, update, and remove events with specifics like the date, time, and place.
   - Organize the use of resources, such as equipment and locations.

2. **Participants**
   - Online registration is available for participants in events.
   - Automated email or SMS ticketing and reminder system.

3. **Feedback Gathering:**
   - Inbuilt feedback forms and post-event surveys on the platform.

4. **Analytics and Reporting:**
   - To help with future event planning, create reports on participant satisfaction, attendance, and other indicators.

## Networking Features

- **RESTful API:** To manage requests for generating, obtaining, editing, and removing event data from the client and server.
- **Safe User Authentication:** Use HTTPS to provide safe application access.
- **Form Data:** Form data is sent from the client to the server via HTTP POST requests, where it is processed and saved in the database.
- **Data Retrieval:** To retrieve raw data from the server for report creation, use HTTP GET requests.

## Database

- **Details of the event:** Keep track of all event-related information, such as times, locations, and relevant resources.
- **User Data:** Organize user profiles and registration details.
- **Feedback and Analytics:** Keep collecting feedback after the event and provide analytics to reveal areas that worked well and those that may use better.

## External Libraries

- **Flask:** Because of its ease of use and versatility, Flask is a micro web framework for Python that is used to develop API servers.
- **SQLAlchemy:** ORM library for effectively managing all PostgreSQL database interactions.
- **SQLite:** Will be used in this project to store participant and event data.
