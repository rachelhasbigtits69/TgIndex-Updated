import asyncio
import logging
from aiohttp import web
from app.main import Indexer

logging.basicConfig(level=logging.INFO)

async def main():
    indexer = Indexer()
    app = await indexer.get_app()
    
    runner = web.AppRunner(app)
    await runner.setup()
    
    site = web.TCPSite(runner, indexer.host, indexer.port)
    logging.info(f"Starting server on http://{indexer.host}:{indexer.port}")
    await site.start()
    
    # Keep server running asynchronously
    await asyncio.Event().wait()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Server stopped.")
