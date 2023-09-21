{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "51e5e9d4",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "b120f327",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Number</th>\n",
       "      <th>City</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Age</th>\n",
       "      <th>Income</th>\n",
       "      <th>Illness</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Dallas</td>\n",
       "      <td>Male</td>\n",
       "      <td>41</td>\n",
       "      <td>40367.0</td>\n",
       "      <td>No</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>Dallas</td>\n",
       "      <td>Male</td>\n",
       "      <td>54</td>\n",
       "      <td>45084.0</td>\n",
       "      <td>No</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>Dallas</td>\n",
       "      <td>Male</td>\n",
       "      <td>42</td>\n",
       "      <td>52483.0</td>\n",
       "      <td>No</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>Dallas</td>\n",
       "      <td>Male</td>\n",
       "      <td>40</td>\n",
       "      <td>40941.0</td>\n",
       "      <td>No</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>Dallas</td>\n",
       "      <td>Male</td>\n",
       "      <td>46</td>\n",
       "      <td>50289.0</td>\n",
       "      <td>No</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Number    City Gender  Age   Income Illness\n",
       "0       1  Dallas   Male   41  40367.0      No\n",
       "1       2  Dallas   Male   54  45084.0      No\n",
       "2       3  Dallas   Male   42  52483.0      No\n",
       "3       4  Dallas   Male   40  40941.0      No\n",
       "4       5  Dallas   Male   46  50289.0      No"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "file_path = 'C:/Users/Ashmit/Downloads/toy_dataset.csv'\n",
    "data = pd.read_csv(file_path)\n",
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "48b9867c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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QK/XIywsTGpTKpUYP348Dh48CAAoLCxEY2OjWY1Wq4W/v79Uk5eXB5VKJQUmABg9ejRUKpVZjb+/vxSYACA8PBwmk8ns40IiIiL6bbJqaPr++++xevVq+Pj44PPPP8fTTz+N+Ph4fPzxxwAAvV4PAFCr1WbPU6vV0jq9Xg97e3u4urretMbDw8Oifw8PD7Oa1v24urrC3t5eqmnNZDKhurra7EFERETdk601O29ubsaoUaOQkpICABgxYgROnDiB1atX48knn5TqFAqF2fOEEBZtrbWuaau+PTXXS01NxZIlS246DiIiIuoerDrT1K9fP/j5+Zm1DR06FKWlpQAAjUYDABYzPZWVldKskEajQUNDAwwGw01rKioqLPqvqqoyq2ndj8FgQGNjo8UMVItFixbBaDRKj7KyMln7TURERF2PVUPT2LFjcerUKbO2b775Bl5eXgAAb29vaDQa5OTkSOsbGhpw4MABjBkzBgAQGBgIOzs7s5ry8nIUFxdLNcHBwTAajTh8+LBUc+jQIRiNRrOa4uJilJeXSzXZ2dlQKpUIDAxsc/xKpRIuLi5mDyIiIuqerPrx3HPPPYcxY8YgJSUF06ZNw+HDh/H+++/j/fffB/DTx2UJCQlISUmBj48PfHx8kJKSAkdHR8TExAAAVCoVZs2ahcTERLi5uaFPnz5ISkpCQEAAJk2aBOCn2avJkydj9uzZWLNmDQBgzpw5iIyMhK+vLwAgLCwMfn5+0Ol0WL58OS5duoSkpCTMnj2bYYiIiIisG5ruuecebN++HYsWLcJrr70Gb29vvP3223j88celmgULFqC+vh5xcXEwGAwICgpCdnY2nJ2dpZpVq1bB1tYW06ZNQ319PUJCQrBu3TrY2NhINZs2bUJ8fLx0lV10dDTS0tKk9TY2NsjIyEBcXBzGjh0LBwcHxMTEYMWKFb/CK0FERESdnVXv09Td8D5NRNbD+zQRdX+/6fs0EREREXUVDE1EREREMjA0EREREcnA0EREREQkA0MTERERkQwMTUREREQyMDQRERERycDQRERERCQDQxMRERGRDAxNRERERDIwNBERERHJwNBEREREJANDExEREZEMDE1EREREMjA0EREREcnA0EREREQkA0MTERERkQwMTUREREQyMDQRERERycDQRERERCQDQxMRERGRDAxNRERERDIwNBERERHJ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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "gen_count = data['Gender'].value_counts()\n",
    "\n",
    "plt.bar(gen_count.index, gen_count.values, color='skyblue')\n",
    "plt.xlabel('Gender')\n",
    "plt.ylabel('Count')\n",
    "plt.title('Distribution of Gender in Toy Dataset')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "781b0721",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d271bdd8",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "33d15e35",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
