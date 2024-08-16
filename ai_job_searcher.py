import os
from typing import List, Dict, Any
from serpapi import GoogleSearch

class JobSearch:
    def __init__(self):
        self.api_key = os.environ["SERPAPI_API_KEY"]

    def job_search(self, query: str, location: str, num_results: int = 10) -> List[Dict[str, str]]:
        params = {
            "engine": "google_jobs",
            "q": query,
            "location": location,
            "hl": "en",
            "api_key": self.api_key,
        }
        search = GoogleSearch(params)
        results = search.get_dict().get("jobs_results", [])
        return results[:num_results]

    def format_results(self, results: List[Dict[str, str]]) -> str:
        output = ""
        for i, job in enumerate(results, 1):
            title = job.get("title", "N/A")
            company = job.get("company_name", "N/A")
            location = job.get("location", "N/A")
            description = job.get("description", "No description available.")
            
            output += f"{i}. {title} - {company}: {description}\n\n"

        output += "Please note that the availability of these positions may vary. It is recommended to check the corresponding company's career page or job portals for the most recent and accurate information."
        return output

def save_to_file(content: str, filename: str):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Results have been saved to {filename}")

if __name__ == "__main__":
    job_searcher = JobSearch()
    query = "Data Scientist"
    location = "Toronto"
    results = job_searcher.job_search(query, location, num_results=10)
    formatted_results = job_searcher.format_results(results)
    
    filename = "job_search_results.txt"
    save_to_file(formatted_results, filename)
