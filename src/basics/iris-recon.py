"""Simple Iris recon exercise
"""

import numpy as np
from sklearn.datasets import load_iris # type: ignore
from sklearn.model_selection import train_test_split # type: ignore
from sklearn.neighbors import KNeighborsClassifier # type: ignore

iris_dataset = load_iris()

def create_knn_model(
        training_data: tuple, 
        neighbors: int, 
        sample: list) -> np.ndarray:
    """Classify data with k next neighbour algorithm.

    Args:
        training_data: A 2-ary tuple containing vectors representing the 
            parametrized data and its targeted outcome, respectively.
        neighbors: An integer representing the amount of neighbors each 
            datapoint may have to consider categorization.
        sample: A list of vectors representing at least one data point with all
            parameters.

    Returns:
        prediction: A ndarray representing the category of each input.

    Raises:
        None.
    """
    knn = KNeighborsClassifier(n_neighbors=neighbors)
    knn.fit(training_data[0], training_data[1])
    X_new = np.array(sample)
    prediction = knn.predict(X_new)

    return prediction

def main() -> None:
    """Main function

    Executes and orchestrates all functions within this module.
    """
    # describe_parameters()
    ds = iris_dataset
    data   = ds['data']
    target = ds['target']
    names  = ds['target_names']
    X_train, X_test, y_train, y_test = train_test_split(data, target, 
                                                        random_state=0)
    prediction = create_knn_model((X_train, y_train), 1, X_test)
    print("Prediction: {}".format(prediction))
    print("Predicted name: {}".format(names[prediction]))
    accuracy = np.mean(prediction == y_test)
    print("Accuracy of model with KNN: {}".format(accuracy))

if __name__ == '__main__':
    main()
