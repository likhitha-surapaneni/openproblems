from ....tools.decorators import metric

import sklearn.metrics
import sklearn.preprocessing


def _f1(adata, average="weighted"):
    encoder = sklearn.preprocessing.LabelEncoder().fit(adata.obs["labels"])
    test_data = adata[~adata.obs["is_train"]]

    test_data.obs["labels"] = encoder.transform(test_data.obs["labels"])
    test_data.obs["labels_pred"] = encoder.transform(test_data.obs["labels_pred"])

    return sklearn.metrics.f1_score(
        test_data.obs["labels"], test_data.obs["labels_pred"], average=average
    )


@metric(metric_name="F1 score", maximize=True)
def f1(adata):
    return _f1(adata, average="weighted")


@metric(metric_name="Micro F1 score", maximize=True)
def f1_micro(adata):
    return _f1(adata, average="micro")
