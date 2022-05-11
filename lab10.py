import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image

df = pd.read_csv('imiona.csv', header = 0, sep=",", decimal=".")
print(df)
cos = df.groupby('Plec').nunique()
print(cos)
plt.bar(df.Plec.nunique,cos.Liczba)
plt.show()
# fig, axs = plt.subplots(1, 3)
# axs[0].bar(df['Plec'].nunique,cos['Liczba'], 'r-')
# axs[0].set_title('wykres sin(x)')
# axs[0].set_xlabel('x')
# axs[0].set_ylabel('sin(x)')

# axs[1].plot(x2, y2, 'r-')
# axs[1].set_title('wykres cos(x)')
# axs[1].set_xlabel('x')
# axs[1].set_ylabel('cos(x)')
#
# axs[2].plot(x2, y2, 'r-')
# axs[2].set_title('wykres cos(x)')
# axs[2].set_xlabel('x')
# axs[2].set_ylabel('cos(x)')

plt.show()