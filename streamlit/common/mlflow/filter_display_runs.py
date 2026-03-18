from typing import Dict, List, Any


DISPLAY_RUN_NAMES = {
    "lightgbm_baseline",
    "hist_gradient_boosting",
    "logistic_regression_baseline",
    "easy_ensemble_baseline",
    "xgboost_random_grid_search",
}


def filter_display_runs(
    run_info_list: List[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    """
    Streamlit 비교에 사용할 대표 run만 필터링합니다.

    규칙:
    - FINISHED 상태만 사용
    - nested run 제외
    - 지정한 5개 run_name만 사용
    - 각 run_name별 최신 1개만 사용
    """
    filtered_runs: List[Dict[str, Any]] = []

    for run_info in run_info_list:
        if run_info["status"] != "FINISHED":
            continue

        if run_info["is_nested"]:
            continue

        if run_info["run_name"] not in DISPLAY_RUN_NAMES:
            continue

        filtered_runs.append(run_info)

    grouped: Dict[str, List[Dict[str, Any]]] = {}
    for run_info in filtered_runs:
        run_name = run_info["run_name"]
        if run_name not in grouped:
            grouped[run_name] = []
        grouped[run_name].append(run_info)

    latest_runs: List[Dict[str, Any]] = []
    for run_name, run_list in grouped.items():
        run_list.sort(key=lambda x: x["start_time"], reverse=True)
        latest_runs.append(run_list[0])

    return latest_runs