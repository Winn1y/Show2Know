import matplotlib.pyplot as plt
import pandas as pd

# 论文时间轴

# Data for the papers
data = {
    'Paper': ['Text2Performer', 'LAVIE', 'Animate Anyone', 'MagicPose', 'Make-An-Animation',
              'HMDM', 'Pose-Conditional GANs', 'VideoGPT', 'HumanML3D', 'Neural Actor'],
    'Date': ['2023/10', '2023/09', '2023/11', '2023/11', '2023/10',
             '2023', '2023', '2023', '2023', '2023']
}

# Create a DataFrame
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'], format='%Y/%m')

# Plotting the timeline
fig, ax = plt.subplots(figsize=(12, 6))

# Plot the events on the timeline
ax.plot(df['Date'], df['Paper'], marker='o', linestyle='-')

# Annotate each event
for i, txt in enumerate(df['Paper']):
    ax.annotate(txt, (df['Date'][i], df['Paper'][i]), textcoords="offset points", xytext=(0,10), ha='center')

# Format the x-axis as date
ax.xaxis_date()
fig.autofmt_xdate()

# Set the title and labels
plt.title('Publication Timeline of 2D Human Video Generation Papers')
plt.xlabel('Publication Date')
plt.ylabel('Papers')

plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()
