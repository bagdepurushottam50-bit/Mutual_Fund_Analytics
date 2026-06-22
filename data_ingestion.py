data_ingestion.py
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "6c96b54b-af7d-458f-bd48-99ecdf576770",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "NAV data downloaded successfully!\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import requests\n",
    "import os\n",
    "\n",
    "os.makedirs(\"data/raw\", exist_ok=True)\n",
    "\n",
    "url = \"https://www.amfiindia.com/spages/NAVAll.txt\"\n",
    "response = requests.get(url)\n",
    "\n",
    "with open(\"data/raw/nav_data.txt\", \"w\", encoding=\"utf-8\") as f:\n",
    "    f.write(response.text)\n",
    "\n",
    "print(\"NAV data downloaded successfully!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "271f6d08-d8c4-4a42-abdf-e5c264733dba",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total Lines: 35032\n",
      "\n",
      "First 10 Lines:\n",
      "\n",
      "Scheme Code;ISIN Div Payout/ ISIN Growth;ISIN Div Reinvestment;Scheme Name;Net Asset Value;Date\n",
      "\n",
      "\n",
      "\n",
      "Open Ended Schemes(Debt Scheme - Banking and PSU Fund)\n",
      "\n",
      "\n",
      "\n",
      "Aditya Birla Sun Life Mutual Fund\n",
      "\n"
     ]
    }
   ],
   "source": [
    "with open(\"data/raw/nav_data.txt\", \"r\", encoding=\"utf-8\") as f:\n",
    "    lines = f.readlines()\n",
    "\n",
    "print(\"Total Lines:\", len(lines))\n",
    "print(\"\\nFirst 10 Lines:\\n\")\n",
    "\n",
    "for line in lines[:10]:\n",
    "    print(line.strip())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "1cde805e-ef0a-4aac-a6c6-b2456c8bc7b7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total Mutual Fund Records: 14219\n",
      "[['119551', 'INF209KA12Z1', 'INF209KA13Z9', 'Aditya Birla Sun Life Banking & PSU Debt Fund  - DIRECT - IDCW', '105.9219', '19-Jun-2026'], ['119552', 'INF209K01YM2', '-', 'Aditya Birla Sun Life Banking & PSU Debt Fund  - DIRECT - MONTHLY IDCW', '117.0754', '19-Jun-2026'], ['119553', 'INF209K01YO8', '-', 'Aditya Birla Sun Life Banking & PSU Debt Fund  - Direct - Quarterly IDCW', '103.9719', '19-Jun-2026'], ['108272', 'INF209K01LX6', 'INF209KA11Z3', 'Aditya Birla Sun Life Banking & PSU Debt Fund  - REGULAR - IDCW', '148.296', '19-Jun-2026'], ['110282', 'INF209K01LU2', '-', 'Aditya Birla Sun Life Banking & PSU Debt Fund  - REGULAR - MONTHLY IDCW', '112.3932', '19-Jun-2026']]\n"
     ]
    }
   ],
   "source": [
    "records = []\n",
    "\n",
    "for line in lines:\n",
    "    parts = line.strip().split(\";\")\n",
    "    \n",
    "    if len(parts) == 6 and parts[0].isdigit():\n",
    "        records.append(parts)\n",
    "\n",
    "print(\"Total Mutual Fund Records:\", len(records))\n",
    "print(records[:5])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "39ddede6-4f91-4d91-b0d3-0a0bead130ba",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Folder created successfully!\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "\n",
    "os.makedirs(\"data/processed\", exist_ok=True)\n",
    "\n",
    "print(\"Folder created successfully!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "4cf792ca-8092-4025-83bd-cdd054fed05d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "CSV File Saved Successfully!\n",
      "Shape: (14219, 6)\n"
     ]
    }
   ],
   "source": [
    "df.to_csv(\"data/processed/mutual_fund_nav.csv\", index=False)\n",
    "\n",
    "print(\"CSV File Saved Successfully!\")\n",
    "print(\"Shape:\", df.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "df26d8b0-daa2-4521-b735-dab3eaf1dd2f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 14219 entries, 0 to 14218\n",
      "Data columns (total 6 columns):\n",
      " #   Column                 Non-Null Count  Dtype \n",
      "---  ------                 --------------  ----- \n",
      " 0   Scheme_Code            14219 non-null  object\n",
      " 1   ISIN_Div_Payout        14219 non-null  object\n",
      " 2   ISIN_Div_Reinvestment  14219 non-null  object\n",
      " 3   Scheme_Name            14219 non-null  object\n",
      " 4   NAV                    14219 non-null  object\n",
      " 5   Date                   14219 non-null  object\n",
      "dtypes: object(6)\n",
      "memory usage: 666.6+ KB\n",
      "None\n",
      "\n",
      "Missing Values:\n",
      "Scheme_Code              0\n",
      "ISIN_Div_Payout          0\n",
      "ISIN_Div_Reinvestment    0\n",
      "Scheme_Name              0\n",
      "NAV                      0\n",
      "Date                     0\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "print(df.info())\n",
    "\n",
    "print(\"\\nMissing Values:\")\n",
    "print(df.isnull().sum())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "fc2b8775-3510-474f-bc53-455d4cd97bb7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total Funds: 14219\n",
      "\n",
      "Sample Fund Names:\n",
      "0    Aditya Birla Sun Life Banking & PSU Debt Fund ...\n",
      "1    Aditya Birla Sun Life Banking & PSU Debt Fund ...\n",
      "2    Aditya Birla Sun Life Banking & PSU Debt Fund ...\n",
      "3    Aditya Birla Sun Life Banking & PSU Debt Fund ...\n",
      "4    Aditya Birla Sun Life Banking & PSU Debt Fund ...\n",
      "5    Aditya Birla Sun Life Banking & PSU Debt Fund ...\n",
      "6    Aditya Birla Sun Life Banking & PSU Debt Fund ...\n",
      "7    Aditya Birla Sun Life Banking & PSU Debt Fund ...\n",
      "8    Aditya Birla Sun Life Banking & PSU Debt Fund ...\n",
      "9    Aditya Birla Sun Life Banking & PSU Debt Fund ...\n",
      "Name: Scheme_Name, dtype: object\n"
     ]
    }
   ],
   "source": [
    "print(\"Total Funds:\", df[\"Scheme_Name\"].nunique())\n",
    "\n",
    "print(\"\\nSample Fund Names:\")\n",
    "print(df[\"Scheme_Name\"].head(10))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "914f1ebe-0613-4e53-ac9b-2b295c157f6d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Maximum NAV: 2458145.8233\n",
      "Minimum NAV: 0.0\n",
      "Average NAV: 1646.9054354407835\n"
     ]
    }
   ],
   "source": [
    "df[\"NAV\"] = pd.to_numeric(df[\"NAV\"], errors=\"coerce\")\n",
    "\n",
    "print(\"Maximum NAV:\", df[\"NAV\"].max())\n",
    "print(\"Minimum NAV:\", df[\"NAV\"].min())\n",
    "print(\"Average NAV:\", df[\"NAV\"].mean())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "65b42bba-7b87-4312-9feb-8b36f305ad87",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
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
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
