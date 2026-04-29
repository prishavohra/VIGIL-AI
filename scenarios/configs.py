SCENARIOS = {

    "shooting.mp4": {
        "title": "Supermarket Shooting",
        "risk": "HIGH",
        "label_folder": "labels/labels_shooting",

        "events": [
            {"time": 1, "msg": "⚠️ SUSPICIOUS ACTIVITY - SHOOTING"},
            {"time": 1, "msg": "🔴 HIGH RISK - WEAPON DETECTED"},
            {"time": 5, "msg": "🔴 HIGH RISK - WEAPON DETECTED"},
            {"time": 6, "msg": "⚠️ SUSPICIOUS ACTIVITY - SHOOTING"},
            {"time": 25, "msg": "🔴 HIGH RISK - WEAPON DETECTED"},
            {"time": 34, "msg": "⚠️ SUSPICIOUS ACTIVITY - BURGLARY"},
        ]
    },

    "weapon_drop.mp4": {
        "title": "Weapon Dropped by Armed Civilian",
        "risk": "MEDIUM",
        "label_folder": "labels/labels_weapon_drop",

        "events": [
            {"time": 2, "msg": "🟡 WEAPON DROP DETECTED"}
        ]
    }, 

    "abuse.mp4": {
        "title": "Police officers abuse caught on bodycam",
        "risk": "HIGH",
        "label_folder": "labels/labels_abuse",

        "events": [
            {"time": 15, "msg": "⚠️ SUSPICIOUS ACTIVITY - ABUSE"},
            {"time": 16, "msg": "⚠️ SUSPICIOUS ACTIVITY - ABUSE"},
            {"time": 18, "msg": "⚠️ SUSPICIOUS ACTIVITY - ABUSE"},
            {"time": 21, "msg": "⚠️ SUSPICIOUS ACTIVITY - ABUSE"},
            {"time": 22, "msg": "⚠️ SUSPICIOUS ACTIVITY - ABUSE"},
            {"time": 23, "msg": "⚠️ SUSPICIOUS ACTIVITY - ABUSE"},
            {"time": 25, "msg": "⚠️ SUSPICIOUS ACTIVITY - ABUSE"},
            {"time": 29, "msg": "⚠️ SUSPICIOUS ACTIVITY - ABUSE"},
            {"time": 31, "msg": "⚠️ SUSPICIOUS ACTIVITY - ABUSE"},
            {"time": 33, "msg": "⚠️ SUSPICIOUS ACTIVITY - ABUSE"},
            {"time": 34, "msg": "⚠️ SUSPICIOUS ACTIVITY - ABUSE"},
            {"time": 36, "msg": "⚠️ SUSPICIOUS ACTIVITY - ABUSE"},
            {"time": 38, "msg": "⚠️ SUSPICIOUS ACTIVITY - ABUSE"},
            {"time": 40, "msg": "⚠️ SUSPICIOUS ACTIVITY - ABUSE"},
            {"time": 43, "msg": "⚠️ SUSPICIOUS ACTIVITY - ABUSE"},
            {"time": 45, "msg": "⚠️ SUSPICIOUS ACTIVITY - ABUSE"},
            {"time": 50, "msg": "⚠️ SUSPICIOUS ACTIVITY - ABUSE"},
            {"time": 51, "msg": "⚠️ SUSPICIOUS ACTIVITY - ABUSE"},
        ]
    }, 

    "weapon.mp4": {
        "title": "Person threatens with a knife",
        "risk": "HIGH",
        "label_folder": "labels/labels_weapon",

        "events": [
            {"time": 1, "msg": "🔴 HIGH RISK - WEAPON DETECTED"},
            {"time": 2, "msg": "🔴 HIGH RISK - WEAPON DETECTED"},
            {"time": 3, "msg": "🔴 HIGH RISK - WEAPON DETECTED"},
            {"time": 4, "msg": "🔴 HIGH RISK - WEAPON DETECTED"},
            {"time": 5, "msg": "🔴 HIGH RISK - WEAPON DETECTED"},
            {"time": 6, "msg": "🔴 HIGH RISK - WEAPON DETECTED"},
            {"time": 7, "msg": "🔴 HIGH RISK - WEAPON DETECTED"},
            {"time": 8, "msg": "🔴 HIGH RISK - WEAPON DETECTED"},
            {"time": 9, "msg": "🔴 HIGH RISK - WEAPON DETECTED"}, 
            {"time": 10, "msg": "🔴 HIGH RISK - WEAPON DETECTED"},
            {"time": 11, "msg": "🔴 HIGH RISK - WEAPON DETECTED"},
            {"time": 12, "msg": "🔴 HIGH RISK - WEAPON DETECTED"},
            {"time": 13, "msg": "🔴 HIGH RISK - WEAPON DETECTED"},
            {"time": 14, "msg": "🔴 HIGH RISK - WEAPON DETECTED"}
        ]
    },

    "assault.mp4": {
        "title": "Person physically attacks another person",
        "risk": "MEDIUM",
        "label_folder": "labels/labels_assault",

        "events": [
            {"time": 3, "msg": "⚠️ SUSPICIOUS ACTIVITY - ASSAULT"},
            {"time": 4, "msg": "⚠️ SUSPICIOUS ACTIVITY - ASSAULT"},
            {"time": 5, "msg": "⚠️ SUSPICIOUS ACTIVITY - ASSAULT"},
            {"time": 6, "msg": "⚠️ SUSPICIOUS ACTIVITY - ASSAULT"},
            {"time": 7, "msg": "⚠️ SUSPICIOUS ACTIVITY - ASSAULT"},
            {"time": 8, "msg": "⚠️ SUSPICIOUS ACTIVITY - ASSAULT"},
            {"time": 9, "msg": "⚠️ SUSPICIOUS ACTIVITY - ASSAULT"}, 
            {"time": 10, "msg": "⚠️ SUSPICIOUS ACTIVITY - ASSAULT"},
            {"time": 11, "msg": "⚠️ SUSPICIOUS ACTIVITY - ASSAULT"},
            {"time": 12, "msg": "⚠️ SUSPICIOUS ACTIVITY - ASSAULT"},
            {"time": 13, "msg": "⚠️ SUSPICIOUS ACTIVITY - ASSAULT"},
            {"time": 16, "msg": "⚠️ SUSPICIOUS ACTIVITY - ASSAULT"}, 
            {"time": 17, "msg": "⚠️ SUSPICIOUS ACTIVITY - ASSAULT"},
            {"time": 18, "msg": "⚠️ SUSPICIOUS ACTIVITY - ASSAULT"},
            {"time": 19, "msg": "⚠️ SUSPICIOUS ACTIVITY - ASSAULT"}
        ]
    },

    "assault2.mp4": {
        "title": "Road Fight between two people",
        "risk": "MEDIUM",
        "label_folder": "labels/labels_assault2",

        "events": [
            {"time": 9, "msg": "⚠️ SUSPICIOUS ACTIVITY - ASSAULT"}, 
            {"time": 10, "msg": "⚠️ SUSPICIOUS ACTIVITY - ASSAULT"},
            {"time": 11, "msg": "⚠️ SUSPICIOUS ACTIVITY - ASSAULT"},
            {"time": 12, "msg": "⚠️ SUSPICIOUS ACTIVITY - ASSAULT"},
            {"time": 13, "msg": "⚠️ SUSPICIOUS ACTIVITY - ASSAULT"},
        ]
    }, 

    "shooting2.mp4": {
        "title": "Man threatens to shoot himself",
        "risk": "HIGH",
        "label_folder": "labels/labels_shooting2",

        "events": [
            {"time": 4, "msg": "🔴 HIGH RISK - WEAPON DETECTED"}, 
            {"time": 20, "msg": "🔴 HIGH RISK - WEAPON DETECTED"},
            {"time": 21, "msg": "🔴 HIGH RISK - WEAPON DETECTED"},
            {"time": 22, "msg": "🔴 HIGH RISK - WEAPON DETECTED"}
        ]
    }
}

GAN_OUTPUTS = {
    "shooting.mp4": "GAN uploads/shooting.mp4",
    "weapon.mp4": "GAN uploads/weapon.mp4",
    "weapon_drop.mp4": "GAN uploads/weapon_drop.mp4",
    "abuse.mp4": "GAN uploads/abuse.mp4",
    "assault.mp4": "GAN uploads/assault.mp4",
    "assault2.mp4": "GAN uploads/assault2.mp4",
    "shooting2.mp4": "GAN uploads/shooting2.mp4"
}
