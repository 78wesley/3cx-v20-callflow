import httpx
import os
import dotenv

dotenv.load_dotenv()


def get_access_token():
    url = "https://3cx-dts.soundofservice.com/webclient/api/Login/GetAccessToken"
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
    }
    data = {"ReCaptchaResponse": None, "SecurityCode": "", "Password": os.getenv("password"), "Username": os.getenv("username")}

    response = httpx.post(url, headers=headers, json=data).json()
    if "access_token" in response:
        return response["access_token"]
    
    return response


if __name__ == "__main__":
    token_response = get_access_token()
    print(token_response)
