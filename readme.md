# **Monthly Planner Web Application**

## **Purpose**

The **Monthly Planner Web Application** is a calendar-based application that helps users plan and organize their monthly schedule. It integrates multiple features, including:
- Displaying holidays dynamically based on the selected year.
- Adding financial updates, tasks, and notes specific to each month.
- Setting monthly priorities and goals.
- Viewing current news headlines related to Malaysia.
  
The application leverages APIs to fetch holidays and news dynamically, providing an interactive and intuitive user experience.

---

## **Features**
- **Dynamic Holiday Display**: Fetches and displays public holidays for Malaysia for any selected year using the [API Ninjas](https://api-ninjas.com/) holiday API.
- **Customizable Planner**: Allows users to add:
  - Financial updates
  - Notes
  - Monthly goals
  - Top priorities
- **News Integration**: Displays current news headlines related to Malaysia using the [GNews API](https://gnews.io/).
- **Interactive Calendar**: Users can navigate between months and years seamlessly while maintaining their data for each month.
  
---

## **Technologies Used**
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask)
- **APIs**:
  - [API Ninjas Holidays API](https://api-ninjas.com/) for holidays
  - [GNews API](https://gnews.io/) for news headlines

---

## **Setup and Installation**

### **Prerequisites**
1. Install [Python 3.8+](https://www.python.org/downloads/).
2. Install [pip](https://pip.pypa.io/en/stable/installation/).

### **Installation Steps**
1. Clone the repository:
   ```bash
   git clone https://github.com/atikahidruss/holiday_planner.git
   cd holiday_planner
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up API keys:
   - Obtain API keys for the [API Ninjas Holidays API](https://api-ninjas.com/) and [GNews API](https://gnews.io/).
   - Update the `main.py` file:
     ```python
     HOLIDAYS_API_KEY = "your_holidays_api_key_here"
     NEWS_API_KEY = "your_news_api_key_here"
     ```

4. Run the application:
   ```bash
   python main.py
   ```
5. Open your browser and visit:
   ```
   http://127.0.0.1:5000/
   ```

---

## **Usage**

1. **Viewing Holidays**:
   - Navigate to different months and years using the **Previous** and **Next** buttons.
   - Holidays will be displayed dynamically for the selected year.

2. **Adding Financial Updates, Tasks, Notes, Goals, and Priorities**:
   - Use the text areas for **Notes**, **Goals**, and **Top Priorities** to add your data for the selected month.
   - Financial updates and tasks can be added directly to the calendar days by clicking on them.

3. **Viewing News**:
   - News headlines for Malaysia will appear on the calendar under the respective dates.

4. **Data Persistence**:
   - Data entered for each month (notes, goals, priorities) is stored and displayed when you return to that month.

---

## **API Configuration**

### Holidays API
- **Endpoint**: `https://api.api-ninjas.com/v1/holidays`
- **Parameters**:
  - `country`: `MY` (Malaysia)
  - `year`: Selected year

### News API
- **Endpoint**: `https://gnews.io/api/v4/search`
- **Parameters**:
  - `q`: `Malaysia`
  - `from` & `to`: Date range based on the selected month
  - `token`: Your GNews API key

---

## **Future Enhancements**
- Enable user authentication to save data across devices.
- Add recurring tasks and reminders for specific dates.
- Provide international support for other countries' holidays.

---

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

