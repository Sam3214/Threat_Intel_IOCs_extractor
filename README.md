# 🛡️ Threat Intel IOCs Extractor

A Python-based threat intelligence automation tool that collects cybersecurity feeds from public sources, parses threat reports, extracts Indicators of Compromise (IOCs), and stores them in structured JSON files for further analysis and threat hunting.

## 📌 Overview

Threat intelligence reports often contain valuable IOCs such as:

- MD5 hashes
- SHA1 hashes
- SHA256 hashes
- Malware indicators
- Threat actor artifacts

This tool automates the process of gathering threat intelligence feeds and extracting relevant indicators, eliminating manual collection and improving threat intelligence workflows.

---

## ✨ Features

- Automated threat feed collection
- IOC extraction from security blogs and reports
- Support for multiple feed sources
- Extraction of:
  - MD5 hashes
  - SHA1 hashes
  - SHA256 hashes
- JSON-based output format
- Organized IOC storage
- Easy to extend with additional feed sources

---

## 🏗️ Project Structure

```text
Threat_Intel_IOCs_extractor/
│
├── IOCs/               # Generated IOC JSON files
├── Main.py             # Main execution script
├── Parser.py           # Feed parsing logic
├── Extractor.py        # IOC extraction engine
├── feeds.txt           # Production feed sources
├── feeds_test.txt      # Test feed sources
└── README.md
```

---

## ⚙️ Requirements

- Python 3.8+
- Internet connectivity
- Required Python packages

Install dependencies:

```bash
pip install -r requirements.txt
```

If no requirements file exists, install commonly used packages manually as needed.

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/Sam3214/Threat_Intel_IOCs_extractor.git
cd Threat_Intel_IOCs_extractor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the application:

```bash
python Main.py
```

The tool will:

1. Read feed URLs from `feeds.txt`
2. Retrieve threat intelligence articles
3. Parse content
4. Extract hashes and other IOCs
5. Save results into the `IOCs/` directory

---

## 📄 Example Output

Example generated IOC file:

```json
{
  "SHA256": [
    "6d9379e365a4da282531d7f234c69eefa48567c01ba173b462e907a1ddfc71b2"
  ],
  "SHA1": [],
  "MD5": [
    "0959deda4982736d1c1647cff354c665"
  ]
}
```

Generated files are stored inside:

```text
IOCs/
```

Each file corresponds to a parsed threat intelligence article. 【2-469071】

---

## 🧠 Use Cases

- SOC Operations
- Threat Hunting
- IOC Collection
- Malware Analysis
- Threat Intelligence Research
- Security Automation Projects

---

## 🔄 Workflow

```text
Threat Feeds
      │
      ▼
 Feed Collection
      │
      ▼
 Content Parsing
      │
      ▼
 IOC Extraction
      │
      ▼
 JSON Output Storage
```

---

## 🚧 Future Improvements

- Domain extraction
- URL extraction
- IP address extraction
- YARA rule generation
- MISP integration
- STIX/TAXII export support
- Threat score enrichment
- VirusTotal enrichment

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature/new-feature
```

3. Commit changes

```bash
git commit -m "Add new feature"
```

4. Push to GitHub

```bash
git push origin feature/new-feature
```

5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Samarth**

GitHub: https://github.com/Sam3214

---

## ⚠️ Disclaimer

This tool is intended for educational, research, and defensive cybersecurity purposes only. Users are responsible for complying with all applicable laws and regulations when collecting and processing threat intelligence data.
