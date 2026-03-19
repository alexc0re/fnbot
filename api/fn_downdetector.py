import requests


def get_fortnite_statuses_ua() -> dict[str, str]:
    url = "https://status.epicgames.com/api/v2/summary.json"
    fortnite_group_id = "wf1ys2kx4pxc"

    target_names = {
        "Parties, Friends, and Messaging": "Друзі, групи та повідомлення",
        "Voice Chat": "Голосовий чат",
        "Matchmaking": "Пошук матчу",
    }

    status_map = {
        "operational": "Працює",
        "under_maintenance": "Технічне обслуговування",
        "degraded_performance": "Погіршена робота",
        "partial_outage": "Частковий збій",
        "major_outage": "Масовий збій",
    }

    response = requests.get(url, timeout=15)
    response.raise_for_status()
    data = response.json()

    result = {
        "Друзі, групи та повідомлення": "Не знайдено",
        "Голосовий чат": "Не знайдено",
        "Пошук матчу": "Не знайдено",
    }

    for component in data.get("components", []):
        if component.get("group_id") != fortnite_group_id:
            continue

        english_name = component.get("name")
        if english_name in target_names:
            ua_name = target_names[english_name]
            raw_status = component.get("status")
            result[ua_name] = status_map.get(raw_status, f"Невідомий статус: {raw_status}")

    return result
