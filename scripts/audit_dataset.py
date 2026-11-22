{
 "cells": [
  {
   "cell_type": "code",
   "id": "initial_id",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "\n",
    "from pathlib import Path\n",
    "import pandas as pd\n",
    "\n",
    "# Chemin du projet\n",
    "BASE_DIR = Path(__file__).resolve().parent.parent\n",
    "DATA_PATH = BASE_DIR / \"data\" / \"raw\" / \"tickets.csv\"\n",
    "\n",
    "# Charger le dataset\n",
    "df = pd.read_csv(\"C:\\Users\\ADMIN\\PycharmProjects\\SupportMind\\data\\raw\\tickets.csv\")\n",
    "\n",
    "# Vérifications initiales\n",
    "print(\"=== SUPPORTMIND V2 : AUDIT DATASET ===\")\n",
    "\n",
    "print(\"\\nDimensions :\")\n",
    "print(df.shape)\n",
    "\n",
    "print(\"\\nColonnes :\")\n",
    "print(df.columns.tolist())\n",
    "\n",
    "print(\"\\nPremiers tickets :\")\n",
    "print(df[[\"ticket_text\", \"category\"]].head())\n",
    "\n",
    "print(\"\\nValeurs manquantes :\")\n",
    "print(df[[\"ticket_text\", \"category\"]].isna().sum())\n",
    "\n",
    "print(\"\\nCatégories :\")\n",
    "print(df[\"category\"].value_counts())\n"
   ],
   "outputs": [],
   "execution_count": null
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
