
# Open Source SCOPE - Geography Lab

An interactive geography atlas for SCOPE school (Yerala Project Society, Jalihal) Geography classes. Open `index.html` in any browser: it is a single self-contained file, so it works offline and can be hosted on GitHub Pages.

Give it a shot here - https://adm-htfre.github.io/Open-Source-SCOPE-Geography-Lab

<img width="1273" height="1017" alt="image" src="https://github.com/user-attachments/assets/6b3bfcc3-ecc7-4a24-903c-f16a4ef89f0f" />


## What it does

- **World map** (Equal Earth projection): population, area, density, life expectancy, income per person (in ₹), urban share and forest cover for 215 countries. Pan, zoom and full-screen.
- **India map**: Census 2011 figures for the 35 States and Union Territories, grouped by Zonal Council.
- **District maps** for Maharashtra and Karnataka: double-click a state. Neighbouring states show faded at the edges; click across the border to switch.
- A "balance of power" style bar showing how population and land are shared, rankings, a detail card for each place, a quiz mode and an English / मराठी switch.

## Data sources

| Level | Source |
|---|---|
| World | World Bank, World Development Indicators (latest available year, mostly 2023–2025). Income converted at ₹87.16 per US$ (World Bank 2025 average, PA.NUS.FCRF). |
| India | Census of India 2011, Primary Census Abstract (via Basic Statistics 2024-25, Table 32); literacy via Ministry of Education. |
| Districts | Census of India 2011 district tables (compiled by census2011.co.in); totals match official State populations. District area is population ÷ density, so approximate. |
| Maps | Natural Earth 1:10m countries, India point-of-view edition (India's official borders); INDIAN-SHAPEFILES for States and districts. |

All figures for India describe 2011 boundaries: Telangana shows undivided Andhra Pradesh, Ladakh shows Jammu & Kashmir, Palghar shows Thane and Vijayanagara shows Ballari.

## Repository layout

- `index.html`: the atlas (everything inlined)
- `data/`: the processed data and projected map shapes baked into the page
- `scripts/`: the scripts used to build the data and the page (`template.html` + `build.py`)


