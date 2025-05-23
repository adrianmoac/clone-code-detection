from difflibSimilarities.main import main as difflib_main
from astSimilarities.main import main as ast_main
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import os
import sys
import json

def main(filePath, detectionAlgorithm):
    if getattr(sys, 'frozen', False):
        base_dir = sys._MEIPASS
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))

    normalized_path = os.path.join(base_dir, 'normalizedTestDataset')
    testDatasetPath = os.path.join(base_dir, 'testDataset')
    jsonPath = os.path.join(base_dir, 'grouped_files.json')

    if not os.path.exists(normalized_path):
        raise FileNotFoundError(f"Directory not found: {normalized_path}")
    if not os.path.exists(testDatasetPath):
        raise FileNotFoundError(f"Directory not found: {testDatasetPath}")
    if not os.path.exists(jsonPath):
        raise FileNotFoundError(f"JSON file not found: {jsonPath}")

    dir_test = [f for f in os.listdir(testDatasetPath) if f.endswith('.py')]
    dir_list = [f for f in os.listdir(normalized_path) if f.endswith('.py')]

    with open(jsonPath, "r") as file:
        data = json.load(file)

    all_y_true = []
    all_y_pred = []

    for test in dir_test:
        difflibResults = []
        astResults = []
        similarityMatrix = []

        test_file_path = os.path.join(testDatasetPath, test)

        for norm_file in dir_list:
            norm_file_path = os.path.join(normalized_path, norm_file)
            if detectionAlgorithm == 'difflib':
                dlResult = difflib_main(test_file_path, norm_file_path)
                difflibResults.append(dlResult)
            elif detectionAlgorithm == 'ast':
                astResult = ast_main(test_file_path, norm_file_path)
                astResults.append(astResult)

        if detectionAlgorithm == 'difflib':
            difflibResults = sorted(difflibResults, key=lambda d: list(d.values())[0], reverse=True)
            for res in difflibResults:
                (file, similarity), = res.items()
                filename = os.path.basename(file)
                isPlagiarism = similarity[0] >= 70
                similarityMatrix.append((filename, isPlagiarism))
        elif detectionAlgorithm == 'ast':
            astResults = sorted(astResults, key=lambda d: list(d.values())[0], reverse=True)
            for res in astResults:
                (file, similarity), = res.items()
                filename = os.path.basename(file)
                isPlagiarism = similarity >= 80
                similarityMatrix.append((filename, isPlagiarism))

        test_results_true = []
        test_results_pred = []

        for compared_file, predicted in similarityMatrix:
            try:
                ground_truth = data[test][compared_file] == 1
            except KeyError:
                continue  # Skip unmatched entries
            test_results_true.append(ground_truth)
            test_results_pred.append(predicted)

        all_y_true.extend(test_results_true)
        all_y_pred.extend(test_results_pred)

    # Final metrics
    accuracy = accuracy_score(all_y_true, all_y_pred)
    precision = precision_score(all_y_true, all_y_pred, average='binary')
    recall = recall_score(all_y_true, all_y_pred, average='binary')
    f1 = f1_score(all_y_true, all_y_pred, average='binary')

    if detectionAlgorithm == 'difflib':
      print('difflib')
    else:
      print('\nast')

    print("Accuracy:", accuracy)
    print("Precision:", precision)
    print("Recall:", recall)
    print("F1 Score:", f1)

    # Return the results for the last test file (optional logic can be added if needed)
    if detectionAlgorithm == 'difflib':
        return difflibResults
    elif detectionAlgorithm == 'ast':
        return astResults
