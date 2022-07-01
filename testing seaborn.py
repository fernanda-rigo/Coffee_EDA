import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
sns.set_theme(style="darkgrid")

# Load an example dataset with long-form data
fmri = sns.load_dataset("fmri")

#Plot the responses for different events and regions
# plt.figure()
# sns.lineplot(x="timepoint", y="signal",
#              hue="region", style="event",
#              data=fmri)
# plt.show()
print(fmri.info())
print(fmri.head(5))