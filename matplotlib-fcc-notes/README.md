# Python Data Visualization Cheat Sheet: Matplotlib & Seaborn
 
**LEGEND:**
-  MPL = matplotlib.pyplot
-  sns = seaborn

 
## IMPORTS

```python   
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
```
 
## PLOT TYPES & COMMANDS

Line Plot:
  - Matplotlib: `plt.plot(x, y)`
  - Seaborn:    `sns.lineplot(x=x, y=y)`

Scatter Plot:
  - Matplotlib: `plt.scatter(x, y)`
  - Seaborn:    `sns.scatterplot(x=x, y=y, hue="group")`

Bar Plot:
  - Matplotlib: `plt.bar(labels, values)`
  - Seaborn:    `sns.barplot(x=labels, y=values)`

Histogram:
  - Matplotlib: `plt.hist(data, bins=10)`
  - Seaborn:    `sns.histplot(data, bins=10, kde=True)`

Box Plot:
  - Matplotlib: `plt.boxplot([list1, list2])`
  - Seaborn:    `sns.boxplot(x="label", y="value", data=df)`

Violin Plot:
  - Matplotlib: (not native)
  - Seaborn:    `sns.violinplot(x, y, data=df)`

Heatmap:
  - Matplotlib: `plt.imshow(array)`
  - Seaborn:    `sns.heatmap(data, annot=True)`

KDE / Density Plot:
  - Matplotlib: (advanced setup)
  - Seaborn:    `sns.kdeplot(data, fill=True)`

Pair Plot:
  - Matplotlib: (not native)
  - Seaborn:    `sns.pairplot(df)`

Count Plot:
  - Matplotlib: (not native)
  - Seaborn:    `sns.countplot(x="col", data=df)`

Swarm Plot:
  - Matplotlib: (not native)
  - Seaborn:    `sns.swarmplot(x="col1", y="col2", data=df)`

Pie Chart:
  - Matplotlib: `plt.pie(sizes, labels=labels)`
  - Seaborn:    Not supported

 
## COMMON SETTINGS

1. Title & Labels:
  - Matplotlib:
      ```python
      plt.title("Title")
      plt.xlabel("X Axis")
      plt.ylabel("Y Axis")
      ```
  - Seaborn:
      `sns.set(title="Title", xlabel="X Axis", ylabel="Y Axis")`

2. Grid:
  - Matplotlib: `plt.grid(True)`
  - Seaborn:    `sns.set_style("whitegrid")`

3. Figure Size:
  - Matplotlib: `plt.figure(figsize=(6,4), dpi=100)`
  - Seaborn:    `sns.set_context("paper")`

4. Legend:
  - Matplotlib: `plt.legend()`
  - Seaborn:    `sns.move_legend(ax, "best")`

5. Save Figure:
  - Matplotlib: `plt.savefig("plot.png", dpi=300)`
  - Seaborn:    same as Matplotlib

6. Style:
  - Matplotlib: `plt.style.use("ggplot")`
  - Seaborn:    `sns.set_style("darkgrid")`

7. Context:
  - Matplotlib: (n/a)
  - Seaborn:    `sns.set_context("notebook")`

 
## DATA OPERATIONS QUICK REFERENCE

1. Load CSV:
  `df = pd.read_csv("file.csv")`

2. View Rows:
  `df.head()`
 ` df.tail()`

3. Filter Rows:
  `df[df["Age"] > 25]`

4. Group By:
  `df.groupby("col").mean()`

5. Missing Data:
  `df.dropna()`
  `df.fillna(0)`

6. NumPy Array:
  `arr = np.array([1,2,3])`

7. Range Array:
  `np.arange(0, 10, 0.5)`

 
## EXAMPLE: Seaborn Boxplot
```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("data.csv")
sns.set_theme(style="whitegrid")

sns.boxplot(x="team", y="score", data=df)
plt.title("Team Score Distribution")
plt.savefig("box.png")
plt.show()

 ```

 
## USEFUL LINKS:
- Matplotlib Docs: https://matplotlib.org/stable/gallery/index.html
- Seaborn Docs:    https://seaborn.pydata.org/examples/index.html
 
