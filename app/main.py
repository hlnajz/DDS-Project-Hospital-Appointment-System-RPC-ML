# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import assurance
import uvicorn
import os

app = FastAPI(title="UIZ Hospital Python RPC")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://dds-project-hospital-appointment-system.onrender.com",
        "https://uizhospital.com"
    ],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(assurance.router, prefix="/rpc", tags=["Assurance"])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # fallback for local
    uvicorn.run("app.main:app", host="0.0.0.0", port=port)



# # app/main.py
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from app.routes import assurance
# import uvicorn
# import os

# app = FastAPI(title="UIZ Hospital Python RPC")

# # CORS: allow backend and frontend URLs
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[
#         "https://dds-project-hospital-appointment-system.onrender.com",  # backend URL
#         "https://uizhospital.com"  # frontend URL
#     ],
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Routes
# app.include_router(assurance.router, prefix="/rpc", tags=["Assurance"])

# # Start server with Render's assigned PORT
# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 5000))
#     uvicorn.run("app.main:app", host="0.0.0.0", port=port)
