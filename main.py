import uvicorn
import os

port = int(os.getenv("PORT", 8080))
print(port)
uvicorn.run(
    "app:app",
    host="0.0.0.0",
    port=port,
    reload=False
)