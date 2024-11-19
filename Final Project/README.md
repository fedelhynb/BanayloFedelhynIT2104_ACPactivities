# <p align="center"> SWIFTRENT: VEHICLE RENTAL SERVICES
<p align="center" > <img width="800" height="550" src="https://github.com/fedelhynb/BanayloFedelhynIT2104_ACPactivities/blob/main/Final%20Project/Green%20Floral%20Coming%20Soon%20Poster.png?raw=true" > </p>

<br/><br/>
## Table of Contents
- __I. Project Overview__
- __II. Python Concepts Application in the Program.__
- __III. The chosen SDG and its integration into the project.__
- __IV. Installation__
<br/><br/>

### I. Project Overview
<p align="justify"> SwiftRent is a vehicle rental management system implemented using the Python language as a basis for the implementation of Object-Oriented Product (OOP) for the construction of a rational, expandable, and sustainable computer enterprise. The system enables customers to only to hire vehicles, monitor bookings and transactions with charges while the back-end enables administrators to monitor the vehicles, and particularly manage the transactions from the clients. A customer can view available cars select the car they want and book it, update it and even cancel it with the system automatically calculating the rental duration and charges. Admins have the ability to add, update, or remove vehicles from the system and monitor vehicle availability. It also incorporates with a database like MySQL or SQLite to keep track of users’ information, vehicles’ information, rentals and payment as well as history to provide persistence. SwiftRent effectively handles all aspects of vehicle rental management, offering a seamless experience for both customers and administrators while maintaining a robust and secure backend.

### &nbsp; &nbsp; &nbsp; &nbsp;• Key Features
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; - __Database Management__: Stores vehicle and reservation data using SQLite.

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; - __Vehicle Management__: Tracks vehicles, availability, and rental rates

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; - __Reservation System__: Allows users to make, update, or cancel reservations.

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; - __Fee Calculation__: Computes rental fees based on duration, vehicle type, and additional charges.

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; - __Availability Tracking__: Updates vehicle availability upon reservation or cancellation.

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; - __Receipts__: Generates detailed receipts for reservations, cancellations, and updates.

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; - __User Dashboard__: Provides a simple menu for viewing vehicles, making reservations, and managing bookings.







### &nbsp; &nbsp; &nbsp; &nbsp;• How does the program works?
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; - __Setup:__
  <p align="justify"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; •	Deletes existing database (vehicle_rental.db), creates a new one.
   
  <p align="justify"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; •	Creates vehicles and reservations tables in the database.
  <p align="justify"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; •	Inserts predefined vehicles into the vehicles table.
  
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; - __User Options:__
  <p align="justify"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; • Dashboard Menu: User can choose from 7 options: 
  <p align="justify"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 1. Company Info: Displays information about the rental service.
  <p align="justify"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 2. Make a Reservation: User inputs client details, selects a vehicle, and calculates rental fee based on duration. 
  <p align="justify"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Reservation is saved and vehicle marked as unavailable.
  <p align="justify"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 3. Cancel Reservation: User can cancel a reservation, restoring vehicle availability.
  <p align="justify"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 4. Update Reservation: User can change pickup/return dates or vehicle, and pay for any additional fees.
  <p align="justify"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 5. View Available Vehicles: Displays all available vehicles.
  <p align="justify"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 6. View All Reservations: Displays all current reservations.
  <p align="justify"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 7. Exit: Exits the program.
  
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; - __Error Handling:__
  <p align="justify"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; • Handles database errors with error messages.

<br/><br/>

### II. Python Concepts Application in the Program.

<img src="https://github.com/fedelhynb/BanayloFedelhynIT2104_ACPactivities/blob/main/Final%20Project/pictures/5.png?raw=true" width="700" height="500">

<img src="https://github.com/fedelhynb/BanayloFedelhynIT2104_ACPactivities/blob/main/Final%20Project/pictures/2.png?raw=true" width="700" height="500">

<img src="https://github.com/fedelhynb/BanayloFedelhynIT2104_ACPactivities/blob/main/Final%20Project/pictures/4.png?raw=true" width="700" height="500">
<br/><br/>

<img src="https://github.com/fedelhynb/BanayloFedelhynIT2104_ACPactivities/blob/main/Final%20Project/pictures/3.png?raw=true" width="700" height="500">

<img src="https://github.com/fedelhynb/BanayloFedelhynIT2104_ACPactivities/blob/main/Final%20Project/pictures/6.png?raw=true" width="700" height="500">
<br/><br/>




### III. The chosen SDG and its integration into the project.
============================================================================================
__<p align="center"> SDG 11 : Sustainable cities and communities__

 <p align="center"> &nbsp; &nbsp; &nbsp; &nbsp;  SDG 11 aims to make cities and human settlements inclusive, safe, resilient, and sustainable. It focuses on improving urban spaces, reducing the environmental impact of cities, ensuring access to affordable and sustainable transportation, and promoting green infrastructure.
 &nbsp; &nbsp; &nbsp; &nbsp; <p align="justify"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  The vehicle rental system contributes to SDG 11 by promoting sustainable transportation options. It reduces the number of private vehicles on the road, lowers traffic congestion, and helps decrease carbon emissions by encouraging shared, efficient mobility solutions. By offering easy access to eco-friendly vehicles, the system supports the creation of more sustainable, resilient, and efficient urban transportation networks, aligning with the goal of building cities that are inclusive and environmentally responsible.
   
============================================================================================
<br/><br/>

### IV. Installation
&nbsp; __Instructions for running the program__
<br/><br/>
- __Step 1: Install Python and Required Libraries__
 &nbsp; &nbsp; &nbsp; &nbsp; <p align="justify">  Ensure you have Python 3 installed on your computer. If not, download and install it from     python.org. 
    &nbsp; Additionally, this script uses SQLite3, which comes pre-installed with Python, so no additional installation is required.
- __Step 2: Save the Script__
  <p align="justify"> &nbsp; 1.	Open a text editor (e.g., VS Code, Sublime Text, or even Notepad).
  <p align="justify"> &nbsp; 2.	Copy the entire Python code you provided.
  <p align="justify"> &nbsp; 3.	Paste the code into the editor.
  <p align="justify"> &nbsp; 4.	Save the file as vehicle_rental.py.
- __Step 3: Prepare Your Working Directory__
  <p align="justify"> Ensure you are working in a directory where you have permission to create and delete files (because the script will create a SQLite database file).
- __Step 4: Run the Script__
  <p align="justify"> &nbsp; 1.	Open your command prompt/terminal.
  <p align="justify"> &nbsp; 2.	Navigate to the folder where vehicle_rental.py is saved. You can use the cd command to change directories. Example:
&nbsp; &nbsp; &nbsp; <img src="https://github.com/fedelhynb/BanayloFedelhynIT2104_ACPactivities/blob/main/Final%20Project/pictures/Screenshot%202024-11-13%20192915.png?raw=true" width="600" height="100"> 

  <p align="justify"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 3.	Run the script by typing the following command:
   
&nbsp; &nbsp; &nbsp; <img src="https://github.com/fedelhynb/BanayloFedelhynIT2104_ACPactivities/blob/main/Final%20Project/pictures/Screenshot%202024-11-13%20192934.png?raw=true" width="600" height="100">  
- __Step 5: Interaction with the System__
   &nbsp; &nbsp; &nbsp; &nbsp; <p align="justify">  Once the script starts running, it will display the dashboard with a list of options:
&nbsp; &nbsp; &nbsp; <img src="https://github.com/fedelhynb/BanayloFedelhynIT2104_ACPactivities/blob/main/Final%20Project/pictures/Screenshot%202024-11-13%20193057.png?raw=true" width="650" height="300">
   &nbsp; &nbsp; &nbsp; &nbsp; <p align="justify">  You will be prompted to enter a choice. Here's what each option will do:
   __<p align="justify"> &nbsp; 1. See Company Information__
   <p align="justify"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; •	This option will display company details and contact information.
    
   __<p align="justify"> &nbsp; 2. Make your Rent__
   <p align="justify"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; -	This option allows you to make a reservation for a vehicle.
   <p align="justify"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; -	The system will ask you to provide personal details such as your name, contact number, and email.
   <p align="justify"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; -	You will then be asked to enter the pickup and return date/time.
   <p align="justify"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; -	The system will show available vehicles and calculate the rental fee.
   <p align="justify"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; -	You can confirm your reservation, after which the system will save it in the database and show a rental receipt.

   __<p align="justify"> &nbsp; 3. Cancel your Rent__
   <p align="justify"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; -	This option allows you to cancel an existing reservation.
   <p align="justify"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; -	You will need to enter the client name associated with the reservation.
   <p align="justify"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; -	The system will ask for confirmation, then cancel the reservation and update vehicle availability.

    __<p align="justify"> &nbsp; 4. Update your Rent__
   <p align="justify"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; -	This option allows you to modify an existing reservation.
   <p align="justify"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; -	You can update the pickup and return time or change the vehicle.
   <p align="justify"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; -	The system will show available vehicles and compute any additional fees based on changes.

    __<p align="justify"> &nbsp; 5. View Available Vehicles__
   <p align="justify"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; •	This option displays a list of all available vehicles, their type, model, plate number, daily rate, and availability status.

    __<p align="justify"> &nbsp; 6. See all Reservations__
   <p align="justify"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; •	This option shows a list of all reservations made, with client details, vehicle information, and rental fee.

    __<p align="justify"> &nbsp; 7. Exit__
   <p align="justify"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; •	This option will exit the program and close the database connection.

- __Step 6: Interaction Details__
   &nbsp; &nbsp; &nbsp; &nbsp; <p align="justify"> 1.	When prompted to enter information (like the client's name, contact number, etc.), follow the system's instructions.
   &nbsp; &nbsp; &nbsp; &nbsp; <p align="justify"> 2. Dates and times should be entered in the specified format: YYYY-MM-DD HH:MM AM/PM.
   &nbsp; &nbsp; &nbsp; &nbsp; <p align="justify"> 3. For some actions (e.g., making, updating, or canceling a reservation), the system will ask you to confirm your choices (e.g., "Do you want to proceed? (yes/no)"). Respond with yes or no.

- __Step 7: Database (SQLite)__
   &nbsp; &nbsp; &nbsp; &nbsp; <p align="justify"> 1.	The script will automatically create a new SQLite database file named vehicle_rental.db in the same directory.
   &nbsp; &nbsp; &nbsp; &nbsp; <p align="justify"> 2. If the database file already exists, it will be deleted and recreated when the program runs.
   &nbsp; &nbsp; &nbsp; &nbsp; <p align="justify"> 3. The database will store:
          <p align="justify"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; o	__Vehicles__: Information about the vehicles available for rent (type, model, plate number, daily rate, and availability).
          <p align="justify"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; o	__Reservations__: Client reservation details including client information, vehicle reserved, rental duration, and rental fee.

- __Step 8: Exit the Program__
   &nbsp; &nbsp; &nbsp; &nbsp; <p align="justify"> 	To exit the system, choose option 7 from the dashboard, and the system will display a thank-you message and safely close the database connection.
