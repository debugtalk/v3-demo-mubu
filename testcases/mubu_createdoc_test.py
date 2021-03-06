# NOTICE: Generated By HttpRunner. DO'NOT EDIT!
# FROM: testcases/mubu.createdoc.yml
from httprunner import HttpRunner, TConfig, TStep


class TestCaseMubuCreatedoc(HttpRunner):
    config = TConfig(
        **{
            "name": "testcase description",
            "variables": {
                "user_phone": "18613143458",
                "password": "moFrwx$!kz3DTRm@@*aV",
            },
            "verify": False,
            "base_url": "https://api2.mubu.com",
            "path": "testcases/mubu_createdoc_test.py",
        }
    )

    teststeps = [
        TStep(**{"name": "login mubu", "testcase": "testcases/mubu.login.yml"}),
        TStep(
            **{
                "name": "/api/list/create_doc",
                "request": {
                    "data": {"folderId": "0", "type": "0"},
                    "headers": {
                        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                        "cookie": "user_persistence=$user_persistence",
                        "referer": "https://mubu.com/list",
                        "sec-fetch-dest": "empty",
                        "sec-fetch-mode": "cors",
                        "sec-fetch-site": "same-origin",
                        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 HttpRunner/${get_httprunner_version()}",
                        "x-requested-with": "XMLHttpRequest",
                    },
                    "method": "POST",
                    "url": "https://mubu.com/api/list/create_doc",
                },
                "extract": {"docId": "body.data.id"},
                "validate": [
                    {"eq": ["status_code", 200]},
                    {"eq": ["body.code", 0]},
                    {"eq": ["body.msg", None]},
                ],
            }
        ),
        TStep(
            **{
                "name": "/doc$docId",
                "request": {
                    "headers": {
                        "cookie": "user_persistence=$user_persistence",
                        "referer": "https://mubu.com/list",
                        "sec-fetch-dest": "document",
                        "sec-fetch-mode": "navigate",
                        "sec-fetch-site": "same-origin",
                        "sec-fetch-user": "?1",
                        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 HttpRunner/${get_httprunner_version()}",
                    },
                    "method": "GET",
                    "url": "https://mubu.com/doc$docId",
                },
                "validate": [{"eq": ["status_code", 200]}],
            }
        ),
        TStep(
            **{
                "name": "/v3/api/user/current_user",
                "request": {
                    "data": "",
                    "headers": {
                        "data-unique-id": "5410ad30-980c-11ea-8923-e551129da490",
                        "jwt-token": "$jwt_token",
                        "referer": "https://mubu.com/doc$docId",
                        "sec-fetch-dest": "empty",
                        "sec-fetch-mode": "cors",
                        "sec-fetch-site": "same-site",
                        "token": "$jwt_token",
                        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 HttpRunner/${get_httprunner_version()}",
                        "x-request-id": "8d64a21f-b97a-4900-9fc2-6ffb60071d7b",
                    },
                    "method": "POST",
                    "url": "https://api2.mubu.com/v3/api/user/current_user",
                },
                "validate": [
                    {"eq": ["status_code", 200]},
                    {"eq": ["body.code", 0]},
                    {"eq": ["body.msg", "success"]},
                ],
            }
        ),
        TStep(
            **{
                "name": "/v3/api/document/get",
                "request": {
                    "headers": {
                        "content-type": "application/json;charset=UTF-8",
                        "data-unique-id": "5410ad30-980c-11ea-8923-e551129da490",
                        "jwt-token": "$jwt_token",
                        "referer": "https://mubu.com/doc$docId",
                        "sec-fetch-dest": "empty",
                        "sec-fetch-mode": "cors",
                        "sec-fetch-site": "same-site",
                        "token": "$jwt_token",
                        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 HttpRunner/${get_httprunner_version()}",
                        "x-request-id": "80f926fe-37c4-45a0-aa85-96d78b3c78e0",
                    },
                    "json": {"docId": "$docId"},
                    "method": "POST",
                    "url": "https://api2.mubu.com/v3/api/document/get",
                },
                "validate": [
                    {"eq": ["status_code", 200]},
                    {"eq": ["body.code", 0]},
                    {"eq": ["body.msg", "Success"]},
                ],
            }
        ),
        TStep(
            **{
                "name": "/v3/api/user/current_level",
                "request": {
                    "headers": {
                        "content-type": "application/json;charset=UTF-8",
                        "data-unique-id": "5410ad30-980c-11ea-8923-e551129da490",
                        "jwt-token": "$jwt_token",
                        "referer": "https://mubu.com/doc$docId",
                        "sec-fetch-dest": "empty",
                        "sec-fetch-mode": "cors",
                        "sec-fetch-site": "same-site",
                        "token": "$jwt_token",
                        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 HttpRunner/${get_httprunner_version()}",
                        "x-request-id": "d7f43e29-a625-4561-95f3-906134e71f37",
                    },
                    "json": {"document_id": "$docId"},
                    "method": "POST",
                    "url": "https://api2.mubu.com/v3/api/user/current_level",
                },
                "validate": [
                    {"eq": ["status_code", 200]},
                    {"eq": ["body.code", 0]},
                    {"eq": ["body.msg", "OK"]},
                ],
            }
        ),
        TStep(
            **{
                "name": "/v3/api/user/get_user_params",
                "request": {
                    "data": "",
                    "headers": {
                        "data-unique-id": "5410ad30-980c-11ea-8923-e551129da490",
                        "jwt-token": "$jwt_token",
                        "referer": "https://mubu.com/doc$docId",
                        "sec-fetch-dest": "empty",
                        "sec-fetch-mode": "cors",
                        "sec-fetch-site": "same-site",
                        "token": "$jwt_token",
                        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 HttpRunner/${get_httprunner_version()}",
                        "x-request-id": "ccddfa20-40d6-42bc-8964-8730a57da9ba",
                    },
                    "method": "POST",
                    "url": "https://api2.mubu.com/v3/api/user/get_user_params",
                },
                "validate": [
                    {"eq": ["status_code", 200]},
                    {"eq": ["body.code", 0]},
                    {"eq": ["body.msg", "success"]},
                ],
            }
        ),
        TStep(
            **{
                "name": "/v3/api/user/get_invite_count",
                "request": {
                    "headers": {
                        "data-unique-id": "5410ad30-980c-11ea-8923-e551129da490",
                        "jwt-token": "$jwt_token",
                        "referer": "https://mubu.com/doc$docId",
                        "sec-fetch-dest": "empty",
                        "sec-fetch-mode": "cors",
                        "sec-fetch-site": "same-site",
                        "token": "$jwt_token",
                        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 HttpRunner/${get_httprunner_version()}",
                        "x-request-id": "5d1ba900-f963-49c2-8125-6ffdbae77eaf",
                    },
                    "method": "GET",
                    "url": "https://api2.mubu.com/v3/api/user/get_invite_count",
                },
                "validate": [
                    {"eq": ["status_code", 200]},
                    {"eq": ["body.code", 0]},
                    {"eq": ["body.msg", None]},
                ],
            }
        ),
        TStep(
            **{
                "name": "/v3/api/colla/register",
                "request": {
                    "headers": {
                        "data-unique-id": "5410ad30-980c-11ea-8923-e551129da490",
                        "jwt-token": "$jwt_token",
                        "referer": "https://mubu.com/doc$docId",
                        "sec-fetch-dest": "empty",
                        "sec-fetch-mode": "cors",
                        "sec-fetch-site": "same-site",
                        "token": "$jwt_token",
                        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 HttpRunner/${get_httprunner_version()}",
                        "x-request-id": "4aca8841-02bb-47da-bb2f-66838ccd9a03",
                    },
                    "method": "GET",
                    "url": "/v3/api/colla/register",
                },
                "validate": [
                    {"eq": ["status_code", 200]},
                    {"eq": ["body.code", 0]},
                    {"eq": ["body.msg", "Success"]},
                ],
            }
        ),
    ]


if __name__ == "__main__":
    TestCaseMubuCreatedoc().test_start()
