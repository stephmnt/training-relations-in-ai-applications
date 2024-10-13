# Training relations in AI applications

## English version

### Project description
This project focuses on analyzing relationships between different variables from a dataset of AI applications in education and training. It explores the co-occurrence of various relations (A1, A2, A3, B1, B2, B3) and provides visualizations such as bar charts, boxplots, and a co-occurrence matrix.

### Key features
- Data cleaning and preprocessing
- Statistical analysis (mean, median, IQR, skewness, kurtosis)
- Visualization of relation frequencies using bar charts
- Boxplot for statistical summary
- Co-occurrence matrix heatmap

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    ```

2. Navigate into the project directory:
    ```bash
    cd your-repository-name
    ```

3. Create a virtual environment and install dependencies:
    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    pip install -r requirements.txt
    ```

4. Launch the Jupyter Notebook:
    ```bash
    jupyter notebook applis-ia.ipynb
    ```

### Usage
The notebook contains several steps:

1. **Loading Data**: Loads the dataset and examines its structure.
2. **Data Cleaning**: Removes unnecessary columns and filters rows based on the relations of interest.
3. **Relation Frequency Analysis**: Explodes the relation column and counts occurrences of each relation.
4. **Statistical Analysis**: Provides descriptive statistics (mean, median, quartiles, etc.).
5. **Visualization**:
    - Bar chart showing the frequency of each relation.
    - Boxplot highlighting key statistical measures.
    - Heatmap of the co-occurrence matrix showing which relations frequently appear together.

---

## Version française

### Description du projet
Ce projet se concentre sur l'analyse des relations entre différentes variables dans un jeu de données d'applications IA en éducation et formation. Il explore la co-occurrence de diverses relations (A1, A2, A3, B1, B2, B3) et propose des visualisations comme des diagrammes en barres, des boîtes à moustaches, et une matrice de co-occurrence.

### Fonctionnalités principales
- Nettoyage et prétraitement des données
- Analyse statistique (moyenne, médiane, IQR, asymétrie, aplatissement)
- Visualisation des fréquences des relations avec des diagrammes en barres
- Boîte à moustaches pour le résumé statistique
- Carte de chaleur de la matrice de co-occurrence

### Installation

1. Cloner le dépôt :
    ```bash
    git clone https://github.com/votre-utilisateur/nom-du-dépôt.git
    ```

2. Accédez au répertoire du projet :
    ```bash
    cd nom-du-dépôt
    ```

3. Créez un environnement virtuel et installez les dépendances :
    ```bash
    python3 -m venv env
    source env/bin/activate  # Sur Windows utilisez `env\Scripts\activate`
    pip install -r requirements.txt
    ```

4. Lancer le Jupyter Notebook :
    ```bash
    jupyter notebook applis-ia.ipynb
    ```

### Utilisation
Le notebook contient plusieurs étapes :

1. **Chargement des Données** : Charge le jeu de données et examine sa structure.
2. **Nettoyage des Données** : Supprime les colonnes inutiles et filtre les lignes en fonction des relations d'intérêt.
3. **Analyse des Fréquences des Relations** : Sépare la colonne des relations et compte les occurrences de chaque relation.
4. **Analyse Statistique** : Fournit des statistiques descriptives (moyenne, médiane, quartiles, etc.).
5. **Visualisation** :
    - Diagramme en barres montrant la fréquence de chaque relation.
    - Boîte à moustaches mettant en évidence les mesures statistiques clés.
    - Carte de chaleur de la matrice de co-occurrence montrant quelles relations apparaissent fréquemment ensemble.
