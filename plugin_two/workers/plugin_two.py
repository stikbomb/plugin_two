from loguru import logger
from shiva.common.base import BaseDaemon
import asyncio


class PluginWorker(BaseDaemon):
    name = "plugin_two_worker"

    async def prepare(self):
        pass

    async def start(self):
        logger.info("Hello from plugin two worker!")
        self.running = True
        while self.running:
            # logger.info('Waiter sleep...')
            await asyncio.sleep(5)
        logger.warning(f"Stopped: {self.name}")

    async def stop(self):
        self.running = False
