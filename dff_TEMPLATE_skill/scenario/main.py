from df_engine.core import Actor
from df_engine.core.keywords import RESPONSE, TRANSITIONS
import df_engine.conditions as cnd
from scenario.condition import employees_search, true, job_search
import scenario.condition as conds
import scenario.response as resps


plot = {
    "service": {
        "start": {
            RESPONSE: "",
            TRANSITIONS: {
                ("service", "choose_lang"): true,
            }
        },
        "choose_lang": {
            RESPONSE: resps.choose_lang,
            TRANSITIONS: {
                ("service", "en_origin"): conds.choosed_en,
                ("service", "ru_origin"): conds.choosed_ru,
            }
        },
        "en_origin": {
            RESPONSE: resps.eng["origin"],
            TRANSITIONS: {
                ("employee", "eng_find_employee"): conds.employees_search,
                ("job", "eng_find_job"): conds.job_search,
            }
        },
        "fallback": {
            RESPONSE: resps.eng["error"],
            TRANSITIONS: {
                ("service", "choose_lang") : conds.start
            }
        },
        "ru_origin": {
            RESPONSE: resps.ru["origin"],
            TRANSITIONS: {
                ("employee", "ru_find_employee"): conds.employees_search,
                ("job", "ru_find_job"): conds.job_search,
            }
        },
    },
    "job": {
        "eng_find_job": {
            RESPONSE: resps.eng["job_search"],
        },
        "ru_find_job": {
            RESPONSE: resps.ru["job_search"],
        },
    },
    "employee" : {
        "eng_find_employee": {
            RESPONSE: resps.eng["employee_search"],
        },
        "ru_find_employee": {
            RESPONSE: resps.ru["employee_search"],
        },
    }
}

actor = Actor(plot, start_label=("service", "start"), fallback_label=("service", "fallback"))
