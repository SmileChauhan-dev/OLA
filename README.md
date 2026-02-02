# 🚖 OLA Data Analyst Project

<p align="center">
  <b>An End-to-End Data Analytics Case Study using SQL & Power BI</b><br>
  <i>Focused on ride trends, cancellations, revenue, and customer behavior</i>
</p>

---

## 📌 Project Overview
This project is an **end-to-end Data Analytics case study** based on ride-booking data for **OLA**.  
It analyzes booking trends, cancellations, revenue patterns, vehicle performance, and customer & driver ratings.

The dataset simulates **real-world ride data for Bengaluru city over one month**, containing **100,000+ records** with realistic business constraints.

---

## 🎯 Project Objectives
- 📊 Analyze ride volume and booking trends over time  
- ❌ Understand customer & driver cancellation behavior  
- 💰 Evaluate revenue and payment method distribution  
- 🚗 Compare vehicle types by distance, ratings, and performance  
- 📈 Build interactive dashboards for business insights  

---

## 🛠️ Tools & Technologies
| Tool | Purpose |
|----|----|
| **SQL** | Data querying, views & analysis |
| **Power BI** | Dashboards & data visualization |
| **Excel / CSV** | Data generation & preprocessing |
| **GitHub** | Version control & documentation |

---

## 📂 Dataset Details
The dataset includes the following key columns:

- Date, Time  
- Booking_ID, Booking_Status  
- Customer_ID  
- Vehicle_Type (Auto, Mini, Prime Sedan, Prime SUV, Bike, eBike, Prime Plus)  
- Pickup_Location, Drop_Location  
- Avg VTAT, Avg CTAT  
- Cancelled Rides (Customer & Driver)  
- Incomplete Rides & Reasons  
- Booking_Value  
- Payment_Method  
- Ride_Distance  
- Driver_Ratings, Customer_Rating  

### 📊 Business Rules Applied
- ✅ Successful bookings ≈ **62%**  
- ❌ Customer cancellations ≤ **7%**  
- ❌ Driver cancellations ≤ **18%**  
- ⚠️ Incomplete rides ≤ **6%**  
- 📈 Higher booking value on weekends  

---

## 🧮 SQL Analysis
SQL queries and **views** were created to answer key business questions:

- Retrieve all successful bookings  
- Average ride distance per vehicle type  
- Total customer & driver cancellations  
- Top 5 customers by number of rides  
- Total revenue from completed rides  
- Ratings analysis for Prime Sedan bookings  

✔️ Views are used for **clean, reusable analysis**.

---

## 📊 Power BI Dashboard Structure

### 🔹 Overall
- Ride Volume Over Time  
- Booking Status Breakdown  

### 🔹 Vehicle Type
- Top 5 Vehicle Types by Ride Distance  

### 🔹 Revenue
- Revenue by Payment Method  
- Top 5 Customers by Total Booking Value  
- Ride Distance Distribution per Day  

### 🔹 Cancellation
- Customer Cancellation Reasons  
- Driver Cancellation Reasons  

### 🔹 Ratings
- Driver Ratings Distribution  
- Customer Ratings Distribution  
- Customer vs Driver Ratings  

---

## 🔍 Key Insights
- 📅 Weekends generate higher ride volume and revenue  
- 🚘 Prime Sedan & SUV dominate long-distance rides  
- ❌ Cancellation reasons differ significantly between customers and drivers  
- ⭐ Higher driver ratings strongly impact customer satisfaction  

---

