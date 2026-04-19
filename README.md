# SCT_SD_task_4 - E-Commerce Web Scraper

A Python-based web scraper that extracts product information (titles, prices, ratings, and availability) from e-commerce websites and stores the data in a structured CSV format.

## 📋 Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Output](#output)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Troubleshooting](#troubleshooting)
- [Author](#author)

## ✨ Features

- ✅ **Simple & Effective** - Easy-to-use scraper for extracting product data
- ✅ **Complete Data Extraction** - Captures Title, Price, Rating, and Availability
- ✅ **CSV Export** - Automatically saves data to structured CSV files using Pandas
- ✅ **Error Handling** - Robust handling for network issues and missing data
- ✅ **Educational** - Perfect for learning web scraping fundamentals

## 📦 Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Internet connection to access the website

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Chethans3413/SCT_SD_task_4.git
cd SCT_SD_task_4
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

**Dependencies:**
- `requests` - HTTP library for fetching web pages
- `beautifulsoup4` - HTML parsing library
- `lxml` - Fast XML/HTML processor
- `pandas` - Data manipulation and CSV export

## 🎯 Usage

### Run the Scraper

```bash
python scraper.py
```

### Expected Output

```
--- Success! ---
Extracted 20 products.
Data saved to 'products.csv'
```

## 📊 Output

The scraper generates a **products.csv** file with the following columns:

| Column | Description |
|--------|-------------|
| Title | Product name/book title |
| Price | Price in the website's currency |
| Rating | Rating as text (e.g., "Three", "Four", "Five") |
| Availability | Stock availability status (e.g., "In stock") |

### Sample CSV Output

```csv
Title,Price,Rating,Availability
A Light in the Attic,£51.77,Three,In stock
Tipping the Velvet,£53.74,One,In stock
Soumission,£50.10,One,In stock
Sharp Objects,£47.82,Four,In stock
Sapiens: A Brief History of Humankind,£54.23,Five,In stock
```

## 📁 Project Structure

```
SCT_SD_task_4/
├── scraper.py              # Main scraper script
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
└── products.csv           # Generated output file (created when script runs)
```

## 🔧 How It Works

The scraper follows these steps:

1. **Fetch** - Sends an HTTP request to the website with appropriate headers
2. **Parse** - Uses BeautifulSoup to parse the HTML content
3. **Extract** - Identifies and extracts product information:
   - Title (from `<h3>` tag)
   - Price (from element with class `price_color`)
   - Rating (from element with class `star-rating`)
   - Availability (from element with class `instock availability`)
4. **Store** - Collects all data into a list of dictionaries
5. **Save** - Uses Pandas DataFrame to export data to CSV file

## 💻 Code Overview

```python
def scrape_books():
    # Step 1: Fetch the website
    response = requests.get(url, headers=headers)
    
    # Step 2: Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Step 3: Extract products
    books = soup.find_all("article", class_="product_pod")
    
    # Step 4: Collect data
    data = []
    for book in books:
        data.append({...})
    
    # Step 5: Save to CSV
    df = pd.DataFrame(data)
    df.to_csv("products.csv", index=False)
```

## 🌐 Data Source

This scraper targets **[books.toscrape.com](http://books.toscrape.com/)** - a free website specifically designed for learning web scraping techniques. It's safe to scrape and perfect for educational purposes.

## ⚠️ Important Notes

### Legal & Ethical Considerations

- ✅ **books.toscrape.com** explicitly allows scraping for educational purposes
- ✅ Always check a website's `robots.txt` and Terms of Service before scraping
- ✅ Respect rate limits and don't overload servers
- ✅ Use appropriate delays between multiple requests
- ✅ Include a User-Agent header (this scraper does automatically)

### Best Practices

- Always verify you have permission to scrape a website
- Check the website's Terms of Service first
- Use delays between requests to be respectful
- Don't scrape sensitive or copyrighted content
- Respect the server's resources

## 🔍 Troubleshooting

### Issue: "Failed to retrieve the website"

**Solution:**
1. Check your internet connection
2. Verify the URL is accessible (try opening in browser)
3. Check if the website is temporarily down
4. Ensure you're not blocked by the website's firewall

### Issue: No data is being extracted

**Solution:**
1. The website structure may have changed
2. HTML selectors might be outdated
3. Check if the website uses JavaScript to load content
4. Inspect the website in browser DevTools to verify CSS selectors

### Issue: Permission Denied when saving CSV

**Solution:**
1. Ensure the directory is writable
2. Close any open CSV files
3. Try saving to a different location
4. Check user permissions on the folder

## 📝 Sample Run

```bash
D:\SCT_SD_task_4> python scraper.py
--- Success! ---
Extracted 20 products.
Data saved to 'products.csv'

D:\SCT_SD_task_4> type products.csv
Title,Price,Rating,Availability
A Light in the Attic,£51.77,Three,In stock
Tipping the Velvet,£53.74,One,In stock
...
```

## 🛠️ Technologies Used

| Technology | Purpose |
|-----------|---------|
| **Python 3** | Programming language |
| **Requests** | HTTP requests to fetch web pages |
| **BeautifulSoup** | HTML parsing and data extraction |
| **Pandas** | Data manipulation and CSV export |
| **lxml** | Fast HTML/XML processing |

## 📚 Learn More

- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests Library](https://requests.readthedocs.io/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Web Scraping Ethics](https://en.wikipedia.org/wiki/Web_scraping#Ethics)



## 📄 License

This project is provided as-is for educational purposes. Feel free to use, modify, and distribute it for learning and educational use.

## 🤝 Contributing

Found a bug or have suggestions? Feel free to open an issue or submit a pull request!

## ✅ Checklist

- [x] Web scraper implementation
- [x] CSV data export
- [x] Error handling
- [x] Documentation
- [x] GitHub repository setup

---

**Last Updated:** April 2026  
**Status:** Active & Maintained
