🚖 OLA Data Analyst Project
📌 Project Overview

This project is an end-to-end Data Analytics case study based on ride-booking data for OLA, focusing on booking trends, cancellations, revenue, vehicle performance, and customer & driver ratings.
The objective is to simulate a real-world business problem and derive actionable insights using SQL and Power BI.

The dataset represents 1 month of ride data for Bengaluru city, containing over 100,000 records with realistic constraints on booking success, cancellations, and ride behavior.

🎯 Objectives

Analyze ride booking patterns and trends over time

Understand cancellation behavior (customer & driver)

Evaluate revenue distribution and payment methods

Compare vehicle types based on distance, ratings, and performance

Build interactive dashboards for business decision-making

🛠️ Tools & Technologies Used

SQL – Data querying, views, and analysis

Power BI – Interactive dashboards & visualizations

Excel / CSV – Data generation & preprocessing

GitHub – Version control & project documentation

📂 Dataset Description

The dataset includes the following key columns:

Date, Time

Booking_ID, Booking_Status

Customer_ID

Vehicle_Type (Auto, Mini, Prime Sedan, Prime SUV, Bike, eBike, Prime Plus)

Pickup_Location, Drop_Location

Avg VTAT, Avg CTAT

Cancelled Rides (Customer & Driver)

Incomplete Rides & Reasons

Booking_Value

Payment_Method

Ride_Distance

Driver_Ratings, Customer_Rating

📊 Business Rules Applied:

Successful bookings ≈ 62%

Customer cancellations ≤ 7%

Driver cancellations ≤ 18%

Incomplete rides ≤ 6%

Higher order value on weekends

🧮 SQL Analysis

The project includes SQL queries and views to answer key business questions such as:

Successful bookings analysis

Average ride distance per vehicle type

Cancellation trends (customer & driver)

Top 5 customers by number of rides

Revenue from completed bookings

Ratings analysis by vehicle type

📁 SQL views are created for reusable and structured querying.

📊 Power BI Dashboard

The Power BI report is divided into 5 major sections:

1️⃣ Overall

Ride Volume Over Time

Booking Status Breakdown

2️⃣ Vehicle Type

Top 5 Vehicle Types by Ride Distance

3️⃣ Revenue

Revenue by Payment Method

Top 5 Customers by Total Booking Value

Ride Distance Distribution per Day

4️⃣ Cancellation

Customer Cancellation Reasons

Driver Cancellation Reasons

5️⃣ Ratings

Driver Ratings Distribution

Customer Ratings Distribution

Customer vs Driver Ratings Comparison

🔍 Key Insights

Weekends show higher ride volume and booking value

Certain vehicle types dominate long-distance travel

Cancellation reasons vary significantly between customers and drivers

Strong correlation observed between driver ratings and customer satisfaction
