# Domain Shark 🦈

Domain Shark is a lightweight, efficient Python module designed to gather comprehensive registration, ownership, and network information for target domains and IP addresses. 

---

## ⚡ Features

* **Domain Lookup:** Retrieves registrar data, creation dates, and expiration dates.
* **IP Geolocation:** Fetches country, region, city, and ISP details for any IPv4/IPv6 address.
* **DNS Resolution:** Resolves common records (A, MX, TXT, NS) for target domains.
* **Structured Output:** Returns data in clean, easy-to-parse Python dictionaries or JSON.

---

## 🚀 Installation

Install Domain Shark and its required dependencies directly using pip:

```bash
pip install domain-shark
```

*Note: Ensure you have `python-whois` installed rather than the conflicting `whois` package.*

---

## 🛠️ Quick Start

### 1. Retrieve Domain Information
```python
from domain_shark import DomainShark

# Initialize the tool
shark = DomainShark()

# Fetch WHOIS and DNS data
domain_info = shark.analyze_domain("example.com")
print(domain_info)
```

### 2. Retrieve IP Address Information
```python
# Fetch geolocation and network data
ip_info = shark.analyze_ip("8.8.8.8")
print(ip_info)
```

---

## 📊 Sample Output (JSON)

When analyzing an IP address, Domain Shark returns structured data like this:

```json
{
  "ip": "8.8.8.8",
  "status": "success",
  "country": "United States",
  "countryCode": "US",
  "regionName": "Virginia",
  "city": "Ashburn",
  "isp": "Google LLC",
  "org": "Google Public DNS"
}
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these simple steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.
