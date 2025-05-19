## Project Title: Solar Data Discovery Challenge

### Overview
This project involves a comprehensive analysis of solar farm data from Benin, togo, and andsierraleone focusing on summary statistics, outlier detection, time series analysis, and correlation assessments. 
### Contents
- Importing necessary libraries 
- Loading the dataset
- Summary Statistics & Missing-Value Report
- Outlier Detection & Cleaning
- Time Series Analysis
- Cleaning Impact Analysis
- Correlation & Relationship Analysis
- Wind & Distribution Analysis
- Temperature Analysis
- Bubble Chart Visualization
- Cross-Country Solar Potential Comparison

### 1. Summary Statistics & Missing-Value Report
- **Key Metrics**: Utilized `df.describe()` to summarize key statistics for numerical columns.
- **Missing Values**: Employed `df.isna().sum()` to identify missing values:
  - All columns except **"Comments"** have zero missing values, indicating complete data.
  - The **"Comments"** column has **525,600** missing values, suggesting it may be a rarely used or free-text field.

### 2. Outlier Detection & Cleaning
- **Z-score Thresholding**: Applied a threshold of |Z| > 3 to detect outliers in the following columns:
  - GHI (Global Horizontal Irradiance)
  - DNI (Direct Normal Irradiance)
  - DHI (Diffuse Horizontal Irradiance)
  - ModA (Module A Temperature)
  - ModB (Module B Temperature)
  - WS (Wind Speed)
  - WSgust (Wind Gust Speed)
- **Handling Outliers**: Outliers were flagged and either dropped or imputed using median values.
- **Cleaned Data**: The cleaned dataset was saved to `data/benin_clean.csv`,`data/togo_clean.csv`, and `data/sierraleone_clean.csv`.

### 3. Time Series Analysis
- **Plots Created**: Visualized GHI, DNI, DHI, and Tamb (Ambient Temperature) against time.

### 4. Cleaning Impact Analysis
- **Comparison**: Analyzed average ModA and ModB readings before and after cleaning using a "Cleaning" flag.
- **Results**: Noted significant improvements in sensor consistency post-cleaning.

### 5. Correlation & Relationship Analysis
- **Heatmap Analysis**: Created a heatmap showing strong correlations:
  - GHI, DNI, DHI, and module temperatures are highly correlated.
  - ModA and ModB show a perfect correlation (1.00), indicating they may measure the same phenomenon or are duplicates.
  - Both modules (ModA and ModB) have nearly perfect correlations (0.99) with GHI.
  - Notable correlations with energy output (0.99) suggest modules are highly responsive to solar conditions.
  - Slightly lower correlations for DNI/DHI compared to modules indicate energy loss between irradiance and conversion.

### 6. Wind & Distribution Analysis
- **Wind Rose**: Created a wind rose to analyze the relationship between wind speed (WS) and wind direction (WD).
- **Histograms**: Plotted histograms for GHI and WS to visualize distributions.

### 7. Temperature Analysis
- **Influence of RH**: Explored how Relative Humidity (RH) might influence Tamb and GHI.

### 8. Bubble Chart Visualization
- **Bubble Chart**: Plotted GHI against Tamb with bubble size representing RH, providing a visual representation of relationships.

## Cross-Country Solar Potential Comparison

### 9. **Metric Comparison**:
   - Create boxplots to visualize the distribution of Global Horizontal Irradiance (GHI), Direct Normal Irradiance (DNI), and Diffuse Horizontal Irradiance (DHI) across the three countries.
   - Provide a summary table comparing the mean, median, and standard deviation of GHI, DNI, and DHI across the countries.
### 10. **Statistical Testing**:
   - Conduct a one-way ANOVA (or Kruskal–Wallis) test on the GHI values to assess whether the differences between countries are statistically significant.
   - Report the p-values.
### 11. **Key Observations**:
   - Summarize the key observations from the analysis in a markdown cell, highlighting the notable findings (e.g., "Country X shows highest median GHI but also greatest variability").
### 12. **(Bonus) Visual Summary**:
   - Create a small bar chart ranking the countries by their average GHI.
## Contribution
If you would like to contribute to this project, please feel free to submit a pull request or raise an issue. Contributions are welcome, and we appreciate your involvement in enhancing the analysis and expanding the project's scope.


