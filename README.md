<!-- TITLE SECTION -->
<h1 align="center">Tichi App - QA Testing Suite</h1>

<p align="center">
  This repository houses the comprehensive Quality Assurance (QA) assets for the <strong>Tichi App</strong>, split into structured automated and manual testing segments to ensure full application stability, high-quality feature releases, and robust defect tracking.
</p>

<p>
  As shown in <code>image_cfeda9.png</code>, the root of the project separates testing efforts into distinct paradigms:
</p>

<ul>
  <li><strong>Automation_Testing:</strong> Python/Pytest framework for automated end-to-end functionality verification.</li>
  <li><strong>Manual_Testing:</strong> Documented validation matrices, test suites, and logged anomalies.</li>
</ul>

<hr />

<!-- REPOSITORY STRUCTURE -->
<h2>📂 Repository Structure</h2>

<p>The complete file tree, detailed across <code>image_cfedfe.png</code> and <code>image_cfee22.png</code>, follows this organizational layout:</p>

<pre>
├── Automation_Testing/
│   ├── tichi_automation/               # Core automation framework
│   │   ├── config/                     # Framework configuration configurations
│   │   ├── data/                       # Test data inputs (JSON, CSV, etc.)
│   │   ├── pages/                      # Page Object Model (POM) design classes
│   │   ├── tests/                      # Pytest execution scripts
│   │   ├── utils/                      # Helper modules and reusable drivers
│   │   ├── allure-results/             # Raw test run logs for Allure
│   │   ├── reports/allure-results/     # Finalized test metrics
│   │   ├── conftest.py                 # Pytest fixtures and global setups
│   │   ├── pytest.ini                  # Pytest run configurations
│   │   └── requirements.txt            # Python dependencies
│   └── execution_report.html           # Standalone HTML execution summary
│
└── Manual_Testing/
    ├── Defect_Report_Tichi_App.xlsx    # Tracked bugs, severity, and statuses
    └── Test_Case_Report_Tichi_App.xlsx  # Manual test scenarios and execution logs
</pre>

<hr />

<!-- AUTOMATION FRAMEWORK DETAILS -->
<h2>⚙️ Automation Framework Details</h2>

<p>The automation suite is built using <strong>Python</strong> and the <strong>Pytest</strong> ecosystem. It follows industry-standard architectural best practices:</p>

<ul>
  <li><strong>Page Object Model (POM):</strong> Located in the <code>pages/</code> directory to separate UI locators and actions from the actual test assertions, maximizing maintainability.</li>
  <li><strong>Data-Driven Testing:</strong> Test scenarios ingest data dynamically from the <code>data/</code> suite.</li>
  <li><strong>Detailed Reporting:</strong> Uses built-in HTML reporters (<code>execution_report.html</code>) and integrates with <strong>Allure Reports</strong> via <code>allure-results/</code> for deep dive diagnostic graphs, steps tracking, and screenshot logging on failures.</li>
</ul>

<h3>Local Setup & Execution</h3>
<p>To spin up and run the automated test suites locally, execute the following commands in your terminal:</p>

<pre><code><b># 1. Navigate to the core automation folder</b>
cd Automation_Testing/tichi_automation

<b># 2. Set up a virtual environment & activate it</b>
python -m venv venv
<span style="color: #888;"># On Windows:</span>
.\venv\Scripts\activate
<span style="color: #888;"># On macOS/Linux:</span>
source venv/bin/activate

<b># 3. Install required packages</b>
pip install -r requirements.txt

<b># 4. Run the suite</b>
pytest</code></pre>

<hr />

<!-- MANUAL TESTING ARTIFACTS -->
<h2>📝 Manual Testing Artifacts</h2>

<p>For exploratory, UI/UX, and complex logic validation that falls outside the automation scope, the <code>Manual_Testing/</code> folder acts as the single source of truth:</p>

<ul>
  <li><strong><code>Test_Case_Report_Tichi_App.xlsx</code>:</strong> Outlines functional test coverages, prerequisites, detailed reproduction steps, expected behaviors, and historic pass/fail matrices.</li>
  <li><strong><code>Defect_Report_Tichi_App.xlsx</code>:</strong> Logged exceptions found during QA lifecycles, mapped cleanly with priority tags, severity scales, environment details, and developer assignees.</li>
</ul>
