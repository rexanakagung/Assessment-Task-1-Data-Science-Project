# Data Science Application (Weather App) 
What is your project about?  
My project is a weather application that displays real time weather data with the ability to save sessions and display reults with visualisations.
 
## Sucess Criteria 
My program should be able to retreive real time weather data from my specific API and display the results with accurate visualisations. It should have a working menu system having saved sessions and the ability to change unit of measurements (e.g celcius). The application should also have the ability to let users exit the app safely and return to a previous menu without the program crashing.
## Functional Requirements 
(What the system should do)

Consider the following elements when developing your functional requirements: 

 #### Data Retrieval: What does the user need to be able to view in the system?  
 The user must be able to view specific information from an external API. At minimum the user must see :
* Data they requested (API data)
* Error Messages
* Help Information
* Past User Interactions
* Visualisations

 #### User Interface: What is required for the user to interact with the system?  
 The system must provide a simple and user‑friendly interface that allows the user to interact with the application effectively. To achieve this, the user interface must include:
* Menu System
* Input Prompts
* Help Instructions
* Error Messages
* Display Of Retrieved Data
* Display Of Past Interactions
* Safe Exit

#### Data Display: What information does the user need to obtain from the system?  
The system must display clear, readable information that helps the user understand the data they requested. At minimum, the user must be able to view:  
* The Main Data Retrieved From the API
* Additional Processed or Cleaned Data
* Visualisations
* User Interaction History
* Error and Status Messages

## Non-Functional Requirements 
(How the system should work)

Consider the following elements when developing your non-functional requirements:

#### Performance: How well does the system need to perform?  
The system must perform efficiently so that users can retrieve and view data without delays or errors. To meet this requirement, the system must:  
* Respond Quickly to User Input
* Handle API Requests Efficiently
* Process and Clean Data Smoothly
* Display Results Without Delay
* Maintain Stability During Use
* Recover Gracefully From Errors

#### Reliability: How reliable does the system and data need to be?  
The system must operate consistently and provide accurate, dependable results whenever the user interacts with it. To meet this requirement, the system must:  
* Provide Accurate Data
* Handle Errors Without Crashing
* Maintain Consistent Behaviour
* Ensure Stable API Communication
* Prevent Data Loss
* Maintain Uptime During Use

#### Usability and Accessibility: How easy to navigate does the system need to be? What instructions will we need for users to access the system?  
The system must be simple to navigate and accessible for users with different levels of technical experience. To achieve this, the system must include:  
* Clear and Simple Navigation
* Straightforward Input Instructions
* Help and Guidance
* Accessible Error Messages
* Readable Output
* Support for All Users  
# Build Plan 
#### Project Overview: A Weather app
***  
### Phase 1: Project Foundation & Setup 
#### 1.1 Environment Setup 

Create project structure with subdirectories:
* data/ - cached API responses and saved datasets
* sessions/ - saved session data
* charts/ - exported chart images
* src/ - main application code 

Create requirements.txt with dependencies:  
* pandas
* requests (for API calls)
* matplotlib (for charting)
* numpy (for data manipulation)
* json (built-in, for data handling)
* Create .gitignore for sensitive data/cache files 


 #### 1.2 API Selection & Testing 
 
 Research and select a free, beginner-friendly API: 

* Requirements: No authentication needed (or simple key), returns JSON, has good documentation
* Test API connectivity and response structure
* Document API endpoints and response format
* Create sample API response files for offline testing 
 
 ### Phase 2: Core Application Architecture  
 #### 1. Main Application Structure 
 Create main.py - entry point with menu system
Design application flow:
* Main menu with options (Load Session (nice to have), New Session, Exit)
* Session management system (nice to have) 
* Implement a basic module selector 

#### 2. API Handler Module (api_handler.py)
* Create function to fetch data from selected API
* Implement error handling for network issues 
* Add data cahing to avoid repeated API calls
* Create function to display raw API response
* Add timestamp tracking for data freshness 
  
#### 3. Date Cleaning Module (data_cleaner.py) 
* Create functions to:
    * Remove/ handing missing values
    * Remove duplicates
    * Convert data types
    * Rename columns
    * Standardize formatting 
#### 4. Data Filtering Module (date_filter.py) 
* Create functions to: 
    * filter by colums value
    * Filter by range numeric
    * Filter by string pattern

#### 5. Data Sorting Module (data_sort.py) 
* Create functions to:   
    * Sort by single column 
    * Sort by multiple columns 
    * sort ascending/descending
    * display results with statistics
     
#### 6. Visuallisations Module (visualisations.py)
* Create functions to:
    * Line charts      
       
#### 7. File I/O Module (file_manager.py)
* Implement TXT export function

# Design  
Flowchart 
https://excalidraw.com/#json=HluweEP8VPTabogF5HYXH,aPXsb7fV9mXIa9o2LfRQgg 

Psuedocode
https://docs.google.com/document/d/1JWWwq7zsxl9fl2WqXb3yi2zimXJ4-T75tFUSd1xUPIk/edit?usp=sharing

Structure chart 
https://excalidraw.com/#json=KlaS-WNRmtD-OxN4DCY61,gczbtztE4MsUn3HTL8VvrQ 

Gantt Chart 
https://docs.google.com/spreadsheets/d/1RGyaAHpXh_0wwzc8tRun7XxMQPgwb2P5gP19mIzfU8U/edit?usp=sharing 
 
Data Dictionary 
https://docs.google.com/document/d/1kKtTU3hnNmV422KWnC1RTu0Oi9Lx-eTbZperTbgYx7I/edit?usp=sharing  

# Development Evidence
# Final Criteria
After I have finished developing the weather application, it sucessfully works without any bugs or errors. It succesfully retrieves API data and parsing it into readable data formatted in an organized matter. The API data shows temperature. humidity, precipitaion, etc. Visualisations also work without any errors, the charts are accurate to the API data. Users can exit safely withou the software crashing and also handles input errors. The software allows to. store saved cities it JSON and also has a function to erase saved cities. What I didnt get to add was more variety of visualisations and a pop up app which would have improved my application by alot. Things that I could improve on is being more efficient with my coding and not reapeating code over and over again. Another thing that i could of have improved on is also removing unused variables that are not being displayed as this just makes the code look unoorganized, I could also improve my flowcharts and sturcture charts to have more detail and be more specific. Overall the development of the Weather Application has been a huge sucess.

# Maintanence
Future Improvements

* Add a reusable function for forecast display to remove duplicate logic.
* Let users delete one saved city instead of clearing all.
* Add unit selection (C/F, kph/mph) and remember preferences. 

Potential Bugs

* API/network failures can return missing fields and cause key errors.
* Date/day matching can be wrong around timezone/day changes.

Maintenance Over Time

* Keep dependencies pinned and update monthly.
* Add small tests for menu input and saved city load/save flows.
* Log API and file read/write errors for easier debugging.