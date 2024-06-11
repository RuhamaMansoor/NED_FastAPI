from fastapi import FastAPI


app= FastAPI()

users_data = {
                "user1": {"name": "Ruhama", "email": "ruhamamansoor96@gmail.com"},
                "user2": {"name": "Jazzy", "email": "jazzy98@gmail.com"}
}

@app.get('/user/')
def get_users():
    return users_data