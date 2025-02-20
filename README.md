# 💼 Automated Job Search Tool  

```


_______       _____                        _____     _________   _________     ______       ________                        ______       ________           ______
___    |___  ___  /_____________ _________ __  /___________  /   ______  /________  /_      __  ___/__________ ________________  /_      ___  __/______________  /
__  /| |  / / /  __/  __ \_  __ `__ \  __ `/  __/  _ \  __  /    ___ _  /_  __ \_  __ \     _____ \_  _ \  __ `/_  ___/  ___/_  __ \     __  /  _  __ \  __ \_  / 
_  ___ / /_/ // /_ / /_/ /  / / / / / /_/ // /_ /  __/ /_/ /     / /_/ / / /_/ /  /_/ /     ____/ //  __/ /_/ /_  /   / /__ _  / / /     _  /   / /_/ / /_/ /  /  
/_/  |_\__,_/ \__/ \____//_/ /_/ /_/\__,_/ \__/ \___/\__,_/      \____/  \____//_.___/      /____/ \___/\__,_/ /_/    \___/ /_/ /_/      /_/    \____/\____//_/   
                                                                                                                                                                  

```

An intelligent job search application leveraging the SerpAPI to fetch and format relevant job listings directly from Google Jobs. This tool is particularly useful for automating job searches, providing concise job descriptions, and saving results in a structured format.

---

## 🚀 **Project Overview**

The AI-Powered Job Search Tool is designed to simplify and automate the job search process using SerpAPI's Google Jobs engine. With a few inputs like the job title and location, the tool fetches job listings, formats the information, and saves it into a text file, enhancing efficiency in job hunting.

---

## 📂 **Project Structure**

```
📁 AI-Job-Search/
├── 📄 job_search.py                 # Core job search and formatting logic
├── 📄 job_search_results.txt        # Output file with formatted job listings
└── 📄 requirements.txt              # Project dependencies
```

---

## 🧠 **Key Features**

- 🔍 **Automated Job Search:** Queries Google Jobs using SerpAPI.
- 📝 **Formatted Results:** Outputs job details, including title, company, location, and description.
- 💾 **Save to File:** Stores results in a neatly formatted `.txt` file.
- 📍 **Location-Based Filtering:** Allows search queries specific to a geographic area.

---

## ⚡ **Getting Started**

### **1. Clone the Repository**

```bash
git clone https://github.com/yourusername/AI-Job-Search.git
cd AI-Job-Search
```

### **2. Install Dependencies**

```bash
pip install -r requirements.txt
```

**requirements.txt:**
```text
serpapi==2.0.0
```

### **3. Set Up SerpAPI Key**

- Obtain an API key from [SerpAPI](https://serpapi.com).
- Set the environment variable:

```bash
export SERPAPI_API_KEY="your_api_key_here"
```

### **4. Run the Job Search Tool**

```bash
python job_search.py
```

---

## 🎯 **Usage Example**

The default script runs a job search for "Data Scientist" roles in "Toronto":

```python
job_searcher = JobSearch()
query = "Data Scientist"
location = "Toronto"
results = job_searcher.job_search(query, location, num_results=10)
formatted_results = job_searcher.format_results(results)

filename = "job_search_results.txt"
save_to_file(formatted_results, filename)
```

- The results will be saved in `job_search_results.txt` with a user-friendly format.

---

## 📄 **Sample Output**

```
1. Data Scientist - XYZ Company: Analyze data trends, build models, and support data-driven decision-making.

2. Machine Learning Engineer - ABC Inc.: Develop and optimize machine learning models for financial forecasting.

...

Please note that the availability of these positions may vary. It is recommended to check the corresponding company's career page or job portals for the most recent and accurate information.
```

---

## 🔮 **Future Enhancements**

- ✅ Add filters for job type (e.g., Full-time, Part-time, Remote).
- 🌐 Integrate additional job search APIs for broader coverage.
- 📈 Implement analytics on job search trends and opportunities.
- 🖥️ Develop a simple web interface using Flask or Streamlit for ease of use.

---

