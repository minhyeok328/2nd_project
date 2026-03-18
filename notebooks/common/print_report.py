import numpy as np
from sklearn.metrics import (
    accuracy_score,
    recall_score,
    f1_score,
    roc_auc_score,
    average_precision_score,
    precision_score
)
from sklearn.preprocessing import label_binarize
from sklearn.utils.multiclass import type_of_target


def print_report(y_true, y_pred, y_proba, classes=None, average="macro", dataset_name="Dataset"):
    target_type = type_of_target(y_true)

    result = {
        "dataset": dataset_name,
        "target_type": target_type,
        "accuracy": accuracy_score(y_true, y_pred),
    }

    # y_proba shape 보정
    y_proba = np.asarray(y_proba)

    if target_type == "binary":
        result["recall"] = recall_score(y_true, y_pred)
        result["f1"] = f1_score(y_true, y_pred)

        # (n_samples, 2) 이면 positive class 확률만 사용
        if y_proba.ndim == 2 and y_proba.shape[1] == 2:
            y_score = y_proba[:, 1]
        # 이미 (n_samples,) 형태면 그대로 사용
        elif y_proba.ndim == 1:
            y_score = y_proba
        else:
            print(f"Binary Classification Shape Error: y_proba.shape = {y_proba.shape}")
            return

        result["roc_auc"] = roc_auc_score(y_true, y_score)
        result["pr_auc"] = average_precision_score(y_true, y_score)
        result["precision_score"] = precision_score(y_true, y_pred)

    elif target_type == "multiclass":
        result["recall"] = recall_score(y_true, y_pred, average=average)
        result["f1"] = f1_score(y_true, y_pred, average=average)

        if y_proba.ndim != 2:
            raise ValueError(f"Multiclass classification에서는 y_proba가 2차원이어야 합니다: {y_proba.shape}")

        result["roc_auc"] = roc_auc_score(
            y_true,
            y_proba,
            multi_class="ovr",
            average=average
        )

        if classes is None:
            classes = np.unique(y_true)

        y_true_bin = label_binarize(y_true, classes=classes)
        result["pr_auc"] = average_precision_score(
            y_true_bin,
            y_proba,
            average=average
        )
        
        result["precision_score"] = precision_score(y_true, y_pred, average=average)

    else:
        raise ValueError(f"지원하지 않는 target type입니다: {target_type}")

    print("=" * 20, f"{result["dataset"]}", "="*20)
    print(f"{"target type":>20}: {result["target_type"]}")
    for k in [key for key in result if key not in ["dataset", "target_type"]]:
        print(f"{k:>20}: {result[k]:.6f}")
